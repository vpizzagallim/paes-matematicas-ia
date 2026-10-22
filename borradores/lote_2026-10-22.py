# Lote inicial (22-oct-2026). Genera lote_2026-10-22.json
import json, os

def P(nivel, eje, tema, gancho, enunciado, alternativas, valores, correcta, pasos, trampa, clave, verificacion):
    return dict(nivel=nivel, eje=eje, tema=tema, gancho=gancho, enunciado=enunciado, alternativas=alternativas,
                valores=valores, correcta=correcta, pasos=pasos, trampa=trampa, clave=clave, verificacion=verificacion)

L = []
N, A, G, E = "Números", "Álgebra y funciones", "Geometría", "Probabilidad y estadística"

L.append(P("M1", N, "Proporcionalidad inversa", "Más trabajadores, menos días… ¿pero cuántos? 👷",
  r"<b>6 obreros</b> terminan un muro en <b>12 días</b>. Trabajando al mismo ritmo, ¿cuántos días demorarían <b>8 obreros</b>?",
  ["16 días", "9 días", "10 días", "8 días", "14 días"], ["16", "9", "10", "8", "14"], 1,
  [r"Más obreros implica <b>menos</b> días: es proporcionalidad <b>inversa</b>, el producto se mantiene constante.",
   r"$$6 \cdot 12 = 72 \text{ días-obrero}$$",
   r"$$72 \div 8 = 9 \text{ días}$$"],
  r"Plantear una regla de tres <strong>directa</strong> ($\tfrac{12 \cdot 8}{6} = 16$) y marcar A.",
  r"Si al aumentar una cantidad la otra disminuye en la misma proporción, su <b>producto</b> es constante: $x \cdot y = k$.",
  "respuesta = Rational(6*12, 8)"))

L.append(P("M1", N, "Potencias", "Las potencias de igual base tienen sus reglas 🔢",
  r"¿Cuál es el valor de la expresión $$\frac{2^3 \cdot 2^5}{2^6}\,?$$",
  ["2", "4", "8", "16", "$2^{14}$"], ["2", "4", "8", "16", "2**14"], 1,
  [r"Al multiplicar potencias de igual base se <b>suman</b> los exponentes: $$2^3 \cdot 2^5 = 2^{8}$$",
   r"Al dividir se <b>restan</b>: $$\frac{2^8}{2^6} = 2^{2} = 4$$"],
  r"Sumar todos los exponentes ($3+5+6=14$) y marcar E, o multiplicarlos.",
  r"$a^m \cdot a^n = a^{m+n}$ y $\dfrac{a^m}{a^n} = a^{m-n}$. Solo funciona con la <b>misma base</b>.",
  "respuesta = Integer(2)**3 * Integer(2)**5 / Integer(2)**6"))

L.append(P("M1", N, "Porcentajes", "El error más común con el IVA 🧾",
  r"Un producto cuesta <b>\$11.900</b> con IVA incluido (19%). ¿Cuál es su precio <b>sin</b> IVA?",
  [r"\$9.639", r"\$10.000", r"\$9.990", r"\$10.190", r"\$9.500"], ["9639", "10000", "9990", "10190", "9500"], 1,
  [r"El precio con IVA es el <b>119%</b> del precio neto: $$P \cdot 1{,}19 = 11.900$$",
   r"Despejando: $$P = \frac{11.900}{1{,}19} = 10.000$$"],
  r"Restar el 19% al precio final ($11.900 \cdot 0{,}81 = 9.639$) y marcar A. El 19% se calcula sobre el precio <strong>neto</strong>, no sobre el final.",
  r"Para \"quitar\" un porcentaje que ya se aplicó, se <b>divide</b> por $(1 + \tfrac{p}{100})$; no se resta.",
  "respuesta = Rational(11900) / Rational(119, 100)"))

L.append(P("M1", N, "Raíces", "¿Se pueden sumar raíces? Depende 🤔",
  r"¿Cuál es el resultado de $$\sqrt{50} + \sqrt{18}\,?$$",
  [r"$\sqrt{68}$", r"$8\sqrt{2}$", r"$6\sqrt{2}$", r"$7\sqrt{2}$", r"$15\sqrt{2}$"],
  ["sqrt(68)", "8*sqrt(2)", "6*sqrt(2)", "7*sqrt(2)", "15*sqrt(2)"], 1,
  [r"Descomponemos cada raíz buscando cuadrados perfectos: $$\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt{2}$$ $$\sqrt{18} = \sqrt{9 \cdot 2} = 3\sqrt{2}$$",
   r"Ahora son raíces semejantes y se suman: $$5\sqrt{2} + 3\sqrt{2} = 8\sqrt{2}$$"],
  r"Sumar los números de adentro: $\sqrt{50} + \sqrt{18} = \sqrt{68}$. Eso es <strong>falso</strong>: la raíz no se distribuye en una suma.",
  r"$\sqrt{a} + \sqrt{b} \neq \sqrt{a+b}$. Solo se suman raíces con el <b>mismo radicando</b>, tras simplificarlas.",
  "respuesta = sqrt(50) + sqrt(18)"))

L.append(P("M1", N, "Razones", "Razones y proporciones en la sala de clases 🏫",
  r"En un curso de <b>40 estudiantes</b>, la razón entre hombres y mujeres es <b>3 : 5</b>. ¿Cuántas mujeres hay?",
  ["15", "25", "24", "30", "20"], ["15", "25", "24", "30", "20"], 1,
  [r"La razón 3 : 5 reparte el curso en $3 + 5 = 8$ partes iguales: $$40 \div 8 = 5 \text{ estudiantes por parte}$$",
   r"Las mujeres son 5 partes: $$5 \cdot 5 = 25$$"],
  r"Confundir hombres con mujeres (A = 15) o pensar que 5 partes de 40 es $\tfrac{5}{40}$ del curso.",
  r"En una razón $a : b$ el total se divide en $a + b$ partes; cada grupo recibe $a$ o $b$ de esas partes.",
  "respuesta = Rational(40, 3+5) * 5"))

L.append(P("M1", N, "Porcentajes", "Pregunta rápida de porcentajes ⚡",
  r"¿Qué porcentaje de <b>80</b> es <b>12</b>?",
  ["12%", "15%", r"$6{,}\overline{6}\%$", "18%", "20%"], ["12", "15", "20/3", "18", "20"], 1,
  [r"Se plantea la parte sobre el total: $$\frac{12}{80} = 0{,}15$$",
   r"Multiplicando por 100: $$0{,}15 \cdot 100 = 15\%$$"],
  r"Invertir la división ($\tfrac{80}{12} = 6{,}\overline{6}$) y marcar C.",
  r"\"¿Qué porcentaje de $T$ es $P$?\" se calcula siempre como $\dfrac{P}{T} \cdot 100$.",
  "respuesta = Rational(12, 80) * 100"))

L.append(P("M1", N, "Fracciones", "El orden de las operaciones decide todo 🧮",
  r"¿Cuál es el valor de $$0{,}25 + \frac{3}{4} \cdot \frac{2}{3}\,?$$",
  [r"$\dfrac{3}{4}$", r"$\dfrac{2}{3}$", "1", r"$\dfrac{5}{12}$", r"$\dfrac{1}{2}$"], ["3/4", "2/3", "1", "5/12", "1/2"], 0,
  [r"Primero la multiplicación: $$\frac{3}{4} \cdot \frac{2}{3} = \frac{6}{12} = \frac{1}{2}$$",
   r"Luego la suma, con $0{,}25 = \tfrac{1}{4}$: $$\frac{1}{4} + \frac{1}{2} = \frac{3}{4}$$"],
  r"Sumar primero $0{,}25 + \tfrac{3}{4} = 1$ y luego multiplicar por $\tfrac{2}{3}$, marcando B.",
  r"Prioridad: paréntesis, potencias, <b>multiplicación y división</b>, y al final suma y resta.",
  "respuesta = Rational(1,4) + Rational(3,4)*Rational(2,3)"))

L.append(P("M1", N, "Notación científica", "Notación científica sin miedo 🔬",
  r"¿Cuál es el resultado de $$0{,}00042 \cdot \left(3 \cdot 10^{5}\right)\,?$$",
  [r"$1{,}26 \cdot 10^{2}$", r"$1{,}26 \cdot 10^{1}$", r"$1{,}26 \cdot 10^{4}$", r"$1{,}26 \cdot 10^{-2}$", r"$1{,}26 \cdot 10^{3}$"],
  ["126", "126/10", "12600", "126/10000", "1260"], 0,
  [r"Escribimos $0{,}00042 = 4{,}2 \cdot 10^{-4}$.",
   r"Multiplicamos coeficientes y sumamos exponentes: $$4{,}2 \cdot 3 \cdot 10^{-4+5} = 12{,}6 \cdot 10^{1}$$",
   r"Ajustamos el coeficiente: $$12{,}6 \cdot 10^{1} = 1{,}26 \cdot 10^{2} = 126$$"],
  r"Quedarse con $12{,}6 \cdot 10^1$ y \"corregir\" el exponente en el sentido equivocado (B).",
  r"En notación científica el coeficiente va entre 1 y 10: si lo divides por 10, el exponente <b>sube</b> en 1.",
  "respuesta = Rational(42, 100000) * 3 * 10**5"))

L.append(P("M1", A, "Ecuaciones lineales", "Ecuación clásica de la PAES ✍️",
  r"¿Cuál es el valor de $x$ en la ecuación $$3(x - 2) = x + 8\,?$$",
  ["7", "5", "3", "4", "10"], ["7", "5", "3", "4", "10"], 0,
  [r"Distribuimos el 3: $$3x - 6 = x + 8$$",
   r"Agrupamos: $$3x - x = 8 + 6 \;\Rightarrow\; 2x = 14$$",
   r"$$x = 7$$"],
  r"Multiplicar solo la $x$ por 3 ($3x - 2 = x + 8$) y obtener $x = 5$ (B).",
  r"El factor fuera del paréntesis multiplica a <b>todos</b> los términos de adentro.",
  "x = symbols('x'); respuesta = solve(Eq(3*(x-2), x+8), x)[0]"))

L.append(P("M1", A, "Sistemas de ecuaciones", "Problema de entradas al cine 🎬",
  r"2 entradas de adulto y 3 de niño cuestan <b>\$17.000</b>. Una de adulto y una de niño cuestan <b>\$7.000</b>. ¿Cuánto cuesta la entrada de <b>adulto</b>?",
  [r"\$3.000", r"\$4.000", r"\$3.500", r"\$5.000", r"\$4.500"], ["3000", "4000", "3500", "5000", "4500"], 1,
  [r"Planteamos: $$2a + 3n = 17.000 \qquad a + n = 7.000$$",
   r"Multiplicamos la segunda por 2 y restamos: $$n = 17.000 - 14.000 = 3.000$$",
   r"Reemplazamos: $$a = 7.000 - 3.000 = 4.000$$"],
  r"Responder el valor de la entrada de <strong>niño</strong> (A), que es lo primero que se despeja.",
  r"Antes de marcar, relee qué variable te piden. En los sistemas suele haber una alternativa con la otra incógnita.",
  "a, n = symbols('a n'); respuesta = solve([2*a+3*n-17000, a+n-7000], [a, n])[a]"))

L.append(P("M1", A, "Función afín", "¿Cuánto cuesta el taxi? 🚕",
  r"Un taxi cobra <b>\$500</b> de bajada de bandera más <b>\$150</b> por cada <b>200 m</b> recorridos. ¿Cuánto cuesta un viaje de <b>3 km</b>?",
  [r"\$2.750", r"\$2.250", r"\$950", r"\$4.500", r"\$2.600"], ["2750", "2250", "950", "4500", "2600"], 0,
  [r"Pasamos a metros: 3 km = 3.000 m, que son $$3.000 \div 200 = 15 \text{ tramos}$$",
   r"El costo es una función afín, $C = 500 + 150t$: $$C = 500 + 150 \cdot 15 = 2.750$$"],
  r"Olvidar la bajada de bandera (B) o contar 3 tramos en vez de 15 (C).",
  r"Una función afín $f(x) = mx + n$ tiene un costo fijo $n$ y un costo variable $m$ por unidad.",
  "respuesta = 500 + 150 * (3000 // 200)"))

L.append(P("M1", A, "Inecuaciones", "Cuidado con el signo de la desigualdad ⚠️",
  r"¿Cuál es el conjunto solución de la inecuación $$2x - 5 < 3x + 1\,?$$",
  [r"$x > -6$", r"$x < -6$", r"$x > 6$", r"$x < 6$", r"$x > -4$"],
  ["Interval.open(-6, oo)", "Interval.open(-oo, -6)", "Interval.open(6, oo)", "Interval.open(-oo, 6)", "Interval.open(-4, oo)"], 0,
  [r"Agrupamos las $x$ a un lado: $$2x - 3x < 1 + 5 \;\Rightarrow\; -x < 6$$",
   r"Multiplicamos por $-1$ e <b>invertimos</b> el signo: $$x > -6$$"],
  r"Olvidar invertir la desigualdad al multiplicar por un número negativo y marcar B.",
  r"Al multiplicar o dividir una inecuación por un número <b>negativo</b>, el signo de la desigualdad se invierte.",
  "x = symbols('x', real=True); respuesta = solve_univariate_inequality(2*x-5 < 3*x+1, x, relational=False)"))

L.append(P("M1", A, "Función cuadrática", "El vértice de la parábola 📈",
  r"¿Cuál es el <b>valor mínimo</b> que alcanza la función $$f(x) = x^2 - 6x + 5\,?$$",
  ["$-4$", "3", "5", "$-5$", "4"], ["-4", "3", "5", "-5", "4"], 0,
  [r"Como $a = 1 > 0$, la parábola abre hacia arriba y su mínimo está en el vértice: $$x_v = \frac{-b}{2a} = \frac{6}{2} = 3$$",
   r"Evaluamos: $$f(3) = 9 - 18 + 5 = -4$$"],
  r"Responder la coordenada $x$ del vértice (B), cuando se pide el <strong>valor</strong> de la función.",
  r"El valor mínimo (o máximo) de una cuadrática es $f(x_v)$, con $x_v = -\tfrac{b}{2a}$.",
  "x = symbols('x'); f = x**2-6*x+5; respuesta = f.subs(x, solve(diff(f, x), x)[0])"))

L.append(P("M1", A, "Productos notables", "Un atajo que ahorra tiempo en la PAES ⏱️",
  r"Si $a + b = 10$ y $a - b = 4$, ¿cuál es el valor de $a^2 - b^2$?",
  ["40", "14", "6", "100", "16"], ["40", "14", "6", "100", "16"], 0,
  [r"Usamos la suma por diferencia: $$a^2 - b^2 = (a + b)(a - b)$$",
   r"Reemplazamos directo: $$10 \cdot 4 = 40$$"],
  r"Restar los cuadrados de los datos ($100 - 16 = 84$) o despejar $a$ y $b$ perdiendo tiempo.",
  r"$a^2 - b^2 = (a+b)(a-b)$. Si te dan la suma y la diferencia, multiplícalas.",
  "a, b = symbols('a b'); s = solve([a+b-10, a-b-4], [a, b]); respuesta = s[a]**2 - s[b]**2"))

L.append(P("M1", A, "Productos notables", "Desarrolla antes de restar 🧠",
  r"Al reducir la expresión $$(x + 3)^2 - (x - 3)^2$$ se obtiene:",
  [r"$12x$", "18", r"$6x$", "0", r"$2x^2 + 18$"], ["12*x", "18", "6*x", "0", "2*x**2+18"], 0,
  [r"Desarrollamos cada cuadrado de binomio: $$(x+3)^2 = x^2 + 6x + 9$$ $$(x-3)^2 = x^2 - 6x + 9$$",
   r"Restamos cuidando los signos: $$(x^2 + 6x + 9) - (x^2 - 6x + 9) = 12x$$"],
  r"Creer que $(x+3)^2 = x^2 + 9$ (olvidar el término central) y llegar a 18 o a 0.",
  r"$(a \pm b)^2 = a^2 \pm 2ab + b^2$. El término $2ab$ es el que más se olvida.",
  "x = symbols('x'); respuesta = expand((x+3)**2 - (x-3)**2)"))

L.append(P("M1", A, "Función lineal", "Dos puntos bastan para una recta 📍",
  r"La función afín $f(x) = mx + n$ cumple $f(1) = 5$ y $f(3) = 11$. ¿Cuál es el valor de $f(0)$?",
  ["2", "3", "5", "$-1$", "8"], ["2", "3", "5", "-1", "8"], 0,
  [r"La pendiente es $$m = \frac{11 - 5}{3 - 1} = 3$$",
   r"Con $f(1) = 5$: $$3 + n = 5 \;\Rightarrow\; n = 2$$",
   r"$f(0) = n = 2$."],
  r"Responder la pendiente (B) en lugar del coeficiente de posición.",
  r"$f(0)$ es siempre el coeficiente de posición $n$: el punto donde la recta corta al eje $Y$.",
  "m, n = symbols('m n'); s = solve([m+n-5, 3*m+n-11], [m, n]); respuesta = s[n]"))

L.append(P("M1", G, "Teorema de Pitágoras", "La escalera y la pared 🪜",
  r"Una escalera de <b>13 m</b> está apoyada en una pared vertical. Su pie está a <b>5 m</b> de la pared. ¿A qué altura toca la pared?",
  ["12 m", "8 m", "18 m", r"$\sqrt{194}$ m", "10 m"], ["12", "8", "18", "sqrt(194)", "10"], 0,
  [r"Pared, suelo y escalera forman un triángulo rectángulo; la escalera es la <b>hipotenusa</b>.",
   r"$$h^2 + 5^2 = 13^2 \;\Rightarrow\; h^2 = 169 - 25 = 144$$",
   r"$$h = 12 \text{ m}$$"],
  r"Sumar los cuadrados como si 13 fuera un cateto, obteniendo $\sqrt{194}$ (D).",
  r"En $a^2 + b^2 = c^2$, $c$ es <b>siempre</b> el lado opuesto al ángulo recto (el más largo).",
  "respuesta = sqrt(13**2 - 5**2)"))

L.append(P("M1", G, "Áreas", "¿Cuánto patio queda? 🏡",
  r"Un terreno rectangular mide <b>20 m × 15 m</b>. En él se construye una casa rectangular de <b>10 m × 8 m</b>. ¿Cuál es el área del terreno que queda libre?",
  [r"220 m²", r"300 m²", r"80 m²", r"52 m²", r"140 m²"], ["220", "300", "80", "52", "140"], 0,
  [r"Área del terreno: $$20 \cdot 15 = 300 \text{ m}^2$$",
   r"Área de la casa: $$10 \cdot 8 = 80 \text{ m}^2$$",
   r"Área libre: $$300 - 80 = 220 \text{ m}^2$$"],
  r"Restar perímetros ($70 - 36$) o responder el área total o la de la casa.",
  r"Área de una zona \"con un hueco\": área total menos área de la parte ocupada.",
  "respuesta = 20*15 - 10*8"))

L.append(P("M1", G, "Semejanza", "Medir un edificio con su sombra ☀️",
  r"A la misma hora, un poste de <b>3 m</b> proyecta una sombra de <b>2 m</b> y un edificio proyecta una sombra de <b>18 m</b>. ¿Cuál es la altura del edificio?",
  ["27 m", "12 m", "19 m", "23 m", "36 m"], ["27", "12", "19", "23", "36"], 0,
  [r"Los rayos de sol forman triángulos <b>semejantes</b>, así que altura y sombra son proporcionales: $$\frac{h}{18} = \frac{3}{2}$$",
   r"$$h = 18 \cdot \frac{3}{2} = 27 \text{ m}$$"],
  r"Invertir la razón ($\tfrac{h}{18} = \tfrac{2}{3}$) y obtener 12 m (B).",
  r"En triángulos semejantes, los lados correspondientes están en la misma razón: altura con altura, sombra con sombra.",
  "respuesta = Rational(18*3, 2)"))

L.append(P("M1", G, "Volumen", "¿Cuánto le cabe al vaso? 🥤",
  r"¿Cuál es el volumen de un cilindro de <b>radio 3 cm</b> y <b>altura 10 cm</b>?",
  [r"$90\pi$ cm³", r"$30\pi$ cm³", r"$60\pi$ cm³", r"$180\pi$ cm³", r"$900\pi$ cm³"],
  ["90*pi", "30*pi", "60*pi", "180*pi", "900*pi"], 0,
  [r"El volumen de un cilindro es el área de la base por la altura: $$V = \pi r^2 h$$",
   r"$$V = \pi \cdot 3^2 \cdot 10 = 90\pi \text{ cm}^3$$"],
  r"No elevar el radio al cuadrado ($\pi \cdot 3 \cdot 10 = 30\pi$) o usar el diámetro como radio.",
  r"Cilindro: $V = \pi r^2 h$. Prisma: $V = A_{base} \cdot h$. La idea es la misma.",
  "respuesta = pi * 3**2 * 10"))

L.append(P("M1", G, "Transformaciones isométricas", "Rotaciones en el plano cartesiano 🔄",
  r"El punto $P(2, -3)$ se rota en <b>90°</b> en sentido <b>antihorario</b> con centro en el origen. ¿Cuáles son las coordenadas de su imagen?",
  ["$(3, 2)$", "$(-3, -2)$", "$(-2, 3)$", "$(2, 3)$", "$(-3, 2)$"],
  ["(3, 2)", "(-3, -2)", "(-2, 3)", "(2, 3)", "(-3, 2)"], 0,
  [r"Una rotación de 90° antihoraria en torno al origen transforma $$(x, y) \;\to\; (-y, x)$$",
   r"Con $x = 2$, $y = -3$: $$(-(-3),\, 2) = (3, 2)$$"],
  r"Aplicar la regla de la rotación <strong>horaria</strong>, $(y, -x)$, y obtener $(-3, -2)$.",
  r"Rotación de 90° antihoraria: $(x, y) \to (-y, x)$. Rotación de 180°: $(x, y) \to (-x, -y)$.",
  "x, y = 2, -3; respuesta = Tuple(-y, x)"))

L.append(P("M1", G, "Vectores", "Operaciones con vectores ➡️",
  r"Si $\vec{u} = (2, -1)$ y $\vec{v} = (-3, 4)$, ¿cuál es el vector $2\vec{u} + \vec{v}$?",
  ["$(1, 2)$", "$(-1, 3)$", "$(4, -2)$", "$(1, -2)$", "$(-1, 2)$"],
  ["(1, 2)", "(-1, 3)", "(4, -2)", "(1, -2)", "(-1, 2)"], 0,
  [r"Multiplicamos $\vec{u}$ por 2: $$2\vec{u} = (4, -2)$$",
   r"Sumamos componente a componente: $$(4 + (-3),\; -2 + 4) = (1, 2)$$"],
  r"Olvidar multiplicar $\vec{u}$ por 2 y sumar directo: $(-1, 3)$ (B).",
  r"Los vectores se suman y se ponderan <b>componente a componente</b>.",
  "u = Matrix([2,-1]); v = Matrix([-3,4]); w = 2*u+v; respuesta = Tuple(w[0], w[1])"))

L.append(P("M1", E, "Promedio", "¿Qué nota necesito para aprobar con 5,5? 📚",
  r"Mis cuatro primeras notas son 5,0; 6,2; 4,8 y 6,0. ¿Qué nota necesito en la <b>quinta</b> evaluación para terminar con promedio <b>5,5</b>?",
  ["5,5", "5,0", "6,0", "4,5", "6,5"], ["11/2", "5", "6", "9/2", "13/2"], 0,
  [r"Para promediar 5,5 en 5 notas, la suma debe ser $$5 \cdot 5{,}5 = 27{,}5$$",
   r"Llevo $5{,}0 + 6{,}2 + 4{,}8 + 6{,}0 = 22{,}0$.",
   r"Me falta: $$27{,}5 - 22{,}0 = 5{,}5$$"],
  r"Calcular el promedio actual (5,5) y creer que da lo mismo la nota que saque.",
  r"Promedio deseado $\times$ cantidad de notas = suma necesaria. Lo que falta para esa suma es la nota pedida.",
  "respuesta = Rational(55,10)*5 - (Rational(50,10)+Rational(62,10)+Rational(48,10)+Rational(60,10))"))

L.append(P("M1", E, "Mediana", "Mediana ≠ promedio 📊",
  r"¿Cuál es la <b>mediana</b> del siguiente conjunto de datos? $$3,\; 8,\; 5,\; 10,\; 2,\; 7$$",
  ["6", "5", "7", "5,8", "8"], ["6", "5", "7", "29/5", "8"], 0,
  [r"Ordenamos los datos: $$2,\; 3,\; 5,\; 7,\; 8,\; 10$$",
   r"Hay 6 datos (cantidad par): la mediana es el promedio de los dos centrales: $$\frac{5 + 7}{2} = 6$$"],
  r"No ordenar y tomar los centrales tal como vienen ($5$ y $10$), o calcular el promedio ($\approx 5{,}8$).",
  r"Para la mediana, <b>primero se ordena</b>. Con cantidad par de datos, se promedian los dos del centro.",
  "respuesta = median([3,8,5,10,2,7]) if False else (lambda d: (d[2]+d[3])/Integer(2))(sorted([3,8,5,10,2,7]))"))

L.append(P("M1", E, "Probabilidad", "Dos dados y la suma más probable 🎲",
  r"Se lanzan <b>dos dados</b> comunes. ¿Cuál es la probabilidad de que la suma de los puntos sea <b>7</b>?",
  [r"$\dfrac{1}{6}$", r"$\dfrac{7}{36}$", r"$\dfrac{1}{12}$", r"$\dfrac{1}{11}$", r"$\dfrac{7}{12}$"],
  ["1/6", "7/36", "1/12", "1/11", "7/12"], 0,
  [r"Hay $6 \cdot 6 = 36$ resultados igualmente probables.",
   r"Casos favorables: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) → 6 casos.",
   r"$$P = \frac{6}{36} = \frac{1}{6}$$"],
  r"Contar las sumas posibles (2 a 12, son 11) como si fueran igual de probables y marcar $\tfrac{1}{11}$.",
  r"Regla de Laplace: casos favorables sobre casos <b>totales igualmente probables</b>.",
  "respuesta = Rational(sum(1 for a in range(1,7) for b in range(1,7) if a+b==7), 36)"))

L.append(P("M1", E, "Probabilidad", "Extracción sin reposición 🔴🔵",
  r"Una urna tiene <b>4 bolitas rojas</b> y <b>6 azules</b>. Se sacan <b>2</b> al azar, <b>sin reposición</b>. ¿Cuál es la probabilidad de que ambas sean rojas?",
  [r"$\dfrac{2}{15}$", r"$\dfrac{4}{25}$", r"$\dfrac{1}{5}$", r"$\dfrac{2}{5}$", r"$\dfrac{3}{25}$"],
  ["2/15", "4/25", "1/5", "2/5", "3/25"], 0,
  [r"Primera roja: $\tfrac{4}{10}$. Queda una roja menos y una bolita menos.",
   r"Segunda roja: $\tfrac{3}{9}$.",
   r"$$P = \frac{4}{10} \cdot \frac{3}{9} = \frac{12}{90} = \frac{2}{15}$$"],
  r"Calcular como si hubiera reposición: $\tfrac{4}{10} \cdot \tfrac{4}{10} = \tfrac{4}{25}$ (B).",
  r"Sin reposición, la segunda extracción cambia el numerador <b>y</b> el denominador.",
  "respuesta = Rational(4,10)*Rational(3,9)"))

L.append(P("M1", E, "Probabilidad", "Fútbol, básquetbol… ¿o ninguno? ⚽🏀",
  r"En un curso de <b>40</b> estudiantes, <b>25</b> juegan fútbol, <b>18</b> juegan básquetbol y <b>8</b> juegan ambos. Al elegir uno al azar, ¿cuál es la probabilidad de que no juegue ninguno?",
  [r"$\dfrac{1}{8}$", "0", r"$\dfrac{7}{8}$", r"$\dfrac{3}{40}$", r"$\dfrac{13}{40}$"],
  ["1/8", "0", "7/8", "3/40", "13/40"], 0,
  [r"Los que juegan al menos uno (sin contar dos veces a los 8): $$25 + 18 - 8 = 35$$",
   r"No juegan ninguno: $40 - 35 = 5$.",
   r"$$P = \frac{5}{40} = \frac{1}{8}$$"],
  r"Sumar $25 + 18 = 43$ sin restar la intersección: da más alumnos que el curso y lleva a responder 0.",
  r"$|A \cup B| = |A| + |B| - |A \cap B|$. La intersección se resta para no contarla dos veces.",
  "respuesta = Rational(40 - (25+18-8), 40)"))

# ---------------- M2 ----------------
L.append(P("M2", N, "Logaritmos", "Logaritmos en 30 segundos ⏱️",
  r"¿Cuál es el valor de $$\log_2 8 + \log_3 \tfrac{1}{9}\,?$$",
  ["1", "5", "$-1$", "0", "$-6$"], ["1", "5", "-1", "0", "-6"], 0,
  [r"$\log_2 8 = 3$, porque $2^3 = 8$.",
   r"$\log_3 \tfrac{1}{9} = -2$, porque $3^{-2} = \tfrac{1}{9}$.",
   r"$$3 + (-2) = 1$$"],
  r"Creer que $\log_3 \tfrac{1}{9} = 2$ (olvidar el signo negativo) y marcar B.",
  r"$\log_b a = c \iff b^c = a$. El logaritmo de un número entre 0 y 1 es <b>negativo</b>.",
  "respuesta = log(8, 2) + log(Rational(1,9), 3)"))

L.append(P("M2", A, "Función exponencial", "Crecimiento de bacterias 🦠",
  r"Una población de <b>500 bacterias</b> se <b>duplica cada 3 horas</b>. ¿Cuántas bacterias habrá después de <b>12 horas</b>?",
  ["8.000", "4.000", "2.000", "16.000", "6.000"], ["8000", "4000", "2000", "16000", "6000"], 0,
  [r"En 12 horas hay $12 \div 3 = 4$ duplicaciones.",
   r"El modelo es exponencial: $$N = 500 \cdot 2^{4} = 500 \cdot 16 = 8.000$$"],
  r"Modelar como crecimiento lineal ($500 \cdot 12 = 6.000$) o contar 12 duplicaciones.",
  r"Si algo se multiplica por $a$ cada $T$ unidades de tiempo: $N(t) = N_0 \cdot a^{t/T}$.",
  "respuesta = 500 * 2**(12//3)"))

L.append(P("M2", G, "Trigonometría", "Rampas y ángulos 📐",
  r"Una rampa de <b>8 m</b> de largo forma un ángulo de <b>30°</b> con el suelo horizontal. ¿Qué altura alcanza la rampa?",
  ["4 m", r"$4\sqrt{3}$ m", r"$8\sqrt{3}$ m", "2 m", r"$\dfrac{16}{\sqrt{3}}$ m"],
  ["4", "4*sqrt(3)", "8*sqrt(3)", "2", "16/sqrt(3)"], 0,
  [r"La rampa es la hipotenusa y la altura es el cateto <b>opuesto</b> al ángulo de 30°: $$\sin 30^\circ = \frac{h}{8}$$",
   r"Como $\sin 30^\circ = \tfrac{1}{2}$: $$h = 8 \cdot \tfrac{1}{2} = 4 \text{ m}$$"],
  r"Usar coseno en vez de seno: $8 \cdot \cos 30^\circ = 4\sqrt{3}$ (B), que es la distancia horizontal.",
  r"$\sin = \tfrac{\text{opuesto}}{\text{hipotenusa}}$, $\cos = \tfrac{\text{adyacente}}{\text{hipotenusa}}$, $\tan = \tfrac{\text{opuesto}}{\text{adyacente}}$.",
  "respuesta = 8*sin(pi/6)"))

L.append(P("M2", E, "Combinatoria", "¿Cuántos comités distintos? 👥",
  r"De un grupo de <b>7 personas</b> se quiere formar un comité de <b>3 integrantes</b>, sin cargos. ¿Cuántos comités distintos se pueden formar?",
  ["35", "210", "21", "343", "7"], ["35", "210", "21", "343", "7"], 0,
  [r"Sin cargos, el orden <b>no importa</b>: son combinaciones.",
   r"$$\binom{7}{3} = \frac{7!}{3!\,4!} = \frac{7 \cdot 6 \cdot 5}{3 \cdot 2 \cdot 1} = 35$$"],
  r"Usar variaciones ($7 \cdot 6 \cdot 5 = 210$) como si el orden importara (B).",
  r"Si el orden importa → variaciones. Si <b>no</b> importa (grupos, comités) → combinaciones $\binom{n}{k}$.",
  "respuesta = binomial(7, 3)"))

L.append(P("M2", E, "Probabilidad condicional", "Probabilidad condicional en una encuesta 📋",
  r"En una empresa, el <b>60%</b> son mujeres. De ellas, el <b>30%</b> usa lentes; de los hombres, el <b>20%</b>. Si se elige al azar una persona que <b>usa lentes</b>, ¿cuál es la probabilidad de que sea mujer?",
  [r"$\dfrac{9}{13}$", r"$\dfrac{3}{10}$", r"$\dfrac{9}{50}$", r"$\dfrac{13}{50}$", r"$\dfrac{3}{5}$"],
  ["9/13", "3/10", "9/50", "13/50", "3/5"], 0,
  [r"Mujeres con lentes: $0{,}6 \cdot 0{,}3 = 0{,}18$. Hombres con lentes: $0{,}4 \cdot 0{,}2 = 0{,}08$.",
   r"Total con lentes: $0{,}18 + 0{,}08 = 0{,}26$.",
   r"$$P(M \mid L) = \frac{0{,}18}{0{,}26} = \frac{9}{13}$$"],
  r"Responder $P(L \mid M) = 0{,}3$ (B): es la condicional al revés.",
  r"$P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$. Fíjate bien en cuál es la condición.",
  "pm = Rational(6,10); respuesta = (pm*Rational(3,10)) / (pm*Rational(3,10) + (1-pm)*Rational(2,10))"))

L.append(P("M2", E, "Modelo binomial", "Monedas y el modelo binomial 🪙",
  r"Se lanza una moneda equilibrada <b>4 veces</b>. ¿Cuál es la probabilidad de obtener <b>exactamente 2 caras</b>?",
  [r"$\dfrac{3}{8}$", r"$\dfrac{1}{2}$", r"$\dfrac{1}{4}$", r"$\dfrac{1}{16}$", r"$\dfrac{1}{8}$"],
  ["3/8", "1/2", "1/4", "1/16", "1/8"], 0,
  [r"Hay $\binom{4}{2} = 6$ formas de ubicar las 2 caras entre los 4 lanzamientos.",
   r"Cada secuencia tiene probabilidad $\left(\tfrac{1}{2}\right)^4 = \tfrac{1}{16}$.",
   r"$$P = 6 \cdot \frac{1}{16} = \frac{3}{8}$$"],
  r"Pensar que \"2 de 4 es la mitad\" y marcar $\tfrac{1}{2}$, u olvidar el factor $\binom{4}{2}$ ($\tfrac{1}{16}$).",
  r"Binomial: $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$.",
  "respuesta = binomial(4,2) * Rational(1,2)**4"))

L.append(P("M2", G, "Ecuación de la recta", "¿Dónde corta la recta al eje Y? 📏",
  r"Una recta pasa por los puntos $A(1, 2)$ y $B(3, 8)$. ¿En qué valor corta al <b>eje $Y$</b>?",
  ["$-1$", "2", "3", "1", "$-3$"], ["-1", "2", "3", "1", "-3"], 0,
  [r"Pendiente: $$m = \frac{8 - 2}{3 - 1} = 3$$",
   r"Con el punto $A$: $y - 2 = 3(x - 1)$, es decir, $$y = 3x - 1$$",
   r"Corte con el eje $Y$ (cuando $x = 0$): $y = -1$."],
  r"Responder la pendiente (C) o la ordenada del punto $A$ (B).",
  r"Ecuación punto-pendiente: $y - y_1 = m(x - x_1)$. El corte con el eje $Y$ es el $n$ de $y = mx + n$.",
  "x = symbols('x'); m = Rational(8-2, 3-1); respuesta = (m*(x-1)+2).subs(x, 0)"))

L.append(P("M2", E, "Medidas de dispersión", "Varianza paso a paso 📉",
  r"¿Cuál es la <b>varianza</b> (poblacional) del conjunto de datos $$2,\; 4,\; 6,\; 8\,?$$",
  ["5", r"$\sqrt{5}$", r"$\dfrac{20}{3}$", "6", r"$\dfrac{5}{2}$"], ["5", "sqrt(5)", "20/3", "6", "5/2"], 0,
  [r"Media: $\bar{x} = \tfrac{2 + 4 + 6 + 8}{4} = 5$.",
   r"Desviaciones al cuadrado: $9,\; 1,\; 1,\; 9$, que suman 20.",
   r"$$\sigma^2 = \frac{20}{4} = 5$$"],
  r"Sacar la raíz (B), que es la desviación estándar, o dividir por $n - 1$ (C), que es la varianza muestral.",
  r"Varianza: promedio de las desviaciones al cuadrado. Desviación estándar: su raíz cuadrada.",
  "d = [2,4,6,8]; m = Rational(sum(d), len(d)); respuesta = sum((v-m)**2 for v in d) / len(d)"))

L.append(P("M2", N, "Matemática financiera", "Interés compuesto vs simple 💰",
  r"Se invierten <b>\$1.000.000</b> a un interés <b>compuesto</b> del <b>10% anual</b>. ¿Cuánto dinero habrá al cabo de <b>2 años</b>?",
  [r"\$1.210.000", r"\$1.200.000", r"\$1.100.000", r"\$210.000", r"\$1.020.000"],
  ["1210000", "1200000", "1100000", "210000", "1020000"], 0,
  [r"Con interés compuesto, cada año se gana sobre el capital acumulado: $$C = 1.000.000 \cdot (1{,}1)^2$$",
   r"$$C = 1.000.000 \cdot 1{,}21 = 1.210.000$$"],
  r"Usar interés simple ($10\% \cdot 2 = 20\%$) y marcar B, o responder solo los intereses (D).",
  r"Compuesto: $C_f = C_0 (1 + i)^n$. Simple: $C_f = C_0 (1 + i \cdot n)$.",
  "respuesta = 1000000 * Rational(11,10)**2"))

import random, re
rnd = random.Random(20261022)
LET = "ABCDE"
METAS = [i % 5 for i in range(len(L))]; rnd.shuffle(METAS)
for p in L:
    for k, v in p.items():
        if isinstance(v, str): p[k] = v.replace('\\"', '"')
        if isinstance(v, list): p[k] = [x.replace('\\"', '"') if isinstance(x, str) else x for x in v]
    destino = METAS.pop()
    resto = [i for i in range(5) if i != p["correcta"]]; rnd.shuffle(resto)
    orden = resto[:destino] + [p["correcta"]] + resto[destino:]   # orden[nuevo] = viejo
    nuevo_de = {viejo: nuevo for nuevo, viejo in enumerate(orden)}
    p["alternativas"] = [p["alternativas"][i] for i in orden]
    p["valores"] = [p["valores"][i] for i in orden]
    p["correcta"] = nuevo_de[p["correcta"]]
    f = lambda m: m.group(1) + LET[nuevo_de[LET.index(m.group(2))]] + m.group(3)
    p["trampa"] = re.sub(r"(marcar |marcando |\()([A-E])(\)|\b)", f, p["trampa"])
json.dump(L, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lote_2026-10-22.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(L), "problemas;", sum(p["nivel"] == "M2" for p in L), "de M2")
