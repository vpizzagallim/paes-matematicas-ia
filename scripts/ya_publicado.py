"""Evita posts duplicados: si ya salio un post hace menos de MINUTOS, avisa que se salte esta ejecucion.

Hay dos relojes que lanzan la publicacion (cron-job.org y, de respaldo, el horario de GitHub).
El primero que llega publica; el otro ve que ya hay un post reciente y no hace nada.
Imprime 'saltar=true' o 'saltar=false' (formato de GITHUB_OUTPUT).
"""
import glob, json, os, sys
from datetime import datetime, timezone

# El reloj externo (workflow_dispatch) llega puntual: solo se frena si hubo un post hace <20 min.
# El respaldo de GitHub (schedule) llega tarde: se frena si hubo un post hace <55 min.
MINUTOS = 55 if os.environ.get("EVENTO") == "schedule" else 20
if os.environ.get("FORZAR") == "true":
    print("saltar=false"); sys.exit()
ultimo = None
for f in glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "publicados", "*", "publicado.json")):
    try:
        t = datetime.strptime(json.load(open(f))["fecha_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except Exception:
        continue
    ultimo = t if ultimo is None or t > ultimo else ultimo
if ultimo:
    hace = (datetime.now(timezone.utc) - ultimo).total_seconds() / 60
    print(f"Ultimo post hace {hace:.0f} min", file=sys.stderr)
    if hace < MINUTOS:
        print(f"::notice::Ya salio un post hace {hace:.0f} min; esta ejecucion no publica (evita duplicados).", file=sys.stderr)
        print("saltar=true"); sys.exit()
print("saltar=false")
