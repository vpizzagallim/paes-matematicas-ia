"""Publica la historia diaria del PDF: "Faltan N días para la PAES" + portada + link en la bio.
La corre .github/workflows/historia-pdf.yml una vez al día (no repite si ya salió hoy)."""
import datetime, json, os, subprocess, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import promo_pdf
from PIL import Image

RAIZ, PROMO = promo_pdf.RAIZ, promo_pdf.PROMO
hoy = datetime.datetime.now(promo_pdf.CHILE).date()
reg_f = os.path.join(PROMO, "historias.json")
reg = json.load(open(reg_f)) if os.path.exists(reg_f) else []
if not promo_pdf.activo() or hoy.isoformat() in reg:
    print("Nada que hacer (promoción apagada o la historia de hoy ya salió)."); sys.exit(0)
import publicar  # usa IG_TOKEN y REPO del entorno

n = promo_pdf.dias_para_paes()
k = -(-500 // max(1, n - 1))
FRASES = [f"Si haces <b>{k} preguntas al día</b>, terminas las 500 justo antes de la PAES",
          "Formulario completo + <b>500 preguntas</b> con pauta paso a paso",
          "<b>155 gráficos</b> y figuras, como en la prueba real",
          "Todo el <b>temario oficial M1</b> en un solo PDF"]
frase = FRASES[hoy.toordinal() % len(FRASES)]
dias = "¡Mañana es la PAES!" if n == 1 else ("¡Hoy es la PAES! 💪" if n <= 0 else f"Faltan {n} días<br>para la PAES")
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>*{{margin:0;box-sizing:border-box}}body{{width:1080px;height:1920px;background:#0f1b2d;color:#fff;
font-family:Inter,'Noto Color Emoji',sans-serif;background-image:linear-gradient(#ffffff08 1px,transparent 1px),linear-gradient(90deg,#ffffff08 1px,transparent 1px);background-size:72px 72px;
display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 70px}}</style></head><body>
<div style="font-size:120px">⏳</div><div style="font-size:104px;font-weight:900;line-height:1.05">{dias}</div>
<img src="file://{PROMO}/portada.jpg" style="width:460px;margin:60px 0 50px;border-radius:12px;box-shadow:0 30px 80px #000a;transform:rotate(-3deg)">
<div style="font-size:52px;line-height:1.3;color:#e2e8f0">{frase}</div>
<div style="margin-top:60px;background:#F6B83C;color:#0f1b2d;font-size:60px;font-weight:900;padding:30px 66px;border-radius:80px">📘 PDF PAES M1 · $5.000</div>
<div style="margin-top:40px;font-size:56px;font-weight:800;color:#F6B83C">👆 Link en la bio · @mathpaes.cl</div></body></html>"""
png = "/tmp/historia_pdf.png"; jpg = f"/tmp/historia_pdf_{hoy.isoformat()}.jpg"
json.dump([{"html": html, "out": png, "w": 1080, "h": 1920}], open("/tmp/hist_job.json", "w"))
subprocess.run(["node", os.path.join(RAIZ, "render", "html2png.js"), "/tmp/hist_job.json"], check=True,
               env={**os.environ, "RENDER_DIR": os.path.join(RAIZ, "render")})
Image.open(png).convert("RGB").save(jpg, quality=90)
quedan = publicar.cupo()
if quedan is not None and quedan < 1:
    print("::notice::Sin cupo de Instagram por ahora; la historia se intenta en la próxima ejecución."); sys.exit(0)
url = publicar.subir_video(jpg, os.path.basename(jpg))
usuario = publicar.llamar("GET", "me", fields="user_id")["user_id"]
c = publicar.llamar("POST", f"{usuario}/media", media_type="STORIES", image_url=url)
publicar.esperar(c["id"])
hid = publicar.llamar("POST", f"{usuario}/media_publish", creation_id=c["id"])["id"]
print(f"Historia del PDF publicada: {hid}")
reg.append(hoy.isoformat()); json.dump(reg, open(reg_f, "w"), indent=1)
g = lambda *a: subprocess.run(["git", *a], cwd=RAIZ, check=True)
subprocess.run(["git", "add", reg_f], cwd=RAIZ, check=True)
g("-c", "user.name=publicador-paes", "-c", "user.email=publicador-paes@users.noreply.github.com", "commit", "-qm", f"Historia PDF {hoy}")
g("push", "origin", "HEAD:main")
