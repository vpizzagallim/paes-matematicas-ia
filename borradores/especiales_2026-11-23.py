# Videos especiales del 23-nov-2026 (sketch con musica de payaso, dato util y cuenta regresiva).
# Orden de publicacion: cuenta (332), sketch (336), dato (340), cuenta (344), sketch (348), cuenta (352), dato (356), sketch (360), dato (364), sketch (368), dato (372).
import json, os
AQUI = os.path.dirname(os.path.abspath(__file__))
H = "#PAES #PAES2027 #PAESMatematica #Matematica #Chile #ProfePi"
PROFE = {"fondo": "aula", "personaje": "profe", "expresion": "feliz", "entrada": "derecha",
         "cartel": "¿Lo sacas en 15 segundos? 🧠", "t_cartel": 0.9, "y_cartel": 700}


def prob(nivel, enunciado, alts, valores, correcta, verif, pasos, cierre):
    return {"nivel": nivel, "enunciado": enunciado, "alternativas": alts, "valores": valores, "correcta": correcta,
            "verificacion": verif,
            "pizarra": {"pasos": [{"lineas": l, "voz": v} for l, v in pasos], "cierre": {"voz": cierre}}}


def sketch(texto, escenas, problema):
    return {"formato": "sketch", "musica": "payaso", "texto_post": texto, "escenas": escenas, "problema": problema}


def dato(texto, cartel, subtitulo, intro, titulo, pasos, remate, cierre):
    return {"formato": "dato", "musica": "rock", "texto_post": texto,
            "pizarra_dato": {"cartel": cartel, "subtitulo": subtitulo, "intro_voz": intro, "titulo": titulo,
                             "pasos": [{"lineas": l, "voz": v} for l, v in pasos], "remate": remate, "cierre": {"voz": cierre}}}


def cuenta(texto, intro, titulo, pasos, remate, cierre):
    return {"formato": "cuenta", "musica": "rock", "texto_post": texto,
            "pizarra_dato": {"subtitulo": "Tip del día 👇", "intro_voz": intro, "titulo": titulo,
                             "pasos": [{"lineas": l, "voz": v} for l, v in pasos], "remate": remate, "cierre": {"voz": cierre}}}



S, D, C = [], [], []

# ---------------- SKETCHES
S.append(sketch(f"Grupo de estudio = 5 amigos y 3 pizzas 🍕📚 ¿Cuántos trozos sobran si todos comen lo mismo? {H} #GrupoDeEstudio #Pizza",
  [{"fondo": "aula", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "¡Grupo de estudio en mi casa! Somos cinco y pedí tres pizzas.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "aula", "personaje": "benja", "expresion": "sorpresa", "cartel": "🍕 3 pizzas × 8 trozos<br>👥 5 amigos, todos comen lo mismo", "efecto": "redoble", "t_cartel": 0.1, "dur_min": 2.4},
   {"fondo": "aula", "personaje": "benja", "expresion": "nervioso", "voz": "Estudiamos cero minutos, pero la pizza la repartimos perfecto… creo.", "efecto": "trombon", "sacudir": True},
   dict(PROFE, voz="Benja, al menos la división te tiene que salir bien. ¿Cuántos trozos sobran?")],
  prob("M1", "Benja pide <b>3 pizzas</b> de <b>8 trozos</b> cada una para <b>5 amigos</b>. Si cada uno come la <b>misma cantidad</b> de trozos enteros, la mayor posible, ¿cuántos trozos <b>sobran</b>?",
       ["0", "4", r"4,8", "1"], ["0", "4", "24/5", "1"], 1,
       "total = 3*8; respuesta = Integer(total % 5)",
       [(["Total de trozos", r"$3 \cdot 8 = 24$"], "Tres pizzas de ocho trozos: veinticuatro trozos."),
        (["Repartimos", r"$24 = 5 \cdot 4 + 4$"], "Cada uno come cuatro trozos, que son veinte, y sobran cuatro.")],
       "La respuesta es la be: sobran cuatro trozos. Y esos cuatro se los come Benja mientras «repasa».")))

S.append(sketch(f"Benja ahorra para unas zapatillas 👟💸 ¿Cuántos días le faltan con el 20% de descuento? {H} #Ahorro #Porcentajes",
  [{"fondo": "pieza", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Voy a ahorrar mil quinientos diarios para mis zapatillas.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "pieza", "personaje": "benja", "expresion": "sorpresa", "cartel": "👟 \\$39.990<br>🔥 ¡20% de descuento!", "efecto": "redoble", "t_cartel": 0.1, "dur_min": 2.4},
   {"fondo": "pieza", "personaje": "benja", "expresion": "nervioso", "voz": "¿Y ahora cuántos días me faltan?", "efecto": "tictac"},
   dict(PROFE, voz="Primero el descuento, Benja. ¿Cuántos días necesitas?")],
  prob("M1", "Unas zapatillas cuestan <b>\\$39.990</b> y tienen <b>20% de descuento</b>. Si Benja ahorra <b>\\$1.500 diarios</b>, ¿cuál es la <b>menor</b> cantidad de días que necesita para comprarlas?",
       ["21", "22", "27", "26"], ["21", "22", "27", "26"], 1,
       "precio = Rational(39990)*Rational(80, 100); d = 0\nwhile d*1500 < precio: d += 1\nrespuesta = Integer(d)",
       [(["Precio con descuento", r"$39.990 \cdot 0{,}8 = 31.992$"], "Con descuento se paga el ochenta por ciento: treinta y un mil novecientos noventa y dos."),
        (["Días de ahorro", r"$31.992 : 1.500 \approx 21{,}3 \Rightarrow 22$"], "Dividido en mil quinientos da veintiuno coma tres. Con veintiún días no alcanza.")],
       "La respuesta es la be: veintidós días. Aquí se redondea hacia arriba.")))

S.append(sketch(f"«Solo un capítulo y me duermo» 📺😴 Benja empezó a las 21:00. ¿A qué hora terminó? {H} #Series #Maraton",
  [{"fondo": "pieza", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Veo un capítulo de mi serie y me acuesto temprano. Mañana hay ensayo.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "pieza", "personaje": "benja", "expresion": "sorpresa", "cartel": "📺 «¿Sigues viendo?»<br>8 capítulos de 45 min", "efecto": "redoble", "t_cartel": 0.1, "dur_min": 2.4},
   {"fondo": "pieza", "personaje": "benja", "expresion": "llora", "voz": "¡¿Ya está saliendo el sol?!", "efecto": "trombon", "sacudir": True},
   dict(PROFE, voz="Benja, calcula a qué hora terminaste, y la próxima vez apaga la tele.")],
  prob("M1", "Benja empieza a ver una serie a las <b>21:00</b> y ve <b>8 capítulos</b> de <b>45 minutos</b> cada uno, sin pausas. ¿A qué hora termina?",
       ["02:00", "03:00", "04:00", "05:00"], ["2", "3", "4", "5"], 1,
       "minutos = 21*60 + 8*45; respuesta = Integer((minutos // 60) % 24)",
       [(["Tiempo total", r"$8 \cdot 45 = 360 \text{ min} = 6 \text{ h}$"], "Ocho capítulos de cuarenta y cinco minutos son trescientos sesenta minutos: seis horas."),
        (["Sumamos", r"$21{:}00 + 6 \text{ h} = 03{:}00$"], "Nueve de la noche más seis horas: las tres de la madrugada.")],
       "La respuesta es la be: a las tres de la mañana. Ese era el capítulo uno, Benja.")))

S.append(sketch(f"Benja imprimió las guías en el negocio de la esquina 🖨️ ¿Cuánto vuelto le dieron? {H} #Guias #Vuelto",
  [{"fondo": "aula", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Hoy sí que estudio. Voy a imprimir tres guías de matemática.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "aula", "personaje": "benja", "expresion": "sorpresa", "cartel": "🖨️ 3 guías × 18 páginas<br>\\$50 por página · paga con \\$5.000", "efecto": "redoble", "t_cartel": 0.1, "dur_min": 2.4},
   {"fondo": "aula", "personaje": "benja", "expresion": "nervioso", "voz": "Me dieron el vuelto y ni lo conté. ¿Me lo habrán dado bien?", "efecto": "bocina"},
   dict(PROFE, voz="Cuéntalo, Benja. ¿Cuánto vuelto te tenían que dar?")],
  prob("M1", "Benja imprime <b>3 guías</b> de <b>18 páginas</b> cada una, a <b>\\$50 por página</b>. Si paga con <b>\\$5.000</b>, ¿cuánto <b>vuelto</b> recibe?",
       ["\\$2.300", "\\$4.100", "\\$2.700", "\\$4.850"], ["2300", "4100", "2700", "4850"], 0,
       "paginas = 3*18; respuesta = Integer(5000 - 50*paginas)",
       [(["Páginas y costo", r"$3 \cdot 18 \cdot 50 = 2.700$"], "Tres guías de dieciocho páginas son cincuenta y cuatro páginas. A cincuenta pesos: dos mil setecientos."),
        (["Vuelto", r"$5.000 - 2.700 = 2.300$"], "Cinco mil menos dos mil setecientos: dos mil trescientos de vuelto.")],
       "La respuesta es la a: dos mil trescientos pesos. Ahora solo falta que lea las guías.")))

# ---------------- DATOS
D.append(dato(f"💡 Truco: multiplicar por 11 de cabeza en 2 segundos 🤯 Guárdalo 📌 {H} #CalculoMental #TipsPAES",
  "💡 TRUCO PAES", "Por 11 sin calculadora", "Truco PAES: multiplicar un número de dos cifras por once, en dos segundos.", "Multiplicar por 11",
  [(["Ejemplo", r"$23 \cdot 11 = \ ?$"], "Tomamos veintitrés por once."),
   (["Separa y suma", r"$2 \ \_\ 3 \quad 2 + 3 = 5$"], "Separa las cifras, el dos y el tres, y pon al medio su suma: cinco."),
   (["Listo", r"$23 \cdot 11 = 253$"], "Queda doscientos cincuenta y tres. Si la suma pasa de nueve, llevas uno a la primera cifra.")],
  "ab · 11 → a (a+b) b", "Prueba con setenta y cuatro: siete más cuatro es once, llevas uno, y queda ochocientos catorce. Sigue a math paes punto c, ele."))

D.append(dato(f"💡 Dato: dividir por 0,5 es multiplicar por 2 🤯 Y dividir por 0,25 es multiplicar por 4. Guárdalo 📌 {H} #Decimales #TipsPAES",
  "💡 DATO PAES", "Dividir por un decimal", "Dato PAES: dividir por cero coma cinco no achica el número, lo duplica.", "Dividir por 0,5 y por 0,25",
  [(["Cero coma cinco es un medio", r"$0{,}5 = \dfrac{1}{2}$"], "Cero coma cinco es lo mismo que un medio."),
   (["Dividir por un medio", r"$8 : 0{,}5 = 8 \cdot 2 = 16$"], "Y dividir por un medio es multiplicar por dos. Ocho dividido en cero coma cinco es dieciséis."),
   (["Con un cuarto", r"$8 : 0{,}25 = 8 \cdot 4 = 32$"], "Lo mismo con cero coma dos cinco, que es un cuarto: se multiplica por cuatro.")],
  "÷ 0,5 = × 2 · ÷ 0,25 = × 4", "Dividir por un número menor que uno siempre agranda el resultado. Si te achicó, revisa. Sigue a math paes punto c, ele."))

D.append(dato(f"💡 Dato: ¿descuento y después IVA, o al revés? Da lo mismo 🤯 Guárdalo 📌 {H} #Porcentajes #TipsPAES",
  "💡 DATO PAES", "Descuento e IVA", "Dato PAES: ¿qué conviene, aplicar primero el descuento o primero el IVA?", "El orden no importa",
  [(["Descuento de 20%", r"$\times\, 0{,}8$"], "Un descuento de veinte por ciento es multiplicar por cero coma ocho."),
   (["IVA de 19%", r"$\times\, 1{,}19$"], "Agregar el diecinueve por ciento de IVA es multiplicar por uno coma uno nueve."),
   (["Mismo resultado", r"$P \cdot 0{,}8 \cdot 1{,}19 = P \cdot 1{,}19 \cdot 0{,}8$"], "Como la multiplicación es conmutativa, el orden no cambia el precio final.")],
  "Porcentajes sucesivos = factores que se multiplican", "Pero ojo: un veinte por ciento menos y un diecinueve por ciento más no es un uno por ciento menos. Se multiplican, no se restan. Sigue a math paes punto c, ele."))

D.append(dato(f"💡 Truco: el promedio de datos que suben de a parejo, en 3 segundos 🤯 Guárdalo 📌 {H} #Promedio #TipsPAES",
  "💡 TRUCO PAES", "Promedio en 3 segundos", "Truco PAES: sacar el promedio de muchos datos sin sumarlos todos.", "Datos que suben parejo",
  [(["Ejemplo", r"$12,\ 15,\ 18,\ 21,\ 24$"], "Estos datos suben de tres en tres."),
   (["Primero más último", r"$\dfrac{12 + 24}{2} = 18$"], "Cuando suben siempre lo mismo, el promedio es el primero más el último, dividido en dos: dieciocho."),
   (["¿Por qué?", r"$12 + 24 = 15 + 21 = 18 + 18$"], "Porque los datos se emparejan desde las puntas y todos los pares suman lo mismo.")],
  "Si suben parejo: media = (primero + último) : 2", "Y en ese caso la media es igual a la mediana. Sigue a math paes punto c, ele."))

# ---------------- CUENTA REGRESIVA
C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: esta semana repasa, no aprendas materia nueva 📚 {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: en la última semana, repasa lo que ya sabes.", "Tip: repasa lo que sabes",
  [(["Nada de materia nueva"], "A pocos días, aprender materia nueva desde cero suele generar más nervios que puntos."),
   (["Asegura lo que ya sabes"], "Repasa los temas que ya dominas y los errores que ya cometiste en tus ensayos."),
   (["Ejercicios cortos"], "Haz ejercicios cortos todos los días para mantener la mano.")],
  "Repasa, no empieces de cero ✅", "Lo que ya sabes también hay que cuidarlo. Sigue a math paes punto c, ele."))

C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: subraya las palabras clave del enunciado ✍️ {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: subraya las palabras clave de cada enunciado.", "Tip: palabras clave",
  [(["Busca el «no»"], "Palabras como «no», «excepto» o «siempre» cambian por completo la pregunta."),
   (["¿Qué te piden?"], "Subraya lo que te piden: no es lo mismo el precio final que el descuento."),
   (["Revisa al final"], "Antes de marcar, vuelve a leer la pregunta y confirma que respondiste eso.")],
  "Subraya lo clave ✅", "Leer bien también es matemática. Sigue a math paes punto c, ele."))

C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: estima antes de marcar 🎯 {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: antes de marcar, pregúntate si el resultado tiene sentido.", "Tip: ¿tiene sentido?",
  [(["Estima el tamaño"], "Antes de calcular, piensa más o menos cuánto debería dar."),
   (["Compara con la realidad"], "Una probabilidad no pasa de uno, y un descuento no puede subir el precio."),
   (["Si no cuadra, revisa"], "Si tu resultado es absurdo, busca el error antes de marcar.")],
  "Si no tiene sentido, revisa ✅", "Un resultado raro es una alarma, no una alternativa. Sigue a math paes punto c, ele."))

E = [C[0], S[0], D[0], C[1], S[1], C[2], D[1], S[2], D[2], S[3], D[3]]
for k, e in enumerate(E, 1):
    e["tipo"] = "especial"; e["uid"] = f"s1123-{k:02d}"
json.dump(E, open(os.path.join(AQUI, "especiales_2026-11-23.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(E), "especiales")
