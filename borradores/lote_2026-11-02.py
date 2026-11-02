# Lote 02-nov-2026: problemas normales (4 alternativas, con guion de voz).
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
L.append(P("M1", N, "Descuentos sucesivos", "30% + 20% NO es 50% de descuento 🛍️",
  r"Una polera cuesta <b>\$40.000</b>. Tiene un <b>30% de descuento</b> y, en caja, un <b>20% adicional</b> sobre el precio ya rebajado. ¿Cuánto se paga?",
  [r"\$22.400", r"\$20.000", r"\$28.000", r"\$32.000"], ["22400", "20000", "28000", "32000"], 0,
  [r"Con el 30% de descuento se paga el 70%: $$40.000 \cdot 0{,}7 = 28.000$$", r"El 20% adicional se aplica sobre \$28.000: $$28.000 \cdot 0{,}8 = 22.400$$"],
  r"Sumar los descuentos (50%) y marcar B (\$20.000).",
  r"Los descuentos sucesivos se <b>multiplican</b>: $0{,}7 \cdot 0{,}8 = 0{,}56$, o sea se paga el 56%.",
  "respuesta = 40000*Rational(7,10)*Rational(8,10)",
  [(["Primer descuento: pagas 70%", r"$40.000 \cdot 0{,}7 = 28.000$"], "Con treinta por ciento de descuento pagas el setenta por ciento: veintiocho mil pesos."),
   (["El 20% va sobre lo rebajado", r"$28.000 \cdot 0{,}8 = 22.400$"], "El veinte por ciento adicional se aplica sobre veintiocho mil. Pagas el ochenta por ciento: veintidós mil cuatrocientos.")],
  "veintidós mil cuatrocientos pesos", "Los descuentos sucesivos se multiplican, no se suman."))

L.append(P("M1", N, "Porcentaje inverso: IVA", "¿Cuánto costaba sin IVA? 🧾",
  r"Una boleta muestra un total de <b>\$11.900</b>, que ya incluye el <b>IVA de 19%</b>. ¿Cuál era el precio <b>sin IVA</b>?",
  [r"\$10.000", r"\$9.639", r"\$6.263", r"\$14.161"], ["10000", "9639", "6263", "14161"], 0,
  [r"Precio con IVA = precio sin IVA $\cdot\, 1{,}19$: $$x \cdot 1{,}19 = 11.900$$", r"$$x = \frac{11.900}{1{,}19} = 10.000$$"],
  r"Restar el 19% de \$11.900 y marcar B (\$9.639): el 19% se calcula sobre el precio sin IVA, no sobre el total.",
  r"Para quitar un aumento de $p\%$ se <b>divide</b> por $(1 + p)$; no se resta el porcentaje.",
  "x = symbols('x'); respuesta = solve(Eq(x*Rational(119,100), 11900), x)[0]",
  [(["Con IVA: por 1,19", r"$x \cdot 1{,}19 = 11.900$"], "Agregar el diecinueve por ciento es multiplicar por uno coma diecinueve."),
   (["Dividimos", r"$x = \dfrac{11.900}{1{,}19} = 10.000$"], "Entonces, para quitarlo, dividimos once mil novecientos en uno coma diecinueve: diez mil pesos.")],
  "diez mil pesos", "Para quitar el IVA se divide por uno coma diecinueve, no se resta el diecinueve por ciento."))

L.append(P("M1", N, "Razones en mezclas", "El jugo perfecto 🧃",
  r"Un jugo se prepara mezclando concentrado y agua en razón <b>1 : 4</b>. ¿Cuánto concentrado se necesita para preparar <b>2 litros</b> de jugo?",
  ["400 mL", "500 mL", "1.600 mL", "800 mL"], ["400", "500", "1600", "800"], 0,
  [r"La razón 1 : 4 forma $1 + 4 = 5$ partes iguales.", r"$$\frac{2.000 \text{ mL}}{5} = 400 \text{ mL}$$ de concentrado."],
  r"Dividir 2 litros en 4 partes y marcar B (500 mL), olvidando que el total tiene 5 partes.",
  r"En una razón $a : b$, el total se divide en $a + b$ partes.",
  "respuesta = 2000*Rational(1, 1+4)",
  [(["1 : 4 son 5 partes", r"$1 + 4 = 5$"], "Uno es a cuatro significa una parte de concentrado y cuatro de agua: cinco partes en total."),
   (["Cada parte", r"$2.000 \div 5 = 400\ \text{mL}$"], "Dos litros son dos mil mililitros. Divididos en cinco: cuatrocientos mililitros por parte.")],
  "cuatrocientos mililitros", "En una razón, primero cuenta cuántas partes forman el total."))

L.append(P("M1", N, "Propiedades de potencias", "Potencias en 10 segundos ⚡",
  r"¿Cuál es el valor de $$\frac{2^5 \cdot 2^3}{2^6}\,?$$",
  ["4", "512", "2", "16"], ["4", "512", "2", "16"], 0,
  [r"Al multiplicar potencias de igual base se suman los exponentes: $2^5 \cdot 2^3 = 2^8$.", r"Al dividir se restan: $$\frac{2^8}{2^6} = 2^2 = 4$$"],
  r"Multiplicar los exponentes ($2^{15}$) y llegar a $2^9 = 512$ (B).",
  r"$a^m \cdot a^n = a^{m+n}$ y $\dfrac{a^m}{a^n} = a^{m-n}$.",
  "respuesta = Integer(2)**5*Integer(2)**3/Integer(2)**6",
  [(["Multiplicar: se suman", r"$2^5 \cdot 2^3 = 2^8$"], "Al multiplicar potencias de igual base, los exponentes se suman: dos elevado a ocho."),
   (["Dividir: se restan", r"$\dfrac{2^8}{2^6} = 2^2 = 4$"], "Al dividir se restan: ocho menos seis, dos. Dos al cuadrado es cuatro.")],
  "cuatro", "Multiplicar potencias de igual base suma los exponentes; dividir los resta."))

L.append(P("M1", N, "Suma de raíces", "Las raíces no se suman así 😬",
  r"¿Cuál es el resultado de $$\sqrt{50} + \sqrt{18}\,?$$",
  [r"$8\sqrt{2}$", r"$\sqrt{68}$", r"$15\sqrt{2}$", "8"], ["8*sqrt(2)", "sqrt(68)", "15*sqrt(2)", "8"], 0,
  [r"Descomponemos: $\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt{2}$ y $\sqrt{18} = \sqrt{9 \cdot 2} = 3\sqrt{2}$.", r"$$5\sqrt{2} + 3\sqrt{2} = 8\sqrt{2}$$"],
  r"Sumar las cantidades subradicales, $\sqrt{50 + 18} = \sqrt{68}$, y marcar B.",
  r"Solo se suman raíces <b>semejantes</b> (misma cantidad subradical): $a\sqrt{n} + b\sqrt{n} = (a+b)\sqrt{n}$.",
  "respuesta = sqrt(50) + sqrt(18)",
  [(["Descomponemos", r"$\sqrt{50} = 5\sqrt{2}$", ], "Raíz de cincuenta es cinco raíz de dos, porque cincuenta es veinticinco por dos."),
   (["y también", r"$\sqrt{18} = 3\sqrt{2}$"], "Raíz de dieciocho es tres raíz de dos."),
   (["Sumamos las semejantes", r"$5\sqrt{2} + 3\sqrt{2} = 8\sqrt{2}$"], "Ahora son raíces semejantes: cinco más tres, ocho raíz de dos.")],
  "ocho raíz de dos", "Las raíces se suman solo si tienen lo mismo adentro."))

L.append(P("M1", N, "Decimales periódicos", "0,666… ¿qué fracción es? 🤔",
  r"¿Qué fracción es igual al decimal periódico $0{,}\overline{6}$?",
  [r"$\dfrac{2}{3}$", r"$\dfrac{3}{5}$", r"$\dfrac{1}{6}$", r"$\dfrac{3}{50}$"], ["2/3", "3/5", "1/6", "3/50"], 0,
  [r"Un periódico puro de una cifra es esa cifra sobre 9: $$0{,}\overline{6} = \frac{6}{9}$$", r"Simplificamos por 3: $$\frac{6}{9} = \frac{2}{3}$$"],
  r"Escribirlo como decimal finito, $0{,}6 = \tfrac{6}{10} = \tfrac{3}{5}$, y marcar B.",
  r"Periódico puro: el período sobre tantos 9 como cifras tenga. Ej.: $0{,}\overline{12} = \tfrac{12}{99}$.",
  "n = symbols('n'); respuesta = summation(6*Rational(1,10)**n, (n, 1, oo))",
  [(["Período sobre 9", r"$0{,}\overline{6} = \dfrac{6}{9}$"], "Cero coma seis periódico es seis novenos, no seis décimos."),
   (["Simplificamos", r"$\dfrac{6}{9} = \dfrac{2}{3}$"], "Simplificando por tres: dos tercios. Compruébalo: dos dividido en tres da cero coma seis seis seis.")],
  "dos tercios", "Un periódico puro es el período sobre tantos nueves como cifras tenga."))

L.append(P("M1", N, "Números enteros: temperatura", "Frío en Punta Arenas 🥶",
  r"En Punta Arenas, la temperatura mínima de un día fue <b>−4 °C</b> y la máxima, <b>7 °C</b>. ¿Cuál fue la diferencia entre la máxima y la mínima?",
  ["11 °C", "3 °C", "−3 °C", "−11 °C"], ["11", "3", "-3", "-11"], 0,
  [r"Diferencia = máxima − mínima: $$7 - (-4)$$", r"Restar un negativo es sumar: $$7 + 4 = 11\ ^\circ\text{C}$$"],
  r"Hacer $7 - 4 = 3$ y marcar B, olvidando que la mínima es negativa.",
  r"Restar un número negativo es sumar su opuesto: $a - (-b) = a + b$.",
  "respuesta = 7 - (-4)",
  [(["Máxima menos mínima", r"$7 - (-4)$"], "La diferencia es la máxima menos la mínima: siete menos menos cuatro."),
   (["Menos por menos", r"$7 + 4 = 11$"], "Restar un negativo es sumar: siete más cuatro, once grados.")],
  "once grados", "Restar un número negativo es lo mismo que sumar."))

L.append(P("M1", N, "Proporcionalidad compuesta", "Más máquinas, menos horas 🏭",
  r"<b>3 máquinas</b> fabrican <b>600 poleras</b> en <b>5 horas</b>. Al mismo ritmo, ¿cuántas poleras fabrican <b>6 máquinas</b> en <b>4 horas</b>?",
  ["960", "1.200", "480", "720"], ["960", "1200", "480", "720"], 0,
  [r"Ritmo de una máquina en una hora: $$\frac{600}{3 \cdot 5} = 40$$ poleras.", r"$$40 \cdot 6 \cdot 4 = 960$$ poleras."],
  r"Considerar solo que se duplican las máquinas y marcar B (1.200), sin ajustar las horas.",
  r"En proporcionalidad compuesta, calcula primero el rendimiento de <b>una</b> máquina en <b>una</b> hora.",
  "respuesta = Rational(600, 3*5) * 6 * 4",
  [(["Una máquina, una hora", r"$\dfrac{600}{3 \cdot 5} = 40$"], "Primero, cuánto hace una máquina en una hora: seiscientas dividido en quince, cuarenta poleras."),
   (["Seis máquinas, cuatro horas", r"$40 \cdot 6 \cdot 4 = 960$"], "Seis máquinas por cuatro horas: cuarenta por veinticuatro, novecientas sesenta.")],
  "novecientas sesenta poleras", "Reduce todo a una unidad y después multiplica."))

L.append(P("M1", N, "Operatoria con fracciones", "¿Cuánto queda del sueldo? 💰",
  r"Camila gasta $\dfrac{2}{5}$ de su sueldo en arriendo y $\dfrac{1}{3}$ en comida. ¿Qué <b>fracción</b> del sueldo le queda?",
  [r"$\dfrac{4}{15}$", r"$\dfrac{5}{8}$", r"$\dfrac{11}{15}$", r"$\dfrac{3}{8}$"], ["4/15", "5/8", "11/15", "3/8"], 0,
  [r"Sumamos lo gastado con denominador 15: $$\frac{6}{15} + \frac{5}{15} = \frac{11}{15}$$", r"$$1 - \frac{11}{15} = \frac{4}{15}$$"],
  r"Responder lo gastado, $\tfrac{11}{15}$, y marcar C; o sumar numeradores y denominadores ($\tfrac{3}{8}$).",
  r"Para sumar fracciones, iguala denominadores. Lo que queda es $1 -$ lo que se gastó.",
  "respuesta = 1 - Rational(2,5) - Rational(1,3)",
  [(["Lo gastado", r"$\dfrac{2}{5} + \dfrac{1}{3} = \dfrac{11}{15}$"], "Dos quintos más un tercio. Con denominador quince: seis más cinco, once quinceavos."),
   (["Lo que queda", r"$1 - \dfrac{11}{15} = \dfrac{4}{15}$"], "Le queda el entero menos lo gastado: cuatro quinceavos.")],
  "cuatro quinceavos", "Lee bien si te preguntan lo que se gastó o lo que queda."))

L.append(P("M1", N, "Porcentaje de un porcentaje", "El 25% del 40% ⚽",
  r"En un curso, el <b>40%</b> son mujeres y, de ellas, el <b>25%</b> juega fútbol. ¿Qué porcentaje del <b>curso</b> son mujeres que juegan fútbol?",
  ["10%", "65%", "15%", "25%"], ["10", "65", "15", "25"], 0,
  [r"El 25% de las mujeres es el 25% del 40%: $$0{,}25 \cdot 0{,}4 = 0{,}1$$", r"$$0{,}1 = 10\%$$ del curso."],
  r"Sumar los porcentajes y marcar B (65%), o restarlos (15%).",
  r"El $a\%$ del $b\%$ se calcula multiplicando: $\dfrac{a}{100} \cdot \dfrac{b}{100}$.",
  "respuesta = Rational(40,100)*Rational(25,100)*100",
  [(["El 25% del 40%", r"$0{,}25 \cdot 0{,}4$"], "Las futbolistas son el veinticinco por ciento de las mujeres, que son el cuarenta por ciento del curso."),
   (["Multiplicamos", r"$0{,}25 \cdot 0{,}4 = 0{,}1 = 10\%$"], "Cero coma veinticinco por cero coma cuatro: cero coma uno, el diez por ciento.")],
  "diez por ciento", "Un porcentaje de otro porcentaje se multiplica."))

L.append(P("M1", N, "MCD en contexto", "Cortar sin que sobre nada ✂️",
  r"Se tienen dos cintas de <b>48 cm</b> y <b>72 cm</b>. Se quieren cortar en trozos <b>iguales</b>, lo más largos posible, sin que sobre nada. ¿Cuánto mide cada trozo?",
  ["24 cm", "12 cm", "144 cm", "6 cm"], ["24", "12", "144", "6"], 0,
  [r"El trozo debe caber exacto en 48 y en 72: buscamos el <b>máximo común divisor</b>.", r"$$48 = 2^4 \cdot 3, \quad 72 = 2^3 \cdot 3^2$$ $$\text{MCD} = 2^3 \cdot 3 = 24$$"],
  r"Calcular el mínimo común múltiplo y marcar C (144 cm), o quedarse con un divisor común que no es el mayor (12 cm).",
  r"Partir en partes iguales lo más grandes posible: MCD. Coincidir en el tiempo o en un múltiplo: MCM.",
  "respuesta = gcd(48, 72)",
  [(["Máximo común divisor", r"$48 = 2^4 \cdot 3 \quad 72 = 2^3 \cdot 3^2$"], "El trozo tiene que caber exacto en las dos cintas. Eso es el máximo común divisor."),
   (["Factores comunes", r"$2^3 \cdot 3 = 24$"], "Tomamos los factores comunes con el menor exponente: dos al cubo por tres, veinticuatro centímetros.")],
  "veinticuatro centímetros", "Partir en trozos iguales lo más grandes posible es el máximo común divisor."))

L.append(P("M1", N, "Conversión de unidades", "De km/h a m/s sin enredarse 🚌",
  r"Un bus avanza por la Ruta 5 a <b>72 km/h</b>. ¿A cuántos <b>metros por segundo</b> equivale esa rapidez?",
  ["20 m/s", "72 m/s", "1.200 m/s", "259,2 m/s"], ["20", "72", "1200", "2592/10"], 0,
  [r"72 km son 72.000 m, y 1 hora son 3.600 s.", r"$$\frac{72.000 \text{ m}}{3.600 \text{ s}} = 20 \text{ m/s}$$"],
  r"Dividir solo por 60, como si una hora tuviera 60 segundos, y marcar C (1.200 m/s).",
  r"De km/h a m/s se divide por $3{,}6$; de m/s a km/h se multiplica por $3{,}6$.",
  "respuesta = Rational(72*1000, 3600)",
  [(["A metros y segundos", r"$\dfrac{72.000\ \text{m}}{3.600\ \text{s}}$"], "Setenta y dos kilómetros son setenta y dos mil metros, y una hora tiene tres mil seiscientos segundos."),
   (["Dividimos", r"$72.000 \div 3.600 = 20$"], "Dividiendo: veinte metros por segundo.")],
  "veinte metros por segundo", "Para pasar de kilómetros por hora a metros por segundo, divide por tres coma seis."))

# ======================= M1 · ÁLGEBRA Y FUNCIONES
L.append(P("M1", A, "Problema de edades", "El clásico de las edades 👨‍👧",
  r"Pedro tiene el <b>triple</b> de la edad de su hija. En <b>10 años</b> tendrá el <b>doble</b> de la edad de ella. ¿Qué edad tiene hoy la hija?",
  ["10 años", "20 años", "30 años", "5 años"], ["10", "20", "30", "5"], 0,
  [r"Hija: $x$; Pedro: $3x$. En 10 años: $$3x + 10 = 2(x + 10)$$", r"$$3x + 10 = 2x + 20 \Rightarrow x = 10$$"],
  r"Responder la edad de Pedro y marcar C (30 años), o sumar los 10 años a una sola persona.",
  r"En problemas de edades, suma los años a las <b>dos</b> personas antes de plantear la ecuación.",
  "x = symbols('x'); respuesta = solve(Eq(3*x + 10, 2*(x + 10)), x)[0]",
  [(["En 10 años, a los dos", r"$3x + 10 = 2(x + 10)$"], "Si la hija tiene equis, Pedro tiene tres equis. En diez años, tres equis más diez es el doble de equis más diez."),
   (["Despejamos", r"$3x + 10 = 2x + 20 \Rightarrow x = 10$"], "Despejando, equis vale diez.")],
  "diez años", "Los años pasan para las dos personas, no solo para una."))

L.append(P("M1", A, "Sistema 2x2: entradas al cine", "Cine en familia 🍿",
  r"En el cine, <b>3 entradas de adulto y 2 de niño</b> cuestan <b>\$23.000</b>, y <b>1 de adulto y 4 de niño</b>, <b>\$21.000</b>. ¿Cuánto cuesta una entrada de niño?",
  [r"\$4.000", r"\$5.000", r"\$4.400", r"\$3.500"], ["4000", "5000", "4400", "3500"], 0,
  [r"De la segunda: $a = 21.000 - 4n$. En la primera: $$3(21.000 - 4n) + 2n = 23.000$$", r"$$63.000 - 10n = 23.000 \Rightarrow n = 4.000$$"],
  r"Resolver bien, pero responder el precio de la entrada de adulto y marcar B (\$5.000).",
  r"En un sistema, despeja la incógnita más fácil (la de coeficiente 1) y reemplázala en la otra ecuación.",
  "a, n = symbols('a n'); s = solve([Eq(3*a + 2*n, 23000), Eq(a + 4*n, 21000)], [a, n]); respuesta = s[n]",
  [(["Despejamos a", r"$a = 21.000 - 4n$"], "De la segunda ecuación, la entrada de adulto es veintiún mil menos cuatro ene."),
   (["Reemplazamos", r"$63.000 - 10n = 23.000$"], "Al reemplazar en la primera queda sesenta y tres mil menos diez ene igual veintitrés mil."),
   (["Despejamos n", r"$10n = 40.000 \Rightarrow n = 4.000$"], "Diez ene es cuarenta mil, así que la entrada de niño cuesta cuatro mil.")],
  "cuatro mil pesos", "Despeja la incógnita con coeficiente uno y reemplázala en la otra ecuación."))

L.append(P("M1", A, "Función afín: cuenta de la luz", "¿Cuánto consumiste? 💡",
  r"Una cuenta de la luz cobra un <b>cargo fijo de \$1.200</b> más <b>\$150 por kWh</b>. Si un mes se pagaron <b>\$28.200</b>, ¿cuántos kWh se consumieron?",
  ["180", "188", "196", "200"], ["180", "188", "196", "200"], 0,
  [r"La cuenta es $C(x) = 1.200 + 150x$: $$1.200 + 150x = 28.200$$", r"$$150x = 27.000 \Rightarrow x = 180$$"],
  r"Dividir \$28.200 por 150 sin restar el cargo fijo y marcar B (188).",
  r"En una función afín $f(x) = mx + n$, el valor fijo $n$ se resta antes de dividir por la pendiente.",
  "x = symbols('x'); respuesta = solve(Eq(1200 + 150*x, 28200), x)[0]",
  [(["Planteamos", r"$1.200 + 150x = 28.200$"], "La cuenta es mil doscientos fijos más ciento cincuenta por cada kilowatt hora."),
   (["Despejamos", r"$150x = 27.000 \Rightarrow x = 180$"], "Restamos el cargo fijo: veintisiete mil. Dividido en ciento cincuenta: ciento ochenta kilowatt hora.")],
  "ciento ochenta kilowatt hora", "Primero se resta el cargo fijo y después se divide."))

L.append(P("M1", A, "Pendiente de una recta", "¿Cuánto sube la recta? 📈",
  r"¿Cuál es la <b>pendiente</b> de la recta que pasa por los puntos $(2, 5)$ y $(6, 13)$?",
  ["2", r"$\dfrac{1}{2}$", "8", "4"], ["2", "1/2", "8", "4"], 0,
  [r"$$m = \frac{y_2 - y_1}{x_2 - x_1}$$", r"$$m = \frac{13 - 5}{6 - 2} = \frac{8}{4} = 2$$"],
  r"Invertir la fórmula (cambio en $x$ sobre cambio en $y$) y marcar B.",
  r"Pendiente = cambio en $y$ dividido por cambio en $x$.",
  "respuesta = Rational(13 - 5, 6 - 2)",
  [(["Pendiente", r"$m = \dfrac{y_2 - y_1}{x_2 - x_1}$"], "La pendiente es la diferencia de las y dividida en la diferencia de las x."),
   (["Reemplazamos", r"$m = \dfrac{13 - 5}{6 - 2} = 2$"], "Trece menos cinco es ocho; seis menos dos es cuatro. Ocho dividido en cuatro: dos.")],
  "dos", "La pendiente es cuánto sube y por cada unidad que avanza x."))

L.append(P("M1", A, "Valor mínimo de una cuadrática", "El punto más bajo de la parábola ⬇️",
  r"¿Cuál es el <b>valor mínimo</b> de la función $$f(x) = x^2 - 6x + 5\,?$$",
  ["$-4$", "3", "5", "$-3$"], ["-4", "3", "5", "-3"], 0,
  [r"El vértice está en $x = -\dfrac{b}{2a} = \dfrac{6}{2} = 3$.", r"$$f(3) = 9 - 18 + 5 = -4$$"],
  r"Responder la coordenada $x$ del vértice en vez del valor de la función, y marcar B (3).",
  r"En $f(x) = ax^2 + bx + c$ con $a > 0$, el mínimo es $f\!\left(-\tfrac{b}{2a}\right)$.",
  "x = symbols('x'); f = x**2 - 6*x + 5; respuesta = f.subs(x, solve(diff(f, x), x)[0])",
  [(["x del vértice", r"$x = -\dfrac{b}{2a} = 3$"], "La parábola abre hacia arriba, así que el mínimo está en el vértice: equis igual menos be partido en dos a, tres."),
   (["Evaluamos", r"$f(3) = 9 - 18 + 5 = -4$"], "Ahora evaluamos en tres: nueve menos dieciocho más cinco, menos cuatro.")],
  "menos cuatro", "El mínimo es el valor de la función en el vértice, no la equis."))

L.append(P("M1", A, "Diferencia de cuadrados", "Cálculo mental de crack 🧠",
  r"Sin calculadora: ¿cuál es el valor de $$101^2 - 99^2\,?$$",
  ["400", "4", "200", "40.000"], ["400", "4", "200", "40000"], 0,
  [r"Diferencia de cuadrados: $a^2 - b^2 = (a+b)(a-b)$.", r"$$(101 + 99)(101 - 99) = 200 \cdot 2 = 400$$"],
  r"Pensar que $a^2 - b^2 = (a - b)^2$ y obtener $2^2 = 4$ (B).",
  r"$a^2 - b^2 = (a+b)(a-b)$: suma por diferencia. Sirve para calcular rápido.",
  "respuesta = 101**2 - 99**2",
  [(["Suma por diferencia", r"$a^2 - b^2 = (a+b)(a-b)$"], "Usamos la diferencia de cuadrados: suma por diferencia."),
   (["Calculamos", r"$200 \cdot 2 = 400$"], "Ciento uno más noventa y nueve es doscientos, y la diferencia es dos. Doscientos por dos: cuatrocientos.")],
  "cuatrocientos", "A al cuadrado menos be al cuadrado es suma por diferencia."))

L.append(P("M1", A, "Inecuación: nota mínima", "¿Qué nota necesito para eximirme? 📝",
  r"Sofía tiene notas <b>5,2</b> y <b>4,6</b>. Para eximirse necesita un promedio de <b>al menos 5,0</b> con una tercera nota. ¿Cuál es la <b>nota mínima</b> que necesita?",
  ["5,2", "5,0", "4,8", "5,4"], ["26/5", "5", "24/5", "27/5"], 0,
  [r"$$\frac{5{,}2 + 4{,}6 + x}{3} \geq 5{,}0$$", r"$$9{,}8 + x \geq 15 \Rightarrow x \geq 5{,}2$$"],
  r"Creer que basta con sacar 5,0 y marcar B: el 4,6 baja el promedio.",
  r"Promedio mínimo $\cdot$ número de notas = suma mínima. Lo que falta es la nota necesaria.",
  "x = symbols('x'); respuesta = solve(Eq((Rational(52,10) + Rational(46,10) + x)/3, 5), x)[0]",
  [(["Planteamos", r"$\dfrac{5{,}2 + 4{,}6 + x}{3} \geq 5$"], "El promedio de las tres notas tiene que ser al menos cinco."),
   (["Despejamos", r"$9{,}8 + x \geq 15 \Rightarrow x \geq 5{,}2$"], "Multiplicando por tres, la suma debe ser al menos quince. Ya tiene nueve coma ocho, así que necesita un cinco coma dos.")],
  "cinco coma dos", "Multiplica el promedio que quieres por la cantidad de notas y resta lo que ya tienes."))

L.append(P("M1", A, "Despeje de fórmulas", "De Fahrenheit a Celsius 🌡️",
  r"La fórmula $F = \dfrac{9}{5}C + 32$ convierte grados Celsius a Fahrenheit. Si un termómetro marca <b>86 °F</b>, ¿a cuántos <b>°C</b> equivale?",
  ["30 °C", "54 °C", "97,2 °C", "22 °C"], ["30", "54", "486/5", "22"], 0,
  [r"Restamos 32: $$\frac{9}{5}C = 86 - 32 = 54$$", r"$$C = 54 \cdot \frac{5}{9} = 30$$"],
  r"Quedarse en $86 - 32 = 54$ (B) sin deshacer el $\tfrac{9}{5}$.",
  r"Para despejar, deshaz las operaciones en orden inverso: primero lo que suma, después lo que multiplica.",
  "C = symbols('C'); respuesta = solve(Eq(Rational(9,5)*C + 32, 86), C)[0]",
  [(["Restamos 32", r"$\dfrac{9}{5}C = 54$"], "Primero deshacemos la suma: ochenta y seis menos treinta y dos, cincuenta y cuatro."),
   (["Multiplicamos por 5/9", r"$C = 54 \cdot \dfrac{5}{9} = 30$"], "Después deshacemos el nueve quintos: cincuenta y cuatro por cinco novenos, treinta grados.")],
  "treinta grados Celsius", "Para despejar, deshaz las operaciones en orden inverso."))

L.append(P("M1", A, "Lenguaje algebraico", "Traduce y resuelve ✍️",
  r"El <b>doble</b> de un número, <b>disminuido en 7</b>, es igual a <b>15</b>. ¿Cuál es el número?",
  ["11", "4", "22", "8"], ["11", "4", "22", "8"], 0,
  [r"Traducimos: $$2x - 7 = 15$$", r"$$2x = 22 \Rightarrow x = 11$$"],
  r"Restar 7 en vez de sumarlo al despejar y obtener 4 (B).",
  r"\"Disminuido en\" es restar; \"el doble\" es multiplicar por 2. Traduce frase por frase.",
  "x = symbols('x'); respuesta = solve(Eq(2*x - 7, 15), x)[0]",
  [(["Traducimos", r"$2x - 7 = 15$"], "El doble de un número es dos equis; disminuido en siete, menos siete. Igual a quince."),
   (["Despejamos", r"$2x = 22 \Rightarrow x = 11$"], "Sumamos siete: dos equis es veintidós. El número es once.")],
  "once", "Traduce la frase pedazo por pedazo antes de despejar."))

L.append(P("M1", A, "Ecuaciones con paréntesis", "Ojo con el signo antes del paréntesis ⚠️",
  r"¿Cuál es la solución de $$3(x - 2) - 2(x + 1) = 4\,?$$",
  ["12", "8", "11", "4"], ["12", "8", "11", "4"], 0,
  [r"Distribuimos (ojo con el signo): $$3x - 6 - 2x - 2 = 4$$", r"$$x - 8 = 4 \Rightarrow x = 12$$"],
  r"Escribir $-2(x+1) = -2x + 2$ y llegar a 8 (B).",
  r"El signo que está antes del paréntesis multiplica a <b>todos</b> los términos de adentro.",
  "x = symbols('x'); respuesta = solve(Eq(3*(x-2) - 2*(x+1), 4), x)[0]",
  [(["Distribuimos", r"$3x - 6 - 2x - 2 = 4$"], "Ojo con el menos dos: multiplica a la equis y también al uno. Queda menos dos equis menos dos."),
   (["Reducimos", r"$x - 8 = 4 \Rightarrow x = 12$"], "Reduciendo: equis menos ocho igual cuatro. Equis vale doce.")],
  "doce", "El signo antes del paréntesis afecta a todos los términos de adentro."))

# ======================= M1 · GEOMETRÍA
L.append(P("M1", G, "Pitágoras: pantalla", "¿Cuántas pulgadas tiene la tele? 📺",
  r"Una pantalla mide <b>40 pulgadas</b> de ancho y <b>30 pulgadas</b> de alto. ¿Cuánto mide su <b>diagonal</b>?",
  ["50 pulgadas", "70 pulgadas", "35 pulgadas", r"$10\sqrt{7}$ pulgadas"], ["50", "70", "35", "10*sqrt(7)"], 0,
  [r"La diagonal es la hipotenusa: $$d^2 = 40^2 + 30^2 = 1.600 + 900 = 2.500$$", r"$$d = \sqrt{2.500} = 50$$"],
  r"Sumar los lados y marcar B (70), o restar los cuadrados en vez de sumarlos ($10\sqrt{7}$).",
  r"Trío pitagórico 3, 4, 5 y sus múltiplos: 30, 40, 50.",
  "respuesta = sqrt(40**2 + 30**2)",
  [(["La diagonal es hipotenusa", r"$d^2 = 40^2 + 30^2 = 2.500$"], "El ancho, el alto y la diagonal forman un triángulo rectángulo. Cuarenta al cuadrado más treinta al cuadrado: dos mil quinientos."),
   (["Raíz", r"$d = \sqrt{2.500} = 50$"], "La raíz de dos mil quinientos es cincuenta pulgadas.")],
  "cincuenta pulgadas", "Treinta, cuarenta y cincuenta es el trío tres, cuatro, cinco por diez."))

L.append(P("M1", G, "Volumen del cilindro", "¿Cuánta agua cabe en el estanque? 💧",
  r"Un estanque cilíndrico tiene <b>radio 1 m</b> y <b>altura 2 m</b>. Usando $\pi \approx 3{,}14$, ¿cuántos <b>litros</b> caben? ($1\ \text{m}^3 = 1.000$ L)",
  ["6.280 L", "3.140 L", "12.560 L", "628 L"], ["6280", "3140", "12560", "628"], 0,
  [r"$$V = \pi r^2 h = 3{,}14 \cdot 1^2 \cdot 2 = 6{,}28 \text{ m}^3$$", r"$$6{,}28 \cdot 1.000 = 6.280 \text{ L}$$"],
  r"Calcular solo el área de la base (3,14) olvidando la altura y marcar B.",
  r"Volumen de un cilindro: área de la base por la altura, $V = \pi r^2 h$.",
  "respuesta = Rational(314,100)*1**2*2*1000",
  [(["Volumen = πr²h", r"$3{,}14 \cdot 1^2 \cdot 2 = 6{,}28\ \text{m}^3$"], "El volumen del cilindro es pi por radio al cuadrado por la altura: seis coma veintiocho metros cúbicos."),
   (["A litros", r"$6{,}28 \cdot 1.000 = 6.280\ \text{L}$"], "Cada metro cúbico son mil litros: seis mil doscientos ochenta litros.")],
  "seis mil doscientos ochenta litros", "Volumen del cilindro: área de la base por la altura."))

L.append(P("M1", G, "Área del trapecio", "Un terreno con forma de trapecio 🏡",
  r"Un terreno tiene forma de <b>trapecio</b>, con bases de <b>12 m</b> y <b>8 m</b>, y altura de <b>5 m</b>. ¿Cuál es su área?",
  ["50 m²", "100 m²", "480 m²", "40 m²"], ["50", "100", "480", "40"], 0,
  [r"$$A = \frac{(B + b)\,h}{2}$$", r"$$A = \frac{(12 + 8) \cdot 5}{2} = \frac{100}{2} = 50 \text{ m}^2$$"],
  r"Olvidar dividir por 2 y marcar B (100 m²).",
  r"Trapecio: promedio de las bases por la altura.",
  "respuesta = Rational((12+8)*5, 2)",
  [(["Área del trapecio", r"$A = \dfrac{(B + b)\,h}{2}$"], "El área del trapecio es base mayor más base menor, por la altura, dividido en dos."),
   (["Reemplazamos", r"$\dfrac{(12 + 8) \cdot 5}{2} = 50$"], "Doce más ocho es veinte, por cinco, cien. Dividido en dos: cincuenta metros cuadrados.")],
  "cincuenta metros cuadrados", "El área del trapecio es el promedio de las bases por la altura."))

L.append(P("M1", G, "Ángulos en polígonos", "El ángulo del hexágono 🐝",
  r"¿Cuánto mide cada <b>ángulo interior</b> de un <b>hexágono regular</b>?",
  ["120°", "60°", "720°", "108°"], ["120", "60", "720", "108"], 0,
  [r"La suma de los ángulos interiores es $180^\circ(n - 2)$: $$180^\circ \cdot 4 = 720^\circ$$", r"Son 6 ángulos iguales: $$720^\circ \div 6 = 120^\circ$$"],
  r"Confundir con el ángulo exterior (60°) y marcar B, o quedarse con la suma total (720°).",
  r"Polígono regular de $n$ lados: cada ángulo interior mide $\dfrac{180^\circ(n-2)}{n}$.",
  "n = 6; respuesta = Rational(180*(n-2), n)",
  [(["Suma de interiores", r"$180^\circ \cdot (6 - 2) = 720^\circ$"], "Los ángulos interiores de un polígono suman ciento ochenta por ene menos dos. Para el hexágono: setecientos veinte grados."),
   (["Repartimos en 6", r"$720^\circ \div 6 = 120^\circ$"], "Como es regular, los seis ángulos son iguales: ciento veinte grados cada uno.")],
  "ciento veinte grados", "La suma de ángulos interiores es ciento ochenta por ene menos dos."))

L.append(P("M1", G, "Homotecia en el plano", "Agrandar un punto desde el origen 🔍",
  r"Se aplica una <b>homotecia</b> de centro en el origen y razón $k = 3$ al punto $P(2, -1)$. ¿Cuáles son las coordenadas de su imagen?",
  [r"$(6, -3)$", r"$(5, 2)$", r"$(6, -1)$", r"$(-6, 3)$"], ["(6,-3)", "(5,2)", "(6,-1)", "(-6,3)"], 0,
  [r"Con centro en el origen, la homotecia multiplica cada coordenada por $k$.", r"$$3 \cdot (2, -1) = (6, -3)$$"],
  r"Sumar 3 a cada coordenada, como si fuera una traslación, y marcar B.",
  r"Homotecia de centro $O$ y razón $k$: $(x, y) \to (kx, ky)$. Si $k < 0$, la imagen queda al otro lado del centro.",
  "P = Matrix([2, -1]); Q = 3*P; respuesta = Tuple(Q[0], Q[1])",
  [(["Multiplicamos por k", r"$(x, y) \to (3x, 3y)$"], "Una homotecia con centro en el origen multiplica las dos coordenadas por la razón."),
   (["Aplicamos", r"$(2, -1) \to (6, -3)$"], "Dos por tres es seis, y menos uno por tres es menos tres.")],
  "el punto seis, menos tres", "Homotecia con centro en el origen: se multiplican las coordenadas, no se suman."))

L.append(P("M1", G, "Rotación en el plano", "Gira el punto 90° 🔄",
  r"El punto $A(3, 2)$ se rota en <b>90° en sentido antihorario</b> en torno al origen. ¿Cuáles son las coordenadas de su imagen?",
  [r"$(-2, 3)$", r"$(2, -3)$", r"$(-3, -2)$", r"$(3, -2)$"], ["(-2,3)", "(2,-3)", "(-3,-2)", "(3,-2)"], 0,
  [r"Rotación de 90° antihoraria en torno al origen: $$(x, y) \to (-y, x)$$", r"$$(3, 2) \to (-2, 3)$$"],
  r"Usar la regla del sentido horario, $(x, y) \to (y, -x)$, y marcar B.",
  r"En torno al origen: 90° antihorario $(-y, x)$; 180° $(-x, -y)$; 270° antihorario $(y, -x)$.",
  "R = Matrix([[0, -1], [1, 0]]); Q = R*Matrix([3, 2]); respuesta = Tuple(Q[0], Q[1])",
  [(["90° antihorario", r"$(x, y) \to (-y, x)$"], "Al rotar noventa grados en sentido antihorario, las coordenadas se intercambian y la nueva primera cambia de signo."),
   (["Aplicamos", r"$(3, 2) \to (-2, 3)$"], "El punto tres, dos queda en menos dos, tres.")],
  "el punto menos dos, tres", "Noventa grados antihorario: equis, y pasa a menos y, equis."))

L.append(P("M1", G, "Módulo de un vector", "El largo de un vector ➡️",
  r"¿Cuál es el <b>módulo</b> (largo) del vector $\vec{v} = (6, -8)$?",
  ["10", "14", "$-2$", "100"], ["10", "14", "-2", "100"], 0,
  [r"$$|\vec{v}| = \sqrt{x^2 + y^2}$$", r"$$\sqrt{6^2 + (-8)^2} = \sqrt{36 + 64} = \sqrt{100} = 10$$"],
  r"Sumar los valores absolutos de las componentes y marcar B (14), o sumarlas con signo (−2).",
  r"El módulo de $(x, y)$ es $\sqrt{x^2 + y^2}$: es Pitágoras. Nunca es negativo.",
  "respuesta = sqrt(6**2 + (-8)**2)",
  [(["Módulo = Pitágoras", r"$|\vec{v}| = \sqrt{6^2 + (-8)^2}$"], "El módulo de un vector se calcula con Pitágoras: raíz de seis al cuadrado más menos ocho al cuadrado."),
   (["Calculamos", r"$\sqrt{36 + 64} = \sqrt{100} = 10$"], "Treinta y seis más sesenta y cuatro es cien, y su raíz es diez.")],
  "diez", "El módulo de un vector es Pitágoras y nunca es negativo."))

L.append(P("M1", G, "Semejanza: sombras", "Mide un edificio con su sombra 🏢",
  r"A cierta hora, un poste de <b>3 m</b> proyecta una sombra de <b>2 m</b>. A la misma hora, un edificio proyecta una sombra de <b>12 m</b>. ¿Cuál es la altura del edificio?",
  ["18 m", "8 m", "13 m", "72 m"], ["18", "8", "13", "72"], 0,
  [r"Los triángulos son semejantes: $$\frac{3}{2} = \frac{h}{12}$$", r"$$h = \frac{3 \cdot 12}{2} = 18 \text{ m}$$"],
  r"Invertir la razón ($\tfrac{2}{3} \cdot 12 = 8$) y marcar B.",
  r"En semejanza, compara lados <b>correspondientes</b>: altura con altura, sombra con sombra.",
  "respuesta = Rational(3, 2)*12",
  [(["Triángulos semejantes", r"$\dfrac{3}{2} = \dfrac{h}{12}$"], "El poste y el edificio forman triángulos semejantes con sus sombras: altura sobre sombra es igual en los dos."),
   (["Despejamos", r"$h = \dfrac{3 \cdot 12}{2} = 18$"], "Tres por doce, dividido en dos: dieciocho metros.")],
  "dieciocho metros", "Compara altura con altura y sombra con sombra."))

L.append(P("M1", G, "Perímetro de la circunferencia", "¿Cuántas vueltas da la rueda? 🚲",
  r"La rueda de una bicicleta tiene <b>radio 35 cm</b>. Usando $\pi \approx \dfrac{22}{7}$, ¿cuántas <b>vueltas completas</b> da para avanzar <b>22 m</b>?",
  ["10", "20", "5", "40"], ["10", "20", "5", "40"], 0,
  [r"En una vuelta avanza su perímetro: $$2\pi r = 2 \cdot \frac{22}{7} \cdot 35 = 220 \text{ cm}$$", r"$$2.200 \text{ cm} \div 220 \text{ cm} = 10$$ vueltas."],
  r"Usar $\pi r$ en vez de $2\pi r$ y marcar B (20 vueltas).",
  r"En cada vuelta, una rueda avanza su perímetro: $2\pi r$. Ojo con las unidades.",
  "respuesta = Rational(2200, 1) / (2*Rational(22,7)*35)",
  [(["Una vuelta = perímetro", r"$2 \cdot \dfrac{22}{7} \cdot 35 = 220\ \text{cm}$"], "En cada vuelta la rueda avanza su perímetro: dos pi erre, doscientos veinte centímetros."),
   (["Cuántas vueltas", r"$2.200 \div 220 = 10$"], "Veintidós metros son dos mil doscientos centímetros. Divididos en doscientos veinte: diez vueltas.")],
  "diez vueltas", "Cada vuelta de la rueda avanza su perímetro, dos pi erre."))

L.append(P("M1", G, "Volumen de la esfera", "El volumen de una pelota ⚽",
  r"Una pelota tiene <b>radio 3 cm</b>. ¿Cuál es su volumen? (Usa $V = \dfrac{4}{3}\pi r^3$.)",
  [r"$36\pi$ cm³", r"$12\pi$ cm³", r"$108\pi$ cm³", r"$27\pi$ cm³"], ["36*pi", "12*pi", "108*pi", "27*pi"], 0,
  [r"$$V = \frac{4}{3}\pi \cdot 3^3 = \frac{4}{3}\pi \cdot 27$$", r"$$V = 36\pi \text{ cm}^3$$"],
  r"Elevar el radio al cuadrado en vez de al cubo y marcar B ($12\pi$).",
  r"Volumen de la esfera: $\tfrac{4}{3}\pi r^3$ (al cubo, porque es volumen). Área: $4\pi r^2$.",
  "respuesta = Rational(4,3)*pi*3**3",
  [(["Volumen de la esfera", r"$V = \dfrac{4}{3}\pi \cdot 3^3$"], "El volumen de la esfera es cuatro tercios de pi por el radio al cubo."),
   (["Calculamos", r"$\dfrac{4}{3} \cdot 27 = 36 \Rightarrow 36\pi$"], "Tres al cubo es veintisiete. Cuatro tercios de veintisiete es treinta y seis: treinta y seis pi centímetros cúbicos.")],
  "treinta y seis pi centímetros cúbicos", "Si es volumen, el radio va al cubo."))

# ======================= M1 · PROBABILIDAD Y ESTADÍSTICA
L.append(P("M1", E, "Probabilidad con dos dados", "¿Por qué el 7 sale tanto? 🎲",
  r"Se lanzan <b>dos dados</b> comunes. ¿Cuál es la probabilidad de que la <b>suma sea 7</b>?",
  [r"$\dfrac{1}{6}$", r"$\dfrac{7}{36}$", r"$\dfrac{1}{11}$", r"$\dfrac{7}{12}$"], ["1/6", "7/36", "1/11", "7/12"], 0,
  [r"Hay $6 \cdot 6 = 36$ resultados igualmente probables.", r"Suman 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1). $$P = \frac{6}{36} = \frac{1}{6}$$"],
  r"Pensar que las 11 sumas posibles (2 a 12) son igualmente probables y marcar C.",
  r"Con dos dados, cuenta pares ordenados: (2,5) y (5,2) son resultados distintos.",
  "from itertools import product; casos = list(product(range(1,7), repeat=2)); respuesta = Rational(len([c for c in casos if sum(c) == 7]), len(casos))",
  [(["36 resultados", r"$6 \cdot 6 = 36$"], "Con dos dados hay seis por seis, treinta y seis resultados igual de probables."),
   (["Casos que suman 7", r"$P = \dfrac{6}{36} = \dfrac{1}{6}$"], "Suman siete: uno y seis, dos y cinco, tres y cuatro, y al revés. Son seis casos: un sexto.")],
  "un sexto", "Dos y cinco no es lo mismo que cinco y dos: cuenta pares ordenados."))

L.append(P("M1", E, "Extracción sin reposición", "Sacar fichas sin devolverlas 🔴",
  r"Una bolsa tiene <b>3 fichas rojas</b> y <b>2 azules</b>. Se sacan <b>2 fichas sin reposición</b>. ¿Cuál es la probabilidad de que <b>ambas sean rojas</b>?",
  [r"$\dfrac{3}{10}$", r"$\dfrac{9}{25}$", r"$\dfrac{3}{5}$", r"$\dfrac{2}{5}$"], ["3/10", "9/25", "3/5", "2/5"], 0,
  [r"Primera roja: $\tfrac{3}{5}$. Quedan 4 fichas, 2 rojas: $\tfrac{2}{4}$.", r"$$P = \frac{3}{5} \cdot \frac{2}{4} = \frac{6}{20} = \frac{3}{10}$$"],
  r"Calcular como si se devolviera la ficha, $\left(\tfrac{3}{5}\right)^2 = \tfrac{9}{25}$, y marcar B.",
  r"Sin reposición, la segunda extracción cambia: hay una ficha menos en total y una menos del color sacado.",
  "from itertools import permutations; b = 'RRRAA'; pares = list(permutations(range(5), 2)); respuesta = Rational(len([p for p in pares if b[p[0]] == 'R' and b[p[1]] == 'R']), len(pares))",
  [(["Primera roja", r"$\dfrac{3}{5}$"], "La primera ficha es roja con probabilidad tres quintos."),
   (["Segunda roja", r"$\dfrac{3}{5} \cdot \dfrac{2}{4} = \dfrac{3}{10}$"], "Sin reponer, quedan cuatro fichas y dos rojas: dos cuartos. Multiplicando: tres décimos.")],
  "tres décimos", "Sin reposición, cambia el total en la segunda extracción."))

L.append(P("M1", E, "Media: dato que falta", "¿Cuántos goles hizo? ⚽",
  r"Un equipo hizo en promedio <b>2 goles</b> en sus primeros <b>4 partidos</b>. Tras el quinto partido, el promedio subió a <b>2,4 goles</b>. ¿Cuántos goles hizo en el quinto partido?",
  ["4", "3", "12", "2,8"], ["4", "3", "12", "14/5"], 0,
  [r"Goles en 4 partidos: $4 \cdot 2 = 8$. En 5 partidos: $5 \cdot 2{,}4 = 12$.", r"$$12 - 8 = 4 \text{ goles}$$"],
  r"Responder el total de goles y marcar C (12), o pensar que basta con un poco más que el promedio.",
  r"Promedio $\cdot$ cantidad de datos = suma. Trabaja con sumas, no con promedios.",
  "x = symbols('x'); respuesta = solve(Eq((4*2 + x)/5, Rational(24,10)), x)[0]",
  [(["Total de goles", r"$4 \cdot 2 = 8 \quad 5 \cdot 2{,}4 = 12$"], "En cuatro partidos con promedio dos, hizo ocho goles. Con cinco partidos y promedio dos coma cuatro, el total es doce."),
   (["La diferencia", r"$12 - 8 = 4$"], "Así que en el quinto partido hizo cuatro goles.")],
  "cuatro goles", "Promedio por cantidad de datos da la suma: trabaja con sumas."))

L.append(P("M1", E, "Gráfico circular", "Grados a porcentaje 🥧",
  r"En un <b>gráfico circular</b> sobre cómo llegan al liceo los estudiantes de un curso, el sector <b>Metro</b> mide <b>72°</b>. ¿Qué porcentaje del curso llega en Metro?",
  ["20%", "72%", "36%", "7,2%"], ["20", "72", "36", "36/5"], 0,
  [r"El círculo completo, $360^\circ$, es el 100%.", r"$$\frac{72^\circ}{360^\circ} = 0{,}2 = 20\%$$"],
  r"Leer los grados como porcentaje y marcar B (72%).",
  r"En un gráfico circular: porcentaje $= \dfrac{\text{ángulo}}{360^\circ} \cdot 100$. Cada 10% son $36^\circ$.",
  "respuesta = Rational(72, 360)*100",
  [(["360° es el 100%", r"$\dfrac{72^\circ}{360^\circ}$"], "En un gráfico circular, la vuelta completa, trescientos sesenta grados, es el cien por ciento."),
   (["Calculamos", r"$\dfrac{72}{360} = 0{,}2 = 20\%$"], "Setenta y dos dividido en trescientos sesenta es cero coma dos: el veinte por ciento.")],
  "veinte por ciento", "Cada diez por ciento del gráfico circular son treinta y seis grados."))

L.append(P("M1", E, "Frecuencia acumulada", "«A lo más» no es «exactamente» 👀",
  r"En una encuesta a <b>20 familias</b>: <b>3</b> no tienen hijos, <b>5</b> tienen 1, <b>8</b> tienen 2 y <b>4</b> tienen 3. ¿Qué porcentaje de las familias tiene <b>a lo más 1 hijo</b>?",
  ["40%", "25%", "15%", "80%"], ["40", "25", "15", "80"], 0,
  [r"\"A lo más 1\" es 0 o 1 hijo: $3 + 5 = 8$ familias.", r"$$\frac{8}{20} = 0{,}4 = 40\%$$"],
  r"Contar solo las familias con exactamente 1 hijo y marcar B (25%).",
  r"\"A lo más $k$\" incluye $k$ y todos los valores menores: es la frecuencia acumulada.",
  "f = {0: 3, 1: 5, 2: 8, 3: 4}; respuesta = Rational(f[0] + f[1], sum(f.values()))*100",
  [(["A lo más 1: cero o uno", r"$3 + 5 = 8$"], "A lo más un hijo significa cero o uno: tres más cinco, ocho familias."),
   (["Porcentaje", r"$\dfrac{8}{20} = 40\%$"], "Ocho de veinte es el cuarenta por ciento.")],
  "cuarenta por ciento", "A lo más uno incluye el cero y el uno."))

L.append(P("M1", E, "Mediana con datos pares", "Mediana: primero ordena 📋",
  r"Los minutos que demoran 6 estudiantes en llegar al liceo son: $$15,\ 4,\ 20,\ 9,\ 12,\ 7$$ ¿Cuál es la <b>mediana</b>?",
  ["10,5", "14,5", r"≈ 11,2", "9"], ["21/2", "29/2", "67/6", "9"], 0,
  [r"Ordenamos: $4,\ 7,\ 9,\ 12,\ 15,\ 20$.", r"Con 6 datos, la mediana es el promedio de los dos centrales: $$\frac{9 + 12}{2} = 10{,}5$$"],
  r"No ordenar y promediar los datos centrales de la lista original (20 y 9), marcando B.",
  r"Mediana: <b>ordena primero</b>. Si la cantidad de datos es par, promedia los dos centrales.",
  "d = sorted([15, 4, 20, 9, 12, 7]); respuesta = Rational(d[2] + d[3], 2)",
  [(["Ordenamos", r"$4,\ 7,\ 9,\ 12,\ 15,\ 20$"], "Primero, siempre ordenar: cuatro, siete, nueve, doce, quince y veinte."),
   (["Los dos centrales", r"$\dfrac{9 + 12}{2} = 10{,}5$"], "Como son seis datos, se promedian los dos del centro: nueve y doce. Diez coma cinco minutos.")],
  "diez coma cinco minutos", "Para la mediana, ordena primero; si son pares, promedia los dos centrales."))

L.append(P("M1", E, "Unión de eventos", "Fútbol, básquetbol o ambos 🏀",
  r"En un curso de <b>30 estudiantes</b>, <b>18</b> practican fútbol, <b>12</b> básquetbol y <b>5</b> ambos deportes. Si se elige uno al azar, ¿cuál es la probabilidad de que practique <b>al menos uno</b> de los dos?",
  [r"$\dfrac{5}{6}$", "1", r"$\dfrac{1}{6}$", r"$\dfrac{2}{3}$"], ["5/6", "1", "1/6", "2/3"], 0,
  [r"Regla aditiva: $$P(F \cup B) = P(F) + P(B) - P(F \cap B)$$", r"$$\frac{18 + 12 - 5}{30} = \frac{25}{30} = \frac{5}{6}$$"],
  r"Sumar 18 + 12 = 30 sin restar a los que hacen ambos y marcar B (probabilidad 1).",
  r"Si los eventos pueden ocurrir juntos, se resta la intersección para no contarla dos veces.",
  "respuesta = Rational(18 + 12 - 5, 30)",
  [(["Regla aditiva", r"$18 + 12 - 5 = 25$"], "Sumamos los de fútbol y los de básquetbol, y restamos los cinco que hacen ambos, porque se contaron dos veces: veinticinco."),
   (["Probabilidad", r"$\dfrac{25}{30} = \dfrac{5}{6}$"], "Veinticinco de treinta: cinco sextos.")],
  "cinco sextos", "Al sumar eventos que se cruzan, resta la intersección."))

L.append(P("M1", E, "Promedio de grupos combinados", "No promedies promedios 🚫",
  r"El <b>3° A</b> (20 estudiantes) tiene promedio <b>5,5</b> y el <b>3° B</b> (30 estudiantes), promedio <b>5,0</b>. ¿Cuál es el promedio de los <b>50 estudiantes</b> juntos?",
  ["5,2", "5,25", "5,3", "5,1"], ["26/5", "21/4", "53/10", "51/10"], 0,
  [r"Sumas de notas: $20 \cdot 5{,}5 = 110$ y $30 \cdot 5{,}0 = 150$.", r"$$\frac{110 + 150}{50} = \frac{260}{50} = 5{,}2$$"],
  r"Promediar los dos promedios, $\tfrac{5{,}5 + 5{,}0}{2} = 5{,}25$, y marcar B, sin considerar que los cursos tienen distinto tamaño.",
  r"Para juntar grupos de distinto tamaño, usa promedio ponderado: suma total dividida por el total de datos.",
  "respuesta = (20*Rational(55,10) + 30*5) / 50",
  [(["Suma de cada curso", r"$20 \cdot 5{,}5 = 110 \quad 30 \cdot 5 = 150$"], "Veinte estudiantes con promedio cinco coma cinco suman ciento diez; treinta con promedio cinco suman ciento cincuenta."),
   (["Promedio total", r"$\dfrac{260}{50} = 5{,}2$"], "En total, doscientos sesenta dividido en cincuenta: cinco coma dos.")],
  "cinco coma dos", "No promedies promedios de grupos de distinto tamaño."))

L.append(P("M1", E, "Eventos independientes: moneda y dado", "Cara y par 🪙🎲",
  r"Se lanzan una <b>moneda</b> y un <b>dado</b> común. ¿Cuál es la probabilidad de obtener <b>cara y un número par</b>?",
  [r"$\dfrac{1}{4}$", r"$\dfrac{1}{2}$", r"$\dfrac{1}{8}$", r"$\dfrac{1}{12}$"], ["1/4", "1/2", "1/8", "1/12"], 0,
  [r"Espacio muestral: $2 \cdot 6 = 12$ resultados.", r"Favorables: (C,2), (C,4), (C,6). $$P = \frac{3}{12} = \frac{1}{4}$$"],
  r"Multiplicar por la probabilidad de un solo número, $\tfrac{1}{2} \cdot \tfrac{1}{6}$, y marcar D ($\tfrac{1}{12}$).",
  r"Eventos independientes: $P(A \cap B) = P(A) \cdot P(B) = \tfrac{1}{2} \cdot \tfrac{1}{2}$.",
  "from itertools import product; casos = list(product('CS', range(1,7))); respuesta = Rational(len([c for c in casos if c[0] == 'C' and c[1] % 2 == 0]), len(casos))",
  [(["12 resultados", r"$2 \cdot 6 = 12$"], "La moneda tiene dos resultados y el dado seis: doce en total."),
   (["Favorables", r"$\dfrac{3}{12} = \dfrac{1}{4}$"], "Cara con dos, cara con cuatro y cara con seis: tres de doce, un cuarto.")],
  "un cuarto", "Para eventos independientes, multiplica las probabilidades."))

# ======================= M2
L.append(P("M2", N, "Interés compuesto", "Los intereses también ganan intereses 🏦",
  r"Se depositan <b>\$1.000.000</b> a un interés compuesto de <b>2% mensual</b>. ¿Cuánto dinero habrá al cabo de <b>2 meses</b>?",
  [r"\$1.040.400", r"\$1.040.000", r"\$1.400.000", r"\$1.020.000"], ["1040400", "1040000", "1400000", "1020000"], 0,
  [r"Cada mes el monto se multiplica por $1{,}02$: $$C = 1.000.000 \cdot 1{,}02^2$$", r"$$1{,}02^2 = 1{,}0404 \Rightarrow C = 1.040.400$$"],
  r"Calcular interés simple (2% + 2% = 4%) y marcar B (\$1.040.000).",
  r"Interés compuesto: $C = C_0(1 + i)^n$. Los intereses también generan intereses.",
  "respuesta = 1000000*Rational(102,100)**2",
  [(["Por 1,02 cada mes", r"$1.000.000 \cdot 1{,}02^2$"], "Con interés compuesto, cada mes el dinero se multiplica por uno coma cero dos."),
   (["Calculamos", r"$1{,}0404 \cdot 1.000.000 = 1.040.400$"], "Uno coma cero dos al cuadrado es uno coma cero cuatro cero cuatro. Hay un millón cuarenta mil cuatrocientos pesos.")],
  "un millón cuarenta mil cuatrocientos pesos", "En el interés compuesto, los intereses también ganan intereses."))

L.append(P("M2", N, "Interés simple: tasa", "¿Qué tasa me pagaron? 💵",
  r"Un capital de <b>\$500.000</b> genera <b>\$45.000</b> de interés <b>simple</b> en <b>6 meses</b>. ¿Cuál es la tasa de interés <b>mensual</b>?",
  ["1,5%", "9%", "0,9%", "7,5%"], ["3/2", "9", "9/10", "15/2"], 0,
  [r"Interés simple: $I = C \cdot i \cdot t$: $$45.000 = 500.000 \cdot i \cdot 6$$", r"$$i = \frac{45.000}{3.000.000} = 0{,}015 = 1{,}5\%$$"],
  r"Calcular el interés de todo el período ($\tfrac{45.000}{500.000} = 9\%$) y marcar B, sin dividir por los 6 meses.",
  r"En interés simple, $I = C \cdot i \cdot t$: el interés es el mismo en cada período.",
  "i = symbols('i'); respuesta = solve(Eq(500000*i*6, 45000), i)[0]*100",
  [(["I = C · i · t", r"$45.000 = 500.000 \cdot i \cdot 6$"], "En interés simple, el interés es capital por tasa por tiempo."),
   (["Despejamos", r"$i = \dfrac{45.000}{3.000.000} = 1{,}5\%$"], "Quinientos mil por seis es tres millones. Cuarenta y cinco mil dividido en tres millones: uno coma cinco por ciento mensual.")],
  "uno coma cinco por ciento", "Si piden tasa mensual, divide también por la cantidad de meses."))

L.append(P("M2", N, "Ecuación logarítmica", "El logaritmo es un exponente 🔑",
  r"¿Cuál es el valor de $x$ en $$\log_3 x = 4\,?$$",
  ["81", "12", "64", r"$\dfrac{4}{3}$"], ["81", "12", "64", "4/3"], 0,
  [r"Por definición: $\log_b x = c \iff b^c = x$.", r"$$x = 3^4 = 81$$"],
  r"Multiplicar la base por el resultado ($3 \cdot 4 = 12$) y marcar B.",
  r"El logaritmo es un exponente: $\log_b x = c$ significa $b^c = x$.",
  "x = symbols('x', positive=True); respuesta = solve(Eq(log(x, 3), 4), x)[0]",
  [(["El log es un exponente", r"$\log_3 x = 4 \iff 3^4 = x$"], "Logaritmo en base tres de equis igual cuatro significa que tres elevado a cuatro es equis."),
   (["Calculamos", r"$3^4 = 81$"], "Tres a la cuatro es ochenta y uno.")],
  "ochenta y uno", "Un logaritmo es un exponente: la base elevada al resultado da el argumento."))

L.append(P("M2", N, "Logaritmo de una potencia", "El exponente baja 👇",
  r"¿Cuál es el valor de $$\log_2\left(8^3\right)\,?$$",
  ["9", "24", "6", "512"], ["9", "24", "6", "512"], 0,
  [r"Propiedad de la potencia: $$\log_2\left(8^3\right) = 3 \log_2 8$$", r"Como $2^3 = 8$, $\log_2 8 = 3$: $$3 \cdot 3 = 9$$"],
  r"Multiplicar el exponente por el argumento ($3 \cdot 8 = 24$) y marcar B.",
  r"$\log_b(a^n) = n \log_b a$: el exponente baja multiplicando.",
  "respuesta = simplify(log(Integer(8)**3) / log(2))",
  [(["El exponente baja", r"$\log_2\left(8^3\right) = 3\log_2 8$"], "El exponente del argumento baja multiplicando: tres por logaritmo en base dos de ocho."),
   (["Calculamos", r"$3 \cdot 3 = 9$"], "Dos al cubo es ocho, así que ese logaritmo vale tres. Tres por tres: nueve.")],
  "nueve", "El exponente del argumento baja multiplicando al logaritmo."))

L.append(P("M2", N, "Racionalización", "Sin raíces abajo 🧹",
  r"Al racionalizar $\dfrac{6}{\sqrt{3}}$ se obtiene:",
  [r"$2\sqrt{3}$", "2", r"$6\sqrt{3}$", r"$\dfrac{\sqrt{3}}{2}$"], ["2*sqrt(3)", "2", "6*sqrt(3)", "sqrt(3)/2"], 0,
  [r"Amplificamos por $\sqrt{3}$: $$\frac{6}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}} = \frac{6\sqrt{3}}{3}$$", r"$$\frac{6\sqrt{3}}{3} = 2\sqrt{3}$$"],
  r"Multiplicar solo el numerador por $\sqrt{3}$ y marcar C ($6\sqrt{3}$).",
  r"Racionalizar: amplificar por la raíz del denominador, porque $\sqrt{a} \cdot \sqrt{a} = a$.",
  "respuesta = radsimp(6/sqrt(3))",
  [(["Amplificamos por √3", r"$\dfrac{6}{\sqrt{3}} \cdot \dfrac{\sqrt{3}}{\sqrt{3}} = \dfrac{6\sqrt{3}}{3}$"], "Multiplicamos arriba y abajo por raíz de tres. Abajo queda tres."),
   (["Simplificamos", r"$\dfrac{6\sqrt{3}}{3} = 2\sqrt{3}$"], "Seis dividido en tres es dos: dos raíz de tres.")],
  "dos raíz de tres", "Para racionalizar, amplifica arriba y abajo por la raíz del denominador."))

L.append(P("M2", N, "Estimación de raíces", "Estima sin calculadora 🎯",
  r"¿Cuál es el <b>número entero más cercano</b> a $\sqrt{70}$?",
  ["8", "9", "35", "7"], ["8", "9", "35", "7"], 0,
  [r"Cuadrados cercanos: $8^2 = 64$ y $9^2 = 81$, así que $8 < \sqrt{70} < 9$.", r"70 está a 6 de 64 y a 11 de 81: $$\sqrt{70} \approx 8{,}4$$"],
  r"Dividir 70 por 2 y marcar C (35), o redondear hacia arriba sin comparar.",
  r"Para estimar $\sqrt{n}$, ubica $n$ entre dos cuadrados perfectos consecutivos.",
  "import math; c = list(range(1, 40)); respuesta = Integer(min(c, key=lambda k: abs(k - math.sqrt(70))))",
  [(["Entre dos cuadrados", r"$64 < 70 < 81$"], "Setenta está entre sesenta y cuatro, que es ocho al cuadrado, y ochenta y uno, que es nueve al cuadrado."),
   (["¿Cuál está más cerca?", r"$\sqrt{70} \approx 8{,}4$"], "Setenta está mucho más cerca de sesenta y cuatro, así que la raíz es cerca de ocho coma cuatro.")],
  "ocho", "Para estimar una raíz, busca los cuadrados perfectos más cercanos."))

L.append(P("M2", A, "Crecimiento exponencial: bacterias", "Se duplican cada 3 horas 🦠",
  r"Un cultivo tiene <b>500 bacterias</b> y su cantidad se <b>duplica cada 3 horas</b>. ¿Cuántas habrá después de <b>12 horas</b>?",
  ["8.000", "2.000", "4.000", "6.000"], ["8000", "2000", "4000", "6000"], 0,
  [r"En 12 horas hay $12 \div 3 = 4$ duplicaciones.", r"$$500 \cdot 2^4 = 500 \cdot 16 = 8.000$$"],
  r"Multiplicar por 4 en vez de duplicar 4 veces y marcar B (2.000).",
  r"Crecimiento exponencial: $N(t) = N_0 \cdot 2^{t/T}$, con $T$ el tiempo de duplicación.",
  "t = symbols('t'); N = 500*2**(t/3); respuesta = N.subs(t, 12)",
  [(["Cuántas duplicaciones", r"$12 \div 3 = 4$"], "Si se duplica cada tres horas, en doce horas se duplica cuatro veces."),
   (["Exponencial", r"$500 \cdot 2^4 = 8.000$"], "Quinientos por dos a la cuatro, que es dieciséis: ocho mil bacterias.")],
  "ocho mil bacterias", "Duplicar cuatro veces es multiplicar por dos a la cuatro, no por cuatro."))

L.append(P("M2", A, "Logaritmos: decibeles", "¿Música 100 veces más fuerte? 🔊",
  r"El nivel de sonido es $L = 10 \log\left(\dfrac{I}{I_0}\right)$ decibeles. Si la intensidad $I$ de una música se multiplica por <b>100</b>, ¿en cuánto aumenta $L$?",
  ["20 dB", "1.000 dB", "100 dB", "2 dB"], ["20", "1000", "100", "2"], 0,
  [r"Como $\log(ab) = \log a + \log b$, multiplicar $I$ por 100 suma $10 \log 100$ al nivel.", r"$$10 \log 100 = 10 \cdot 2 = 20 \text{ dB}$$"],
  r"Pensar que el nivel en decibeles también se multiplica por 100 y marcar C (100 dB).",
  r"En escalas logarítmicas (decibeles, Richter, pH), multiplicar la cantidad <b>suma</b> al nivel.",
  "I, I0 = symbols('I I0', positive=True); d = 10*log(100*I/I0, 10) - 10*log(I/I0, 10); respuesta = nsimplify(simplify(expand_log(d, force=True)))",
  [(["Log del producto", r"$\log(100\,I) = \log 100 + \log I$"], "Por la propiedad del producto, multiplicar la intensidad por cien suma diez por logaritmo de cien al nivel."),
   (["Calculamos", r"$10 \cdot \log 100 = 10 \cdot 2 = 20$"], "Logaritmo de cien es dos. Diez por dos: veinte decibeles más.")],
  "veinte decibeles", "En una escala logarítmica, multiplicar la intensidad suma decibeles."))

L.append(P("M2", A, "Rectas perpendiculares", "Perpendicular: invierte y cambia el signo ⊥",
  r"¿Cuál es la pendiente de una recta <b>perpendicular</b> a $y = 2x + 1$?",
  [r"$-\dfrac{1}{2}$", r"$\dfrac{1}{2}$", "$-2$", "2"], ["-1/2", "1/2", "-2", "2"], 0,
  [r"Rectas perpendiculares: $m_1 \cdot m_2 = -1$.", r"$$2 \cdot m_2 = -1 \Rightarrow m_2 = -\frac{1}{2}$$"],
  r"Solo invertir la pendiente sin cambiar el signo y marcar B, o solo cambiar el signo (−2).",
  r"Paralelas: misma pendiente. Perpendiculares: pendiente inversa y de signo contrario.",
  "m = symbols('m'); respuesta = solve(Eq(2*m, -1), m)[0]",
  [(["Perpendiculares", r"$m_1 \cdot m_2 = -1$"], "Dos rectas son perpendiculares si el producto de sus pendientes es menos uno."),
   (["Despejamos", r"$m_2 = -\dfrac{1}{2}$"], "La pendiente es dos, así que la perpendicular tiene pendiente menos un medio: se invierte y cambia de signo.")],
  "menos un medio", "Perpendicular: invierte la pendiente y cámbiale el signo."))

L.append(P("M2", G, "Ecuación de la recta por dos puntos", "La recta que pasa por dos puntos 📍",
  r"¿Cuál es la <b>ecuación de la recta</b> que pasa por los puntos $(1, 3)$ y $(3, 7)$?",
  [r"$y = 2x + 1$", r"$y = 2x + 3$", r"$y = \dfrac{1}{2}x + \dfrac{5}{2}$", r"$y = 4x - 1$"], ["2*x+1", "2*x+3", "x/2+5/2", "4*x-1"], 0,
  [r"Pendiente: $$m = \frac{7 - 3}{3 - 1} = 2$$", r"Con el punto $(1, 3)$: $y - 3 = 2(x - 1)$, o sea $$y = 2x + 1$$"],
  r"Calcular bien la pendiente, pero usar 3 como coeficiente de posición y marcar B.",
  r"Ecuación punto-pendiente: $y - y_1 = m(x - x_1)$. Comprueba con el otro punto.",
  "x = symbols('x'); m = Rational(7 - 3, 3 - 1); respuesta = expand(m*(x - 1) + 3)",
  [(["Pendiente", r"$m = \dfrac{7 - 3}{3 - 1} = 2$"], "La pendiente es siete menos tres, dividido en tres menos uno: dos."),
   ([r"$y - 3 = 2(x - 1)$", r"$y = 2x + 1$"], "Con el punto uno, tres: y menos tres igual dos por equis menos uno. Queda y igual dos equis más uno.")],
  "y igual dos equis más uno", "Siempre comprueba la recta con el otro punto."))

L.append(P("M2", G, "Seno en contexto: rampa", "¿A qué altura llega la rampa? ♿",
  r"Una rampa de <b>10 m</b> de largo forma un ángulo de <b>30°</b> con el suelo. ¿A qué <b>altura</b> llega?",
  ["5 m", r"$5\sqrt{3}$ m", r"$10\sqrt{3}$ m", "20 m"], ["5", "5*sqrt(3)", "10*sqrt(3)", "20"], 0,
  [r"La rampa es la hipotenusa y la altura, el cateto opuesto: $$\sin 30^\circ = \frac{h}{10}$$", r"$$h = 10 \cdot \frac{1}{2} = 5 \text{ m}$$"],
  r"Usar coseno en vez de seno y marcar B ($5\sqrt{3}$ m).",
  r"Opuesto e hipotenusa: seno. $\sin 30^\circ = \tfrac{1}{2}$, $\sin 45^\circ = \tfrac{\sqrt{2}}{2}$, $\sin 60^\circ = \tfrac{\sqrt{3}}{2}$.",
  "respuesta = 10*sin(pi/6)",
  [(["Opuesto/hipotenusa = seno", r"$\sin 30^\circ = \dfrac{h}{10}$"], "El largo de la rampa es la hipotenusa y la altura es el cateto opuesto al ángulo: eso es seno."),
   (["sen 30° = 1/2", r"$h = 10 \cdot \dfrac{1}{2} = 5$"], "Seno de treinta grados es un medio. Diez por un medio: cinco metros.")],
  "cinco metros", "Con opuesto e hipotenusa se usa el seno."))

L.append(P("M2", G, "Razones trigonométricas a partir de una", "Del seno a la tangente 📐",
  r"Si $\alpha$ es un ángulo agudo y $\sin \alpha = \dfrac{3}{5}$, ¿cuál es el valor de $\tan \alpha$?",
  [r"$\dfrac{3}{4}$", r"$\dfrac{4}{3}$", r"$\dfrac{4}{5}$", r"$\dfrac{5}{3}$"], ["3/4", "4/3", "4/5", "5/3"], 0,
  [r"Triángulo con opuesto 3 e hipotenusa 5. El adyacente: $$\sqrt{5^2 - 3^2} = 4$$", r"$$\tan \alpha = \frac{\text{opuesto}}{\text{adyacente}} = \frac{3}{4}$$"],
  r"Invertir la tangente (adyacente sobre opuesto) y marcar B.",
  r"Dibuja el triángulo: con dos lados, Pitágoras da el tercero y salen todas las razones.",
  "a = asin(Rational(3,5)); respuesta = simplify(tan(a))",
  [(["Falta el adyacente", r"$\sqrt{5^2 - 3^2} = 4$"], "Seno tres quintos: opuesto tres, hipotenusa cinco. Por Pitágoras, el adyacente es cuatro."),
   (["Tangente", r"$\tan\alpha = \dfrac{3}{4}$"], "Tangente es opuesto sobre adyacente: tres cuartos.")],
  "tres cuartos", "Dibuja el triángulo y completa el lado que falta con Pitágoras."))

L.append(P("M2", E, "Varianza", "Varianza en 3 pasos 📊",
  r"¿Cuál es la <b>varianza</b> de los datos $$2,\ 4,\ 6\,?$$",
  [r"$\dfrac{8}{3}$", "4", r"$\dfrac{2\sqrt{6}}{3}$", r"$\dfrac{4}{3}$"], ["8/3", "4", "2*sqrt(6)/3", "4/3"], 0,
  [r"Media: $\dfrac{2 + 4 + 6}{3} = 4$.", r"$$\sigma^2 = \frac{(2-4)^2 + (4-4)^2 + (6-4)^2}{3} = \frac{8}{3}$$"],
  r"Dividir por 2 en vez de 3 y marcar B (4), o confundir la varianza con la desviación estándar ($\sqrt{\tfrac{8}{3}}$).",
  r"Varianza: promedio de las distancias al cuadrado a la media. Desviación estándar: su raíz.",
  "d = [2, 4, 6]; m = Rational(sum(d), len(d)); respuesta = Rational(sum([(v - m)**2 for v in d]), len(d))",
  [(["Media", r"$\bar{x} = 4$"], "La media de dos, cuatro y seis es cuatro."),
   (["Distancias al cuadrado", r"$\dfrac{4 + 0 + 4}{3} = \dfrac{8}{3}$"], "Las distancias a la media son menos dos, cero y dos. Al cuadrado: cuatro, cero y cuatro. Su promedio es ocho tercios.")],
  "ocho tercios", "La varianza es el promedio de las distancias al cuadrado; la desviación es su raíz."))

L.append(P("M2", E, "Combinaciones", "¿Importa el orden? 🤝",
  r"De un grupo de <b>6 estudiantes</b> se elegirá una <b>comisión de 3</b>, sin cargos. ¿Cuántas comisiones distintas se pueden formar?",
  ["20", "120", "18", "216"], ["20", "120", "18", "216"], 0,
  [r"Sin cargos, el orden no importa: son combinaciones. $$\binom{6}{3} = \frac{6 \cdot 5 \cdot 4}{3 \cdot 2 \cdot 1}$$", r"$$\frac{120}{6} = 20$$"],
  r"Contar como si importara el orden ($6 \cdot 5 \cdot 4 = 120$) y marcar B.",
  r"¿Importa el orden? Sí: variaciones. No: combinaciones, $\binom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$.",
  "from itertools import combinations; respuesta = Integer(len(list(combinations(range(6), 3))))",
  [(["El orden no importa", r"$\dbinom{6}{3} = \dfrac{6 \cdot 5 \cdot 4}{3 \cdot 2 \cdot 1}$"], "En una comisión sin cargos el orden no importa: son combinaciones de seis en tres."),
   (["Calculamos", r"$\dfrac{120}{6} = 20$"], "Seis por cinco por cuatro es ciento veinte, dividido en seis: veinte comisiones.")],
  "veinte", "Si el orden no importa, divide por las formas de ordenar a los elegidos."))

L.append(P("M2", E, "Variaciones sin repetición", "¿Cuántas claves posibles? 🔐",
  r"La clave de un celular tiene <b>4 dígitos distintos</b> (del 0 al 9). ¿Cuántas claves posibles hay?",
  ["5.040", "10.000", "210", "40"], ["5040", "10000", "210", "40"], 0,
  [r"Primer dígito: 10 opciones; segundo: 9; tercero: 8; cuarto: 7.", r"$$10 \cdot 9 \cdot 8 \cdot 7 = 5.040$$"],
  r"Permitir dígitos repetidos ($10^4$) y marcar B (10.000), o usar combinaciones (210), donde el orden no importa.",
  r"Si importa el orden y no se repite: $n(n-1)(n-2)\cdots$. Si se puede repetir: $n^k$.",
  "from itertools import permutations; respuesta = Integer(len(list(permutations(range(10), 4))))",
  [(["Opciones por posición", r"$10 \cdot 9 \cdot 8 \cdot 7$"], "Para el primer dígito hay diez opciones, después nueve, ocho y siete, porque no se repiten."),
   (["Multiplicamos", r"$10 \cdot 9 \cdot 8 \cdot 7 = 5.040$"], "En total: cinco mil cuarenta claves.")],
  "cinco mil cuarenta", "Si no se pueden repetir, las opciones bajan en uno en cada posición."))

L.append(P("M2", E, "Binomial: exactamente k éxitos", "Exactamente 2 caras 🪙",
  r"Se lanza una moneda <b>4 veces</b>. ¿Cuál es la probabilidad de obtener <b>exactamente 2 caras</b>?",
  [r"$\dfrac{3}{8}$", r"$\dfrac{1}{2}$", r"$\dfrac{1}{16}$", r"$\dfrac{1}{4}$"], ["3/8", "1/2", "1/16", "1/4"], 0,
  [r"Modelo binomial: $$P = \binom{4}{2}\left(\frac{1}{2}\right)^2\left(\frac{1}{2}\right)^2$$", r"$$P = 6 \cdot \frac{1}{16} = \frac{3}{8}$$"],
  r"Pensar que \"la mitad caras\" tiene probabilidad $\tfrac{1}{2}$ y marcar B, u olvidar el $\binom{4}{2}$ ($\tfrac{1}{16}$).",
  r"Binomial: $P(X = k) = \binom{n}{k}\,p^k (1-p)^{n-k}$. El $\binom{n}{k}$ cuenta en qué lanzamientos salen los éxitos.",
  "from itertools import product; r = list(product('CS', repeat=4)); respuesta = Rational(len([t for t in r if t.count('C') == 2]), len(r))",
  [(["En qué lanzamientos", r"$\dbinom{4}{2} = 6$"], "Las dos caras pueden salir en seis posiciones distintas: cuatro sobre dos es seis."),
   (["Cada secuencia", r"$6 \cdot \dfrac{1}{16} = \dfrac{3}{8}$"], "Cada secuencia tiene probabilidad un dieciseisavo. Seis por un dieciseisavo: tres octavos.")],
  "tres octavos", "En la binomial, no olvides contar las posiciones con ene sobre ka."))

L.append(P("M2", E, "Probabilidad condicional con porcentajes", "Dado que rinde M2… 🤓",
  r"En un preuniversitario, el <b>60%</b> son mujeres. Rinden M2 el <b>50%</b> de las mujeres y el <b>25%</b> de los hombres. Si se elige al azar a alguien que <b>rinde M2</b>, ¿cuál es la probabilidad de que sea mujer?",
  [r"$\dfrac{3}{4}$", r"$\dfrac{1}{2}$", r"$\dfrac{3}{10}$", r"$\dfrac{3}{5}$"], ["3/4", "1/2", "3/10", "3/5"], 0,
  [r"Mujeres que rinden M2: $0{,}6 \cdot 0{,}5 = 0{,}3$. Hombres: $0{,}4 \cdot 0{,}25 = 0{,}1$.", r"$$P(\text{mujer} \mid M2) = \frac{0{,}3}{0{,}3 + 0{,}1} = \frac{3}{4}$$"],
  r"Responder $P(\text{M2} \mid \text{mujer})$ y marcar B, o la intersección (C).",
  r"$P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$: el universo se reduce a los que cumplen $B$.",
  "pm, ph = Rational(6,10), Rational(4,10); a = pm*Rational(1,2); b = ph*Rational(1,4); respuesta = a/(a + b)",
  [(["Quiénes rinden M2", r"$0{,}6 \cdot 0{,}5 = 0{,}3$", ], "Mujeres que rinden eme dos: cero coma seis por cero coma cinco, cero coma tres."),
   (["Hombres", r"$0{,}4 \cdot 0{,}25 = 0{,}1$"], "Hombres: cero coma cuatro por cero coma veinticinco, cero coma uno."),
   (["Dentro de los de M2", r"$\dfrac{0{,}3}{0{,}4} = \dfrac{3}{4}$"], "De los que rinden eme dos, que son cero coma cuatro, las mujeres son cero coma tres: tres cuartos.")],
  "tres cuartos", "En la condicional, el universo son solo los que cumplen la condición."))

# Frase extra del cierre (el error típico, dicho en voz alta) para que el audio dure 25-35 s.
EXTRA = {
 "Descuentos sucesivos": "Ojo, el segundo descuento se calcula sobre el precio ya rebajado, por eso no es un cincuenta por ciento.",
 "Porcentaje inverso: IVA": "Si restas el diecinueve por ciento del total, lo estás calculando sobre un precio que ya tenía el impuesto.",
 "Razones en mezclas": "El error típico es dividir en cuatro, pero el total tiene cinco partes: una de concentrado y cuatro de agua.",
 "Propiedades de potencias": "Ojo, los exponentes no se multiplican al multiplicar potencias: eso solo pasa con una potencia de una potencia.",
 "Suma de raíces": "Raíz de cincuenta más raíz de dieciocho no es raíz de sesenta y ocho: las raíces no se suman por dentro.",
 "Decimales periódicos": "El error típico es tratarlo como cero coma seis, que es un decimal finito y vale tres quintos.",
 "Números enteros: temperatura": "Si haces siete menos cuatro, olvidas que la mínima estaba bajo cero y te faltan cuatro grados.",
 "Proporcionalidad compuesta": "Si solo duplicas por las máquinas, te olvidas de que ahora trabajan una hora menos.",
 "Operatoria con fracciones": "Y nunca sumes los denominadores: dos quintos más un tercio no es tres octavos.",
 "Porcentaje de un porcentaje": "Sumar cuarenta y veinticinco no tiene sentido: el veinticinco por ciento se calcula solo sobre las mujeres.",
 "MCD en contexto": "Si calculas el mínimo común múltiplo, te da ciento cuarenta y cuatro, un trozo más largo que las cintas.",
 "Conversión de unidades": "Una hora tiene tres mil seiscientos segundos, no sesenta: ese es el error más común.",
 "Problema de edades": "Y lee bien qué te preguntan: la edad de la hija, no la de Pedro, que tiene treinta.",
 "Sistema 2x2: entradas al cine": "Y lee bien la pregunta: cinco mil es la entrada de adulto, no la de niño.",
 "Función afín: cuenta de la luz": "Si divides el total directo por ciento cincuenta, te da ciento ochenta y ocho, porque incluiste el cargo fijo.",
 "Pendiente de una recta": "Si inviertes la división, te da un medio. Siempre va la diferencia de las y arriba.",
 "Valor mínimo de una cuadrática": "El tres es dónde se alcanza el mínimo; el valor mínimo es lo que vale la función ahí.",
 "Diferencia de cuadrados": "Ojo, a al cuadrado menos be al cuadrado no es a menos be al cuadrado: ese error da cuatro.",
 "Inecuación: nota mínima": "Un cinco no alcanza, porque el cuatro coma seis tira el promedio hacia abajo.",
 "Despeje de fórmulas": "Si te quedas en cincuenta y cuatro, olvidaste deshacer la multiplicación por nueve quintos.",
 "Lenguaje algebraico": "Al despejar, el menos siete pasa sumando al otro lado, no restando.",
 "Ecuaciones con paréntesis": "Si escribes menos dos equis más dos, llegas a ocho: el menos multiplica a todo el paréntesis.",
 "Pitágoras: pantalla": "No se suman los lados: la diagonal siempre es más corta que el ancho más el alto.",
 "Volumen del cilindro": "Si olvidas la altura, solo calculas el área de la base y te queda la mitad del estanque.",
 "Área del trapecio": "El error más común es olvidar dividir por dos y responder cien metros cuadrados.",
 "Ángulos en polígonos": "Sesenta grados es el ángulo exterior, y setecientos veinte es la suma de todos.",
 "Homotecia en el plano": "Si sumas tres a cada coordenada, estás haciendo una traslación, no una homotecia.",
 "Rotación en el plano": "Si usas la regla del sentido horario, llegas a dos, menos tres, que está al otro lado.",
 "Módulo de un vector": "No se suman las componentes: el módulo es una distancia, así que nunca es negativo.",
 "Semejanza: sombras": "Si inviertes la razón, el edificio te queda más bajo que su sombra, y eso no calza con el poste.",
 "Perímetro de la circunferencia": "Si usas pi por radio, cuentas solo media vuelta y te da el doble de vueltas.",
 "Volumen de la esfera": "Si elevas el radio al cuadrado en vez de al cubo, te da doce pi, que no es un volumen.",
 "Probabilidad con dos dados": "Las once sumas posibles no son igual de probables: el siete es la que más sale.",
 "Extracción sin reposición": "Si usas tres quintos por tres quintos, estás devolviendo la ficha, y eso es con reposición.",
 "Media: dato que falta": "No respondas doce, que es el total de goles: te preguntan solo por el quinto partido.",
 "Gráfico circular": "Los setenta y dos grados no son setenta y dos por ciento: el círculo completo tiene trescientos sesenta.",
 "Frecuencia acumulada": "Si cuentas solo las familias con un hijo, te faltan las tres que no tienen hijos.",
 "Mediana con datos pares": "Si no ordenas, el centro de la lista no significa nada.",
 "Unión de eventos": "Si sumas dieciocho más doce, cuentas dos veces a los cinco que hacen ambos deportes.",
 "Promedio de grupos combinados": "Promediar cinco coma cinco y cinco da cinco coma veinticinco, pero el tercero be tiene más estudiantes.",
 "Eventos independientes: moneda y dado": "Par no es un solo número: hay tres pares en el dado, así que la probabilidad es un medio.",
 "Interés compuesto": "Con interés simple te daría un millón cuarenta mil, pero aquí el segundo mes gana sobre lo ya ganado.",
 "Interés simple: tasa": "Nueve por ciento es la tasa de los seis meses juntos, no la mensual.",
 "Ecuación logarítmica": "Tres por cuatro, doce, es el error típico: el logaritmo pide elevar, no multiplicar.",
 "Logaritmo de una potencia": "Si multiplicas tres por ocho, te da veinticuatro: el exponente multiplica al logaritmo, no al número.",
 "Racionalización": "Si amplificas solo arriba, cambias el valor de la fracción.",
 "Estimación de raíces": "Raíz de setenta no es la mitad de setenta: compárala con los cuadrados perfectos.",
 "Crecimiento exponencial: bacterias": "Multiplicar por cuatro sería crecer en forma lineal; aquí se duplica cuatro veces.",
 "Logaritmos: decibeles": "Los decibeles no se multiplican por cien: por eso una escala logarítmica crece tan lento.",
 "Rectas perpendiculares": "Si solo inviertes, te da un medio, que es otra recta que sube.",
 "Ecuación de la recta por dos puntos": "Compruébalo: con equis igual tres, dos por tres más uno da siete.",
 "Seno en contexto: rampa": "Coseno daría el largo horizontal de la rampa, no la altura.",
 "Razones trigonométricas a partir de una": "Si inviertes, te da cuatro tercios, que es la tangente del otro ángulo agudo.",
 "Varianza": "En la PAES la varianza se divide por la cantidad de datos, en este caso tres.",
 "Combinaciones": "Ciento veinte sería si hubiera presidente, secretario y tesorero, porque ahí sí importa el orden.",
 "Variaciones sin repetición": "Diez mil serían las claves con dígitos repetidos permitidos.",
 "Binomial: exactamente k éxitos": "Un medio parece lógico, pero salir justo la mitad de caras es menos probable de lo que crees.",
 "Probabilidad condicional con porcentajes": "No es lo mismo la probabilidad de rendir eme dos siendo mujer, que es un medio.",
}
for p in L:
    p["_clave_voz"] = p["_clave_voz"] + " " + EXTRA[p["tema"]]


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


rnd = random.Random(20261102)
metas = [i % 4 for i in range(len(L))]; rnd.shuffle(metas)
lote = [finalizar(p, rnd, metas[i]) for i, p in enumerate(L)]
json.dump(lote, open(os.path.join(AQUI, "lote_2026-11-02.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(lote), "problemas")
