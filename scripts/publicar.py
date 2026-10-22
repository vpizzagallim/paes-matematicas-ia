"""Publica el siguiente post de cola/ como carrusel en Instagram y lo mueve a publicados/.

Variables de entorno:
  IG_TOKEN   token de larga duracion (Instagram API con inicio de sesion de Instagram)
  REPO       usuario/repositorio en GitHub (lo entrega GitHub Actions)
  BRANCH     rama (por defecto main)
"""
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request

API = "https://graph.instagram.com/v22.0"
TOKEN = os.environ["IG_TOKEN"]
REPO = os.environ["REPO"]
BRANCH = os.environ.get("BRANCH", "main")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLA = os.path.join(RAIZ, "cola")
PUBLICADOS = os.path.join(RAIZ, "publicados")


def llamar(metodo, ruta, **params):
    params["access_token"] = TOKEN
    datos = urllib.parse.urlencode(params).encode()
    if metodo == "GET":
        req = urllib.request.Request(f"{API}/{ruta}?{datos.decode()}")
    else:
        req = urllib.request.Request(f"{API}/{ruta}", data=datos, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        cuerpo = e.read().decode(errors="replace")
        sys.exit(f"Error de Instagram en {ruta}: {e.code} {cuerpo}")


def esperar(contenedor):
    for _ in range(30):
        estado = llamar("GET", contenedor, fields="status_code").get("status_code")
        if estado == "FINISHED":
            return
        if estado in ("ERROR", "EXPIRED"):
            sys.exit(f"El contenedor {contenedor} quedo en estado {estado}")
        time.sleep(5)
    sys.exit(f"Tiempo agotado esperando el contenedor {contenedor}")


def main():
    pendientes = sorted(d for d in os.listdir(COLA) if os.path.isdir(os.path.join(COLA, d)))
    if not pendientes:
        print("::warning::La cola esta vacia, no hay nada que publicar.")
        return
    post = pendientes[0]
    carpeta = os.path.join(COLA, post)
    imagenes = sorted(f for f in os.listdir(carpeta) if f.endswith(".jpg"))
    with open(os.path.join(carpeta, "caption.txt"), encoding="utf-8") as f:
        texto = f.read()

    ig_id = llamar("GET", "me", fields="user_id,username")
    usuario = ig_id["user_id"]
    print(f"Publicando post {post} en @{ig_id.get('username')} ({len(imagenes)} imagenes)")

    hijos = []
    for img in imagenes:
        url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/cola/{post}/{img}"
        c = llamar("POST", f"{usuario}/media", image_url=url, is_carousel_item="true")
        esperar(c["id"])
        hijos.append(c["id"])

    carrusel = llamar("POST", f"{usuario}/media", media_type="CAROUSEL",
                      children=",".join(hijos), caption=texto)
    esperar(carrusel["id"])
    publicado = llamar("POST", f"{usuario}/media_publish", creation_id=carrusel["id"])
    print(f"Publicado: id {publicado['id']}")

    with open(os.path.join(carpeta, "publicado.json"), "w") as f:
        json.dump({"media_id": publicado["id"], "fecha_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}, f)
    os.makedirs(PUBLICADOS, exist_ok=True)
    shutil.move(carpeta, os.path.join(PUBLICADOS, post))

    subprocess.run(["git", "config", "user.name", "publicador-paes"], check=True, cwd=RAIZ)
    subprocess.run(["git", "config", "user.email", "publicador-paes@users.noreply.github.com"], check=True, cwd=RAIZ)
    subprocess.run(["git", "add", "-A", "cola", "publicados"], check=True, cwd=RAIZ)
    subprocess.run(["git", "commit", "-m", f"Publicado post {post}"], check=True, cwd=RAIZ)
    subprocess.run(["git", "push"], check=True, cwd=RAIZ)


if __name__ == "__main__":
    main()
