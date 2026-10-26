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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import promo_pdf  # promocion del PDF PAES M1 (franja, tarjeta final, videos programados)

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
    intentos = 1 if ruta.endswith("media_publish") else 4  # publicar no se reintenta (podria duplicar el post)
    for i in range(intentos):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            cuerpo = e.read().decode(errors="replace")
            sys.exit(f"Error de Instagram en {ruta}: {e.code} {cuerpo}")
        except (urllib.error.URLError, ConnectionError, TimeoutError, OSError) as e:
            if i == intentos - 1:
                raise
            print(f"::warning::Falla de conexion con Instagram en {ruta} ({e}); reintento en {10 * (i + 1)} s", flush=True)
            time.sleep(10 * (i + 1))


def esperar(contenedor, intentos=30):
    for _ in range(intentos):
        estado = llamar("GET", contenedor, fields="status_code").get("status_code")
        if estado == "FINISHED":
            return
        if estado in ("ERROR", "EXPIRED"):
            sys.exit(f"El contenedor {contenedor} quedo en estado {estado}")
        time.sleep(5)
    sys.exit(f"Tiempo agotado esperando el contenedor {contenedor}")


LIMITE = ("2207042", "Media Publish Limit")  # Instagram: maximo de publicaciones por API en 24 h moviles


def es_limite(e):
    return any(x in str(e) for x in LIMITE)


def cupo():
    """Publicaciones que quedan en las ultimas 24 h (Instagram permite ~50 por API, Reels e historias cuentan)."""
    try:
        usuario = llamar("GET", "me", fields="user_id")["user_id"]
        d = llamar("GET", f"{usuario}/content_publishing_limit", fields="quota_usage,config")["data"][0]
        uso, total = int(d.get("quota_usage", 0)), int(d.get("config", {}).get("quota_total", 50))
        print(f"Cupo de Instagram: {uso}/{total} usados en 24 h")
        return total - uso
    except (SystemExit, Exception) as e:
        print(f"::warning::No se pudo leer el cupo de Instagram ({e}); se intenta igual")
        return None


def subir_video(ruta, nombre):
    """Sube el video a la rama 'media' (un solo commit, se reescribe cada vez) y devuelve su URL publica."""
    g = lambda *a, **k: subprocess.run(["git", *a], cwd=RAIZ, check=True, capture_output=True, text=True, **k).stdout.strip()
    blob = g("hash-object", "-w", ruta)
    tree = g("mktree", input=f"100644 blob {blob}\t{nombre}\n")
    commit = g("-c", "user.name=publicador-paes", "-c", "user.email=publicador-paes@users.noreply.github.com",
               "commit-tree", tree, "-m", f"video {nombre}")
    g("push", "-f", "origin", f"{commit}:refs/heads/media")
    url = f"https://raw.githubusercontent.com/{REPO}/media/{nombre}"
    for _ in range(12):  # esperar a que el archivo este disponible
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=30) as r:
                if r.status == 200:
                    return url
        except Exception:
            pass
        time.sleep(5)
    sys.exit("El video no quedo disponible en la URL publica")


def cerrar(post, carpeta, registro):
    with open(os.path.join(carpeta, "publicado.json"), "w") as f:
        json.dump(registro, f)
    os.makedirs(PUBLICADOS, exist_ok=True)
    shutil.move(carpeta, os.path.join(PUBLICADOS, post))
    subprocess.run(["git", "config", "user.name", "publicador-paes"], check=True, cwd=RAIZ)
    subprocess.run(["git", "config", "user.email", "publicador-paes@users.noreply.github.com"], check=True, cwd=RAIZ)
    subprocess.run(["git", "add", "-A", "cola", "publicados"], check=True, cwd=RAIZ)
    subprocess.run(["git", "commit", "-m", f"Publicado post {post}"], check=True, cwd=RAIZ)
    subprocess.run(["git", "push", "origin", f"HEAD:{BRANCH}"], check=True, cwd=RAIZ)


def duracion(ruta):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", ruta], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def publicar_video(post, carpeta, video, texto, thumb_ms, historia=True):
    url = subir_video(video, f"reel_{post}.mp4")
    ig = llamar("GET", "me", fields="user_id,username")
    usuario = ig["user_id"]
    print(f"Publicando Reel {post} en @{ig.get('username')}")
    c = llamar("POST", f"{usuario}/media", media_type="REELS", video_url=url, caption=texto,
               share_to_feed="true", thumb_offset=str(thumb_ms))
    esperar(c["id"], intentos=60)
    publicado = llamar("POST", f"{usuario}/media_publish", creation_id=c["id"])
    print(f"Reel publicado: id {publicado['id']}")
    registro = {"media_id": publicado["id"], "tipo": "reel", "fecha_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    if not historia:  # desde el 26-oct: los ejercicios normales van solo como Reel (12 al dia)
        return registro
    try:
        quedan = cupo()
        if quedan is not None and quedan < 1:
            raise RuntimeError("no queda cupo en Instagram para la historia (se publica solo el Reel)")
        url_h = url
        if duracion(video) > 59:  # las historias admiten hasta 60 s: se sube recortada
            corto = video.replace(".mp4", "_historia.mp4")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-t", "59", "-c", "copy", corto], check=True)
            url_h = subir_video(corto, f"historia_{post}.mp4")
        h = llamar("POST", f"{usuario}/media", media_type="STORIES", video_url=url_h)
        esperar(h["id"], intentos=60)
        registro["story_id"] = llamar("POST", f"{usuario}/media_publish", creation_id=h["id"])["id"]
        print(f"Historia publicada: id {registro['story_id']}")
    except (SystemExit, Exception) as e:
        print(f"::warning::No se pudo publicar la historia: {e}")
    return registro


def publicar_reel(post, carpeta, datos):
    video = os.path.join("/tmp", f"reel_{post}.mp4")
    subprocess.run([sys.executable, os.path.join(RAIZ, "scripts", "armar_reel_voz.py"),
                    os.path.join(carpeta, "post.json"), video], check=True)
    with open(os.path.join(carpeta, "caption.txt"), encoding="utf-8") as f:
        texto = promo_pdf.promo_texto() + f.read()
    video = promo_pdf.decorar(video, video.replace(".mp4", "_promo.mp4"))
    cerrar(post, carpeta, publicar_video(post, carpeta, video, texto, 9000, historia=False))


def publicar_especial(post, carpeta, datos):
    video = os.path.join("/tmp", f"reel_{post}.mp4")
    subprocess.run([sys.executable, os.path.join(RAIZ, "scripts", "armar_especial.py"),
                    os.path.join(carpeta, "post.json"), video], check=True)
    video = promo_pdf.decorar(video, video.replace(".mp4", "_promo.mp4"))
    texto = promo_pdf.promo_texto() + datos.get("texto_post", "")
    registro = publicar_video(post, carpeta, video, texto, datos.get("portada_ms", 1500))
    registro["especial"] = datos.get("formato")
    cerrar(post, carpeta, registro)


def publicar_promo(e):
    """Video promocional del PDF ya armado (rama 'promo' del repo), programado en promo/plan.json."""
    url = f"https://raw.githubusercontent.com/{REPO}/promo/{e['video']}"
    local = os.path.join("/tmp", e["video"])
    urllib.request.urlretrieve(url, local)
    print(f"Video promocional del PDF: {e['video']}")
    registro = publicar_video("promo_" + e["fecha"] + "_" + str(e["hora"]), None, local, e["texto"], 1000)
    promo_pdf.marcar_publicado(e, registro["media_id"])
    subprocess.run(["git", "add", "-A", "promo"], check=True, cwd=RAIZ)
    subprocess.run(["git", "-c", "user.name=publicador-paes", "-c", "user.email=publicador-paes@users.noreply.github.com",
                    "commit", "-m", f"Publicado promo {e['video']}"], check=True, cwd=RAIZ)
    subprocess.run(["git", "push", "origin", f"HEAD:{BRANCH}"], check=True, cwd=RAIZ)


def main():
    os.makedirs(COLA, exist_ok=True)
    quedan = cupo()
    if quedan is not None and quedan < 1:
        print("::notice::Instagram no deja publicar mas por ahora (limite de 24 h). Este horario se salta; el post sigue primero en la cola.")
        return
    e = promo_pdf.promo_pendiente()
    if e:  # en su horario, el video del PDF va en lugar del post de la cola (que espera al siguiente horario)
        try:
            return publicar_promo(e)
        except (Exception, SystemExit) as err:
            if es_limite(err):
                print("::notice::Sin cupo de Instagram; el video del PDF se intenta en el próximo horario."); return
            print(f"::warning::Fallo el video del PDF ({err}); se publica el post normal de la cola")
    pendientes = sorted(d for d in os.listdir(COLA) if os.path.isdir(os.path.join(COLA, d)))
    if not pendientes:
        print("::warning::La cola esta vacia, no hay nada que publicar.")
        return
    post = pendientes[0]
    carpeta = os.path.join(COLA, post)
    datos = json.load(open(os.path.join(carpeta, "post.json"), encoding="utf-8"))
    if datos.get("tipo") == "especial":
        try:
            return publicar_especial(post, carpeta, datos)
        except (Exception, SystemExit) as e:
            if es_limite(e):
                print("::notice::Instagram no deja publicar mas por ahora (limite de 24 h); el especial sigue en la cola.")
                return
            # no trabar la cola: se aparta el especial fallido y se publica el siguiente
            print(f"::warning::Fallo el especial {post} ({e}); se aparta a fallidos/ y sigue la cola")
            os.makedirs(os.path.join(RAIZ, "fallidos"), exist_ok=True)
            shutil.move(carpeta, os.path.join(RAIZ, "fallidos", post))
            subprocess.run(["git", "add", "-A", "cola", "fallidos"], check=True, cwd=RAIZ)
            subprocess.run(["git", "-c", "user.name=publicador-paes", "-c", "user.email=publicador-paes@users.noreply.github.com",
                            "commit", "-m", f"Especial {post} fallido"], check=True, cwd=RAIZ)
            return main()
    if datos.get("pizarra"):
        try:
            return publicar_reel(post, carpeta, datos)
        except (Exception, SystemExit) as e:
            if es_limite(e):
                print("::notice::Instagram no deja publicar mas por ahora (limite de 24 h); el post sigue en la cola.")
                return
            if not os.path.exists(os.path.join(carpeta, "1.jpg")):
                raise
            print(f"::warning::Fallo el Reel ({e}); se publica el carrusel de respaldo.")
    imagenes = sorted(f for f in os.listdir(carpeta) if f.endswith(".jpg") and f[0].isdigit())
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

    registro = {"media_id": publicado["id"], "fecha_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}

    # Historia: la lamina del problema en formato vertical. Si falla, no detiene nada.
    if os.path.exists(os.path.join(carpeta, "historia.jpg")):
        try:
            url = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/cola/{post}/historia.jpg"
            h = llamar("POST", f"{usuario}/media", image_url=url, media_type="STORIES")
            esperar(h["id"])
            registro["story_id"] = llamar("POST", f"{usuario}/media_publish", creation_id=h["id"])["id"]
            print(f"Historia publicada: id {registro['story_id']}")
        except SystemExit as e:
            print(f"::warning::No se pudo publicar la historia: {e}")

    with open(os.path.join(carpeta, "publicado.json"), "w") as f:
        json.dump(registro, f)
    os.makedirs(PUBLICADOS, exist_ok=True)
    shutil.move(carpeta, os.path.join(PUBLICADOS, post))

    subprocess.run(["git", "config", "user.name", "publicador-paes"], check=True, cwd=RAIZ)
    subprocess.run(["git", "config", "user.email", "publicador-paes@users.noreply.github.com"], check=True, cwd=RAIZ)
    subprocess.run(["git", "add", "-A", "cola", "publicados"], check=True, cwd=RAIZ)
    subprocess.run(["git", "commit", "-m", f"Publicado post {post}"], check=True, cwd=RAIZ)
    subprocess.run(["git", "push"], check=True, cwd=RAIZ)


if __name__ == "__main__":
    main()
