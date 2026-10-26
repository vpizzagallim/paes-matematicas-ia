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
PRUEBA = os.environ.get("PRUEBA") == "true"  # solo genera la imagen y la guarda en promo/prueba_historia.jpg
if not PRUEBA and (not promo_pdf.activo() or hoy.isoformat() in reg):
    print("Nada que hacer (promoción apagada o la historia de hoy ya salió)."); sys.exit(0)


n = promo_pdf.dias_para_paes()
# Diseno de la historia: promo/historia.html (__N__ = dias que faltan, __PORTADA__ = imagen de la portada del PDF)
aviso = "⏳ ¡Mañana es la PAES!" if n == 1 else ("💪 ¡Hoy es la PAES!" if n <= 0 else None)
html = open(os.path.join(PROMO, "historia.html"), encoding="utf-8").read()
html = html.replace("__PORTADA__", os.path.join(PROMO, "portada.jpg"))
# la fuente se carga desde el archivo (en GitHub la familia instalada se llama "Inter Variable" y no calza con "Inter")
fuente = next((f for f in [os.path.expanduser("~/.local/share/fonts/InterVariable.ttf"), os.path.expanduser("~/sysdeps/InterVariable.ttf")]
               if os.path.exists(f)), "")
html = html.replace("__FUENTE__", fuente)
html = html.replace("⏳ Faltan __N__ días para la PAES", aviso) if aviso else html.replace("__N__", str(n))
png = "/tmp/historia_pdf.png"; jpg = f"/tmp/historia_pdf_{hoy.isoformat()}.jpg"
json.dump([{"html": html, "out": png, "w": 1080, "h": 1920}], open("/tmp/hist_job.json", "w"))
subprocess.run(["node", os.path.join(RAIZ, "render", "html2png.js"), "/tmp/hist_job.json"], check=True,
               env={**os.environ, "RENDER_DIR": os.path.join(RAIZ, "render")})
Image.open(png).convert("RGB").save(jpg, quality=90)
if PRUEBA:
    import shutil
    shutil.copy(jpg, os.path.join(PROMO, "prueba_historia.jpg"))
    subprocess.run(["git", "add", os.path.join(PROMO, "prueba_historia.jpg")], cwd=RAIZ, check=True)
    subprocess.run(["git", "-c", "user.name=publicador-paes", "-c", "user.email=publicador-paes@users.noreply.github.com",
                    "commit", "-qm", "Prueba historia PDF"], cwd=RAIZ, check=True)
    subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=RAIZ, check=True)
    print("Prueba lista: promo/prueba_historia.jpg"); sys.exit(0)
import publicar  # usa IG_TOKEN y REPO del entorno
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
