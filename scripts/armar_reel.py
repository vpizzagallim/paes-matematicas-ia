"""Arma reel.mp4 (1080x1920, 30 fps, H.264 + AAC) a partir de las escenas que genera render/reel.js.

Uso: python3 scripts/armar_reel.py carpeta_escenas salida.mp4
La música y los efectos se sintetizan aquí mismo (sin derechos de autor).
"""
import json
import os
import subprocess
import sys
import wave

import numpy as np

SR = 44100
T = 0.3  # duración de cada transición (s)


def sintetizar(escenas, total, ruta):
    t = np.arange(int(total * SR)) / SR
    audio = np.zeros_like(t)
    # Fondo: acordes suaves (La m - Fa - Do - Sol), 2 s cada uno
    acordes = [[220.0, 261.63, 329.63], [174.61, 220.0, 261.63], [261.63, 329.63, 392.0], [196.0, 246.94, 293.66]]
    for i in range(int(total // 2) + 1):
        ini, fin = i * 2.0, min((i + 1) * 2.0, total)
        m = (t >= ini) & (t < fin)
        tt = t[m] - ini
        env = np.minimum(1, tt / 0.4) * np.minimum(1, (fin - ini - tt) / 0.4)
        for f in acordes[i % 4]:
            audio[m] += 0.045 * env * (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * 2 * f * tt))
    # Pulso suave tipo bombo cada 0,5 s
    for b in np.arange(0, total, 0.5):
        n = int(0.18 * SR); s = int(b * SR)
        if s + n > len(audio): break
        tt = np.arange(n) / SR
        audio[s:s + n] += 0.12 * np.sin(2 * np.pi * (90 - 200 * tt) * tt) * np.exp(-tt * 22)
    # Efectos por escena
    inicio = 0.0
    for e in escenas:
        s = int(inicio * SR)
        if e["tick"]:
            n = int(0.06 * SR); tt = np.arange(n) / SR
            audio[s:s + n] += 0.35 * np.sin(2 * np.pi * 1800 * tt) * np.exp(-tt * 70)
        if e["ding"]:
            n = int(1.2 * SR); tt = np.arange(n) / SR
            for f, a in ((1046.5, 0.25), (1318.5, 0.18), (1568.0, 0.12)):
                audio[s:s + n] += a * np.sin(2 * np.pi * f * tt) * np.exp(-tt * 4)
        if e["whoosh"]:
            n = int(0.35 * SR); tt = np.arange(n) / SR
            ruido = np.random.default_rng(1).standard_normal(n)
            ruido = np.convolve(ruido, np.ones(40) / 40, mode="same")
            audio[s:s + n] += 0.5 * ruido * np.sin(np.pi * tt / 0.35)
        inicio += e["dur"] - T
    audio = audio / max(1e-9, np.abs(audio).max()) * 0.8
    pcm = (audio * 32767).astype(np.int16)
    with wave.open(ruta, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())


def main():
    carpeta, salida = sys.argv[1], sys.argv[2]
    escenas = json.load(open(os.path.join(carpeta, "escenas.json")))
    entradas, filtros = [], []
    for e in escenas:
        entradas += ["-loop", "1", "-framerate", "30", "-t", f"{e['dur']:.2f}", "-i", e["png"]]
    # Cadena de fundidos entre escenas, con un leve zoom de entrada
    for i in range(len(escenas)):
        filtros.append(f"[{i}:v]scale=1080:1920,format=yuv420p,setsar=1[v{i}]")
    actual, offset = "v0", 0.0
    for i in range(1, len(escenas)):
        offset += escenas[i - 1]["dur"] - T
        estilo = "fade" if escenas[i].get("tick") else "slideleft" if escenas[i].get("whoosh") else "fade"
        filtros.append(f"[{actual}][v{i}]xfade=transition={estilo}:duration={T}:offset={offset:.2f}[x{i}]")
        actual = f"x{i}"
    total = offset + escenas[-1]["dur"]
    wav = os.path.join(carpeta, "audio.wav")
    sintetizar(escenas, total, wav)
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *entradas, "-i", wav,
           "-filter_complex", ";".join(filtros), "-map", f"[{actual}]", "-map", f"{len(escenas)}:a",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", "30",
           "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", salida]
    subprocess.run(cmd, check=True)
    print(f"{salida}: {total:.1f} s")


if __name__ == "__main__":
    main()
