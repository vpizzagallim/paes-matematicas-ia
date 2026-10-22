"""Agrega el guion de voz ('pizarra') a los posts que siguen en cola/.
Uso: python3 scripts/aplicar_pizarras.py borradores/parche_pizarras.json
"""
import json, os, sys
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parche = json.load(open(sys.argv[1], encoding="utf-8"))
n = 0
for pid, pz in parche.items():
    f = os.path.join(RAIZ, "cola", pid, "post.json")
    if not os.path.exists(f):
        continue
    p = json.load(open(f, encoding="utf-8"))
    p["pizarra"] = pz
    json.dump(p, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    n += 1
print(f"Pizarras aplicadas: {n}")
