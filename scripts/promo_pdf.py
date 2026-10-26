"""Promoción del PDF PAES M1 (desde el 26-oct-2026).

- decorar(video_in, video_out): agrega a un Reel la franja "PDF PAES M1 · Link en la bio" durante todo el video
  y una tarjeta final de 2,5 s con el PDF y el precio.
- PROMO_TEXTO: línea que va al comienzo del texto de cada post.
- promo_pendiente(): el video promocional programado para este horario (promo/plan.json), si corresponde.
- historia_del_dia(): imagen JPG de la historia diaria "Faltan N días" (scripts/historia_pdf.py la publica).
Para apagar toda la promoción: poner "activo": false en promo/config.json.
"""
import json, os, subprocess, datetime
from zoneinfo import ZoneInfo

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMO = os.path.join(RAIZ, "promo")
CHILE = ZoneInfo("America/Santiago")
FECHA_PAES = datetime.date(2026, 11, 30)


def config():
    try:
        return json.load(open(os.path.join(PROMO, "config.json"), encoding="utf-8"))
    except Exception:
        return {"activo": False}


def activo():
    c = config()
    return c.get("activo", False) and datetime.datetime.now(CHILE).date() <= datetime.date.fromisoformat(c.get("hasta", "2026-11-30"))


def promo_texto():
    return config().get("texto_post", "") if activo() else ""


def inicio_solucion(video):
    """Segundo en que empieza la solución (primer cuadro de fondo claro, el 'cuaderno'). None si no hay."""
    try:
        r = subprocess.run(["ffmpeg", "-v", "error", "-i", video, "-vf", "fps=4,scale=16:28,format=gray",
                            "-f", "rawvideo", "-"], capture_output=True, check=True)
        n = 16 * 28
        datos = r.stdout
        for i in range(len(datos) // n):
            cuadro = datos[i * n:(i + 1) * n]
            if sum(cuadro) / n > 150:
                return i / 4
    except Exception as e:
        print(f"::warning::No se pudo detectar el inicio de la solución ({e})")
    return None


# La franja va bajo la barra superior de Instagram (zona segura) y dentro del recorte 3:4 de la grilla del perfil.
Y_FRANJA = 250


def decorar(video_in, video_out):
    """Franja (solo mientras se muestra el problema) + tarjeta final. Si algo falla, deja el video original."""
    if not activo():
        return video_in
    franja, fin = os.path.join(PROMO, "franja.png"), os.path.join(PROMO, "fin.png")
    t = inicio_solucion(video_in)
    hasta = f":enable='lt(t,{max(t - 0.2, 0):.2f})'" if t is not None else ""
    try:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video_in, "-i", franja, "-loop", "1", "-t", "2.5", "-i", fin,
                        "-f", "lavfi", "-t", "2.5", "-i", "anullsrc=r=44100:cl=mono",
                        "-filter_complex",
                        f"[0:v]scale=1080:1920,fps=30,setsar=1[b];[b][1:v]overlay=0:{Y_FRANJA}{hasta}[v0];"
                        "[2:v]scale=1080:1920,fps=30,setsar=1,format=yuv420p[v1];"
                        "[0:a]aresample=44100,aformat=channel_layouts=mono[a0];[3:a]aformat=channel_layouts=mono[a1];"
                        "[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]",
                        "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "21", "-pix_fmt", "yuv420p",
                        "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", video_out], check=True)
        return video_out
    except Exception as e:
        print(f"::warning::No se pudo agregar la promoción al video ({e}); va sin ella")
        return video_in


def _publicados():
    f = os.path.join(PROMO, "publicados.json")
    return json.load(open(f)) if os.path.exists(f) else []


def promo_pendiente():
    """Devuelve la entrada de promo/plan.json que toca ahora (misma fecha, hora ya alcanzada) y no se ha publicado."""
    if not activo():
        return None
    try:
        plan = json.load(open(os.path.join(PROMO, "plan.json"), encoding="utf-8"))
    except Exception:
        return None
    ahora = datetime.datetime.now(CHILE)
    hechos = set(_publicados())
    for e in plan:
        if e["video"] in hechos:
            continue
        if e["fecha"] == ahora.date().isoformat() and ahora.hour >= e["hora"]:
            return e
    return None


def marcar_publicado(e, media_id):
    f = os.path.join(PROMO, "publicados.json")
    hechos = _publicados() + [e["video"]]
    json.dump(hechos, open(f, "w"), indent=1)
    reg = os.path.join(PROMO, "registro.json")
    r = json.load(open(reg)) if os.path.exists(reg) else []
    r.append({"video": e["video"], "media_id": media_id, "fecha_utc": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")})
    json.dump(r, open(reg, "w"), indent=1)


def dias_para_paes():
    return (FECHA_PAES - datetime.datetime.now(CHILE).date()).days
