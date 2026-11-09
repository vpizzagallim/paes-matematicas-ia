# Lote 09-nov-2026: problemas normales (4 alternativas, con guion de voz).
import json, os, random, re

AQUI = os.path.dirname(os.path.abspath(__file__))
N, A, G, E = "Números", "Álgebra y funciones", "Geometría", "Probabilidad y estadística"
LET = "ABCD"; VOZ_LET = {"A": "a", "B": "be", "C": "ce", "D": "de"}


def P(nivel, eje, tema, gancho, enunciado, alts, valores, correcta, pasos, trampa, clave, verif, pz_pasos, resp_voz, clave_voz):
    return dict(nivel=nivel, eje=eje, tema=tema, gancho=gancho, enunciado=enunciado, alternativas=alts, valores=valores,
                correcta=correcta, pasos=pasos, trampa=trampa, clave=clave, verificacion=verif,
                _pz=pz_pasos, _resp=resp_voz, _clave_voz=clave_voz)


L = []
# ======================= M1 · NÚMEROS
L.append(P("M1", N, "Comparación de precios por unidad", "¿Conviene el pack? 🛒",
  r"En el supermercado, un <b>pack de 6 yogures</b> cuesta <b>\$2.700</b> y cada yogur <b>suelto</b> cuesta <b>\$520</b>. Si se necesitan 6 yogures, ¿cuánto se <b>ahorra</b> comprando el pack?",
  [r"\$420", r"\$70", r"\$450", r"\$3.120"], ["420", "70", "450", "3120"], 0,
  [r"Seis yogures sueltos cuestan $$6 \cdot 520 = 3.120$$", r"El ahorro es la diferencia: $$3.120 - 2.700 = 420$$"],
  r"Calcular solo el ahorro por yogur ($520 - 450 = 70$) y marcar B, olvidando que son 6 yogures.",
  r"Para comparar ofertas, calcula el costo de la <b>misma cantidad</b> en ambas opciones, o el precio por unidad.",
  "respuesta = 6*520 - 2700",
  [(["Seis sueltos", r"$6 \cdot 520 = 3.120$"], "Seis yogures sueltos cuestan seis por quinientos veinte: tres mil ciento veinte pesos."),
   (["Ahorro con el pack", r"$3.120 - 2.700 = 420$"], "El pack cuesta dos mil setecientos. La diferencia es cuatrocientos veinte pesos.")],
  "cuatrocientos veinte pesos", "Para comparar ofertas, compara la misma cantidad de producto."))

# ======================= M1 · ÁLGEBRA
L.append(P("M1", A, "Discriminante: solución única", "Una sola solución 🎯",
  r"¿Para qué valor de $k$ la ecuación $$x^2 + 4x + k = 0$$ tiene <b>una única solución real</b>?",
  ["4", "16", "-4", "2"], ["4", "16", "-4", "2"], 0,
  [r"Hay una única solución cuando el discriminante es cero: $$\Delta = b^2 - 4ac = 0$$", r"$$4^2 - 4 \cdot 1 \cdot k = 0 \Rightarrow 16 = 4k \Rightarrow k = 4$$"],
  r"Igualar $k$ a $b^2 = 16$ y marcar B, olvidando el factor $4a$.",
  r"Discriminante $\Delta = b^2 - 4ac$: si es positivo hay 2 soluciones, si es cero hay 1 y si es negativo, ninguna real.",
  "k, x = symbols('k x'); sols = [s for s in solve(Eq(4**2 - 4*1*k, 0), k)]; assert len(solve(x**2 + 4*x + sols[0], x)) == 1; respuesta = sols[0]",
  [(["Una solución: Δ = 0", r"$\Delta = b^2 - 4ac = 0$"], "Una ecuación cuadrática tiene una única solución cuando su discriminante es cero."),
   (["Reemplazamos", r"$16 - 4k = 0 \Rightarrow k = 4$"], "Be al cuadrado es dieciséis, y cuatro a ce es cuatro ka. Dieciséis igual a cuatro ka: ka vale cuatro.")],
  "cuatro", "Discriminante cero, una sola solución; positivo, dos; negativo, ninguna real. El error típico es igualar ka a dieciséis y olvidar el cuatro a ce."))

# ======================= M1 · GEOMETRÍA
L.append(P("M1", G, "Área total de un paralelepípedo", "¿Cuánto papel de regalo? 🎁",
  r"Una caja de regalo mide <b>20 cm</b> de largo, <b>10 cm</b> de ancho y <b>5 cm</b> de alto. ¿Cuántos <b>cm²</b> de papel se necesitan para forrar <b>toda su superficie</b>, sin traslapes?",
  [r"700 cm²", r"1.000 cm²", r"350 cm²", r"70 cm²"], ["700", "1000", "350", "70"], 0,
  [r"La caja tiene 3 pares de caras iguales: $$20 \cdot 10 = 200,\quad 20 \cdot 5 = 100,\quad 10 \cdot 5 = 50$$", r"$$A = 2\,(200 + 100 + 50) = 700 \text{ cm}^2$$"],
  r"Calcular el volumen ($20 \cdot 10 \cdot 5 = 1.000$) y marcar B, o contar cada cara una sola vez (350).",
  r"Área total de un paralelepípedo: $A = 2(ab + ac + bc)$. El volumen, $abc$, mide lo que cabe adentro, no lo que la cubre.",
  "a, b, c = 20, 10, 5; respuesta = 2*(a*b + a*c + b*c)",
  [(["Tres pares de caras", r"$200 + 100 + 50 = 350$"], "La caja tiene tres pares de caras iguales: doscientos, cien y cincuenta centímetros cuadrados."),
   (["Cada una dos veces", r"$2 \cdot 350 = 700\ \text{cm}^2$"], "Cada cara aparece dos veces, arriba y abajo, adelante y atrás. Total: setecientos.")],
  "setecientos centímetros cuadrados", "Para forrar se usa el área total; el volumen, mil, es lo que cabe adentro."))

# ======================= M1 · PROBABILIDAD
L.append(P("M1", E, "Probabilidad de una intersección", "Hombre Y en Metro 🚇",
  r"En un curso de <b>40 estudiantes</b>, <b>22</b> llegan en Metro y el resto en micro. De los que llegan en Metro, <b>12 son mujeres</b>. Si se elige al azar un estudiante del curso, ¿cuál es la probabilidad de que sea <b>hombre y llegue en Metro</b>?",
  [r"$\dfrac{1}{4}$", r"$\dfrac{5}{11}$", r"$\dfrac{11}{20}$", r"$\dfrac{3}{10}$"], ["1/4", "5/11", "11/20", "3/10"], 0,
  [r"Hombres que llegan en Metro: $22 - 12 = 10$.", r"Sobre el total del curso: $$P = \frac{10}{40} = \frac{1}{4}$$"],
  r"Dividir por los 22 del Metro y marcar B ($\tfrac{10}{22}$): eso sería la probabilidad <i>dado que</i> llega en Metro.",
  r"Si se elige del curso completo, el denominador es el total; solo con «dado que» se reduce el universo.",
  "metro, mujeres_metro, total = 22, 12, 40; respuesta = Rational(metro - mujeres_metro, total)",
  [(["Hombres en Metro", r"$22 - 12 = 10$"], "De los veintidós que llegan en Metro, doce son mujeres. Entonces diez son hombres."),
   (["Sobre todo el curso", r"$\dfrac{10}{40} = \dfrac{1}{4}$"], "Se elige del curso completo, así que dividimos por cuarenta: un cuarto.")],
  "un cuarto", "Si no dice dado que, el denominador es el total. Diez veintidosavos sería la probabilidad de ser hombre sabiendo que llega en Metro."))

# ======================= M2
L.append(P("M2", G, "Coseno en contexto: escalera", "La escalera y el coseno 🪜",
  r"Una escalera de <b>5 m</b> está apoyada en una pared y forma con el suelo un ángulo $\alpha$ tal que $\cos\alpha = 0{,}6$. ¿A qué distancia de la pared está el <b>pie de la escalera</b>?",
  ["3 m", "4 m", r"$\dfrac{25}{3}$ m", "2 m"], ["3", "4", "25/3", "2"], 0,
  [r"El pie de la escalera es el cateto <b>adyacente</b> al ángulo y la escalera es la hipotenusa: $$\cos\alpha = \frac{d}{5}$$", r"$$d = 5 \cdot 0{,}6 = 3 \text{ m}$$"],
  r"Usar el seno, $\sqrt{1 - 0{,}36} = 0{,}8$, y marcar B (4 m), o dividir $5 : 0{,}6$ (C).",
  r"$\cos\alpha = \dfrac{\text{adyacente}}{\text{hipotenusa}}$: el lado del suelo sale multiplicando la hipotenusa por el coseno.",
  "d = symbols('d'); respuesta = solve(Eq(d/5, Rational(6,10)), d)[0]",
  [(["Adyacente sobre hipotenusa", r"$\cos\alpha = \dfrac{d}{5}$"], "La distancia a la pared es el cateto adyacente, y la escalera es la hipotenusa."),
   (["Despejamos", r"$d = 5 \cdot 0{,}6 = 3\ \text{m}$"], "Cinco por cero coma seis: tres metros.")],
  "tres metros", "El coseno relaciona el adyacente con la hipotenusa. Cuatro metros es la altura que alcanza en la pared, que sale con el seno."))

L.append(P("M2", E, "Permutaciones con repetición: anagramas", "¿Cuántas palabras con CASA? 🔤",
  r"¿Cuántas «palabras» distintas, con o sin sentido, se pueden formar usando <b>todas las letras</b> de la palabra <b>CASA</b>?",
  ["12", "24", "6", "4"], ["12", "24", "6", "4"], 0,
  [r"Si las 4 letras fueran distintas habría $4! = 24$ ordenamientos.", r"Pero la A se repite 2 veces, así que se divide por $2!$: $$\frac{4!}{2!} = \frac{24}{2} = 12$$"],
  r"Contar $4! = 24$ y marcar B, sin considerar que intercambiar las dos A da la misma palabra.",
  r"Permutaciones con repetición: $\dfrac{n!}{a!\,b!\cdots}$, dividiendo por el factorial de cada letra repetida.",
  "from itertools import permutations; respuesta = Integer(len(set(permutations('CASA'))))",
  [(["Si fueran distintas", r"$4! = 24$"], "Con cuatro letras distintas habría cuatro factorial: veinticuatro ordenamientos."),
   (["La A se repite", r"$\dfrac{4!}{2!} = 12$"], "Pero hay dos A, y cambiarlas de lugar da la misma palabra. Dividimos por dos factorial: doce.")],
  "doce", "Cuando una letra se repite, divide por el factorial de sus repeticiones; si no, cuentas cada palabra dos veces."))

EXTRA = {
 "Comparación de precios por unidad": "Ojo: setenta pesos es lo que ahorras en cada yogur, pero son seis yogures. En el pack, cada uno sale a cuatrocientos cincuenta, así que siempre conviene sacar la cuenta antes de pasar por la caja.",
 "Discriminante: solución única": "Compruébalo: equis más dos al cuadrado es cero.",
 "Área total de un paralelepípedo": "Y si cuentas cada cara una sola vez, te quedan trescientos cincuenta, que alcanza solo para media caja.",
 "Probabilidad de una intersección": "Y lee bien: hombre y Metro al mismo tiempo.",
 "Coseno en contexto: escalera": "Si divides cinco en cero coma seis, te da más que la escalera, y un cateto nunca es más largo que la hipotenusa.",
 "Permutaciones con repetición: anagramas": "Por ejemplo, con la palabra ala serían tres factorial dividido en dos factorial: tres palabras.",
}
for p in L:
    p["_clave_voz"] = p["_clave_voz"] + (" " + EXTRA[p["tema"]] if p["tema"] in EXTRA else "")

def finalizar(p, rnd, destino):
    orden = [i for i in range(4) if i != p["correcta"]]; rnd.shuffle(orden)
    orden.insert(destino, p["correcta"])
    nuevo = {v: k for k, v in enumerate(orden)}
    p["alternativas"] = [p["alternativas"][i] for i in orden]; p["valores"] = [p["valores"][i] for i in orden]
    p["correcta"] = nuevo[p["correcta"]]
    p["trampa"] = re.sub(r"(marcar |marcando |\()([A-D])(\)|\b)", lambda m: m.group(1) + LET[nuevo[LET.index(m.group(2))]] + m.group(3), p["trampa"])
    for k in list(p):
        if isinstance(p[k], str): p[k] = p[k].replace('\\"', '"')
    letra = LET[p["correcta"]]
    p["pizarra"] = {"pasos": [{"lineas": [l.replace("\\tfrac", "\\dfrac") for l in ls], "voz": v} for ls, v in p.pop("_pz")],
                    "cierre": {"voz": f"La respuesta correcta es la {VOZ_LET[letra]}: {p.pop('_resp')}. {p.pop('_clave_voz')} Sigue a math paes punto c, ele."}}
    return p


rnd = random.Random(20261109)
metas = [i % 4 for i in range(len(L))]; rnd.shuffle(metas)
lote = [finalizar(p, rnd, metas[i]) for i, p in enumerate(L)]
json.dump(lote, open(os.path.join(AQUI, "lote_2026-11-09.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(lote), "problemas")
