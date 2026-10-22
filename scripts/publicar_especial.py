"""Publica un video suelto como Reel (y como historia), sin tocar la cola.
Variables: IG_TOKEN, VIDEO_URL, TEXTO (caption), HISTORIA (si/no).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import publicar as p

url, texto = os.environ["VIDEO_URL"], os.environ.get("TEXTO", "")
ig = p.llamar("GET", "me", fields="user_id,username")
u = ig["user_id"]
print(f"Publicando video especial en @{ig.get('username')}")
c = p.llamar("POST", f"{u}/media", media_type="REELS", video_url=url, caption=texto, share_to_feed="true", thumb_offset="1500")
p.esperar(c["id"], intentos=60)
r = p.llamar("POST", f"{u}/media_publish", creation_id=c["id"])
print(f"Reel publicado: {r['id']}")
if os.environ.get("HISTORIA", "si") == "si":
    h = p.llamar("POST", f"{u}/media", media_type="STORIES", video_url=url)
    p.esperar(h["id"], intentos=60)
    print(f"Historia publicada: {p.llamar('POST', f'{u}/media_publish', creation_id=h['id'])['id']}")
