"""Voz chilena (Microsoft Edge TTS, gratis): es-CL-LorenzoNeural (hombre) y es-CL-CatalinaNeural (mujer).
sintetizar(texto, sr, quien) -> np.array float32 mono a 'sr' Hz, o None si falla (el llamador usa su voz de respaldo)."""
import asyncio, os, subprocess, tempfile
import numpy as np

VOCES = {
    "profe_h": ("es-CL-LorenzoNeural", "+0%", "+0Hz"),
    "narrador": ("es-CL-LorenzoNeural", "+4%", "+0Hz"),
    "benja": ("es-CL-LorenzoNeural", "+10%", "+18Hz"),
    "profe": ("es-CL-CatalinaNeural", "+4%", "+0Hz"),
}


def sintetizar(texto, sr, quien="profe_h"):
    if os.environ.get("SIN_VOZ_CL"):
        return None
    try:
        import edge_tts
        voz, rate, pitch = VOCES.get(quien, VOCES["profe_h"])
        tmp = tempfile.mktemp(suffix=".mp3")

        async def _go():
            await edge_tts.Communicate(texto, voz, rate=rate, pitch=pitch).save(tmp)
        for intento in range(3):
            try:
                asyncio.run(_go()); break
            except Exception:
                if intento == 2: raise
        r = subprocess.run(["ffmpeg", "-v", "error", "-i", tmp, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"], capture_output=True, check=True)
        os.remove(tmp)
        x = np.frombuffer(r.stdout, dtype=np.float32).copy()
        nz = np.where(np.abs(x) > 0.01)[0]
        if len(nz) == 0:
            return None
        x = x[max(0, nz[0] - int(0.02 * sr)): nz[-1] + int(0.08 * sr)]
        return x / max(1e-9, np.abs(x).max()) * 0.9
    except Exception as e:
        print(f"::warning::Voz chilena no disponible ({e}); se usa la voz de respaldo")
        return None
