"""Videos especiales (1 de cada 4 publicaciones). Se arman al momento de publicar.

Formatos (campo "formato" del post.json):
  sketch : escenas comicas con personajes (Benja / Profe Pi), carteles y efectos; musica de payaso.
           Opcional: "problema" al final (cuenta regresiva 15 s + solucion de la Profe).
  dato   : la Profe Pi explica una propiedad o atajo en la pizarra ("pizarra_dato").
  cuenta : "Faltan N dias para la PAES" (N se calcula hoy) + tip en la pizarra.

Uso: python3 scripts/armar_especial.py post.json salida.mp4
Entorno: CHROME, KOKORO_DIR (kokoro-v1.0.onnx y voices-v1.0.bin).
"""
import datetime, glob, json, math, os, subprocess, sys, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RENDER = os.path.join(RAIZ, "render")
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
import musica_rock

SR, FPS, W, H = 44100, 30, 1080, 1920
FECHA_PAES = datetime.date(2026, 11, 30)
L = "ABCDE"
TMP = "/tmp/especial"; os.makedirs(TMP, exist_ok=True)
KATEX_CSS = os.path.join(RENDER, "node_modules/katex/dist/katex.min.css")
CAVEAT = os.path.join(RENDER, "node_modules/@fontsource/caveat/files/caveat-latin-700-normal.woff2")
_f = sorted(glob.glob("/usr/share/fonts/**/Inter*Black*.otf", recursive=True) + glob.glob("/usr/share/fonts/**/Inter*Black*.ttf", recursive=True))
F_BOLD = _f[0] if _f else (glob.glob("/usr/share/fonts/**/DejaVuSans-Bold.ttf", recursive=True) or [None])[0]
HANDLE = "@" + json.load(open(os.path.join(RAIZ, "config.json")))["handle"]
VOCES = {"benja": "em_alex", "profe": "ef_dora", "narrador": "em_santa"}


# ------------------------------------------------------------------ utilidades
def numero_en_palabras(n):
    u = "cero uno dos tres cuatro cinco seis siete ocho nueve diez once doce trece catorce quince dieciséis diecisiete dieciocho diecinueve veinte".split()
    if n <= 20: return u[n]
    if n < 30: return "veinti" + ["", "uno", "dós", "trés", "cuatro", "cinco", "séis", "siete", "ocho", "nueve"][n - 20]
    dec = {3: "treinta", 4: "cuarenta", 5: "cincuenta", 6: "sesenta", 7: "setenta", 8: "ochenta", 9: "noventa"}
    if n < 100: return dec[n // 10] + ("" if n % 10 == 0 else " y " + u[n % 10])
    return str(n)


def tex(s):
    out = subprocess.run(["node", "-e", """
const katex=require(process.argv[1]);let s=require('fs').readFileSync(0,'utf8');
s=s.replace(/\\\\\\$/g,'\\u0000').replace(/\\$\\$([\\s\\S]+?)\\$\\$/g,(_,m)=>katex.renderToString(m,{displayMode:true}))
 .replace(/\\$([^$]+?)\\$/g,(_,m)=>katex.renderToString(m)).replace(/\\u0000/g,'$');process.stdout.write(s);""",
        os.path.join(RENDER, "node_modules/katex")], input=s.encode(), capture_output=True, check=True)
    return out.stdout.decode()


CSS = f"""
@font-face{{font-family:Tiza;src:url(file://{CAVEAT}) format('woff2')}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:transparent}}
.pizarra{{position:absolute;inset:0;background:#5B3A1E;padding:34px}}
.verde{{position:absolute;inset:34px;border-radius:10px;background:radial-gradient(ellipse at 30% 20%,rgba(255,255,255,.07),transparent 55%),#1F4D3A;box-shadow:inset 0 0 80px rgba(0,0,0,.45)}}
.c{{position:absolute;left:90px;right:90px;top:120px;font-family:Tiza,cursive;color:#F5F5EE}}
.katex{{color:#F5F5EE;white-space:nowrap}}
.tag{{font-family:Tiza;font-size:44px;color:#FDE68A}}
.tit{{font-size:96px;color:#FDE68A;line-height:1.05;margin:20px 0 34px}}
.enun{{font-size:60px;line-height:1.18}}
.opts{{margin-top:36px;display:grid;grid-template-columns:1fr 1fr;gap:12px 30px;font-size:60px}}
.opt b{{color:#FDE68A;margin-right:14px}}
.linea{{display:block;font-size:70px;line-height:1.14}}
.linea.f{{font-size:60px;padding:8px 0 4px 40px}}
.paso{{margin-bottom:38px}}
.caja{{display:inline-block;white-space:nowrap;font-size:76px;color:#FDE68A;padding:6px 36px;border:6px solid #FDE68A;border-radius:46% 54% 50% 50%/60% 45% 55% 40%}}
.cartel{{position:absolute;left:60px;right:60px;text-align:center;font-family:Inter,sans-serif;font-weight:900}}
.cartel .a{{display:inline-block;background:#FDE68A;color:#111;line-height:1.08;padding:24px 34px;border-radius:26px;transform:rotate(-2deg);box-shadow:0 14px 0 #B45309}}
.cartel .b{{margin-top:34px;color:#111;font-size:60px}}
.fin{{position:absolute;left:60px;right:60px;top:1225px;text-align:center;font-family:Inter,sans-serif;font-weight:900}}
.fin .a{{display:inline-block;background:#F43F5E;color:#fff;font-size:70px;padding:22px 34px;border-radius:24px;transform:rotate(2deg)}}
.fin .b{{margin-top:30px;color:#FDE68A;font-size:54px}}
"""
FONDOS = {
    "aula": """<div style="position:absolute;inset:0;background:linear-gradient(#F3E9D2 0 70%,#B98B5E 70%)"></div>
      <div style="position:absolute;left:90px;right:90px;top:140px;height:420px;background:#1F4D3A;border:22px solid #7A5230;border-radius:8px;
        font-family:Tiza;color:#F5F5EE;font-size:96px;text-align:center;padding-top:70px">PAES 2026<div style="font-size:56px;color:#FDE68A">Sala 12</div></div>""",
    "pieza": """<div style="position:absolute;inset:0;background:linear-gradient(#C7D2FE 0 68%,#8B5CF6 68%)"></div>
      <div style="position:absolute;left:120px;top:220px;width:300px;height:380px;background:#E0F2FE;border:18px solid #fff;border-radius:10px"></div>
      <div style="position:absolute;right:110px;top:260px;width:330px;height:220px;background:#FDE68A;border-radius:16px;font-family:Tiza;font-size:64px;color:#7C2D12;text-align:center;padding-top:40px">¡Estudiar<br>PAES!</div>""",
    "pizarra": '<div class="pizarra"><div class="verde"></div></div>',
}


def pagina(cuerpo, fondo=None):
    f = FONDOS.get(fondo, "") if fondo else ""
    return f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="file://{KATEX_CSS}"><style>{CSS}</style></head><body>{f}{cuerpo}</body></html>'


def renderizar(trabajos):
    json.dump(trabajos, open(f"{TMP}/trabajos.json", "w"))
    subprocess.run(["node", os.path.join(RENDER, "html2png.js"), f"{TMP}/trabajos.json"], check=True, env={**os.environ, "RENDER_DIR": RENDER})


# ------------------------------------------------------------------ audio
_KK = None
def voz(texto, quien, vel=1.05):
    global _KK
    if _KK is None:
        from kokoro_onnx import Kokoro
        d = os.environ["KOKORO_DIR"]; _KK = Kokoro(os.path.join(d, "kokoro-v1.0.onnx"), os.path.join(d, "voices-v1.0.bin"))
    s, sr = _KK.create(texto, voice=VOCES.get(quien, quien), speed=vel, lang="es")
    t = np.arange(int(len(s) * SR / sr)) / SR
    return np.interp(t, np.arange(len(s)) / sr, s).astype(np.float64) * 0.9


def nota(f, dur, forma="tri", dec=8.0, vib=0.0):
    t = np.arange(int(dur * SR)) / SR
    fase = 2 * np.pi * f * t + (vib * np.sin(2 * np.pi * 6 * t) if vib else 0)
    y = 2 / np.pi * np.arcsin(np.sin(fase)) if forma == "tri" else (2 * ((f * t) % 1) - 1 if forma == "saw" else np.sin(fase) + 0.4 * np.sin(2 * fase))
    return y * np.exp(-t * dec) * np.minimum(1, t / 0.005)


def musica_payaso(total, semilla=0):
    """Musica de circo original: tuba oom-pah, cromatismos y melodia de organillo."""
    rng = np.random.default_rng(abs(int(str(semilla).encode().hex(), 16)) % (2 ** 32))
    bpm = int(rng.integers(150, 176)); b = 60 / bpm
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    base = int(rng.choice([60, 62, 65, 67]))
    y = np.zeros(int(total * SR))
    def poner(s, ini, g):
        i = int(ini * SR); n = min(len(s), len(y) - i)
        if n > 0: y[i:i + n] += g * s[:n]
    # motivo cromatico descendente/ascendente al azar (estilo circo, original)
    motivos = [[7, 6, 5, 4, 5, 6, 7, None], [12, 11, 10, 9, 7, None, 5, 4], [0, 1, 2, 3, 4, None, 7, None], [4, 3, 4, 7, 12, 11, 12, None]]
    m1, m2 = motivos[rng.integers(4)], motivos[rng.integers(4)]
    t, k = 0.0, 0
    while t < total:
        compas = k // 4
        raiz = base - 12 + [0, 7, 0, 5][compas % 4]
        if k % 2 == 0: poner(nota(hz(raiz - 12), b * 0.8, "sin", 9), t, 0.55)   # tuba
        else:
            for i in (0, 4, 7): poner(nota(hz(raiz + 12 + i), b * 0.4, "tri", 20), t, 0.1)
        mot = m1 if (compas // 2) % 2 == 0 else m2
        m = mot[(k * 2) % 8]
        if m is not None: poner(nota(hz(base + 12 + m), b * 0.45, "tri", 6, vib=0.6), t, 0.2)
        m = mot[(k * 2 + 1) % 8]
        if m is not None: poner(nota(hz(base + 12 + m), b * 0.45, "tri", 6, vib=0.6), t + b / 2, 0.2)
        if k % 8 == 7: poner(nota(1800, 0.05, "sin", 60), t + b / 2, 0.2)       # bocina chica
        t += b; k += 1
    return y / np.abs(y).max()


def efecto(nombre):
    t = lambda d: np.arange(int(d * SR)) / SR
    if nombre == "boing":
        x = t(0.4); return np.sin(2 * np.pi * (180 + 220 * np.exp(-x * 8)) * x + 6 * np.sin(2 * np.pi * 18 * x)) * np.exp(-x * 6) * 0.6
    if nombre == "trombon":
        y = np.concatenate([nota(f, d, "saw", 1.2 if d > 1 else 2.5) for f, d in [(233.1, .45), (220, .45), (207.7, .45), (196, 1.3)]])
        return np.convolve(y, np.ones(18) / 18, "same") * 0.8
    if nombre == "redoble":
        n = int(1.2 * SR); y = np.zeros(n); rng = np.random.default_rng(5)
        for tt in np.arange(0, 1.2, 0.045):
            s = int(tt * SR); m = min(int(0.04 * SR), n - s)
            y[s:s + m] += (0.2 + 0.8 * tt / 1.2) * rng.standard_normal(m) * np.exp(-np.arange(m) / SR * 60)
        return y * 0.5
    if nombre == "tictac":
        y = np.zeros(int(1.6 * SR))
        for k, tt in enumerate(np.arange(0, 1.6, 0.12)):
            s = nota(2000 if k % 2 else 1400, 0.03, "sin", 80); i = int(tt * SR); y[i:i + len(s)] += s[:len(y) - i] * 0.5
        return y
    if nombre == "ding":
        x = t(1.0); return sum(a * np.sin(2 * np.pi * f * x) for f, a in ((1046.5, .25), (1318.5, .18), (1568, .12))) * np.exp(-x * 4)
    if nombre == "bocina":
        x = t(0.5); return np.sign(np.sin(2 * np.pi * 330 * x)) * 0.25 * np.exp(-x * 3) + np.sign(np.sin(2 * np.pi * 440 * x)) * 0.15 * np.exp(-x * 3)
    return np.zeros(1)


# ------------------------------------------------------------------ personajes
def cargar_sprites():
    P = os.path.join(RENDER, "personajes")
    return {q: {os.path.basename(f)[:-4]: Image.open(f) for f in glob.glob(f"{P}/{q}/*.png")} for q in ("benja", "profe")}


EXPRESIONES = {  # personaje -> expresion -> (ojos, boca_fija o None, extras)
    "benja": {"feliz": ("a", None, ()), "nervioso": ("s", 3, ("sudor",)), "llora": ("c", 3, ("lagrimas",)), "sorpresa": ("s", 2, ())},
    "profe": {"feliz": ("a", None, ()), "nervioso": ("a", 0, ()), "llora": ("c", 0, ()), "sorpresa": ("a", 2, ())},
}


def personaje(spr, quien, expresion, boca_habla, parpadeo, esc):
    ojos, boca_fija, extras = EXPRESIONES[quien].get(expresion, EXPRESIONES[quien]["feliz"])
    s = spr[quien]
    im = s["cuerpo"].copy()
    o = "c" if (parpadeo and ojos == "a") else ojos
    im.alpha_composite(s.get(f"ojos_{o}", s["ojos_a"]))
    b = boca_habla if (boca_habla > 0 or boca_fija is None) else boca_fija
    if quien == "profe": b = min(b, 2)
    im.alpha_composite(s[f"boca{b}"])
    for e in extras:
        if e in s: im.alpha_composite(s[e])
    return im.resize((int(560 * esc), int(760 * esc)), Image.LANCZOS)


# ------------------------------------------------------------------ armado
def main():
    post = json.load(open(sys.argv[1], encoding="utf-8")); salida = sys.argv[2]
    fmt = post.get("formato", "sketch")
    spr = cargar_sprites()
    trabajos, escenas = [], []

    # --- escenas de sketch
    if fmt == "sketch":
        for i, e in enumerate(post["escenas"]):
            if e.get("cartel"):
                tam = e.get("tam", 84 if len(e["cartel"]) < 26 else 66)
                sub = f'<div class="b">{e["subcartel"]}</div>' if e.get("subcartel") else ""
                trabajos.append({"html": pagina(f'<div class="cartel" style="top:{e.get("y_cartel", 860)}px"><div class="a" style="font-size:{tam}px">{e["cartel"]}</div>{sub}</div>'),
                                 "out": f"{TMP}/cartel{i}.png", "w": W, "h": H, "transparente": True})
        for f in {e.get("fondo", "aula") for e in post["escenas"]}:
            trabajos.append({"html": pagina("", f), "out": f"{TMP}/fondo_{f}.png", "w": W, "h": H})

    # --- pizarra (dato / cuenta / solucion del problema)
    pz, titulo, intro_voz = None, None, None
    if fmt in ("dato", "cuenta"):
        pz = post["pizarra_dato"]
        if fmt == "cuenta":
            dias = (FECHA_PAES - datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3))).date()).days
            titulo = f"⏳ Faltan {dias} días"
            intro_voz = f"Faltan {numero_en_palabras(dias)} días para la PAES. " + pz.get("intro_voz", "")
            post["_cartel_intro"] = f"⏳ FALTAN {dias} DÍAS<br>PARA LA PAES"
        else:
            titulo = pz.get("titulo", "💡 Dato PAES")
            intro_voz = pz.get("intro_voz", "")
            post["_cartel_intro"] = pz.get("cartel", "💡 DATO PAES")
        trabajos.append({"html": pagina(f'<div class="cartel" style="top:300px"><div class="a" style="font-size:88px">{post["_cartel_intro"]}</div>'
                                        f'<div class="b" style="color:#fff">{pz.get("subtitulo", "")}</div></div>', "pizarra"), "out": f"{TMP}/intro.png", "w": W, "h": H})
    prob = post.get("problema")
    if prob:
        pz = prob["pizarra"]; titulo = "Solución"
        opts = "".join(f'<div class="opt"><b>{L[i]})</b>{tex(a)}</div>' for i, a in enumerate(prob["alternativas"]))
        trabajos.append({"html": pagina(f'<div class="c"><div class="tag">PAES {prob.get("nivel","M1")} · {HANDLE}</div><div class="tit">¿Cuál es?</div>'
                                        f'<div class="enun">{tex(prob["enunciado"])}</div><div class="opts">{opts}</div></div>', "pizarra"),
                         "out": f"{TMP}/problema.png", "w": W, "h": H})
    if pz:
        pasos = "".join('<div class="paso" data-bloque>' + "".join(
            f"<span class='linea {'f' if l.strip().startswith('$') else ''}'>{tex(l)}</span>" for l in p["lineas"]) + '</div>' for p in pz["pasos"])
        caja = f'<div data-bloque class="caja">{L[prob["correcta"]]}) {tex(prob["alternativas"][prob["correcta"]])}</div>' if prob else \
               (f'<div data-bloque class="caja">{pz["remate"]}</div>' if pz.get("remate") else "")
        trabajos.append({"html": pagina(f'<div class="c"><div class="tag">{HANDLE}</div><div class="tit" data-bloque><span class="linea" style="font-size:96px">{titulo}</span></div>{pasos}{caja}</div>', "pizarra"),
                         "out": f"{TMP}/sol.png", "w": W, "h": H, "rects": True, "oculto": ".c{visibility:hidden}"})
    trabajos.append({"html": pagina(f'<div class="fin"><div class="a">{post.get("fin", "¿Te sirvió? Comenta 👇")}</div><div class="b">Sigue a {HANDLE}</div></div>'),
                     "out": f"{TMP}/fin.png", "w": W, "h": H, "transparente": True})
    renderizar(trabajos)
    img = lambda n: Image.open(f"{TMP}/{n}.png").convert("RGBA")

    # --- voces y linea de tiempo
    pistas = {"benja": None, "profe": None, "narrador": None}
    largo = 0.0
    def reservar(n):
        nonlocal largo
        largo = max(largo, n)
    voces = []  # (inicio, audio, quien, texto)
    linea = []  # (ini, fin, tipo, datos)
    t = 0.0
    if fmt == "sketch":
        for i, e in enumerate(post["escenas"]):
            ini = t; ent = 0.8 if e.get("entrada") else 0.0
            v = voz(e["voz"], e.get("personaje", "benja"), e.get("vel", 1.05)) if e.get("voz") else None
            t_voz = ini + ent + e.get("pausa", 0.15)
            dur = max(e.get("dur_min", 1.6), (t_voz - ini) + (len(v) / SR if v is not None else 0) + 0.35)
            if v is not None: voces.append((t_voz, v, e.get("personaje", "benja"), e["voz"]))
            linea.append((ini, ini + dur, "escena", {**e, "_i": i}))
            t += dur
    if fmt in ("dato", "cuenta"):
        vi = voz(intro_voz, "profe", 1.05)
        voces.append((0.3, vi, "profe", intro_voz))
        dur = len(vi) / SR + 0.7
        linea.append((t, t + dur, "intro", {})); t += dur
    if prob:
        linea.append((t, t + 15.0, "problema", {})); t += 15.0
    plan = []
    if pz:
        rects = json.load(open(f"{TMP}/sol.png.json"))
        t0 = t; plan.append((rects[0], t0 + 0.1, 0.6)); t = t0 + 0.7
        bloques = [p["voz"] for p in pz["pasos"]] + ([pz["cierre"]["voz"]] if pz.get("cierre") else [])
        for i, b in enumerate(bloques):
            v = voz(b, "profe", 1.08); voces.append((t, v, "profe", b))
            if i < len(pz["pasos"]): plan.append((rects[1 + i], t, len(v) / SR * 0.85))
            elif len(rects) > len(pz["pasos"]) + 1: plan.append((rects[-1], t, 1.6))
            t += len(v) / SR + 0.2
        if not pz.get("cierre") and len(rects) > len(pz["pasos"]) + 1:
            plan.append((rects[-1], t, 1.4)); t += 1.4
        linea.append((t0, t + 2.0, "pizarra", {})); t += 2.0
    total = t

    # --- audio
    estilo = post.get("musica", "payaso" if fmt == "sketch" else "rock")
    mus = musica_payaso(total, post.get("id", 0)) if estilo == "payaso" else musica_rock.rock_variado(total, post.get("id", 0))
    tt = np.arange(len(mus)) / SR
    vol = np.full(len(mus), 0.10)
    for ini, fin, tipo, d in linea:
        m = (tt >= ini) & (tt < fin)
        vol[m] = {"escena": d.get("vol_musica", 0.25), "intro": 0.2, "problema": 0.6, "pizarra": 0.09}[tipo]
    vol = np.convolve(vol, np.ones(int(0.25 * SR)) / int(0.25 * SR), "same")
    mezcla = mus * vol
    hablan = {q: np.zeros(len(mus)) for q in ("benja", "profe", "narrador")}
    for ini, v, q, _ in voces:
        i = int(ini * SR); n = min(len(v), len(mezcla) - i); hablan[q][i:i + n] += v[:n]
    for ini, fin, tipo, d in linea:
        if tipo == "escena" and d.get("efecto"):
            s = efecto(d["efecto"]); i = int((ini + d.get("t_efecto", 0.0)) * SR); n = min(len(s), len(mezcla) - i)
            if n > 0: mezcla[i:i + n] += 0.8 * s[:n]
    for q in hablan: mezcla += hablan[q]
    mezcla[-SR:] *= np.linspace(1, 0, SR)
    mezcla = mezcla / np.abs(mezcla).max() * 0.9
    with wave.open(f"{TMP}/mezcla.wav", "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mezcla * 32767).astype(np.int16).tobytes())
    def env(p):
        v = int(SR / FPS); e = np.array([np.sqrt(np.mean(p[i:i + v] ** 2)) for i in range(0, len(p), v)])
        pos = e[e > 0]; return e / (np.percentile(pos, 95) if len(pos) else 1)
    envs = {q: env(hablan[q]) for q in hablan}
    boca = lambda q, fr: (lambda e: 2 if e > 0.55 else 1 if e > 0.18 else 0)(envs[q][fr] if fr < len(envs[q]) else 0)

    # --- subtitulos
    subs = []
    for bi, (ini, v, q, txt) in enumerate(voces):
        pal = txt.split(); dd = len(v) / SR * 0.95; tot = sum(len(p) + 2 for p in pal); c = ini
        for j, p in enumerate(pal):
            du = dd * (len(p) + 2) / tot; subs.append((c, c + du, p, bi, j)); c += du
    fuente = ImageFont.truetype(F_BOLD, 62)
    def subtitulo(cuadro, ahora, y):
        idx = [i for i, x in enumerate(subs) if x[0] <= ahora < x[1] + 0.25]
        if not idx: return
        i = idx[-1]; g = i - (subs[i][4] % 4)  # grupos de 4 palabras dentro de la misma frase
        grupo = [subs[k][2] for k in range(g, min(g + 4, len(subs))) if subs[k][3] == subs[i][3]]
        dr = ImageDraw.Draw(cuadro); f = fuente
        anchos = [dr.textlength(p.upper() + "  ", font=f) for p in grupo]
        if sum(anchos) > W - 80:  # achica la letra si la frase no cabe
            f = ImageFont.truetype(F_BOLD, int(62 * (W - 80) / sum(anchos)))
            anchos = [dr.textlength(p.upper() + "  ", font=f) for p in grupo]
        x = (W - sum(anchos)) / 2
        for k, p in enumerate(grupo):
            dr.text((x, y), p.upper(), font=f, fill=(253, 230, 138) if g + k == i else (255, 255, 255), stroke_width=8, stroke_fill=(0, 0, 0)); x += anchos[k]
    def pop(cuadro, capa, ini, ahora):
        k = min(1.0, (ahora - ini) / 0.22); s = 0.5 + 0.5 * k + 0.08 * math.sin(k * math.pi)
        c = capa.resize((int(W * s), int(H * s))); cuadro.alpha_composite(c, ((W - c.width) // 2, (H - c.height) // 2))

    fondos = {f: img(f"fondo_{f}") for f in {e.get("fondo", "aula") for e in post.get("escenas", [])}} if fmt == "sketch" else {}
    carteles = {i: img(f"cartel{i}") for i, e in enumerate(post.get("escenas", [])) if e.get("cartel")}
    intro = img("intro") if fmt in ("dato", "cuenta") else None
    probimg = img("problema") if prob else None
    llena = img("sol") if pz else None; lienzo = img("sol_vacia") if pz else None
    fin = img("fin")
    fcont = ImageFont.truetype(F_BOLD, 120); fpeq = ImageFont.truetype(F_BOLD, 40)

    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-i", f"{TMP}/mezcla.wav", "-c:v", "libx264", "-crf", "21", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                           "-shortest", "-movflags", "+faststart", salida], stdin=subprocess.PIPE)
    for fr in range(int(total * FPS)):
        ahora = fr / FPS
        parp = (ahora % 3.1) < 0.12
        seg = next((x for x in linea if x[0] <= ahora < x[1]), linea[-1])
        ini, finseg, tipo, d = seg
        if tipo == "escena":
            q = d.get("personaje", "benja")
            cuadro = fondos[d.get("fondo", "aula")].copy()
            esc = d.get("escala", 1.0)
            pj = personaje(spr, q, d.get("expresion", "feliz"), boca(q, fr), parp, esc)
            x_fin = (W - pj.width) // 2; y = H - pj.height - 120
            x = x_fin
            u = (ahora - ini) / 0.8
            if d.get("entrada") and u < 1:
                desde = -pj.width if d["entrada"] in ("izquierda", "caminando") else W
                x = int(desde + (x_fin - desde) * (1 - (1 - u) ** 2))
                if d["entrada"] in ("caminando", "izquierda", "derecha"): y += int(-abs(math.sin(ahora * 14)) * 30)
            if d.get("expresion") in ("nervioso", "llora"): x += int(6 * math.sin(ahora * 50))
            cuadro.alpha_composite(pj, (x, y))
            if (d["_i"]) in carteles and ahora - ini > d.get("t_cartel", 0.3):
                if d.get("sacudir"):
                    c2 = Image.new("RGBA", (W, H)); pop(c2, carteles[d["_i"]], ini + d.get("t_cartel", 0.3), ahora)
                    cuadro.alpha_composite(c2, (int(14 * math.sin((ahora - ini) * 50) * math.exp(-(ahora - ini) * 5)), 0))
                else:
                    pop(cuadro, carteles[d["_i"]], ini + d.get("t_cartel", 0.3), ahora)
            subtitulo(cuadro, ahora, 1660)
        elif tipo == "intro":
            cuadro = intro.copy()
            cuadro.alpha_composite(personaje(spr, "profe", "feliz", boca("profe", fr), parp, 1.0), ((W - 560) // 2, H - 760 - 100))
            subtitulo(cuadro, ahora, 1720)
        elif tipo == "problema":
            t0 = finseg
            cuadro = probimg.copy()
            cuadro.alpha_composite(personaje(spr, "benja", "nervioso", 0, parp, 0.72), (10 + int(3 * math.sin(ahora * 40)), 1370))
            n = math.ceil(t0 - ahora); dr = ImageDraw.Draw(cuadro)
            pulso = 1 + 0.12 * max(0, 1 - ((t0 - ahora) % 1) * 4); r = int(110 * pulso); cx, cy = 800, 1560
            dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(239, 68, 68) if n <= 3 else (253, 230, 138))
            dr.text((cx, cy), str(n), font=fcont, fill=(17, 17, 17), anchor="mm")
            frac = (t0 - ahora) / 15.0
            dr.rounded_rectangle([90, 1260, 990, 1280], 10, fill=(255, 255, 255, 60))
            dr.rounded_rectangle([90, 1260, 90 + int(900 * frac), 1280], 10, fill=(253, 230, 138))
            dr.text((540, 1215), "¡RESPONDE ANTES DE QUE TERMINE!", font=fpeq, fill=(255, 255, 255), anchor="mm")
        else:  # pizarra con la Profe
            for rr, i0, du in plan:
                if ahora < i0: continue
                av = min(1.0, (ahora - i0) / du) * sum(b["w"] for b in rr)
                for b in rr:
                    if av <= 0: break
                    w = int(min(b["w"], av)); caja = (b["x"], b["y"], b["x"] + w, b["y"] + b["h"])
                    lienzo.paste(llena.crop(caja), caja[:2]); av -= b["w"]
            cuadro = lienzo.copy()
            cuadro.alpha_composite(personaje(spr, "profe", "feliz", boca("profe", fr), parp, 0.72), (10, 1370 + int(6 * math.sin(ahora * 3.2))))
            if ahora > total - 2.0: cuadro.alpha_composite(fin)
            else: subtitulo(cuadro, ahora, 1285)
        ff.stdin.write(cuadro.convert("RGB").tobytes())
    ff.stdin.close(); ff.wait()
    print(f"{salida}: {total:.1f} s")


if __name__ == "__main__":
    main()
