# Videos especiales del 16-nov-2026 (sketch con musica de payaso, dato util y cuenta regresiva).
# Orden de publicacion: sketch (304), dato (308), cuenta (312), sketch (316), dato (320), cuenta (324), sketch (328).
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
S.append(sketch(f"Benja puso la alarma a las 6:30 para estudiar… y apretó «5 minutitos más» 😴⏰ ¿A qué hora se levantó? {H} #Alarma #CalculoMental",
  [{"fondo": "pieza", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Mañana me levanto tempranito a estudiar. Alarma a las seis y media.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "pieza", "personaje": "benja", "expresion": "nervioso", "cartel": "⏰ 6:30 «cinco minutitos más»<br>Posponer: 9 min × 5 veces", "efecto": "tictac", "t_cartel": 0.1, "dur_min": 2.4},
   {"fondo": "pieza", "personaje": "benja", "expresion": "llora", "voz": "¡¿Qué hora es?! ¡Nadie me despertó!", "efecto": "trombon", "sacudir": True},
   dict(PROFE, voz="Benja, la alarma sí te despertó. Calcula a qué hora te levantaste.")],
  prob("M1", "La alarma de Benja suena a las <b>6:30</b>. Cada vez que la pospone, vuelve a sonar <b>9 minutos</b> después. Si la pospone <b>5 veces</b> y se levanta con el último sonido, ¿a qué hora se levanta?",
       ["6:44", "7:15", "7:24", "7:45"], ["404", "435", "444", "465"], 1,
       "inicio = 6*60 + 30; t = inicio\nfor _ in range(5): t += 9\nrespuesta = Integer(t)",
       [(["Minutos de más", r"$5 \cdot 9 = 45\ \text{min}$"], "Cinco veces nueve minutos: cuarenta y cinco minutos de más."),
        (["Sumamos a las 6:30", r"$6{:}30 + 0{:}45 = 7{:}15$"], "Seis y media más cuarenta y cinco minutos: siete y cuarto.")],
       "La respuesta es la be: siete y cuarto. Cinco minutitos más salen caros, Benja.")))

S.append(sketch(f"«Una partidita y estudio» 🎮🔋 La mamá de Benja le quita el celular al 25%. ¿Cuántas horas jugó? {H} #Gamer #FuncionAfin",
  [{"fondo": "pieza", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Una partidita corta y después estudio. Lo prometo.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "pieza", "personaje": "benja", "expresion": "sorpresa", "cartel": "🔋 Parte en 100%<br>Baja 15% por hora de juego", "efecto": "redoble", "t_cartel": 0.1, "dur_min": 2.4},
   {"fondo": "pieza", "personaje": "benja", "expresion": "llora", "voz": "¡Mi mamá me quitó el celular cuando quedó en veinticinco por ciento!", "efecto": "bocina", "sacudir": True},
   dict(PROFE, voz="Tranquilo, Benja. Calcula cuántas horas jugaste.")],
  prob("M1", "La batería del celular de Benja parte en <b>100%</b> y baja <b>15%</b> por cada hora de juego. ¿Después de cuántas horas queda en <b>25%</b>?",
       ["4", r"$\dfrac{5}{3}$", "5", r"$\dfrac{20}{3}$"], ["4", "5/3", "5", "20/3"], 2,
       "h = symbols('h'); respuesta = solve(Eq(100 - 15*h, 25), h)[0]",
       [(["Planteamos", r"$100 - 15h = 25$"], "La batería es cien menos quince por las horas, y queremos que llegue a veinticinco."),
        (["Despejamos", r"$15h = 75 \Rightarrow h = 5$"], "Quince hache es setenta y cinco, así que hache vale cinco horas.")],
       "La respuesta es la ce: cinco horas. Una partidita, dijo.")))

S.append(sketch(f"Benja fue a la feria por «una palta» y volvió con kilo y medio 🥑😅 ¿Cuánto pagó? {H} #Feria #Palta",
  [{"fondo": "aula", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Mi mamá me mandó a la feria a comprar una palta.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "aula", "personaje": "benja", "expresion": "sorpresa", "cartel": "🥑 «¿Le pongo kilo y medio, casero?»<br>Palta: \\$3.800 el kilo", "efecto": "redoble", "t_cartel": 0.1, "dur_min": 2.4},
   {"fondo": "aula", "personaje": "benja", "expresion": "nervioso", "voz": "Le dije que sí… ¿y ahora cuánto le pago?", "efecto": "tictac"},
   dict(PROFE, voz="Precio por kilo por cantidad de kilos, Benja. ¿Cuánto pagas?")],
  prob("M1", "En la feria, la palta cuesta <b>\\$3.800 el kilo</b>. Si Benja compra <b>1,5 kg</b>, ¿cuánto paga?",
       ["\\$5.300", "\\$5.700", "≈ \\$2.533", "\\$57.000"], ["5300", "5700", "7600/3", "57000"], 1,
       "respuesta = Rational(3800) * Rational(3, 2)",
       [(["Un kilo y medio kilo", r"$3.800 + 1.900$"], "Un kilo cuesta tres mil ochocientos y medio kilo, la mitad: mil novecientos."),
        (["Total", r"$3.800 \cdot 1{,}5 = 5.700$"], "Sumados dan cinco mil setecientos pesos.")],
       "La respuesta es la be: cinco mil setecientos pesos. Y la próxima vez, pide por unidad, Benja.")))

# ---------------- DATOS
D.append(dato(f"💡 Truco: el 8% de 50 es lo mismo que el 50% de 8 🤯 Porcentajes reversibles. Guárdalo 📌 {H} #CalculoMental #TipsPAES",
  "💡 TRUCO PAES", "8% de 50 en 2 segundos", "Truco PAES: calcular el ocho por ciento de cincuenta en dos segundos, sin calculadora.", "Porcentajes reversibles",
  [(["¿8% de 50?", r"$\dfrac{8}{100} \cdot 50$"], "El ocho por ciento de cincuenta parece difícil de cabeza."),
   (["Da vuelta los números", r"$50\% \text{ de } 8 = 4$"], "Pero es igual al cincuenta por ciento de ocho, que es la mitad de ocho: cuatro."),
   (["¿Por qué funciona?", r"$\dfrac{a \cdot b}{100} = \dfrac{b \cdot a}{100}$"], "Porque en los dos casos multiplicas los mismos números y divides por cien.")],
  "a% de b = b% de a", "Prueba con el dieciséis por ciento de veinticinco: es el veinticinco por ciento de dieciséis, o sea, cuatro. Sigue a math paes punto c, ele."))

D.append(dato(f"💡 Truco: 35² de cabeza en 3 segundos 🤯 Cuadrados que terminan en 5. Guárdalo 📌 {H} #CalculoMental #TipsPAES",
  "💡 TRUCO PAES", "35² sin calculadora", "Truco PAES: elevar al cuadrado un número que termina en cinco, en tres segundos.", "Cuadrados terminados en 5",
  [(["Termina en 5", r"$35^2 = \ ?$"], "Tomamos treinta y cinco al cuadrado."),
   (["Multiplica por el siguiente", r"$3 \cdot 4 = 12$"], "Toma el tres y multiplícalo por el número que le sigue, el cuatro: doce."),
   (["Pega un 25 al final", r"$35^2 = 1.225$"], "Al final siempre va veinticinco. Doce y veinticinco: mil doscientos veinticinco.")],
  "Termina en 5: n · (n + 1) y pega 25", "Prueba con sesenta y cinco: seis por siete, cuarenta y dos, y pegas veinticinco: cuatro mil doscientos veinticinco. Sigue a math paes punto c, ele."))

# ---------------- CUENTA REGRESIVA
C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: planifica cómo llegar 🗺️ {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: planifica cómo vas a llegar a rendir la prueba.", "Tip: el trayecto",
  [(["¿Dónde rindes?"], "Revisa con tiempo dónde te toca rendir, no la noche anterior."),
   (["Prueba el recorrido"], "Si puedes, haz el trayecto antes, a la misma hora, para saber cuánto demoras."),
   (["Sal con margen"], "Ese día sal con tiempo de sobra. Llegar corriendo te quita la calma.")],
  "Planifica el trayecto ✅", "Llegar tranquilo también suma puntos. Sigue a math paes punto c, ele."))

C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: lee las 4 alternativas antes de marcar 👀 {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: lee todas las alternativas antes de marcar.", "Tip: las alternativas",
  [(["Lee las cuatro"], "Aunque creas tener la respuesta, lee las cuatro alternativas antes de marcar."),
   (["¿No aparece tu resultado?"], "Si tu resultado no está, revisa signos, unidades y qué te preguntaban."),
   (["Ojo con las parecidas"], "Las alternativas incorrectas suelen salir de errores típicos, por eso a veces parecen correctas.")],
  "Lee las 4 alternativas ✅", "Un segundo de revisión vale más que un punto perdido. Sigue a math paes punto c, ele."))

E = [S[0], D[0], C[0], S[1], D[1], C[1], S[2]]
for k, e in enumerate(E, 1):
    e["tipo"] = "especial"; e["uid"] = f"s1116-{k:02d}"
json.dump(E, open(os.path.join(AQUI, "especiales_2026-11-16.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(E), "especiales")
