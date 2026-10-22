"""Reel con voz: problema 15 s con musica rock + hoja de cuaderno donde un lapiz escribe
la solucion mientras una voz femenina la explica.

Uso: python3 scripts/armar_reel_voz.py post.json salida.mp4
Requiere: node (render/), ffmpeg, piper-tts y el modelo de voz en VOZ_MODELO (.onnx).
"""
import json
import math
import os
import subprocess
import sys
import tempfile
import wave

import numpy as np
from PIL import Image, ImageDraw

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SR = 44100
FPS = 30
VOZ = os.environ.get("VOZ_MODELO", os.path.join(RAIZ, "voces", "es_MX-claude-high.onnx"))


# ---------------------------------------------------------------- audio
def leer_wav(ruta):
    with wave.open(ruta) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
        sr = w.getframerate()
    if sr != SR:  # remuestreo lineal simple
        t = np.arange(int(len(x) * SR / sr)) / SR
        x = np.interp(t, np.arange(len(x)) / sr, x)
    return x


def hablar(texto, ruta):
    subprocess.run([sys.executable, "-m", "piper", "-m", VOZ, "-f", ruta, "--length-scale", "0.85", "--sentence-silence", "0.15"],
                   input=texto.encode(), check=True, capture_output=True)
    return leer_wav(ruta)


def rock(total, bpm=140):
    t = np.arange(int(total * SR)) / SR
    y = np.zeros_like(t)
    beat = 60 / bpm
    rng = np.random.default_rng(7)

    def golpe(inicio, sonido):
        s = int(inicio * SR)
        n = min(len(sonido), len(y) - s)
        if n > 0:
            y[s:s + n] += sonido[:n]

    n_kick = int(0.25 * SR); tk = np.arange(n_kick) / SR
    kick = 0.9 * np.sin(2 * np.pi * (55 + 90 * np.exp(-tk * 30)) * tk) * np.exp(-tk * 9)
    n_sn = int(0.22 * SR); ts = np.arange(n_sn) / SR
    snare = (0.45 * rng.standard_normal(n_sn) + 0.35 * np.sin(2 * np.pi * 190 * ts)) * np.exp(-ts * 16)
    n_hh = int(0.05 * SR); th = np.arange(n_hh) / SR
    hh = rng.standard_normal(n_hh); hh = (hh - np.convolve(hh, np.ones(6) / 6, "same")) * 0.18 * np.exp(-th * 60)
    # Riff de guitarra con power chords distorsionados (Mi - Mi - Do - Re por compas)
    raices = [82.41, 82.41, 65.41, 73.42]
    n_g = int(beat / 2 * SR); tg = np.arange(n_g) / SR
    k = 0
    tiempo = 0.0
    while tiempo < total:
        compas = int(tiempo / (4 * beat))
        f = raices[compas % 4]
        if k % 8 in (0, 4):
            golpe(tiempo, kick)
        if k % 8 in (2, 6):
            golpe(tiempo, snare)
        golpe(tiempo, hh)
        onda = sum(((tg * fr) % 1.0) * 2 - 1 for fr in (f, f * 1.5, f * 2))
        acento = 1.0 if k % 2 == 0 else 0.7
        guitarra = np.tanh(6 * onda) * 0.22 * acento * np.exp(-tg * (3 if k % 8 == 0 else 7))
        golpe(tiempo, guitarra)
        tiempo += beat / 2
        k += 1
    y = np.convolve(y, np.ones(3) / 3, "same")
    return y / max(1e-9, np.abs(y).max())


# ---------------------------------------------------------------- lapiz
def hacer_lapiz():
    L = 260
    im = Image.new("RGBA", (L, L), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # lapiz horizontal con la punta en (0, 30); luego se rota
    d.polygon([(0, 30), (34, 14), (34, 46)], fill=(230, 196, 150, 255))   # madera
    d.polygon([(0, 30), (12, 25), (12, 35)], fill=(40, 40, 40, 255))      # mina
    d.rectangle([34, 14, 190, 46], fill=(245, 190, 50, 255))               # cuerpo
    d.line([(34, 30), (190, 30)], fill=(220, 160, 30, 255), width=3)
    d.rectangle([190, 12, 210, 48], fill=(170, 170, 180, 255))             # metal
    d.rounded_rectangle([208, 12, 245, 48], radius=10, fill=(240, 130, 150, 255))  # goma
    rot = im.rotate(35, resample=Image.BICUBIC, center=(0, 30), expand=False, translate=(0, 160))
    return rot, (0, 190)  # imagen y posicion de la punta dentro de ella


def main():
    post_json, salida = sys.argv[1], sys.argv[2]
    post = json.load(open(post_json, encoding="utf-8"))
    chrome = os.environ.get("CHROME")
    tmp = tempfile.mkdtemp(prefix="reelvoz_")
    env = {**os.environ, "REEL_MODO": "problema"}

    # 1) Escenas del problema (gancho + 15 s de cuenta regresiva)
    subprocess.run(["node", os.path.join(RAIZ, "render", "reel.js"), post_json, os.path.join(tmp, "prob")], check=True, env=env, capture_output=True)
    escenas = json.load(open(os.path.join(tmp, "prob", "escenas.json")))
    lista = os.path.join(tmp, "prob.txt")
    with open(lista, "w") as f:
        for e in escenas:
            dur = 1.0 if e["tick"] else e["dur"]
            f.write(f"file '{e['png']}'\nduration {dur}\n")
        f.write(f"file '{escenas[-1]['png']}'\n")
    t_prob = sum(1.0 if e["tick"] else e["dur"] for e in escenas)
    v_prob = os.path.join(tmp, "prob.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lista,
                    "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-crf", "20", "-t", f"{t_prob:.2f}", v_prob], check=True)

    # 2) Hoja de cuaderno
    subprocess.run(["node", os.path.join(RAIZ, "render", "pizarra.js"), post_json, os.path.join(tmp, "hoja")], check=True, capture_output=True)
    hoja = json.load(open(os.path.join(tmp, "hoja", "pizarra.json")))
    vacia = Image.open(os.path.join(tmp, "hoja", "vacia.png")).convert("RGB")
    llena = Image.open(os.path.join(tmp, "hoja", "llena.png")).convert("RGB")

    # 3) Voz por bloque y linea de tiempo
    bloques = [p["voz"] for p in post["pizarra"]["pasos"]] + [post["pizarra"]["cierre"]["voz"]]
    voces = [hablar(txt, os.path.join(tmp, f"voz{i}.wav")) for i, txt in enumerate(bloques)]
    t = 0.8  # tiempo para escribir el titulo antes de hablar
    plan = [("titulo", [hoja["h1"]], 0.15, 0.9)]
    inicios_voz = []
    for i, v in enumerate(voces):
        dur = len(v) / SR
        inicios_voz.append(t)
        rects = hoja["pasos"][i]
        escribir = dur * 0.85 if i < len(voces) - 1 else min(2.2, dur * 0.6)
        plan.append(("paso", rects, t, escribir))
        t += dur + 0.2
    t_pie = t
    t_hoja = t + 1.2

    # 4) Cuadros de la hoja con el lapiz
    lapiz, punta = hacer_lapiz()
    v_hoja = os.path.join(tmp, "hoja.mp4")
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1080x1920",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", v_hoja], stdin=subprocess.PIPE)
    lienzo = vacia.copy()
    n_frames = int(t_hoja * FPS)
    for fr in range(n_frames):
        ahora = fr / FPS
        pos_lapiz = None
        for _, rects, ini, dur in plan:
            if ahora < ini:
                continue
            total_w = sum(r["w"] for r in rects)
            avance = min(1.0, (ahora - ini) / dur) * total_w
            for r in rects:
                if avance <= 0:
                    break
                w = int(min(r["w"], avance))
                caja = (r["x"], r["y"], r["x"] + w, r["y"] + r["h"])
                lienzo.paste(llena.crop(caja), caja[:2])
                if 0 < avance < r["w"] or (avance >= r["w"] and r is rects[-1] and ahora - ini < dur):
                    ondula = 10 * math.sin(ahora * 38)
                    pos_lapiz = (r["x"] + w, int(r["y"] + r["h"] * 0.7 + ondula))
                avance -= r["w"]
        if ahora >= t_pie:
            caja = (hoja["pie"]["x"], hoja["pie"]["y"], hoja["pie"]["x"] + hoja["pie"]["w"], hoja["pie"]["y"] + hoja["pie"]["h"])
            lienzo.paste(llena.crop(caja), caja[:2])
        cuadro = lienzo.copy()
        if pos_lapiz:
            cuadro.paste(lapiz, (pos_lapiz[0] - punta[0], pos_lapiz[1] - punta[1]), lapiz)
        ff.stdin.write(cuadro.tobytes())
    ff.stdin.close(); ff.wait()

    # 5) Audio: rock fuerte en el problema, luego bajo; voz encima
    X = 0.4  # transicion
    total = t_prob + t_hoja - X
    musica = rock(total)
    tt = np.arange(len(musica)) / SR
    vol = np.where(tt < t_prob - X, 0.85, 0.85 - (0.85 - 0.10) * np.clip((tt - (t_prob - X)) / 0.8, 0, 1))
    mezcla = musica * vol
    fin = tt > total - 1.2
    mezcla[fin] *= np.linspace(1, 0, fin.sum())
    for ini, v in zip(inicios_voz, voces):
        s = int((t_prob - X + ini) * SR)
        n = min(len(v), len(mezcla) - s)
        mezcla[s:s + n] += 0.95 * v[:n]
    mezcla = mezcla / max(1e-9, np.abs(mezcla).max()) * 0.9
    wav = os.path.join(tmp, "mezcla.wav")
    with wave.open(wav, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mezcla * 32767).astype(np.int16).tobytes())

    # 6) Unir
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", v_prob, "-i", v_hoja, "-i", wav, "-filter_complex",
                    f"[0:v][1:v]xfade=transition=slideup:duration={X}:offset={t_prob - X:.2f}[v]",
                    "-map", "[v]", "-map", "2:a", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-r", "30",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", salida], check=True)
    print(f"{salida}: {total:.1f} s")


if __name__ == "__main__":
    main()
