"""Verifica un lote de problemas y renderiza los aprobados en cola/NNN/.

Uso: python3 scripts/preparar_lote.py borradores/lote.json

Cada problema del lote (lista JSON) debe traer:
  nivel, eje, tema, gancho, enunciado, alternativas[5], correcta (0-4), pasos[], trampa, clave
  valores[5]     : valor de cada alternativa como expresion sympy (texto), p.ej. "38400", "sqrt(2)/2"
  verificacion   : codigo Python (sympy disponible) que calcula la variable `respuesta`
                   de forma independiente a partir de los datos del enunciado.
Se rechaza el problema si: la verificacion falla, `respuesta` no coincide con valores[correcta],
coincide con mas de una alternativa, o hay alternativas repetidas.
"""
import json
import os
import subprocess
import sys

import sympy as sp

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLA = os.path.join(RAIZ, "cola")
PUB = os.path.join(RAIZ, "publicados")


def iguales(a, b):
    a, b = sp.sympify(a), sp.sympify(b)
    if not (isinstance(a, sp.Expr) and isinstance(b, sp.Expr)):
        return sp.simplify(a) == sp.simplify(b)
    try:
        return sp.simplify(sp.nsimplify(a) - sp.nsimplify(b)) == 0
    except Exception:
        try:
            return abs(float(a) - float(b)) < 1e-9
        except Exception:
            return False


def verificar(p):
    for campo in ["nivel", "eje", "tema", "enunciado", "alternativas", "correcta", "pasos", "trampa", "clave", "valores", "verificacion", "pizarra"]:
        if campo not in p:
            return f"falta el campo {campo}"
    if len(p["alternativas"]) != 5 or len(p["valores"]) != 5:
        return "debe haber 5 alternativas y 5 valores"
    vals = [sp.sympify(v) for v in p["valores"]]
    for i in range(5):
        for j in range(i + 1, 5):
            if iguales(vals[i], vals[j]):
                return f"alternativas {i} y {j} tienen el mismo valor"
    ns = {"sp": sp, **{k: getattr(sp, k) for k in dir(sp) if not k.startswith("_")}}
    try:
        exec(p["verificacion"], ns)
    except Exception as e:
        return f"la verificacion fallo: {e}"
    if "respuesta" not in ns:
        return "la verificacion no definio `respuesta`"
    r = ns["respuesta"]
    coincide = [i for i, v in enumerate(vals) if iguales(r, v)]
    if coincide != [p["correcta"]]:
        return f"respuesta calculada {r} coincide con alternativas {coincide}, clave dice {p['correcta']}"
    return None


def siguiente_id():
    usados = [int(d) for base in (COLA, PUB) if os.path.isdir(base) for d in os.listdir(base) if d.isdigit()]
    return max(usados, default=0) + 1


def main():
    lote = json.load(open(sys.argv[1], encoding="utf-8"))
    os.makedirs(COLA, exist_ok=True)
    aprobados, rechazados = 0, 0
    for p in lote:
        error = verificar(p)
        if error:
            rechazados += 1
            print(f"RECHAZADO ({p.get('tema')}): {error}")
            continue
        n = siguiente_id()
        p["id"] = f"{n:03d}"
        destino = os.path.join(COLA, p["id"])
        tmp = os.path.join(RAIZ, "borradores", f"_{p['id']}.json")
        json.dump(p, open(tmp, "w", encoding="utf-8"), ensure_ascii=False)
        res = subprocess.run(["node", os.path.join(RAIZ, "render", "render.js"), tmp, destino], capture_output=True, text=True)
        os.remove(tmp)
        if res.returncode != 0:
            import shutil
            shutil.rmtree(destino, ignore_errors=True)
            rechazados += 1
            print(f"RECHAZADO ({p['tema']}): {res.stderr.strip().splitlines()[-1] if res.stderr.strip() else 'error al renderizar'}")
            continue
        res = subprocess.run(["node", os.path.join(RAIZ, "render", "pizarra.js"), os.path.join(destino, "post.json"),
                              os.path.join("/tmp", "pizarra_" + p["id"])], capture_output=True, text=True)
        if res.returncode != 0:
            import shutil
            shutil.rmtree(destino, ignore_errors=True)
            rechazados += 1
            print(f"RECHAZADO ({p['tema']}): la hoja del Reel no cabe")
            continue
        aprobados += 1
        print(f"OK {p['id']} · {p['nivel']} · {p['tema']}")
    print(f"\nAprobados: {aprobados} · Rechazados: {rechazados} · En cola: {len(os.listdir(COLA))}")


if __name__ == "__main__":
    main()
