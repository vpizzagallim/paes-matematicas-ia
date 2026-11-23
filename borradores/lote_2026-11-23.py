# Lote 23-nov-2026: problemas normales (4 alternativas, con guion de voz).
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

L = []
# ======================= M1 · NÚMEROS
L.append(P("M1", N, "División con resto: viajes con la tarjeta", "¿Te alcanza para volver? 🚇",
  r"Martina carga <b>\$5.000</b> en su tarjeta de transporte. Si cada viaje le cuesta <b>\$760</b>, ¿cuántos <b>viajes completos</b> puede pagar con esa carga?",
  ["6", "7", r"6,58", "5"], ["6", "7", "329/50", "5"], 0,
  [r"Se divide la carga por el valor del viaje: $$5.000 : 760 \approx 6{,}58$$", r"Solo cuentan los viajes completos: $$6 \cdot 760 = 4.560 \le 5.000$$ y $$7 \cdot 760 = 5.320 > 5.000$$"],
  r"Redondear $6{,}58$ hacia arriba y marcar B, o dar el decimal como respuesta (C).",
  r"Cuando se pregunta por unidades <b>completas</b>, se toma la parte entera de la división, sin redondear hacia arriba.",
  "carga, viaje = 5000, 760; n = 0\nwhile (n + 1)*viaje <= carga: n += 1\nrespuesta = Integer(n)",
  [(["Dividimos", r"$5.000 : 760 \approx 6{,}58$"], "Cinco mil dividido en setecientos sesenta da seis coma cinco ocho."),
   (["Solo viajes completos", r"$6 \cdot 760 = 4.560$"], "Pero no existe medio viaje. Seis viajes cuestan cuatro mil quinientos sesenta, y el séptimo ya no alcanza.")],
  "seis viajes", "Si preguntan por cosas completas, te quedas con la parte entera. Redondear a siete te deja atrapado en el torniquete."))

L.append(P("M1", N, "Porcentaje de aumento: puntaje de ensayo", "¿Cuánto subiste? 📈",
  r"En el primer ensayo, Diego obtuvo <b>640 puntos</b> y en el segundo, <b>720 puntos</b>. ¿En qué <b>porcentaje</b> aumentó su puntaje?",
  [r"12,5%", "80%", r"≈ 11,1%", "8%"], ["25/2", "80", "100/9", "8"], 0,
  [r"El aumento fue $$720 - 640 = 80$$ puntos.", r"Se compara con el puntaje <b>inicial</b>: $$\frac{80}{640} = 0{,}125 = 12{,}5\%$$"],
  r"Dar los 80 puntos como si fueran porcentaje (B), o dividir por el puntaje final, $80 : 720$ (C).",
  r"Variación porcentual: $\dfrac{\text{final} - \text{inicial}}{\text{inicial}} \cdot 100$.",
  "ini, fin = 640, 720; respuesta = Rational(fin - ini, ini)*100",
  [(["Cuánto subió", r"$720 - 640 = 80$"], "Diego subió ochenta puntos."),
   (["Sobre el inicial", r"$\dfrac{80}{640} = 12{,}5\%$"], "Ochenta sobre seiscientos cuarenta, el puntaje inicial, es cero coma uno dos cinco: doce coma cinco por ciento.")],
  "doce coma cinco por ciento", "El porcentaje de aumento siempre se calcula sobre el valor de partida. Si divides por el final, te sale once coma uno, y eso no es lo que subiste."))

L.append(P("M1", N, "Proporcionalidad directa: receta de sopaipillas", "Sopaipillas para todo el curso 🌧️",
  r"Una receta usa <b>500 g de harina</b> para hacer <b>20 sopaipillas</b>. Manteniendo la proporción, ¿cuánta harina se necesita para <b>32 sopaipillas</b>?",
  ["800 g", "512 g", "640 g", "1.280 g"], ["800", "512", "640", "1280"], 0,
  [r"Harina por sopaipilla: $$500 : 20 = 25 \text{ g}$$", r"Para 32 sopaipillas: $$25 \cdot 32 = 800 \text{ g}$$"],
  r"Sumar la diferencia, $500 + 12 = 512$ (B), o armar mal la proporción, $\dfrac{20 \cdot 32}{1}$ (C).",
  r"En una proporción directa, si una cantidad se multiplica por $k$, la otra también: busca el <b>valor unitario</b>.",
  "x = symbols('x'); respuesta = solve(Eq(Rational(500, 20), x/32), x)[0]",
  [(["Por cada sopaipilla", r"$500 : 20 = 25 \text{ g}$"], "Quinientos gramos para veinte sopaipillas son veinticinco gramos por cada una."),
   (["Para treinta y dos", r"$25 \cdot 32 = 800 \text{ g}$"], "Veinticinco por treinta y dos: ochocientos gramos.")],
  "ochocientos gramos", "En proporción directa, calcula primero cuánto va por unidad. Sumar doce gramos porque son doce sopaipillas más no tiene sentido: cada una lleva veinticinco."))

L.append(P("M1", N, "Suma de raíces semejantes", "Raíces que se pueden sumar ✨",
  r"¿Cuál es el valor de $$\sqrt{50} + \sqrt{18}$$?",
  [r"$8\sqrt{2}$", r"$\sqrt{68}$", r"$15\sqrt{2}$", r"$4\sqrt{2}$"], ["8*sqrt(2)", "sqrt(68)", "15*sqrt(2)", "4*sqrt(2)"], 0,
  [r"Se descompone cada raíz: $$\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt{2}$$ $$\sqrt{18} = \sqrt{9 \cdot 2} = 3\sqrt{2}$$", r"Ahora son semejantes: $$5\sqrt{2} + 3\sqrt{2} = 8\sqrt{2}$$"],
  r"Sumar los números dentro de la raíz, $\sqrt{68}$ (B), o multiplicar los coeficientes, $15\sqrt{2}$ (C).",
  r"Solo se suman raíces con el <b>mismo radicando</b>; antes, saca de la raíz los cuadrados perfectos.",
  "respuesta = sqrt(50) + sqrt(18)",
  [(["Descomponemos", r"$5\sqrt{2} + 3\sqrt{2}$"], "Raíz de cincuenta es cinco raíz de dos, y raíz de dieciocho es tres raíz de dos."),
   (["Sumamos", r"$8\sqrt{2}$"], "Ahora tienen la misma raíz y se suman como términos semejantes: ocho raíz de dos.")],
  "ocho raíz de dos", "Las raíces no se suman por dentro: raíz de cincuenta más raíz de dieciocho no es raíz de sesenta y ocho. Primero simplifica y después suma las semejantes."))

L.append(P("M1", N, "Fracción de una fracción: el curso", "¿Cuántos usan Metro? 🚇",
  r"En un curso de <b>40 estudiantes</b>, $\dfrac{3}{5}$ llega en Metro. De ellos, $\dfrac{3}{4}$ hace <b>combinación</b> con micro. ¿Cuántos estudiantes del curso llegan en Metro y hacen combinación?",
  ["18", "24", "30", "6"], ["18", "24", "30", "6"], 0,
  [r"Llegan en Metro: $$\frac{3}{5} \cdot 40 = 24$$", r"De ellos, hacen combinación: $$\frac{3}{4} \cdot 24 = 18$$"],
  r"Quedarse con los que llegan en Metro (B) o aplicar $\dfrac{3}{4}$ al curso completo (C).",
  r"«Una fracción <b>de</b> otra» se resuelve multiplicando: $\dfrac{3}{4} \cdot \dfrac{3}{5} = \dfrac{9}{20}$ del total.",
  "total = 40; metro = Rational(3, 5)*total; respuesta = Rational(3, 4)*metro",
  [(["En Metro", r"$\dfrac{3}{5} \cdot 40 = 24$"], "Tres quintos de cuarenta son veinticuatro estudiantes que llegan en Metro."),
   (["Con combinación", r"$\dfrac{3}{4} \cdot 24 = 18$"], "Y tres cuartos de esos veinticuatro: dieciocho.")],
  "dieciocho estudiantes", "Cuando dice «de ellos», la segunda fracción se aplica a lo que quedó, no al total. Si usas los cuarenta, te sale treinta, que es otra alternativa."))

L.append(P("M1", N, "Redondeo y truncamiento", "¿Redondear o truncar? ✂️",
  r"El número $7{,}48$ se <b>redondea</b> a la décima y también se <b>trunca</b> a la décima. ¿Cuál es la <b>diferencia</b> entre ambos resultados?",
  [r"0,1", "0", r"0,08", r"0,02"], ["1/10", "0", "2/25", "1/50"], 0,
  [r"Redondeo a la décima: la centésima es 8, que es mayor o igual a 5, así que sube: $$7{,}48 \to 7{,}5$$", r"Truncamiento: se cortan las cifras sobrantes: $$7{,}48 \to 7{,}4$$ La diferencia es $$7{,}5 - 7{,}4 = 0{,}1$$"],
  r"Creer que redondear y truncar dan lo mismo (B) o restar al número original, $7{,}48 - 7{,}4$ (C).",
  r"<b>Truncar</b> corta sin mirar la cifra siguiente; <b>redondear</b> sube una unidad si la cifra siguiente es 5 o más.",
  "x = Rational(748, 100); red = floor(x*10 + Rational(1, 2))/Integer(10); tru = floor(x*10)/Integer(10); respuesta = red - tru",
  [(["Redondeo", r"$7{,}48 \to 7{,}5$"], "Para redondear a la décima miramos el ocho. Como es cinco o más, sube: siete coma cinco."),
   (["Truncamiento", r"$7{,}48 \to 7{,}4$"], "Truncar es cortar sin mirar nada: siete coma cuatro. La diferencia es cero coma uno.")],
  "cero coma uno", "Truncar es cortar, redondear es mirar la cifra siguiente. En la PAES preguntan justamente por esa diferencia."))

# ======================= M1 · ÁLGEBRA
L.append(P("M1", A, "Ecuación lineal: tarifa de taxi", "¿Cuántos kilómetros anduvo? 🚕",
  r"Un taxi cobra <b>\$400</b> fijos más <b>\$160</b> por cada <b>200 m</b> recorridos. Si un viaje costó <b>\$5.200</b>, ¿cuántos <b>kilómetros</b> recorrió?",
  ["6 km", "30 km", "3 km", "7 km"], ["6", "30", "3", "7"], 0,
  [r"Si $n$ es el número de tramos de 200 m: $$400 + 160n = 5.200 \Rightarrow n = 30$$", r"La distancia es $$30 \cdot 200 \text{ m} = 6.000 \text{ m} = 6 \text{ km}$$"],
  r"Responder el número de tramos (B), o sumar los \$400 en vez de restarlos: $5.600 : 160 = 35$ tramos, 7 km (D).",
  r"Ojo con las unidades: la incógnita suele ser una cantidad de <b>tramos</b>, que después hay que convertir.",
  "n = symbols('n'); tramos = solve(Eq(400 + 160*n, 5200), n)[0]; respuesta = tramos*200/Integer(1000)",
  [(["Planteamos", r"$400 + 160n = 5.200$"], "Cuatrocientos fijos más ciento sesenta por cada tramo igual a cinco mil doscientos. Ene vale treinta tramos."),
   (["Pasamos a kilómetros", r"$30 \cdot 200 \text{ m} = 6 \text{ km}$"], "Treinta tramos de doscientos metros son seis mil metros: seis kilómetros.")],
  "seis kilómetros", "La ecuación te da tramos, no kilómetros. Antes de marcar, revisa en qué unidad te preguntan."))

L.append(P("M1", A, "Sistema 2x2: monedas en la alcancía", "Rompe la alcancía 🐷",
  r"En una alcancía hay <b>30 monedas</b>, solo de <b>\$100</b> y de <b>\$500</b>, que suman <b>\$7.400</b>. ¿Cuántas monedas de <b>\$500</b> hay?",
  ["11", "19", "15", r"14,8"], ["11", "19", "15", "74/5"], 0,
  [r"Con $x$ monedas de \$100 e $y$ de \$500: $$x + y = 30$$ $$100x + 500y = 7.400$$", r"Reemplazando $x = 30 - y$: $$3.000 + 400y = 7.400 \Rightarrow y = 11$$"],
  r"Responder las monedas de \$100 (B), o dividir $7.400 : 500 = 14{,}8$ ignorando las otras monedas (D).",
  r"Un sistema 2x2 nace de dos datos distintos: <b>cantidad</b> de objetos y <b>valor</b> total.",
  "x, y = symbols('x y'); s = solve([Eq(x + y, 30), Eq(100*x + 500*y, 7400)], [x, y]); respuesta = s[y]",
  [(["Planteamos", r"$x + y = 30$", r"$100x + 500y = 7.400$"], "Equis monedas de cien e ye de quinientos. Suman treinta monedas y siete mil cuatrocientos pesos."),
   (["Sustituimos", r"$3.000 + 400y = 7.400 \Rightarrow y = 11$"], "Reemplazando equis por treinta menos ye, queda cuatrocientos ye igual a cuatro mil cuatrocientos. Ye vale once.")],
  "once monedas", "Revisa qué incógnita te piden: once son las de quinientos y diecinueve las de cien. Elegir la otra es el error más típico."))

L.append(P("M1", A, "Eje de simetría de una parábola", "El espejo de la parábola 🪞",
  r"La parábola de una función cuadrática pasa por los puntos $(-1,\ 5)$ y $(7,\ 5)$. ¿Cuál es la ecuación de su <b>eje de simetría</b>?",
  [r"$x = 3$", r"$x = 4$", r"$y = 5$", r"$x = 6$"], ["3", "4", "5", "6"], 0,
  [r"Los dos puntos tienen la misma altura ($y = 5$), así que son simétricos respecto del eje.", r"El eje pasa por el punto medio de sus abscisas: $$x = \frac{-1 + 7}{2} = 3$$"],
  r"Restar en vez de sumar, $\dfrac{7 - (-1)}{2} = 4$ (B), o confundir el eje con la recta $y = 5$ (C).",
  r"Dos puntos de una parábola con la <b>misma ordenada</b> están a igual distancia del eje de simetría.",
  "a, b, c, x = symbols('a b c x')\nf = a*(x + 1)*(x - 7) + 5\nrespuesta = solve(diff(f, x), x)[0]",
  [(["Misma altura", r"$(-1,\ 5)\ \text{y}\ (7,\ 5)$"], "Los dos puntos están a la misma altura, cinco. Por eso son simétricos respecto del eje."),
   (["Punto medio", r"$x = \dfrac{-1 + 7}{2} = 3$"], "El eje pasa justo al medio: menos uno más siete, dividido en dos, da tres.")],
  "equis igual a tres", "Si dos puntos de una parábola tienen la misma altura, el eje de simetría está justo al medio. Y recuerda: el eje es vertical, siempre es equis igual a algo."))

L.append(P("M1", A, "Inecuación: compra con despacho", "¿Cuántas poleras alcanzan? 👕",
  r"Una tienda online vende poleras a <b>\$6.990</b> cada una y cobra <b>\$3.500</b> de despacho por pedido. Con <b>\$50.000</b>, ¿cuál es la <b>máxima</b> cantidad de poleras que se pueden comprar en un pedido?",
  ["6", "7", "5", "8"], ["6", "7", "5", "8"], 0,
  [r"Con $n$ poleras: $$6.990n + 3.500 \le 50.000$$", r"$$6.990n \le 46.500 \Rightarrow n \le 6{,}65\ldots$$ Como $n$ es entero, el máximo es 6."],
  r"Olvidar el despacho, $50.000 : 6.990 \approx 7{,}15$, y marcar B, o redondear $6{,}65$ hacia arriba (también B).",
  r"En una inecuación con objetos enteros, el máximo es la <b>parte entera</b> de la solución.",
  "n = symbols('n', integer=True, positive=True); m = 0\nwhile 6990*(m + 1) + 3500 <= 50000: m += 1\nrespuesta = Integer(m)",
  [(["Planteamos", r"$6.990n + 3.500 \le 50.000$"], "El total, poleras más despacho, no puede pasar de cincuenta mil."),
   (["Despejamos", r"$n \le 6{,}65 \Rightarrow 6$"], "Ene es menor o igual a seis coma seis cinco. Como no se compran pedazos de polera, el máximo es seis.")],
  "seis poleras", "No olvides los cobros fijos como el despacho, y en cantidades enteras nunca redondees hacia arriba: con siete poleras te pasas del presupuesto."))

L.append(P("M1", A, "Lenguaje algebraico: el número pensado", "Adivina el número 🔢",
  r"Si al <b>triple</b> de un número se le restan <b>7</b>, se obtiene lo mismo que al sumarle <b>5</b> a su <b>doble</b>. ¿Cuál es el número?",
  ["12", "26", "2", "-2"], ["12", "26", "2", "-2"], 0,
  [r"Traducimos: $$3x - 7 = 2x + 5$$", r"Despejamos: $$3x - 2x = 5 + 7 \Rightarrow x = 12$$"],
  r"Escribir $3(x - 7) = 2x + 5$, que da 26 (B), o equivocarse con los signos al despejar (C o D).",
  r"«El triple de un número» es $3x$; si la resta es al triple, el paréntesis <b>no</b> va.",
  "x = symbols('x'); respuesta = solve(Eq(3*x - 7, 2*x + 5), x)[0]",
  [(["Traducimos", r"$3x - 7 = 2x + 5$"], "Triple del número menos siete, igual a doble del número más cinco."),
   (["Despejamos", r"$x = 5 + 7 = 12$"], "Restamos dos equis y sumamos siete a ambos lados: equis vale doce.")],
  "doce", "Comprueba siempre: triple de doce es treinta y seis, menos siete, veintinueve. Doble de doce es veinticuatro, más cinco, veintinueve. Cuadra."))

L.append(P("M1", A, "Suma de cuadrados con a + b y ab", "Sin calcular a ni b 🤯",
  r"Si $a + b = 7$ y $a \cdot b = 10$, ¿cuál es el valor de $$a^2 + b^2$$?",
  ["29", "49", "39", "69"], ["29", "49", "39", "69"], 0,
  [r"Del cuadrado de binomio: $$(a + b)^2 = a^2 + 2ab + b^2$$", r"Despejando: $$a^2 + b^2 = 7^2 - 2 \cdot 10 = 49 - 20 = 29$$"],
  r"Creer que $a^2 + b^2 = (a + b)^2 = 49$ (B), o restar solo $ab$ una vez, $49 - 10 = 39$ (C).",
  r"$a^2 + b^2 = (a + b)^2 - 2ab$: no necesitas conocer $a$ ni $b$ por separado.",
  "a, b = symbols('a b'); s = solve([Eq(a + b, 7), Eq(a*b, 10)], [a, b]); respuesta = s[0][0]**2 + s[0][1]**2",
  [(["Cuadrado de binomio", r"$(a + b)^2 = a^2 + 2ab + b^2$"], "Usamos el cuadrado de binomio: a más be al cuadrado es a cuadrado, más dos a be, más be cuadrado."),
   (["Despejamos", r"$49 - 2 \cdot 10 = 29$"], "Siete al cuadrado es cuarenta y nueve. Le restamos dos veces diez y quedan veintinueve.")],
  "veintinueve", "a cuadrado más be cuadrado no es lo mismo que a más be al cuadrado: falta restar dos a be. Ese es el error que la PAES espera que cometas."))

# ======================= M1 · GEOMETRÍA
L.append(P("M1", G, "Perímetro de un rombo con sus diagonales", "El rombo escondido 💎",
  r"Las diagonales de un rombo miden <b>12 cm</b> y <b>16 cm</b>. ¿Cuál es el <b>perímetro</b> del rombo?",
  ["40 cm", "56 cm", "96 cm", "20 cm"], ["40", "56", "96", "20"], 0,
  [r"Las diagonales se cortan perpendicularmente en su punto medio, formando triángulos de catetos 6 y 8: $$\ell = \sqrt{6^2 + 8^2} = 10$$", r"El perímetro es $$4 \cdot 10 = 40 \text{ cm}$$"],
  r"Sumar dos veces las diagonales, $2(12 + 16) = 56$ (B), o calcular el área en vez del perímetro, $12 \cdot 16 : 2 = 96$ (C).",
  r"En un rombo, las diagonales se cortan en ángulo recto y por la mitad: el lado sale con <b>Pitágoras</b>.",
  "d1, d2 = 12, 16; lado = sqrt(Rational(d1, 2)**2 + Rational(d2, 2)**2); respuesta = 4*lado",
  [(["Mitad de cada diagonal", r"$\ell = \sqrt{6^2 + 8^2} = 10$"], "Las diagonales se cortan por la mitad y en ángulo recto. Con catetos seis y ocho, el lado mide diez."),
   (["Perímetro", r"$4 \cdot 10 = 40 \text{ cm}$"], "Los cuatro lados son iguales: cuarenta centímetros.")],
  "cuarenta centímetros", "En el rombo, las diagonales forman cuatro triángulos rectángulos. Usa las mitades: seis, ocho, diez, el trío pitagórico de siempre."))

L.append(P("M1", G, "Sector circular: la pizza", "¿Cuánta pizza te toca? 🍕",
  r"Una pizza circular de <b>40 cm de diámetro</b> se corta en <b>8 trozos iguales</b>. ¿Cuál es el <b>área</b> de un trozo?",
  [r"$50\pi$ cm²", r"$200\pi$ cm²", r"$5\pi$ cm²", r"$400\pi$ cm²"], ["50*pi", "200*pi", "5*pi", "400*pi"], 0,
  [r"El radio es la mitad del diámetro: $r = 20$. Área total: $$\pi \cdot 20^2 = 400\pi$$", r"Cada trozo es un octavo: $$\frac{400\pi}{8} = 50\pi \text{ cm}^2$$"],
  r"Usar el diámetro como radio, $\pi \cdot 40^2 : 8 = 200\pi$ (B), o dividir el perímetro, $40\pi : 8$ (C).",
  r"Área de un sector: $\dfrac{\text{ángulo}}{360°} \cdot \pi r^2$. Siempre con el <b>radio</b>, no con el diámetro.",
  "r = Rational(40, 2); respuesta = pi*r**2/8",
  [(["Área total", r"$\pi \cdot 20^2 = 400\pi$"], "El radio es veinte. El área de la pizza es pi por veinte al cuadrado: cuatrocientos pi."),
   (["Un trozo", r"$\dfrac{400\pi}{8} = 50\pi$"], "Dividida en ocho: cincuenta pi centímetros cuadrados por trozo.")],
  "cincuenta pi centímetros cuadrados", "Si te dan el diámetro, divídelo por dos antes de usar la fórmula. Con el diámetro te sale una pizza cuatro veces más grande."))

L.append(P("M1", G, "Capacidad de un acuario", "Llenando el acuario 🐠",
  r"Un acuario con forma de paralelepípedo mide <b>60 cm</b> de largo, <b>30 cm</b> de ancho y <b>40 cm</b> de alto. ¿Cuántos <b>litros</b> de agua caben?",
  ["72 L", "720 L", r"7,2 L", "130 L"], ["72", "720", "36/5", "130"], 0,
  [r"Volumen: $$60 \cdot 30 \cdot 40 = 72.000 \text{ cm}^3$$", r"Como $1 \text{ L} = 1.000 \text{ cm}^3$: $$72.000 : 1.000 = 72 \text{ L}$$"],
  r"Dividir por 100 en vez de 1.000 (B), o sumar las medidas, $60 + 30 + 40 = 130$ (D).",
  r"$1 \text{ litro} = 1 \text{ dm}^3 = 1.000 \text{ cm}^3$.",
  "v = 60*30*40; respuesta = Rational(v, 1000)",
  [(["Volumen", r"$60 \cdot 30 \cdot 40 = 72.000 \text{ cm}^3$"], "Largo por ancho por alto: setenta y dos mil centímetros cúbicos."),
   (["A litros", r"$72.000 : 1.000 = 72 \text{ L}$"], "Un litro son mil centímetros cúbicos. Entonces caben setenta y dos litros.")],
  "setenta y dos litros", "Un litro es un cubo de diez centímetros por lado, o sea, mil centímetros cúbicos. Si divides por cien, tu acuario se convierte en piscina."))

L.append(P("M1", G, "Composición de traslaciones", "Dos traslaciones seguidas ➡️",
  r"El punto $P(1,\ 2)$ se traslada según el vector $\vec{u} = (3,\ -1)$ y, luego, el punto obtenido se traslada según $\vec{v} = (-5,\ 4)$. ¿Cuáles son las coordenadas del punto final?",
  [r"$(-1,\ 5)$", r"$(-2,\ 3)$", r"$(9,\ 1)$", r"$(-1,\ -1)$"], ["-1 + 5*I", "-2 + 3*I", "9 + I", "-1 - I"], 0,
  [r"Primera traslación: $$(1 + 3,\ 2 - 1) = (4,\ 1)$$", r"Segunda traslación: $$(4 - 5,\ 1 + 4) = (-1,\ 5)$$"],
  r"Sumar solo los vectores y olvidar el punto, $(-2,\ 3)$ (B), o restar el segundo vector en vez de sumarlo (C).",
  r"Dos traslaciones seguidas equivalen a <b>una sola</b>, con vector $\vec{u} + \vec{v}$.",
  "P = Matrix([1, 2]); u = Matrix([3, -1]); v = Matrix([-5, 4]); F = P + u + v; respuesta = F[0] + F[1]*I",
  [(["Primera", r"$(1,\ 2) + (3,\ -1) = (4,\ 1)$"], "Sumamos el primer vector: el punto queda en cuatro coma uno."),
   (["Segunda", r"$(4,\ 1) + (-5,\ 4) = (-1,\ 5)$"], "Sumamos el segundo: menos uno coma cinco.")],
  "menos uno, cinco", "Trasladar es sumar el vector, coordenada por coordenada. Y si son dos traslaciones, puedes sumar primero los vectores: menos dos, tres, y después al punto."))

L.append(P("M1", G, "Área de un triángulo en el plano", "Triángulo en la cuadrícula 📐",
  r"Un triángulo tiene vértices en $A(0,\ 0)$, $B(6,\ 0)$ y $C(2,\ 5)$. ¿Cuál es su <b>área</b>?",
  ["15", "30", "12", r"$\dfrac{25}{2}$"], ["15", "30", "12", "25/2"], 0,
  [r"La base $AB$ está sobre el eje $X$ y mide 6. La altura es la distancia de $C$ al eje: 5.", r"$$\text{Área} = \frac{6 \cdot 5}{2} = 15$$"],
  r"Olvidar dividir por 2 (B), o usar como altura la coordenada $x$ de $C$ y además no dividir: $6 \cdot 2 = 12$ (C).",
  r"Si un lado está sobre un eje, la <b>altura</b> es la otra coordenada del vértice opuesto.",
  "A, B, C = Point(0, 0), Point(6, 0), Point(2, 5); respuesta = abs(Polygon(A, B, C).area)",
  [(["Base y altura", r"$b = 6,\quad h = 5$"], "La base va de cero a seis sobre el eje equis: mide seis. La altura es la distancia del punto ce al eje: cinco."),
   (["Área", r"$\dfrac{6 \cdot 5}{2} = 15$"], "Base por altura, dividido en dos: quince.")],
  "quince", "En el plano, busca un lado apoyado en un eje: así la base y la altura se leen directo. Y nunca olvides dividir por dos."))

# ======================= M1 · PROBABILIDAD Y ESTADÍSTICA
L.append(P("M1", E, "Promedio al agregar un dato", "La nota que salvó el promedio 📊",
  r"Camila tiene <b>5 notas</b> con promedio <b>5,0</b>. Si obtiene un <b>7,0</b> como sexta nota, todas con igual ponderación, ¿cuál es su nuevo promedio?",
  [r"≈ 5,3", r"6,0", r"5,4", r"≈ 5,2"], ["16/3", "6", "27/5", "26/5"], 0,
  [r"La suma de las 5 notas es $$5 \cdot 5{,}0 = 25$$", r"Con la sexta nota: $$\frac{25 + 7}{6} = \frac{32}{6} \approx 5{,}3$$"],
  r"Promediar solo $5{,}0$ y $7{,}0$ (B), o dividir por 5 en vez de 6 (C).",
  r"Para agregar datos a un promedio, recupera primero la <b>suma total</b>: promedio × cantidad.",
  "suma = 5*5; respuesta = Rational(suma + 7, 6)",
  [(["Suma de las notas", r"$5 \cdot 5{,}0 = 25$"], "Cinco notas con promedio cinco suman veinticinco."),
   (["Nuevo promedio", r"$\dfrac{25 + 7}{6} \approx 5{,}3$"], "Sumamos el siete y dividimos por seis notas: treinta y dos sextos, cerca de cinco coma tres.")],
  "aproximadamente cinco coma tres", "Un siete no te sube el promedio a seis: pesa lo mismo que cada una de las otras notas. Siempre vuelve a la suma total."))

L.append(P("M1", E, "Regla aditiva con un dado", "Primo o mayor que 4 🎲",
  r"Se lanza un dado común de 6 caras. ¿Cuál es la probabilidad de obtener un número <b>primo</b> o un número <b>mayor que 4</b>?",
  [r"$\dfrac{2}{3}$", r"$\dfrac{5}{6}$", r"$\dfrac{1}{6}$", r"$\dfrac{1}{2}$"], ["2/3", "5/6", "1/6", "1/2"], 0,
  [r"Primos: $\{2, 3, 5\}$. Mayores que 4: $\{5, 6\}$. El 5 está en ambos.", r"$$P = \frac{3}{6} + \frac{2}{6} - \frac{1}{6} = \frac{4}{6} = \frac{2}{3}$$"],
  r"Sumar sin restar la intersección, $\dfrac{5}{6}$ (B), o calcular solo la intersección (C).",
  r"$P(A \cup B) = P(A) + P(B) - P(A \cap B)$: lo que está en ambos se cuenta <b>una vez</b>.",
  "A = {2, 3, 5}; B = {x for x in range(1, 7) if x > 4}; respuesta = Rational(len(A | B), 6)",
  [(["Los casos", r"$\{2, 3, 5\} \cup \{5, 6\}$"], "Primos: dos, tres y cinco. Mayores que cuatro: cinco y seis. Ojo, el cinco está en los dos."),
   (["Sin contar doble", r"$\dfrac{3}{6} + \dfrac{2}{6} - \dfrac{1}{6} = \dfrac{2}{3}$"], "Tres más dos menos uno: cuatro casos de seis, o sea, dos tercios.")],
  "dos tercios", "Cuando dos eventos comparten resultados, réstalos una vez. Recuerda también que el uno no es primo."))

L.append(P("M1", E, "Probabilidad experimental: la feria", "Sopaipillas en la feria 📊",
  r"En una feria, de <b>200 personas</b> que pasaron por un carro, <b>46</b> compraron sopaipillas. Usando esa frecuencia relativa, ¿cuántas compras se esperan si pasan <b>1.500 personas</b>?",
  ["345", "460", "690", "23"], ["345", "460", "690", "23"], 0,
  [r"Frecuencia relativa: $$\frac{46}{200} = 0{,}23$$", r"Valor esperado de compras: $$0{,}23 \cdot 1.500 = 345$$"],
  r"Multiplicar $46 \cdot 10$ sin ajustar la proporción (B), o dar el porcentaje como cantidad (D).",
  r"La <b>frecuencia relativa</b> de muchas repeticiones estima la probabilidad del evento.",
  "f = Rational(46, 200); respuesta = f*1500",
  [(["Frecuencia relativa", r"$\dfrac{46}{200} = 0{,}23$"], "Cuarenta y seis de doscientos es cero coma dos tres: el veintitrés por ciento compró."),
   (["Estimación", r"$0{,}23 \cdot 1.500 = 345$"], "Si pasan mil quinientas personas, se esperan trescientas cuarenta y cinco compras.")],
  "trescientas cuarenta y cinco", "La frecuencia relativa sirve como probabilidad estimada. Primero sácala en decimal y después multiplícala por el nuevo total."))

L.append(P("M1", E, "Tabla de frecuencias relativas", "¿Cómo llegan al liceo? 🚲",
  r"En una encuesta a <b>240 estudiantes</b>: el <b>40%</b> llega en Metro, el <b>30%</b> en micro y el resto se reparte en partes iguales entre <b>bicicleta</b> y <b>caminando</b>. ¿Cuántos llegan <b>caminando</b>?",
  ["36", "72", "15", "30"], ["36", "72", "15", "30"], 0,
  [r"Queda $$100\% - 40\% - 30\% = 30\%$$ que se reparte en dos partes iguales: 15% cada una.", r"$$0{,}15 \cdot 240 = 36$$"],
  r"No repartir el 30% restante (B), o dar el porcentaje como número de estudiantes (C).",
  r"En una tabla de frecuencias relativas, los porcentajes <b>suman 100%</b>.",
  "p = (100 - 40 - 30)/Integer(2); respuesta = Rational(p, 100)*240",
  [(["Lo que falta", r"$100 - 40 - 30 = 30\%$"], "Metro y micro suman setenta por ciento. Queda un treinta, que se reparte en dos: quince por ciento cada uno."),
   (["Caminando", r"$0{,}15 \cdot 240 = 36$"], "El quince por ciento de doscientos cuarenta es treinta y seis.")],
  "treinta y seis estudiantes", "Los porcentajes de una tabla siempre suman cien. Encuentra lo que falta, repártelo si te lo piden, y recién ahí pasa a cantidad."))

# ======================= M2
L.append(P("M2", N, "Logaritmos con fracciones", "Logaritmos sin calculadora 🧮",
  r"¿Cuál es el valor de $$\log_2 8 + \log_3 \frac{1}{9}$$?",
  ["1", "5", r"$\log_6 \dfrac{8}{9}$", "-1"], ["1", "5", "log(Rational(8,9))/log(6)", "-1"], 0,
  [r"$$\log_2 8 = 3 \quad (2^3 = 8)$$ $$\log_3 \frac{1}{9} = -2 \quad (3^{-2} = \tfrac{1}{9})$$", r"$$3 + (-2) = 1$$"],
  r"Tomar $\log_3 \dfrac{1}{9}$ como $+2$ y sumar 5 (B), o «juntar» bases distintas en un solo logaritmo (C).",
  r"$\log_b a = c$ significa $b^c = a$; las fracciones con base en el denominador dan exponentes <b>negativos</b>.",
  "respuesta = log(8, 2) + log(Rational(1, 9), 3)",
  [(["Cada logaritmo", r"$\log_2 8 = 3,\quad \log_3 \dfrac{1}{9} = -2$"], "Dos al cubo es ocho, así que el primero vale tres. Tres a la menos dos es un noveno: el segundo vale menos dos."),
   (["Sumamos", r"$3 + (-2) = 1$"], "Tres más menos dos: uno.")],
  "uno", "Pregúntate siempre a qué exponente hay que elevar la base. Si el número es una fracción como un noveno, el exponente es negativo."))

L.append(P("M2", N, "Interés simple: capital inicial", "¿Cuánto se depositó? 🏦",
  r"Un capital se invierte a <b>interés simple</b> con una tasa de <b>6% anual</b>. Después de <b>3 años</b>, el monto acumulado es <b>\$1.180.000</b>. ¿Cuál fue el <b>capital inicial</b>?",
  [r"\$1.000.000", r"\$967.600", r"\$1.112.000", r"\$990.758"], ["1000000", "967600", "1112000", "990758"], 0,
  [r"Con interés simple: $$C(1 + 0{,}06 \cdot 3) = 1.180.000$$", r"$$C \cdot 1{,}18 = 1.180.000 \Rightarrow C = 1.000.000$$"],
  r"Restar el 18% al monto, $1.180.000 \cdot 0{,}82$ (B), o restar solo un año de interés (C).",
  r"Interés simple: $M = C(1 + i \cdot t)$. Para volver al capital se <b>divide</b>, no se resta el porcentaje.",
  "C = symbols('C'); respuesta = solve(Eq(C*(1 + Rational(6, 100)*3), 1180000), C)[0]",
  [(["Planteamos", r"$C(1 + 0{,}06 \cdot 3) = 1.180.000$"], "En tres años, al seis por ciento simple, el capital crece un dieciocho por ciento."),
   (["Despejamos", r"$C = 1.180.000 : 1{,}18 = 1.000.000$"], "Dividimos por uno coma uno ocho: el capital era un millón de pesos.")],
  "un millón de pesos", "Para volver atrás desde el monto final se divide por el factor, no se resta el porcentaje. Restar el dieciocho por ciento te deja con menos plata de la que se depositó."))

L.append(P("M2", A, "Ecuación exponencial: seguidores", "Seguidores que se duplican 📱",
  r"Los seguidores de una cuenta de matemáticas se modelan por $$N(t) = 500 \cdot 2^t$$ donde $t$ son semanas. ¿En qué semana la cuenta llega a <b>16.000 seguidores</b>?",
  ["5", "32", "6", "4"], ["5", "32", "6", "4"], 0,
  [r"$$500 \cdot 2^t = 16.000 \Rightarrow 2^t = 32$$", r"Como $2^5 = 32$: $$t = 5$$"],
  r"Responder $2^t = 32$ sin despejar el exponente (B), o contar mal las potencias de 2 (C o D).",
  r"En una ecuación exponencial, deja la potencia sola y escribe ambos lados con la <b>misma base</b>.",
  "t = symbols('t'); respuesta = solve(Eq(500*2**t, 16000), t)[0]",
  [(["Aislamos la potencia", r"$2^t = 16.000 : 500 = 32$"], "Dividimos dieciséis mil por quinientos: dos elevado a te es treinta y dos."),
   (["Misma base", r"$2^t = 2^5 \Rightarrow t = 5$"], "Treinta y dos es dos a la quinta, así que te vale cinco semanas.")],
  "la semana cinco", "Primero aísla la potencia y después iguala las bases. Treinta y dos es lo que vale la potencia, no el número de semanas."))

L.append(P("M2", A, "Exponentes fraccionarios", "Potencias con fracción 🧠",
  r"¿Cuál es el valor de $$27^{\frac{2}{3}} + 16^{\frac{3}{4}}$$?",
  ["17", "30", "12", "26"], ["17", "30", "12", "26"], 0,
  [r"$$27^{\frac{2}{3}} = \left(\sqrt[3]{27}\right)^2 = 3^2 = 9$$", r"$$16^{\frac{3}{4}} = \left(\sqrt[4]{16}\right)^3 = 2^3 = 8$$ Suma: $9 + 8 = 17$."],
  r"Multiplicar la base por la fracción: $27 \cdot \dfrac{2}{3} + 16 \cdot \dfrac{3}{4} = 30$ (B), o invertir raíz y potencia en alguno de los términos.",
  r"$a^{\frac{m}{n}} = \left(\sqrt[n]{a}\right)^m$: el <b>denominador</b> es la raíz y el numerador, la potencia.",
  "respuesta = Integer(27)**Rational(2, 3) + Integer(16)**Rational(3, 4)",
  [(["Primer término", r"$27^{\frac{2}{3}} = 3^2 = 9$"], "El denominador es la raíz: raíz cúbica de veintisiete es tres, y tres al cuadrado es nueve."),
   (["Segundo término", r"$16^{\frac{3}{4}} = 2^3 = 8$"], "Raíz cuarta de dieciséis es dos, y dos al cubo es ocho. Nueve más ocho: diecisiete.")],
  "diecisiete", "El denominador del exponente es la raíz y el numerador es la potencia. Saca primero la raíz: los números quedan chicos y no te equivocas."))

L.append(P("M2", G, "Seno en contexto: volantín", "El volantín de septiembre 🪁",
  r"El hilo de un volantín mide <b>40 m</b>, está completamente estirado y forma un ángulo de <b>60°</b> con el suelo. Despreciando la altura de la mano, ¿a qué <b>altura</b> está el volantín?",
  [r"$20\sqrt{3}$ m", "20 m", r"$40\sqrt{3}$ m", r"$\dfrac{40\sqrt{3}}{3}$ m"], ["20*sqrt(3)", "20", "40*sqrt(3)", "40*sqrt(3)/3"], 0,
  [r"El hilo es la hipotenusa y la altura es el cateto <b>opuesto</b> al ángulo: $$h = 40 \cdot \text{sen}\,60°$$", r"$$h = 40 \cdot \frac{\sqrt{3}}{2} = 20\sqrt{3} \text{ m}$$"],
  r"Usar coseno en vez de seno, $40 \cdot \cos 60° = 20$ (B), o multiplicar por $\tan 60°$ (C).",
  r"Con la hipotenusa conocida: cateto opuesto = hipotenusa · seno; cateto adyacente = hipotenusa · coseno.",
  "h = 40*sin(pi/3); respuesta = h",
  [(["Identificamos", r"$h = 40 \cdot \text{sen}\,60°$"], "El hilo es la hipotenusa, y la altura es el cateto opuesto al ángulo. Eso es seno."),
   (["Calculamos", r"$40 \cdot \dfrac{\sqrt{3}}{2} = 20\sqrt{3}$"], "Seno de sesenta es raíz de tres partido en dos. La altura es veinte raíz de tres metros.")],
  "veinte raíz de tres metros", "Fíjate qué lado conoces y cuál buscas. Hipotenusa y opuesto: seno. Si usas coseno te da veinte metros, que es la distancia por el suelo."))

L.append(P("M2", A, "Recta y área con los ejes", "El triángulo de la recta 📐",
  r"La recta de ecuación $$2x + 3y = 12$$ forma un triángulo con los ejes coordenados. ¿Cuál es el <b>área</b> de ese triángulo?",
  ["12", "24", "6", "10"], ["12", "24", "6", "10"], 0,
  [r"Corte con el eje $X$ ($y = 0$): $x = 6$. Corte con el eje $Y$ ($x = 0$): $y = 4$.", r"El triángulo es rectángulo, con catetos 6 y 4: $$\text{Área} = \frac{6 \cdot 4}{2} = 12$$"],
  r"Olvidar dividir por 2 (B), o sumar los cortes, $6 + 4 = 10$ (D).",
  r"Para los cortes con los ejes: $y = 0$ da el corte con $X$; $x = 0$ da el corte con $Y$.",
  "x, y = symbols('x y'); a = solve(Eq(2*x, 12), x)[0]; b = solve(Eq(3*y, 12), y)[0]; respuesta = a*b/2",
  [(["Cortes con los ejes", r"$x = 6,\quad y = 4$"], "Con ye igual a cero, equis vale seis. Con equis igual a cero, ye vale cuatro."),
   (["Área", r"$\dfrac{6 \cdot 4}{2} = 12$"], "Es un triángulo rectángulo de catetos seis y cuatro: el área es doce.")],
  "doce", "Una recta que corta ambos ejes forma un triángulo rectángulo con ellos. Busca los cortes, y el resto es base por altura partido en dos."))

L.append(P("M2", E, "Varianza al multiplicar por una constante", "Datos multiplicados por 3 ✖️",
  r"Los datos $2,\ 4,\ 6,\ 8$ tienen varianza <b>5</b>. Si cada dato se <b>multiplica por 3</b>, ¿cuál es la varianza de los nuevos datos?",
  ["45", "15", "5", "8"], ["45", "15", "5", "8"], 0,
  [r"Al multiplicar cada dato por $k$, las distancias a la media se multiplican por $k$, y la varianza por $k^2$.", r"$$3^2 \cdot 5 = 9 \cdot 5 = 45$$"],
  r"Multiplicar la varianza solo por 3 (B), o creer que no cambia, como pasa al <b>sumar</b> una constante (C).",
  r"Si $Y = kX$, entonces $\text{Var}(Y) = k^2\,\text{Var}(X)$ y $\sigma_Y = |k|\,\sigma_X$.",
  "d = [3*v for v in [2, 4, 6, 8]]; m = Rational(sum(d), len(d)); respuesta = sum((v - m)**2 for v in d)/len(d)",
  [(["Regla", r"$\text{Var}(kX) = k^2\,\text{Var}(X)$"], "Si multiplicas todos los datos por tres, las distancias a la media también se triplican, y la varianza, que usa cuadrados, se multiplica por nueve."),
   (["Calculamos", r"$9 \cdot 5 = 45$"], "Nueve por cinco: cuarenta y cinco.")],
  "cuarenta y cinco", "Sumar una constante no cambia la varianza, pero multiplicar sí, y por el cuadrado. La desviación estándar, en cambio, solo se multiplica por tres."))

L.append(P("M2", E, "Combinaciones con dos grupos", "Arma la directiva 🗳️",
  r"Para la directiva del centro de estudiantes postulan <b>6 mujeres</b> y <b>4 hombres</b>. ¿De cuántas formas se puede elegir una comisión de <b>2 mujeres y 1 hombre</b>?",
  ["60", "120", "19", "24"], ["60", "120", "19", "24"], 0,
  [r"Mujeres: $$\binom{6}{2} = 15$$ Hombres: $$\binom{4}{1} = 4$$", r"Por el principio multiplicativo: $$15 \cdot 4 = 60$$"],
  r"Contar las mujeres en orden, $6 \cdot 5 \cdot 4 = 120$ (B), o sumar en vez de multiplicar, $15 + 4$ (C).",
  r"Si el orden no importa, se usan <b>combinaciones</b>; si se eligen de grupos distintos, los resultados se <b>multiplican</b>.",
  "respuesta = binomial(6, 2)*binomial(4, 1)",
  [(["Cada grupo", r"$\dbinom{6}{2} = 15,\quad \dbinom{4}{1} = 4$"], "Dos mujeres de seis: quince formas. Un hombre de cuatro: cuatro formas."),
   (["Multiplicamos", r"$15 \cdot 4 = 60$"], "Cada par de mujeres se combina con cada hombre: sesenta comisiones.")],
  "sesenta", "En una comisión el orden no importa, así que usa combinaciones. Y como eliges de los dos grupos a la vez, multiplica."))

L.append(P("M2", E, "Probabilidad condicional en tabla de doble entrada", "Preu y ensayo 📋",
  r"De <b>120 estudiantes</b>, <b>50</b> van a preuniversitario. De ellos, <b>35</b> superaron los 700 puntos en un ensayo. De los que <b>no</b> van, <b>21</b> superaron los 700 puntos. Si se elige al azar a alguien que superó los 700 puntos, ¿cuál es la probabilidad de que vaya a preuniversitario?",
  [r"$\dfrac{5}{8}$", r"$\dfrac{7}{10}$", r"$\dfrac{7}{24}$", r"$\dfrac{3}{10}$"], ["5/8", "7/10", "7/24", "3/10"], 0,
  [r"Superaron los 700 puntos: $$35 + 21 = 56$$", r"De esos 56, van a preuniversitario 35: $$P = \frac{35}{56} = \frac{5}{8}$$"],
  r"Calcular al revés, $P(\text{supera} \mid \text{preu}) = \dfrac{35}{50}$ (B), o dividir por el total, $\dfrac{35}{120}$ (C).",
  r"En $P(A \mid B)$, el total de referencia es <b>solo el grupo B</b>, lo que ya se sabe que ocurrió.",
  "preu_sup, nopreu_sup = 35, 21; respuesta = Rational(preu_sup, preu_sup + nopreu_sup)",
  [(["El grupo dado", r"$35 + 21 = 56$"], "Sabemos que la persona superó los setecientos. Ese grupo tiene treinta y cinco más veintiuno: cincuenta y seis."),
   (["Dentro del grupo", r"$\dfrac{35}{56} = \dfrac{5}{8}$"], "De esos, treinta y cinco van al preu: treinta y cinco sobre cincuenta y seis, cinco octavos.")],
  "cinco octavos", "En probabilidad condicional, lo que ya sabes reduce el total. Aquí el total no son los ciento veinte ni los cincuenta: son los cincuenta y seis que superaron los setecientos."))

L.append(P("M2", E, "Binomial: penales", "Tanda de penales ⚽",
  r"Una jugadora convierte cada penal con probabilidad <b>0,8</b>, de forma independiente. Si patea <b>3 penales</b>, ¿cuál es la probabilidad de que convierta <b>exactamente 2</b>?",
  [r"0,384", r"0,128", r"0,64", r"0,096"], ["48/125", "16/125", "16/25", "12/125"], 0,
  [r"Una secuencia como «gol, gol, falla» tiene probabilidad $$0{,}8^2 \cdot 0{,}2 = 0{,}128$$", r"La falla puede estar en 3 posiciones: $$\binom{3}{2} \cdot 0{,}128 = 0{,}384$$"],
  r"Olvidar las 3 posiciones de la falla (B), o calcular solo $0{,}8^2$ (C).",
  r"Binomial: $P(X = k) = \dbinom{n}{k} p^k (1 - p)^{n - k}$. El combinatorio cuenta <b>en qué orden</b> pueden ocurrir.",
  "n, p = 3, Rational(4, 5); respuesta = binomial(n, 2)*p**2*(1 - p)",
  [(["Una secuencia", r"$0{,}8^2 \cdot 0{,}2 = 0{,}128$"], "Dos goles y una falla, en un orden fijo, tiene probabilidad cero coma uno dos ocho."),
   (["Tres órdenes posibles", r"$3 \cdot 0{,}128 = 0{,}384$"], "La falla puede ser en el primero, el segundo o el tercer penal: tres por eso, cero coma tres ocho cuatro.")],
  "cero coma tres ocho cuatro", "En la binomial no olvides el combinatorio: cuenta todas las formas de ordenar los éxitos y los fracasos."))
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


rnd = random.Random(20261123)
metas = [i % 4 for i in range(len(L))]; rnd.shuffle(metas)
lote = [finalizar(p, rnd, metas[i]) for i, p in enumerate(L)]
json.dump(lote, open(os.path.join(AQUI, "lote_2026-11-23.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(lote), "problemas")
