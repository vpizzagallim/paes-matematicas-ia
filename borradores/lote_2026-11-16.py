# Lote 16-nov-2026: problemas normales (4 alternativas, con guion de voz).
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
# ======================= M1 · NÚMEROS
L.append(P("M1", N, "Cambio de moneda con comisión", "Dólares para Mendoza ✈️",
  r"Sofía tiene <b>\$190.000</b> para su viaje a Mendoza. La casa de cambio le cobra una <b>comisión de \$9.500</b>, que se descuenta antes de cambiar, y vende cada dólar a <b>\$950</b>. ¿Cuántos <b>dólares</b> recibe?",
  ["190", "200", "210", "10"], ["190", "200", "210", "10"], 0,
  [r"Primero se descuenta la comisión: $$190.000 - 9.500 = 180.500$$", r"Luego se divide por el valor del dólar: $$180.500 : 950 = 190$$"],
  r"Olvidar la comisión y dividir $190.000 : 950 = 200$, marcando B, o sumarla en vez de restarla (C).",
  r"Cuando hay cobros previos, primero se ajusta el monto y después se convierte: <b>pesos ÷ precio del dólar</b>.",
  "pesos, comision, dolar = 190000, 9500, 950; respuesta = Rational(pesos - comision, dolar)",
  [(["Descontamos la comisión", r"$190.000 - 9.500 = 180.500$"], "Primero se descuenta la comisión: quedan ciento ochenta mil quinientos pesos."),
   (["Pasamos a dólares", r"$180.500 : 950 = 190$"], "Cada dólar cuesta novecientos cincuenta. Dividimos y salen ciento noventa dólares.")],
  "ciento noventa dólares", "Para convertir pesos a dólares se divide por el precio del dólar, pero solo con la plata que realmente se cambia. Si olvidas la comisión te salen doscientos, y en la casa de cambio no te van a regalar esos diez dólares."))

L.append(P("M1", N, "Recargo por pagar en cuotas", "¿Contado o en cuotas? 📱",
  r"Un celular cuesta <b>\$240.000</b> al contado, o bien <b>12 cuotas de \$22.000</b>. ¿En qué <b>porcentaje</b> aumenta el precio si se paga en cuotas?",
  ["10%", "24%", r"≈ 9,1%", "110%"], ["10", "24", "100/11", "110"], 0,
  [r"En cuotas se paga $$12 \cdot 22.000 = 264.000$$", r"El recargo es $24.000$, y se compara con el precio <b>original</b>: $$\frac{24.000}{240.000} = 0{,}1 = 10\%$$"],
  r"Dividir el recargo por el precio en cuotas ($24.000 : 264.000 ≈ 9,1\%$) y marcar C, o confundir el factor 1,1 con 110% (D).",
  r"El porcentaje de aumento siempre se calcula sobre el <b>valor inicial</b>: $\dfrac{\text{final} - \text{inicial}}{\text{inicial}}$.",
  "contado, cuotas = 240000, 12*22000; respuesta = Rational(cuotas - contado, contado)*100",
  [(["Total en cuotas", r"$12 \cdot 22.000 = 264.000$"], "Doce cuotas de veintidós mil suman doscientos sesenta y cuatro mil pesos."),
   (["Recargo sobre el contado", r"$\dfrac{24.000}{240.000} = 10\%$"], "Son veinticuatro mil pesos más. Sobre el precio al contado, eso es un diez por ciento.")],
  "diez por ciento", "El aumento porcentual se calcula sobre el valor inicial, no sobre el final. Si divides por el precio en cuotas te sale nueve coma uno, y ese no es el recargo que te cobra la tienda."))

L.append(P("M1", N, "Potencias en contexto: cadena de mensajes", "El meme que se viralizó 📲",
  r"Benja envía un meme a <b>3 amigos</b> (ronda 1). En la ronda 2, cada uno lo reenvía a <b>3 personas nuevas</b>, y así sucesivamente. ¿Cuántas personas reciben el meme <b>en la ronda 5</b>?",
  ["243", "15", "125", "363"], ["243", "15", "125", "363"], 0,
  [r"En cada ronda el número de personas se multiplica por 3: $$3,\ 9,\ 27,\ 81,\ \ldots$$", r"En la ronda 5: $$3^5 = 243$$"],
  r"Multiplicar $3 \cdot 5 = 15$ y marcar B, invertir la potencia ($5^3 = 125$) o sumar todas las rondas (363).",
  r"Si algo se multiplica por el mismo factor en cada etapa, después de $n$ etapas se usa una <b>potencia</b>: $a^n$.",
  "rondas = [3]\nfor _ in range(4): rondas.append(rondas[-1]*3)\nrespuesta = Integer(rondas[-1])",
  [(["Se multiplica por tres", r"$3,\ 9,\ 27,\ 81,\ \ldots$"], "En cada ronda, cada persona lo manda a tres. Tres, nueve, veintisiete, ochenta y uno."),
   (["Ronda cinco", r"$3^5 = 243$"], "En la quinta ronda son tres elevado a cinco: doscientas cuarenta y tres personas.")],
  "doscientas cuarenta y tres", "Cuando algo se multiplica por lo mismo en cada paso, piensa en potencias. Ojo: si sumas todas las rondas te dan trescientos sesenta y tres, pero eso es el total acumulado, no lo que pasa solo en la quinta."))

L.append(P("M1", N, "Precios terminados en 990", "El truco del 990 🛒",
  r"En el supermercado, Martina compra productos de <b>\$1.990</b>, <b>\$2.990</b>, <b>\$990</b> y <b>\$4.990</b>. Si paga con <b>\$20.000</b>, ¿cuánto <b>vuelto</b> recibe?",
  [r"\$9.040", r"\$9.000", r"\$10.960", r"\$8.960"], ["9040", "9000", "10960", "8960"], 0,
  [r"Cada precio es $10$ menos que un número redondo: $$2.000 + 3.000 + 1.000 + 5.000 - 40 = 10.960$$", r"El vuelto es $$20.000 - 10.960 = 9.040$$"],
  r"Redondear y olvidar restar los \$40 (marcar B), o sumarlos en vez de restarlos (D).",
  r"Con precios terminados en 990, redondea hacia arriba y después <b>resta 10 por cada producto</b>.",
  "total = 1990 + 2990 + 990 + 4990; respuesta = Integer(20000 - total)",
  [(["Redondeamos y corregimos", r"$11.000 - 40 = 10.960$"], "Cada precio es diez pesos menos que un número redondo. Once mil menos cuarenta: diez mil novecientos sesenta."),
   (["Vuelto", r"$20.000 - 10.960 = 9.040$"], "Veinte mil menos eso: nueve mil cuarenta pesos de vuelto.")],
  "nueve mil cuarenta pesos", "Con precios terminados en noventa, redondea y luego corrige diez por cada producto. Si te quedas solo con el redondeo, te faltan cuarenta pesos, y en la PAES esa diferencia es otra alternativa."))

# ======================= M1 · ÁLGEBRA
L.append(P("M1", A, "Simplificación de fracciones algebraicas", "Factoriza y vuela 🚀",
  r"¿Cuál es el valor de la expresión $$\frac{x^2 - 9}{x - 3}$$ cuando $x = 97$?",
  ["100", "94", "9.400", "1"], ["100", "94", "9400", "1"], 0,
  [r"Se factoriza el numerador como suma por diferencia: $$\frac{(x + 3)(x - 3)}{x - 3} = x + 3$$", r"Con $x = 97$: $$97 + 3 = 100$$"],
  r"Calcular solo el numerador, $97^2 - 9 = 9.400$, y marcar C, o simplificar mal y quedarse con $x - 3 = 94$ (B).",
  r"Antes de reemplazar, <b>factoriza y simplifica</b>: $a^2 - b^2 = (a + b)(a - b)$.",
  "x = symbols('x'); respuesta = ((x**2 - 9)/(x - 3)).subs(x, 97)",
  [(["Factorizamos", r"$\dfrac{(x+3)(x-3)}{x-3} = x + 3$"], "Equis al cuadrado menos nueve es suma por diferencia: equis más tres por equis menos tres. Se simplifica y queda equis más tres."),
   (["Reemplazamos", r"$97 + 3 = 100$"], "Noventa y siete más tres: cien.")],
  "cien", "Antes de reemplazar números grandes, factoriza y simplifica. Te ahorras calcular noventa y siete al cuadrado, y además evitas el error de quedarte con nueve mil cuatrocientos, que es solo el numerador."))

L.append(P("M1", A, "Ceros de una función cuadrática", "¿Dónde corta al eje X? 📉",
  r"La gráfica de la función $$f(x) = x^2 - 2x - 15$$ corta al eje $X$ en dos puntos. ¿Cuál es la <b>distancia</b> entre esos dos puntos?",
  ["8", "2", "15", "1"], ["8", "2", "15", "1"], 0,
  [r"Se iguala a cero y se factoriza: $$x^2 - 2x - 15 = (x - 5)(x + 3) = 0$$", r"Los ceros son $x = 5$ y $x = -3$; la distancia es $$5 - (-3) = 8$$"],
  r"Restar $5 - 3 = 2$ olvidando el signo negativo y marcar B, o confundir con el vértice, $x = 1$ (D).",
  r"Los puntos donde la parábola corta al eje $X$ son las soluciones de $f(x) = 0$.",
  "x = symbols('x'); r = solve(x**2 - 2*x - 15, x); respuesta = max(r) - min(r)",
  [(["Igualamos a cero", r"$(x - 5)(x + 3) = 0$"], "Cortar el eje equis es que efe de equis valga cero. Factorizamos: equis menos cinco por equis más tres."),
   (["Distancia", r"$5 - (-3) = 8$"], "Los ceros son cinco y menos tres. La distancia entre ellos es ocho.")],
  "ocho", "Los cortes con el eje equis salen de igualar la función a cero. Cuidado con el menos tres: la distancia es cinco menos menos tres, no cinco menos tres."))

L.append(P("M1", A, "Inecuación doble en contexto", "Plan de datos a tu medida 📶",
  r"Un plan de datos cobra <b>\$5.000</b> fijos más <b>\$800 por cada GB</b>. Josefa quiere gastar <b>entre \$9.000 y \$13.000</b>, ambos incluidos. ¿Cuántas cantidades <b>enteras</b> de GB puede contratar?",
  ["6", "5", "10", "4"], ["6", "5", "10", "4"], 0,
  [r"Se plantea: $$9.000 \le 5.000 + 800g \le 13.000$$", r"Restando 5.000 y dividiendo por 800: $$5 \le g \le 10$$ Los enteros son 5, 6, 7, 8, 9 y 10: <b>6 valores</b>."],
  r"Restar $10 - 5 = 5$ y marcar B, olvidando que ambos extremos se cuentan.",
  r"En una inecuación doble se hace la <b>misma operación en las tres partes</b>. Para contar enteros entre $a$ y $b$, inclusive: $b - a + 1$.",
  "respuesta = Integer(len([g for g in range(0, 100) if 9000 <= 5000 + 800*g <= 13000]))",
  [(["Planteamos", r"$9.000 \le 5.000 + 800g \le 13.000$"], "El costo es cinco mil más ochocientos por ge, y debe quedar entre nueve mil y trece mil."),
   (["Despejamos", r"$5 \le g \le 10$"], "Restamos cinco mil y dividimos por ochocientos: ge va de cinco a diez. Son seis valores.")],
  "seis", "Al contar enteros entre dos números incluidos, se resta y se suma uno. Si solo restas, diez menos cinco, te sale cinco y dejas fuera un extremo."))

L.append(P("M1", A, "Números pares consecutivos", "Tres pares seguidos 🔢",
  r"La suma de <b>tres números pares consecutivos</b> es <b>138</b>. ¿Cuál es el <b>mayor</b> de ellos?",
  ["48", "46", "44", "47"], ["48", "46", "44", "47"], 0,
  [r"Si el menor es $n$, los otros son $n + 2$ y $n + 4$: $$n + (n + 2) + (n + 4) = 138$$", r"$$3n + 6 = 138 \Rightarrow n = 44$$ El mayor es $44 + 4 = 48$."],
  r"Responder con el menor (44, marcar C) o el del medio (46, marcar B), o usar consecutivos de 1 en 1 (D).",
  r"Pares (o impares) consecutivos van de 2 en 2: $n$, $n + 2$, $n + 4$. Fíjate qué número te preguntan.",
  "n = symbols('n'); menor = solve(Eq(n + (n + 2) + (n + 4), 138), n)[0]; assert menor % 2 == 0; respuesta = menor + 4",
  [(["De dos en dos", r"$n + (n+2) + (n+4) = 138$"], "Si el menor es ene, los siguientes pares son ene más dos y ene más cuatro."),
   (["Despejamos", r"$3n + 6 = 138 \Rightarrow n = 44$"], "Tres ene más seis es ciento treinta y ocho, así que ene es cuarenta y cuatro. El mayor es cuarenta y ocho.")],
  "cuarenta y ocho", "Los pares consecutivos van de dos en dos. Y lee bien qué te preguntan: cuarenta y cuatro es el menor y cuarenta y seis el del medio, y los dos aparecen como alternativas."))

# ======================= M1 · GEOMETRÍA
L.append(P("M1", G, "Área de un deltoide: el volantín", "El volantín de septiembre 🪁",
  r"Un volantín tiene forma de <b>deltoide</b>, con diagonales de <b>60 cm</b> y <b>40 cm</b>. ¿Cuál es su <b>área</b>?",
  ["1.200 cm²", "2.400 cm²", "200 cm²", "600 cm²"], ["1200", "2400", "200", "600"], 0,
  [r"El área de un deltoide (o de un rombo) es el producto de las diagonales dividido por 2: $$A = \frac{d_1 \cdot d_2}{2}$$", r"$$A = \frac{60 \cdot 40}{2} = 1.200 \text{ cm}^2$$"],
  r"Multiplicar las diagonales sin dividir por 2 (2.400, marcar B), o sumar las diagonales (C).",
  r"Deltoide y rombo: $A = \dfrac{d_1 \cdot d_2}{2}$, porque ocupan la mitad del rectángulo formado por sus diagonales.",
  "d1, d2 = 60, 40; respuesta = Rational(d1*d2, 2)",
  [(["Fórmula del deltoide", r"$A = \dfrac{d_1 \cdot d_2}{2}$"], "El área de un deltoide es diagonal por diagonal, dividido en dos."),
   (["Reemplazamos", r"$\dfrac{60 \cdot 40}{2} = 1.200$"], "Sesenta por cuarenta es dos mil cuatrocientos. La mitad: mil doscientos centímetros cuadrados.")],
  "mil doscientos centímetros cuadrados", "El volantín ocupa justo la mitad del rectángulo que forman sus diagonales. Por eso, si no divides por dos, te sale el doble: dos mil cuatrocientos."))

L.append(P("M1", G, "Volumen de un prisma triangular", "¿Cuánto aire cabe en la carpa? ⛺",
  r"Una carpa tiene forma de <b>prisma triangular</b>. Su cara frontal es un triángulo de <b>2 m de base</b> y <b>1,5 m de altura</b>, y la carpa mide <b>3 m de largo</b>. ¿Cuál es su <b>volumen</b>?",
  ["4,5 m³", "9 m³", "1,5 m³", "6,5 m³"], ["9/2", "9", "3/2", "13/2"], 0,
  [r"El área del triángulo frontal es $$\frac{2 \cdot 1{,}5}{2} = 1{,}5 \text{ m}^2$$", r"El volumen del prisma es área basal por largo: $$1{,}5 \cdot 3 = 4{,}5 \text{ m}^3$$"],
  r"Olvidar dividir por 2 el área del triángulo (9 m³, marcar B) o quedarse solo con el área (C).",
  r"Volumen de cualquier prisma: <b>área de la base × largo</b>. Si la base es un triángulo, su área lleva el «dividido por 2».",
  "b, h, largo = 2, Rational(3, 2), 3; respuesta = b*h/2*largo",
  [(["Área del triángulo", r"$\dfrac{2 \cdot 1{,}5}{2} = 1{,}5$"], "La cara frontal es un triángulo: dos por uno coma cinco, dividido en dos, da uno coma cinco metros cuadrados."),
   (["Por el largo", r"$1{,}5 \cdot 3 = 4{,}5\ \text{m}^3$"], "Lo multiplicamos por los tres metros de largo: cuatro coma cinco metros cúbicos.")],
  "cuatro coma cinco metros cúbicos", "Todo prisma es área basal por largo. El error típico es olvidar que el área del triángulo se divide por dos, y ahí te sale nueve."))

L.append(P("M1", G, "Distancia entre dos puntos", "De la casa al liceo 🗺️",
  r"En un plano de la comuna, con unidades en kilómetros, la casa de Martina está en $(1, 2)$ y su liceo en $(7, 10)$. ¿Cuál es la <b>distancia en línea recta</b> entre ambos?",
  ["10 km", "14 km", "100 km", r"$4\sqrt{13}$ km"], ["10", "14", "100", "4*sqrt(13)"], 0,
  [r"Las diferencias son $7 - 1 = 6$ y $10 - 2 = 8$. Por Pitágoras: $$d = \sqrt{6^2 + 8^2}$$", r"$$d = \sqrt{36 + 64} = \sqrt{100} = 10$$"],
  r"Sumar las diferencias, $6 + 8 = 14$ (marcar B), u olvidar la raíz (C).",
  r"Distancia entre dos puntos: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$, que es Pitágoras en el plano.",
  "respuesta = sqrt((7 - 1)**2 + (10 - 2)**2)",
  [(["Diferencias", r"$\Delta x = 6,\ \Delta y = 8$"], "Restamos las coordenadas: seis en equis y ocho en ye."),
   (["Pitágoras", r"$\sqrt{36 + 64} = 10$"], "Treinta y seis más sesenta y cuatro es cien, y la raíz de cien es diez kilómetros.")],
  "diez kilómetros", "La distancia en línea recta es Pitágoras con las diferencias de coordenadas. Catorce sería caminar seis y después ocho por las calles, no en línea recta."))

L.append(P("M1", G, "Ángulos de un triángulo isósceles", "El techo de la casa 🏠",
  r"El frontón de un techo es un <b>triángulo isósceles</b>. El ángulo de la punta, entre los dos lados iguales, mide <b>40°</b>. ¿Cuánto mide <b>cada uno</b> de los otros dos ángulos?",
  ["70°", "140°", "40°", "50°"], ["70", "140", "40", "50"], 0,
  [r"Los ángulos de un triángulo suman 180°: $$180° - 40° = 140°$$", r"En un isósceles, los ángulos basales son iguales: $$140° : 2 = 70°$$"],
  r"Olvidar dividir por 2 y marcar B (140°), o creer que los tres ángulos son iguales a 40° (C).",
  r"Triángulo isósceles: los ángulos opuestos a los lados iguales son <b>iguales</b>. Siempre suman 180° en total.",
  "a = symbols('a'); respuesta = solve(Eq(40 + 2*a, 180), a)[0]",
  [(["Suma 180°", r"$180° - 40° = 140°$"], "Los tres ángulos suman ciento ochenta. Quitando los cuarenta de la punta, quedan ciento cuarenta."),
   (["Dos ángulos iguales", r"$140° : 2 = 70°$"], "Como es isósceles, los otros dos son iguales: setenta grados cada uno.")],
  "setenta grados", "En un isósceles, los ángulos de la base son iguales. Ciento cuarenta es lo que suman los dos juntos, no cada uno."))

# ======================= M1 · PROBABILIDAD Y ESTADÍSTICA
L.append(P("M1", E, "Diagrama de cajón", "¿Qué hay dentro de la caja? 📦",
  r"En un <b>diagrama de cajón</b> sobre el tiempo que demoran los estudiantes en llegar al liceo, el primer cuartil es <b>15 min</b> y el tercer cuartil es <b>35 min</b>. ¿Qué <b>porcentaje</b> de los estudiantes demora entre 15 y 35 minutos, aproximadamente?",
  ["50%", "25%", "75%", "20%"], ["50", "25", "75", "20"], 0,
  [r"Bajo el primer cuartil queda el 25% de los datos y bajo el tercero, el 75%.", r"Entre ambos: $$75\% - 25\% = 50\%$$"],
  r"Confundir los cuartiles con porcentajes acumulados distintos (25% o 75%), o restar los minutos, $35 - 15 = 20$ (D).",
  r"La «caja» del diagrama va de $Q_1$ a $Q_3$ y siempre contiene cerca del <b>50% central</b> de los datos.",
  "Q1, Q3 = 25, 75; respuesta = Integer(Q3 - Q1)",
  [(["Los cuartiles", r"$Q_1 \to 25\%,\ Q_3 \to 75\%$"], "Bajo el primer cuartil está el veinticinco por ciento, y bajo el tercero, el setenta y cinco."),
   (["La caja", r"$75\% - 25\% = 50\%$"], "Entre los dos queda la mitad de los estudiantes: el cincuenta por ciento.")],
  "cincuenta por ciento", "La caja del diagrama siempre encierra la mitad central de los datos, sin importar los números. Y no restes los minutos: veinte es un tiempo, no un porcentaje."))

L.append(P("M1", E, "Probabilidad con ruleta", "Gira la ruleta 🎡",
  r"En una kermés, una ruleta circular tiene un sector <b>premiado</b> cuyo ángulo central mide <b>72°</b>. Si la ruleta se detiene al azar, ¿cuál es la probabilidad de ganar el premio?",
  [r"$\dfrac{1}{5}$", r"$\dfrac{18}{25}$", r"$\dfrac{1}{72}$", r"$\dfrac{1}{4}$"], ["1/5", "18/25", "1/72", "1/4"], 0,
  [r"La vuelta completa mide 360°, así que $$P = \frac{72}{360}$$", r"Simplificando: $$\frac{72}{360} = \frac{1}{5}$$"],
  r"Dividir por 100 en vez de 360 ($\tfrac{72}{100}$, marcar B) o creer que solo un número de 72 sirve (C).",
  r"Con sectores circulares, la probabilidad es <b>ángulo del sector ÷ 360°</b>.",
  "respuesta = Rational(72, 360)",
  [(["Sobre la vuelta completa", r"$P = \dfrac{72}{360}$"], "Toda la ruleta mide trescientos sesenta grados. El sector premiado ocupa setenta y dos."),
   (["Simplificamos", r"$\dfrac{72}{360} = \dfrac{1}{5}$"], "Setenta y dos trescientos sesentavos es lo mismo que un quinto.")],
  "un quinto", "En una ruleta, la probabilidad es el ángulo del sector dividido por trescientos sesenta. El error típico es dividir por cien, como si los grados fueran porcentajes."))

L.append(P("M1", E, "Porcentajes en una tabla de frecuencias", "¿Cómo llegas al liceo? 🚌",
  r"Se encuestó a <b>200 estudiantes</b> sobre cómo llegan al liceo: <b>Metro 80</b>, <b>micro 60</b>, <b>a pie 40</b> y <b>bicicleta 20</b>. ¿Qué porcentaje <b>no</b> usa ni Metro ni micro?",
  ["30%", "60%", "20%", "70%"], ["30", "60", "20", "70"], 0,
  [r"No usan Metro ni micro los que van a pie o en bicicleta: $$40 + 20 = 60$$", r"Sobre el total: $$\frac{60}{200} = 0{,}3 = 30\%$$"],
  r"Responder 60 (la cantidad de estudiantes, no el porcentaje, marcar B) o calcular el porcentaje de los que sí usan Metro o micro (D).",
  r"Porcentaje = $\dfrac{\text{parte}}{\text{total}} \cdot 100$. Lee si te piden cantidad o porcentaje.",
  "datos = {'metro': 80, 'micro': 60, 'pie': 40, 'bici': 20}; total = sum(datos.values()); assert total == 200; respuesta = Rational(datos['pie'] + datos['bici'], total)*100",
  [(["Ni Metro ni micro", r"$40 + 20 = 60$"], "Los que no usan ni Metro ni micro son los que van a pie o en bicicleta: sesenta."),
   (["Porcentaje", r"$\dfrac{60}{200} = 30\%$"], "Sesenta de doscientos es el treinta por ciento.")],
  "treinta por ciento", "Primero identifica la parte, después divide por el total. Sesenta es la cantidad de estudiantes, y setenta por ciento es justo lo contrario de lo que te preguntan."))

L.append(P("M1", E, "Rango intercuartílico", "¿Qué tan dispersos? 📊",
  r"En un ensayo PAES, los puntajes de un curso tienen <b>mínimo 410</b>, <b>Q1 = 520</b>, <b>mediana 610</b>, <b>Q3 = 700</b> y <b>máximo 850</b>. ¿Cuál es el <b>rango intercuartílico</b>?",
  ["180", "440", "90", "610"], ["180", "440", "90", "610"], 0,
  [r"El rango intercuartílico es la diferencia entre el tercer y el primer cuartil: $$RIC = Q_3 - Q_1$$", r"$$RIC = 700 - 520 = 180$$"],
  r"Calcular el rango, $850 - 410 = 440$ (marcar B), o restar $Q_3$ menos la mediana (C).",
  r"<b>Rango</b> = máximo − mínimo. <b>Rango intercuartílico</b> = $Q_3 - Q_1$: mide la dispersión del 50% central.",
  "Q1, Q3 = 520, 700; respuesta = Integer(Q3 - Q1)",
  [(["Tercer menos primer cuartil", r"$RIC = Q_3 - Q_1$"], "El rango intercuartílico es el tercer cuartil menos el primero."),
   (["Reemplazamos", r"$700 - 520 = 180$"], "Setecientos menos quinientos veinte: ciento ochenta puntos.")],
  "ciento ochenta", "No lo confundas con el rango, que es máximo menos mínimo y aquí da cuatrocientos cuarenta. El intercuartílico solo mira la mitad central, por eso no le afectan los puntajes extremos."))

# ======================= M2
L.append(P("M2", N, "Logaritmos: escala de pH", "¿Qué tan ácido es el limón? 🍋",
  r"El pH se define como $\text{pH} = -\log[H^+]$. El jugo de limón tiene <b>pH 2</b> y el jugo de tomate, <b>pH 4</b>. ¿Cuántas veces <b>mayor</b> es la concentración $[H^+]$ del limón que la del tomate?",
  ["100", "2", "20", "1.000"], ["100", "2", "20", "1000"], 0,
  [r"Despejando: $[H^+] = 10^{-\text{pH}}$, así que $$\text{limón: } 10^{-2},\quad \text{tomate: } 10^{-4}$$", r"$$\frac{10^{-2}}{10^{-4}} = 10^{2} = 100$$"],
  r"Restar o dividir los pH ($4 - 2$ o $4 : 2$) y marcar B, sin pasar a potencias de 10.",
  r"En escalas logarítmicas (pH, Richter, decibeles), <b>cada unidad es un factor 10</b>: $n$ unidades de diferencia son $10^n$ veces.",
  "limon, tomate = Integer(10)**(-2), Integer(10)**(-4); assert -log(limon, 10) == 2; respuesta = limon/tomate",
  [(["Despejamos la concentración", r"$[H^+] = 10^{-\text{pH}}$"], "Si el pH es menos el logaritmo, la concentración es diez elevado a menos el pH."),
   (["Comparamos", r"$\dfrac{10^{-2}}{10^{-4}} = 100$"], "Diez a la menos dos dividido por diez a la menos cuatro es diez al cuadrado: cien.")],
  "cien veces", "En escalas logarítmicas cada unidad multiplica por diez, así que dos unidades de diferencia son cien veces. Si restas los pH te queda dos, y te olvidas de que la escala es logarítmica."))

L.append(P("M2", G, "Tangente en contexto: altura de una antena", "La antena del cerro 📡",
  r"Desde un punto ubicado a <b>30 m</b> de la base de una antena, se ve su punta con un ángulo de elevación $\alpha$ tal que $\tan\alpha = 1{,}2$. ¿Cuál es la <b>altura</b> de la antena?",
  ["36 m", "25 m", "31,2 m", "3,6 m"], ["36", "25", "156/5", "18/5"], 0,
  [r"La altura es el cateto <b>opuesto</b> y los 30 m son el cateto <b>adyacente</b>: $$\tan\alpha = \frac{h}{30}$$", r"$$h = 30 \cdot 1{,}2 = 36 \text{ m}$$"],
  r"Dividir $30 : 1{,}2 = 25$ y marcar B, o sumar $30 + 1{,}2$ (C).",
  r"$\tan\alpha = \dfrac{\text{opuesto}}{\text{adyacente}}$: sirve cuando conoces la distancia horizontal y buscas una altura.",
  "h = symbols('h'); respuesta = solve(Eq(h/30, Rational(6, 5)), h)[0]",
  [(["Opuesto sobre adyacente", r"$\tan\alpha = \dfrac{h}{30}$"], "La altura es el cateto opuesto al ángulo, y los treinta metros son el adyacente."),
   (["Despejamos", r"$h = 30 \cdot 1{,}2 = 36$"], "Treinta por uno coma dos: treinta y seis metros.")],
  "treinta y seis metros", "Con distancia horizontal y altura, la razón que manda es la tangente. Si divides en vez de multiplicar te sale veinticinco, y con una tangente mayor que uno la altura tiene que ser mayor que la distancia."))

L.append(P("M2", E, "Probabilidad con combinaciones: sorteo", "¿Le achuntas al sorteo? 🎟️",
  r"En un sorteo del curso se eligen al azar <b>2 números distintos</b> del 1 al 10, sin importar el orden. Si Ignacio apostó por un par de números, ¿cuál es la probabilidad de que <b>acierte los dos</b>?",
  [r"$\dfrac{1}{45}$", r"$\dfrac{1}{90}$", r"$\dfrac{1}{100}$", r"$\dfrac{1}{5}$"], ["1/45", "1/90", "1/100", "1/5"], 0,
  [r"Como no importa el orden, los pares posibles son $$\binom{10}{2} = \frac{10 \cdot 9}{2} = 45$$", r"Solo uno es el de Ignacio: $$P = \frac{1}{45}$$"],
  r"Contar con orden, $10 \cdot 9 = 90$ pares (marcar B), o permitir números repetidos, $10 \cdot 10$ (C).",
  r"Si el orden <b>no</b> importa, se usan combinaciones: $\binom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$.",
  "from itertools import combinations; casos = list(combinations(range(1, 11), 2)); respuesta = Rational(1, len(casos))",
  [(["Pares sin orden", r"$\dbinom{10}{2} = 45$"], "Como no importa el orden, contamos combinaciones de diez en dos: cuarenta y cinco pares."),
   (["Un solo par gana", r"$P = \dfrac{1}{45}$"], "Ignacio tiene uno de esos pares: la probabilidad es uno partido en cuarenta y cinco.")],
  "uno partido en cuarenta y cinco", "Si el orden no importa, usa combinaciones. Contar diez por nueve es contar el tres-siete distinto del siete-tres, y ahí cuentas cada par dos veces."))

L.append(P("M2", A, "Intersección de rectas: planes de gimnasio", "¿Qué plan conviene? 🏋️",
  r"El gimnasio A cobra <b>\$15.000</b> de matrícula más <b>\$3.000</b> por clase: $y = 15.000 + 3.000x$. El gimnasio B no cobra matrícula y cobra <b>\$6.000</b> por clase: $y = 6.000x$. ¿Con cuántas clases <b>cuestan lo mismo</b>?",
  ["5", r"2,5", r"$\dfrac{5}{3}$", "10"], ["5", "5/2", "5/3", "10"], 0,
  [r"Las rectas se cortan donde los costos son iguales: $$15.000 + 3.000x = 6.000x$$", r"$$15.000 = 3.000x \Rightarrow x = 5$$"],
  r"Dividir $15.000 : 6.000 = 2{,}5$ (marcar B) o sumar las tarifas, $15.000 : 9.000$ (C).",
  r"El punto de intersección de dos rectas se obtiene <b>igualando sus ecuaciones</b>.",
  "x, y = symbols('x y'); sol = solve([Eq(y, 15000 + 3000*x), Eq(y, 6000*x)], [x, y]); respuesta = sol[x]",
  [(["Igualamos", r"$15.000 + 3.000x = 6.000x$"], "Los dos planes cuestan lo mismo donde las rectas se cortan. Igualamos."),
   (["Despejamos", r"$15.000 = 3.000x \Rightarrow x = 5$"], "Restamos tres mil equis: quince mil igual a tres mil equis. Equis vale cinco clases.")],
  "cinco clases", "Para encontrar dónde se cortan dos rectas, iguala las ecuaciones. Con cinco clases ambos cuestan treinta mil; con más clases conviene el gimnasio A."))

L.append(P("M2", E, "Variable aleatoria: tabla de probabilidades", "Completa la tabla 🎲",
  r"Una variable aleatoria $X$ toma los valores 0, 1, 2 y 3 con probabilidades <b>0,1</b>, <b>0,3</b>, $k$ y <b>0,2</b>, respectivamente. ¿Cuál es $P(X \ge 2)$?",
  ["0,6", "0,4", "0,2", "0,9"], ["3/5", "2/5", "1/5", "9/10"], 0,
  [r"Las probabilidades suman 1: $$0{,}1 + 0{,}3 + k + 0{,}2 = 1 \Rightarrow k = 0{,}4$$", r"$$P(X \ge 2) = P(X = 2) + P(X = 3) = 0{,}4 + 0{,}2 = 0{,}6$$"],
  r"Responder solo $k = 0{,}4$ (marcar B) o solo $P(X = 3) = 0{,}2$ (C).",
  r"En toda distribución de probabilidad, las probabilidades de todos los valores <b>suman 1</b>.",
  "k = symbols('k'); kv = solve(Eq(Rational(1,10) + Rational(3,10) + k + Rational(2,10), 1), k)[0]; respuesta = kv + Rational(2, 10)",
  [(["Todo suma uno", r"$0{,}6 + k = 1 \Rightarrow k = 0{,}4$"], "Las probabilidades suman uno. Cero coma uno, más cero coma tres, más cero coma dos es cero coma seis, así que ka es cero coma cuatro."),
   (["Mayor o igual a dos", r"$0{,}4 + 0{,}2 = 0{,}6$"], "Mayor o igual a dos incluye el dos y el tres: cero coma seis.")],
  "cero coma seis", "Primero encuentra el dato que falta usando que todo suma uno. Después lee bien: mayor o igual a dos incluye el dos."))

L.append(P("M2", E, "Binomial: al menos un acierto", "Respondiendo al azar 🍀",
  r"Benja responde <b>al azar</b> 3 preguntas de 4 alternativas cada una (una correcta). ¿Cuál es la probabilidad de que acierte <b>al menos una</b>?",
  [r"$\dfrac{37}{64}$", r"$\dfrac{3}{4}$", r"$\dfrac{27}{64}$", r"$\dfrac{1}{64}$"], ["37/64", "3/4", "27/64", "1/64"], 0,
  [r"Es más fácil usar el complemento: la probabilidad de <b>no acertar ninguna</b> es $$\left(\frac{3}{4}\right)^3 = \frac{27}{64}$$", r"$$P = 1 - \frac{27}{64} = \frac{37}{64}$$"],
  r"Sumar $\tfrac{1}{4}$ tres veces y marcar B, o quedarse con la probabilidad de no acertar ninguna (C).",
  r"«Al menos uno» se calcula casi siempre como $1 - P(\text{ninguno})$.",
  "n, p = 3, Rational(1, 4); respuesta = sum(binomial(n, j)*p**j*(1 - p)**(n - j) for j in range(1, n + 1))",
  [(["Ninguna correcta", r"$\left(\dfrac{3}{4}\right)^3 = \dfrac{27}{64}$"], "Usamos el complemento. Fallar una es tres cuartos, y fallar las tres es tres cuartos al cubo: veintisiete sesenta y cuatroavos."),
   (["Al menos una", r"$1 - \dfrac{27}{64} = \dfrac{37}{64}$"], "Al menos una es uno menos eso: treinta y siete sesenta y cuatroavos.")],
  "treinta y siete sesenta y cuatroavos", "Al menos uno es uno menos la probabilidad de ninguno. Sumar un cuarto tres veces no funciona: con cuatro preguntas te daría uno, y adivinar no te asegura nada."))
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


rnd = random.Random(20261116)
metas = [i % 4 for i in range(len(L))]; rnd.shuffle(metas)
lote = [finalizar(p, rnd, metas[i]) for i, p in enumerate(L)]
json.dump(lote, open(os.path.join(AQUI, "lote_2026-11-16.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(lote), "problemas")
