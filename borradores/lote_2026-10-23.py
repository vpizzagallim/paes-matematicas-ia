# Lote 23-oct-2026: 16 problemas normales (4 alternativas, con guion de voz) + 8 especiales.
import json, os, random, re

AQUI = os.path.dirname(os.path.abspath(__file__))
N, A, G, E = "Números", "Álgebra y funciones", "Geometría", "Probabilidad y estadística"
LET = "ABCD"; VOZ_LET = {"A": "a", "B": "be", "C": "ce", "D": "de"}


def P(nivel, eje, tema, gancho, enunciado, alts, valores, correcta, pasos, trampa, clave, verif, pz_pasos, resp_voz, clave_voz):
    return dict(nivel=nivel, eje=eje, tema=tema, gancho=gancho, enunciado=enunciado, alternativas=alts, valores=valores,
                correcta=correcta, pasos=pasos, trampa=trampa, clave=clave, verificacion=verif,
                _pz=pz_pasos, _resp=resp_voz, _clave_voz=clave_voz)


L = []
L.append(P("M1", N, "Proporcionalidad directa", "La receta no se arma sumando 🥞",
  r"Para <b>10 panqueques</b> se usan <b>4 huevos</b>. Manteniendo la receta, ¿cuántos huevos se necesitan para <b>25 panqueques</b>?",
  ["10", "19", "8", "12"], ["10", "19", "8", "12"], 0,
  [r"Es proporcionalidad directa: $$\frac{4}{10} = \frac{x}{25}$$", r"$$x = \frac{4 \cdot 25}{10} = 10$$"],
  r"Sumar: \"son 15 panqueques más, entonces 15 huevos más\" y marcar B (19).",
  r"En proporcionalidad directa el <b>cociente</b> se mantiene; no se suman diferencias.",
  "respuesta = Rational(4*25, 10)",
  [(["Directa: el cociente se mantiene", r"$\dfrac{4}{10} = \dfrac{x}{25}$"], "Más panqueques, más huevos en la misma proporción. Cuatro es a diez como equis es a veinticinco."),
   (["Despejamos", r"$x = \dfrac{4 \cdot 25}{10} = 10$"], "Cuatro por veinticinco, dividido en diez: diez huevos.")],
  "diez huevos", "En proporcionalidad directa se multiplica, no se suman diferencias."))

L.append(P("M1", G, "Escalas", "¿Cuánto mide en la realidad? 🗺️",
  r"En un mapa a escala <b>1 : 50.000</b>, dos plazas están a <b>6 cm</b>. ¿Cuál es la distancia real entre ellas?",
  ["3 km", "30 km", "300 km", "0,3 km"], ["3", "30", "300", "3/10"], 0,
  [r"Cada cm del mapa son 50.000 cm reales: $$6 \cdot 50.000 = 300.000 \text{ cm}$$", r"$$300.000 \text{ cm} = 3.000 \text{ m} = 3 \text{ km}$$"],
  r"Equivocarse al pasar de centímetros a kilómetros y marcar B.",
  r"Escala 1 : $k$ significa que 1 unidad del mapa son $k$ unidades reales. Después convierte unidades con calma.",
  "respuesta = Rational(6*50000, 100000)",
  [(["Multiplicamos por la escala", r"$6 \cdot 50.000 = 300.000\ \text{cm}$"], "Cada centímetro del mapa son cincuenta mil centímetros reales. Seis por cincuenta mil: trescientos mil centímetros."),
   (["Convertimos", r"$300.000\ \text{cm} = 3\ \text{km}$"], "Trescientos mil centímetros son tres mil metros, o sea tres kilómetros.")],
  "tres kilómetros", "Primero multiplica por la escala y después convierte unidades."))

L.append(P("M1", N, "Porcentaje de variación", "¿Cuánto subió tu sueldo? 💸",
  r"Un sueldo sube de <b>\$500.000</b> a <b>\$575.000</b>. ¿En qué porcentaje aumentó?",
  ["15%", "75%", r"≈ 13%", "7,5%"], ["15", "75", "75/575*100", "15/2"], 0,
  [r"Aumento: $575.000 - 500.000 = 75.000$.", r"Se compara con el valor <b>inicial</b>: $$\frac{75.000}{500.000} = 0{,}15 = 15\%$$"],
  r"Dividir el aumento por el sueldo nuevo ($\tfrac{75.000}{575.000} \approx 13\%$) y marcar C.",
  r"Variación porcentual $= \dfrac{\text{final} - \text{inicial}}{\text{inicial}} \cdot 100$.",
  "respuesta = Rational(575000-500000, 500000)*100",
  [(["Cuánto subió", r"$575.000 - 500.000 = 75.000$"], "Primero, cuánto subió: setenta y cinco mil pesos."),
   (["Se divide por el valor inicial", r"$\dfrac{75.000}{500.000} = 15\%$"], "Ese aumento se compara con el sueldo inicial: setenta y cinco mil dividido en quinientos mil, quince por ciento.")],
  "quince por ciento", "El porcentaje de variación siempre se calcula sobre el valor inicial."))

L.append(P("M1", G, "Ángulos", "Triángulo isósceles en 20 segundos 📐",
  r"En un triángulo <b>isósceles</b>, el ángulo distinto mide <b>40°</b>. ¿Cuánto mide cada uno de los otros dos ángulos?",
  ["70°", "140°", "40°", "50°"], ["70", "140", "40", "50"], 0,
  [r"Los ángulos interiores suman $180^\circ$: quedan $180^\circ - 40^\circ = 140^\circ$.", r"Los otros dos son iguales: $$140^\circ \div 2 = 70^\circ$$"],
  r"Quedarse con los 140° (B) y olvidar repartirlos entre los dos ángulos iguales.",
  r"Suma de ángulos interiores de un triángulo: $180^\circ$. Isósceles: dos ángulos iguales.",
  "respuesta = Rational(180-40, 2)",
  [(["Suman 180°", r"$180^\circ - 40^\circ = 140^\circ$"], "Los ángulos de un triángulo suman ciento ochenta grados. Quitando los cuarenta, quedan ciento cuarenta."),
   (["Isósceles: dos iguales", r"$140^\circ \div 2 = 70^\circ$"], "Como es isósceles, los otros dos son iguales: ciento cuarenta dividido en dos, setenta grados.")],
  "setenta grados", "En un isósceles, los dos ángulos basales son iguales."))

L.append(P("M1", G, "Área del círculo", "La pizza y el área 🍕",
  r"Una pizza circular tiene <b>radio 5 cm</b>. Usando $\pi \approx 3{,}14$, ¿cuál es su área?",
  [r"78,5 cm²", r"31,4 cm²", r"15,7 cm²", r"157 cm²"], ["785/10", "314/10", "157/10", "157"], 0,
  [r"$A = \pi r^2$", r"$$A = 3{,}14 \cdot 5^2 = 3{,}14 \cdot 25 = 78{,}5 \text{ cm}^2$$"],
  r"Usar la fórmula del perímetro, $2\pi r = 31{,}4$, y marcar B.",
  r"Área del círculo: $\pi r^2$. Perímetro: $2\pi r$. No las confundas.",
  "respuesta = Rational(314,100)*5**2",
  [(["Área = π · r²", r"$3{,}14 \cdot 5^2$"], "El área del círculo es pi por radio al cuadrado."),
   (["Calculamos", r"$3{,}14 \cdot 25 = 78{,}5$"], "Cinco al cuadrado es veinticinco, por tres coma catorce: setenta y ocho coma cinco centímetros cuadrados.")],
  "setenta y ocho coma cinco centímetros cuadrados", "Área es pi erre cuadrado; dos pi erre es el perímetro."))

L.append(P("M1", A, "Ecuaciones con fracciones", "Fracciones sin miedo ✍️",
  r"¿Cuál es el valor de $x$ en la ecuación $$\frac{x}{3} + \frac{x}{6} = 5\,?$$",
  ["10", "15", "30", "5"], ["10", "15", "30", "5"], 0,
  [r"Sumamos las fracciones con denominador 6: $$\frac{2x}{6} + \frac{x}{6} = \frac{3x}{6} = \frac{x}{2}$$", r"$$\frac{x}{2} = 5 \;\Rightarrow\; x = 10$$"],
  r"Sumar los denominadores ($\tfrac{2x}{9} = 5$) o multiplicar todo por 3 y olvidar un término.",
  r"Para sumar fracciones algebraicas, iguala denominadores; nunca sumes denominadores.",
  "x = symbols('x'); respuesta = solve(Eq(x/3 + x/6, 5), x)[0]",
  [(["Igualamos denominadores", r"$\dfrac{2x}{6} + \dfrac{x}{6} = \dfrac{x}{2}$"], "Escribe equis tercios como dos equis sextos. Sumando, tres equis sextos, que es equis medios."),
   (["Despejamos", r"$\dfrac{x}{2} = 5 \Rightarrow x = 10$"], "Equis medios igual cinco, entonces equis vale diez.")],
  "diez", "Para sumar fracciones se igualan los denominadores."))

L.append(P("M1", E, "Probabilidad del complemento", "Al menos una cara 🪙",
  r"Se lanzan <b>3 monedas</b>. ¿Cuál es la probabilidad de obtener <b>al menos una cara</b>?",
  [r"$\dfrac{7}{8}$", r"$\dfrac{1}{8}$", r"$\dfrac{3}{8}$", r"$\dfrac{1}{2}$"], ["7/8", "1/8", "3/8", "1/2"], 0,
  [r"Es más fácil calcular lo contrario: ninguna cara (tres sellos): $\left(\tfrac{1}{2}\right)^3 = \tfrac{1}{8}$.", r"$$P = 1 - \frac{1}{8} = \frac{7}{8}$$"],
  r"Calcular solo la probabilidad de tres sellos y marcar B, o contar \"exactamente una cara\" (C).",
  r"\"Al menos uno\" se resuelve rápido con el complemento: $P(A) = 1 - P(\text{no } A)$.",
  "respuesta = 1 - Rational(1,2)**3",
  [(["Usamos el complemento", r"$P(\text{ninguna}) = \left(\dfrac{1}{2}\right)^3 = \dfrac{1}{8}$"], "Al menos una cara es lo contrario de cero caras. Tres sellos tiene probabilidad un octavo."),
   (["Restamos de 1", r"$1 - \dfrac{1}{8} = \dfrac{7}{8}$"], "Uno menos un octavo: siete octavos.")],
  "siete octavos", "Para al menos uno, usa uno menos la probabilidad de ninguno."))

L.append(P("M1", G, "Semejanza", "Agrandar una foto sin deformarla 🖼️",
  r"Una foto de <b>10 cm × 15 cm</b> se amplía para que el lado de 10 cm mida <b>20 cm</b>, sin deformarla. ¿Cuánto medirá el otro lado?",
  ["30 cm", "25 cm", "20 cm", "35 cm"], ["30", "25", "20", "35"], 0,
  [r"La razón de ampliación es $\dfrac{20}{10} = 2$.", r"$$15 \cdot 2 = 30 \text{ cm}$$"],
  r"Sumar 10 cm a cada lado y marcar B (25 cm): eso deforma la foto.",
  r"Ampliar sin deformar es multiplicar <b>todos</b> los lados por la misma razón.",
  "respuesta = 15 * Rational(20, 10)",
  [(["Razón de ampliación", r"$20 \div 10 = 2$"], "El lado de diez pasa a veinte: la foto se amplía al doble."),
   (["El otro lado también", r"$15 \cdot 2 = 30$"], "Entonces el otro lado también se duplica: treinta centímetros.")],
  "treinta centímetros", "Ampliar es multiplicar todos los lados por la misma razón, no sumar."))

L.append(P("M1", N, "Potencias de exponente negativo", "El exponente negativo no hace negativo 🤯",
  r"¿Cuál es el valor de $2^{-3}$?",
  [r"$\dfrac{1}{8}$", "$-8$", "$-6$", r"$\dfrac{1}{6}$"], ["1/8", "-8", "-6", "1/6"], 0,
  [r"Un exponente negativo invierte la base: $$2^{-3} = \frac{1}{2^3}$$", r"$$\frac{1}{2^3} = \frac{1}{8}$$"],
  r"Pensar que el exponente negativo hace negativo el resultado y marcar B.",
  r"$a^{-n} = \dfrac{1}{a^n}$: el signo menos del exponente invierte, no cambia el signo.",
  "respuesta = Integer(2)**-3",
  [(["Negativo: se invierte", r"$2^{-3} = \dfrac{1}{2^3}$"], "Un exponente negativo no hace negativo el resultado: lo invierte."),
   (["Calculamos", r"$\dfrac{1}{2^3} = \dfrac{1}{8}$"], "Dos al cubo es ocho, así que el resultado es un octavo.")],
  "un octavo", "Exponente negativo significa inverso."))

L.append(P("M1", A, "Ecuación cuadrática", "Sin fórmula, con un atajo ⚡",
  r"¿Cuál es la <b>suma</b> de las soluciones de la ecuación $$x^2 - 5x + 6 = 0\,?$$",
  ["5", "6", "$-5$", "1"], ["5", "6", "-5", "1"], 0,
  [r"Factorizamos: $(x - 2)(x - 3) = 0$, así que $x = 2$ o $x = 3$.", r"$$2 + 3 = 5$$"],
  r"Confundir la suma con el producto de las soluciones (6) o tomar $b = -5$ sin cambiar el signo.",
  r"En $x^2 + bx + c = 0$: suma de soluciones $= -b$, producto $= c$.",
  "x = symbols('x'); respuesta = sum(solve(x**2 - 5*x + 6, x))",
  [(["Factorizamos", r"$(x-2)(x-3) = 0$"], "Busca dos números que multiplicados den seis y sumados den cinco: dos y tres."),
   (["Sumamos las soluciones", r"$2 + 3 = 5$"], "Las soluciones son dos y tres, y su suma es cinco.")],
  "cinco", "La suma de las soluciones es menos be, y el producto es ce."))

L.append(P("M1", E, "Moda", "La moda no es el promedio 📊",
  r"¿Cuál es la <b>moda</b> del conjunto de datos $$2,\; 3,\; 3,\; 5,\; 7,\; 3,\; 5\,?$$",
  ["3", "5", "4", "7"], ["3", "5", "4", "7"], 0,
  [r"La moda es el dato que más se repite.", r"El 3 aparece 3 veces; el 5, dos veces. La moda es 3."],
  r"Calcular el promedio (4) o la mediana en vez de la moda.",
  r"Moda: el más repetido. Mediana: el del centro (ordenado). Media: el promedio.",
  "from collections import Counter; respuesta = Counter([2,3,3,5,7,3,5]).most_common(1)[0][0]",
  [(["Moda = el más repetido", r"$3 \to 3\ \text{veces}$"], "La moda es el dato que más se repite."),
   (["Comparamos", r"$5 \to 2\ \text{veces}$"], "El tres aparece tres veces y el cinco solo dos. La moda es tres.")],
  "tres", "Moda es el más repetido, mediana el del centro y media el promedio."))

L.append(P("M1", G, "Perímetro y área", "Del área al perímetro 🟦",
  r"Un cuadrado tiene un área de <b>49 cm²</b>. ¿Cuál es su perímetro?",
  ["28 cm", "49 cm", "14 cm", "196 cm"], ["28", "49", "14", "196"], 0,
  [r"El lado es la raíz del área: $\sqrt{49} = 7$ cm.", r"$$P = 4 \cdot 7 = 28 \text{ cm}$$"],
  r"Confundir área con perímetro o sumar solo dos lados (14 cm).",
  r"En un cuadrado: área $= a^2$ y perímetro $= 4a$.",
  "respuesta = 4*sqrt(49)",
  [(["Lado = raíz del área", r"$\sqrt{49} = 7$"], "Si el área es cuarenta y nueve, el lado es la raíz: siete centímetros."),
   (["Perímetro: 4 lados", r"$4 \cdot 7 = 28$"], "El perímetro son cuatro lados: veintiocho centímetros.")],
  "veintiocho centímetros", "Del área sacas el lado con la raíz; después multiplicas por cuatro."))

L.append(P("M2", N, "Propiedades de logaritmos", "El logaritmo que da 1 🔢",
  r"¿Cuál es el valor de $$\log 2 + \log 5\,?$$ (logaritmos en base 10)",
  ["1", r"$\log 7$", "10", "7"], ["1", "log(7,10)", "10", "7"], 0,
  [r"La suma de logaritmos de igual base es el logaritmo del producto: $$\log 2 + \log 5 = \log(2 \cdot 5)$$", r"$$\log 10 = 1$$"],
  r"Sumar los argumentos: $\log 2 + \log 5 = \log 7$, y marcar B.",
  r"$\log a + \log b = \log(ab)$ y $\log a - \log b = \log\!\left(\tfrac{a}{b}\right)$.",
  "respuesta = simplify(log(2,10) + log(5,10))",
  [(["Suma de logs = log del producto", r"$\log 2 + \log 5 = \log 10$"], "Sumar logaritmos de igual base es el logaritmo del producto: logaritmo de diez."),
   (["Base 10", r"$\log 10 = 1$"], "Y el logaritmo en base diez de diez es uno.")],
  "uno", "Logaritmo de a más logaritmo de be es logaritmo de a por be."))

L.append(P("M2", A, "Decaimiento exponencial", "¿Cuánto vale tu auto en 2 años? 🚗",
  r"Un auto vale <b>\$10.000.000</b> y pierde el <b>20%</b> de su valor cada año. ¿Cuánto valdrá en <b>2 años</b>?",
  [r"\$6.400.000", r"\$6.000.000", r"\$8.000.000", r"\$3.600.000"], ["6400000", "6000000", "8000000", "3600000"], 0,
  [r"Cada año conserva el 80%: se multiplica por 0,8.", r"$$10.000.000 \cdot 0{,}8^2 = 6.400.000$$"],
  r"Restar 20% dos veces sobre el valor inicial (40%) y marcar B.",
  r"Disminuir un $p\%$ cada periodo: $V = V_0 \,(1 - p)^n$.",
  "respuesta = 10000000 * Rational(8,10)**2",
  [(["Cada año conserva el 80%", r"$\times\, 0{,}8$ por año"], "Perder el veinte por ciento es quedarse con el ochenta: multiplicar por cero coma ocho."),
   (["Dos años", r"$10.000.000 \cdot 0{,}8^2 = 6.400.000$"], "Dos años: diez millones por cero coma ocho al cuadrado, seis millones cuatrocientos mil.")],
  "seis millones cuatrocientos mil pesos", "Una baja porcentual repetida es exponencial, no se resta dos veces."))

L.append(P("M2", E, "Permutaciones", "¿De cuántas formas ordenas tus libros? 📚",
  r"¿De cuántas formas distintas se pueden ordenar <b>4 libros diferentes</b> en una repisa?",
  ["24", "16", "12", "256"], ["24", "16", "12", "256"], 0,
  [r"Para el primer lugar hay 4 opciones, luego 3, luego 2 y luego 1.", r"$$4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24$$"],
  r"Multiplicar $4 \cdot 4 = 16$ como si se pudiera repetir el mismo libro.",
  r"Ordenar $n$ objetos distintos: $n!$ formas.",
  "respuesta = factorial(4)",
  [(["Opciones por lugar", r"$4 \cdot 3 \cdot 2 \cdot 1$"], "Para el primer lugar hay cuatro libros, para el segundo quedan tres, después dos y al final uno."),
   (["Factorial", r"$4! = 24$"], "Cuatro factorial: veinticuatro formas.")],
  "veinticuatro", "Ordenar ene objetos distintos se hace de ene factorial formas."))

L.append(P("M2", G, "Trigonometría", "La altura del árbol con un ángulo 🌳",
  r"Desde <b>10 m</b> de la base de un árbol, se ve su punta con un ángulo de elevación de <b>60°</b>. ¿Cuál es la altura del árbol?",
  [r"$10\sqrt{3}$ m", "10 m", "20 m", r"$5\sqrt{3}$ m"], ["10*sqrt(3)", "10", "20", "5*sqrt(3)"], 0,
  [r"La altura es el cateto opuesto y los 10 m el adyacente: $$\tan 60^\circ = \frac{h}{10}$$", r"Como $\tan 60^\circ = \sqrt{3}$: $$h = 10\sqrt{3} \text{ m}$$"],
  r"Usar seno o coseno con los 10 m como si fueran la hipotenusa.",
  r"Opuesto y adyacente: tangente. $\tan 30^\circ = \tfrac{\sqrt3}{3}$, $\tan 45^\circ = 1$, $\tan 60^\circ = \sqrt3$.",
  "respuesta = 10*tan(pi/3)",
  [(["Opuesto / adyacente = tangente", r"$\tan 60^\circ = \dfrac{h}{10}$"], "La altura es el cateto opuesto al ángulo y los diez metros son el adyacente. Eso es tangente."),
   (["tan 60° = √3", r"$h = 10\sqrt{3}$"], "Tangente de sesenta grados es raíz de tres, así que la altura es diez raíz de tres metros.")],
  "diez raíz de tres metros", "Con opuesto y adyacente se usa la tangente."))


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


rnd = random.Random(20261023)
metas = [i % 4 for i in range(len(L))]; rnd.shuffle(metas)
lote = [finalizar(p, rnd, metas[i]) for i, p in enumerate(L)]
json.dump(lote, open(os.path.join(AQUI, "lote_2026-10-23.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(lote), "problemas")
