# Videos especiales del 02-nov-2026 (sketch con musica de payaso, dato util y cuenta regresiva).
# Orden de publicacion: sketch, dato, cuenta, sketch, dato, cuenta... (19 en total).
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
S.append(sketch(f"Benja pasó una hora en la micro mirando el techo 🚌😐 ¿Y si repasa en el camino? {H} #Micro",
  [{"fondo": "pieza", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Hoy no alcancé a estudiar. Estuve una hora en la micro.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "pieza", "personaje": "benja", "expresion": "sorpresa", "cartel": "🚌 1 hora en micro<br>= 1 hora mirando el techo", "efecto": "bocina", "t_cartel": 0.1, "sacudir": True, "dur_min": 2.2},
   {"fondo": "pieza", "personaje": "benja", "expresion": "llora", "voz": "Y el celular con cero batería.", "efecto": "trombon"},
   dict(PROFE, voz="¿Y si repasas quince minutos en cada viaje? Calcula.")],
  prob("M1", "Si repasas <b>15 minutos</b> en cada viaje, de ida y de vuelta, durante <b>5 días</b>, ¿cuántas <b>horas</b> repasas en total?",
       ["1,25 horas", "2,5 horas", "1,5 horas", "75 horas"], ["5/4", "5/2", "3/2", "75"], 1,
       "respuesta = Rational(15*2*5, 60)",
       [(["Minutos totales", r"$15 \cdot 2 \cdot 5 = 150\ \text{min}$"], "Quince minutos, dos viajes al día, cinco días: ciento cincuenta minutos."),
        (["A horas", r"$150 \div 60 = 2{,}5\ \text{h}$"], "Ciento cincuenta minutos son dos horas y media.")],
       "La respuesta es la be: dos coma cinco horas. El tiempo muerto también sirve para estudiar.")))

S.append(sketch(f"Benja invitó a todos a completos… y no sacó la cuenta 🌭💸 ¿Le alcanza con $10.000? {H} #CalculoMental",
  [{"fondo": "aula", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "¡Invito yo! Tres completos y dos bebidas.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "aula", "personaje": "benja", "expresion": "sorpresa", "cartel": "🌭 Completo $2.500 · Bebida $1.200<br>Tiene $10.000", "efecto": "redoble", "t_cartel": 0.1, "dur_min": 2.4},
   {"fondo": "aula", "personaje": "benja", "expresion": "nervioso", "voz": "Eh… ¿alguien sabe sumar rápido?", "efecto": "tictac"},
   dict(PROFE, voz="Cálculo mental, Benja. ¿Cuánto vuelto te dan?")],
  prob("M1", "Benja compra <b>3 completos</b> a <b>\\$2.500</b> y <b>2 bebidas</b> a <b>\\$1.200</b>. Si paga con <b>\\$10.000</b>, ¿cuánto vuelto recibe?",
       ["\\$1.300", "\\$2.500", "\\$100", "\\$9.900"], ["1300", "2500", "100", "9900"], 2,
       "respuesta = 10000 - (3*2500 + 2*1200)",
       [(["Total de la compra", r"$7.500 + 2.400 = 9.900$"], "Tres completos son siete mil quinientos y dos bebidas, dos mil cuatrocientos. Total: nueve mil novecientos."),
        (["Vuelto", r"$10.000 - 9.900 = 100$"], "Diez mil menos nueve mil novecientos: cien pesos de vuelto.")],
       "La respuesta es la ce: cien pesos. Justo le alcanzó, Benja.")))

S.append(sketch(f"Grupo de estudio: 2 horas… 15 minutos de matemática 🍕😅 ¿Qué porcentaje fue estudio? {H} #GrupoDeEstudio",
  [{"fondo": "aula", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Hicimos grupo de estudio dos horas seguidas.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "aula", "personaje": "benja", "expresion": "sorpresa", "cartel": "🍕 105 min de pizza y conversa<br>📐 15 min de matemática", "efecto": "bocina", "t_cartel": 0.1, "sacudir": True, "dur_min": 2.4},
   {"fondo": "aula", "personaje": "benja", "expresion": "llora", "voz": "Pero la pizza estaba buenísima.", "efecto": "trombon"},
   dict(PROFE, voz="Benja, calcula qué porcentaje fue estudio de verdad.")],
  prob("M1", "De un grupo de estudio de <b>2 horas</b>, solo <b>15 minutos</b> fueron de matemática. ¿Qué <b>porcentaje</b> del tiempo se estudió?",
       ["15%", "7,5%", "12,5%", "25%"], ["15", "15/2", "25/2", "25"], 2,
       "respuesta = Rational(15, 2*60)*100",
       [(["Todo en minutos", r"$2\ \text{h} = 120\ \text{min}$"], "Dos horas son ciento veinte minutos."),
        (["Porcentaje", r"$\dfrac{15}{120} = 0{,}125 = 12{,}5\%$"], "Quince de ciento veinte es cero coma uno dos cinco: doce coma cinco por ciento.")],
       "La respuesta es la ce: doce coma cinco por ciento. Primero la matemática y después la pizza.")))

S.append(sketch(f"Benja compró alfombra para su pieza… usando el perímetro 🧶🤦 ¿Cuánta necesitaba? {H} #Geometria",
  [{"fondo": "pieza", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Mi pieza mide tres por cuatro. Compré catorce metros de alfombra.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "pieza", "personaje": "benja", "expresion": "sorpresa", "cartel": "🧶 Le sobró alfombra<br>¿Área o perímetro?", "efecto": "bocina", "t_cartel": 0.1, "sacudir": True, "dur_min": 2.2},
   {"fondo": "pieza", "personaje": "benja", "expresion": "llora", "voz": "¿Por qué tengo alfombra en el pasillo?", "efecto": "trombon"},
   dict(PROFE, voz="Para cubrir el piso se usa el área, Benja. Mira.")],
  prob("M1", "Una pieza rectangular mide <b>3 m</b> por <b>4 m</b>. ¿Cuántos <b>m²</b> de alfombra se necesitan para cubrir <b>todo el piso</b>?",
       ["14 m²", "7 m²", "24 m²", "12 m²"], ["14", "7", "24", "12"], 3,
       "respuesta = 3*4",
       [(["Cubrir el piso = área", r"$A = 3 \cdot 4$"], "Para cubrir el piso necesitas el área: largo por ancho."),
        (["Calculamos", r"$A = 12\ \text{m}^2$"], "Tres por cuatro: doce metros cuadrados. Catorce era el perímetro, el borde.")],
       "La respuesta es la de: doce metros cuadrados. El área cubre; el perímetro rodea.")))

S.append(sketch(f"Benja: «Con 90% de batería estudio todo el día» 📱🔋 Spoiler: TikTok no opina lo mismo {H} #Bateria",
  [{"fondo": "pieza", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Tengo noventa por ciento de batería. Me alcanza para todo el día.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "pieza", "personaje": "benja", "expresion": "sorpresa", "cartel": "📱 TikTok gasta<br>15% de batería por hora", "efecto": "redoble", "t_cartel": 0.1, "dur_min": 2.2},
   {"fondo": "pieza", "personaje": "benja", "expresion": "llora", "voz": "¿Y dónde quedaron mis apuntes?", "efecto": "trombon"},
   dict(PROFE, voz="Calcula cuánto te dura, Benja.")],
  prob("M1", "Un celular tiene <b>90% de batería</b> y gasta <b>15%</b> por cada hora de uso. ¿Cuántas <b>horas</b> dura hasta quedar en 0%?",
       ["5", "6", "9", "4"], ["5", "6", "9", "4"], 1,
       "h = symbols('h'); respuesta = solve(Eq(90 - 15*h, 0), h)[0]",
       [(["Planteamos", r"$90 - 15h = 0$"], "La batería baja quince por ciento por hora, desde noventa."),
        (["Despejamos", r"$h = \dfrac{90}{15} = 6$"], "Noventa dividido en quince: seis horas.")],
       "La respuesta es la be: seis horas. Y si es de estudio, mejor con el celular lejos.")))

S.append(sketch(f"Benja quiere subir 150 puntos en 5 semanas 📈😰 ¿Cuánto por semana? {H} #MetaPAES",
  [{"fondo": "aula", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Este año saco setecientos cincuenta. Fijo.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "aula", "personaje": "benja", "expresion": "sorpresa", "cartel": "📈 Último ensayo: 600 puntos<br>Quedan 5 semanas", "efecto": "redoble", "t_cartel": 0.1, "dur_min": 2.2},
   {"fondo": "aula", "personaje": "benja", "expresion": "nervioso", "voz": "¿Eso es mucho o poco?", "efecto": "tictac"},
   dict(PROFE, voz="Vamos por partes, Benja. Una meta por semana.")],
  prob("M1", "Benja tiene <b>600 puntos</b> y quiere llegar a <b>750</b> en <b>5 semanas</b>, subiendo lo mismo cada semana. ¿Cuántos puntos debe subir por semana?",
       ["25", "150", "35", "30"], ["25", "150", "35", "30"], 3,
       "respuesta = Rational(750 - 600, 5)",
       [(["Cuánto le falta", r"$750 - 600 = 150$"], "De seiscientos a setecientos cincuenta le faltan ciento cincuenta puntos."),
        (["Por semana", r"$150 \div 5 = 30$"], "Repartidos en cinco semanas: treinta puntos por semana.")],
       "La respuesta es la de: treinta puntos. Una meta grande se logra con metas chicas.")))

S.append(sketch(f"Mamá mandó a Benja a la feria por 750 g de palta 🥑😅 ¿Cuánto le paga al casero? {H} #Feria",
  [{"fondo": "pieza", "personaje": "benja", "expresion": "feliz", "entrada": "caminando", "voz": "Mi mamá me mandó a la feria por tres cuartos de kilo de palta.", "efecto": "boing", "t_efecto": 0.75},
   {"fondo": "pieza", "personaje": "benja", "expresion": "sorpresa", "cartel": "🥑 Palta a $4.000 el kilo<br>Pide 750 g", "efecto": "bocina", "t_cartel": 0.1, "sacudir": True, "dur_min": 2.2},
   {"fondo": "pieza", "personaje": "benja", "expresion": "nervioso", "voz": "¿Y cuánto le pago al casero?", "efecto": "tictac"},
   dict(PROFE, voz="Proporción, Benja. Calcula antes de llegar al puesto.")],
  prob("M1", "La palta cuesta <b>\\$4.000 el kilo</b>. ¿Cuánto se paga por <b>750 gramos</b>?",
       ["\\$3.000", "\\$3.250", "\\$2.000", "\\$750"], ["3000", "3250", "2000", "750"], 0,
       "respuesta = Rational(4000, 1000)*750",
       [(["750 g son 3/4 de kilo", r"$\dfrac{750}{1.000} = \dfrac{3}{4}$"], "Setecientos cincuenta gramos son tres cuartos de kilo."),
        (["Tres cuartos del precio", r"$4.000 \cdot \dfrac{3}{4} = 3.000$"], "Tres cuartos de cuatro mil: tres mil pesos.")],
       "La respuesta es la a: tres mil pesos. Y no olvides la yapa.")))

# ---------------- DATOS UTILES
D.append(dato(f"💡 Truco: multiplicar por 5 sin calculadora en 2 segundos ✋ Guárdalo 📌 {H} #CalculoMental #TipsPAES",
  "💡 TRUCO PAES", "Multiplicar por 5 al toque", "Truco PAES: multiplicar por cinco en dos segundos, sin calculadora.", "Por 5 = por 10 ÷ 2",
  [(["Multiplica por 10", r"$48 \cdot 10 = 480$"], "Multiplicar por cinco es lo mismo que multiplicar por diez y sacar la mitad. Cuarenta y ocho por diez, cuatrocientos ochenta."),
   (["Saca la mitad", r"$480 \div 2 = 240$"], "La mitad de cuatrocientos ochenta es doscientos cuarenta. Listo: cuarenta y ocho por cinco es doscientos cuarenta."),
   (["Sirve con decimales", r"$3{,}6 \cdot 5 = 36 \div 2 = 18$"], "Con decimales también: tres coma seis por diez es treinta y seis, y la mitad, dieciocho.")],
  "× 5 = × 10 ÷ 2", "Y para dividir por cinco, haz lo contrario: divide por diez y multiplica por dos."))

D.append(dato(f"💡 (a + b)² NO es a² + b² 😱 El error de álgebra más común de la PAES. Guárdalo 📌 {H} #Algebra #TipsPAES",
  "💡 DATO PAES", "Cuadrado de binomio", "Dato PAES: el error de álgebra que más puntos quita.", "Cuadrado de binomio",
  [(["No es la suma de cuadrados", r"$(a + b)^2 \neq a^2 + b^2$"], "Un binomio al cuadrado no es la suma de los cuadrados. Ese es el error más común."),
   (["Falta el doble producto", r"$(a + b)^2 = a^2 + 2ab + b^2$"], "Es el primero al cuadrado, más el doble del primero por el segundo, más el segundo al cuadrado."),
   (["Ejemplo", r"$(x + 3)^2 = x^2 + 6x + 9$"], "Por ejemplo, equis más tres al cuadrado es equis cuadrado, más seis equis, más nueve.")],
  "¡No olvides el 2ab!", "Si dudas, compruébalo con números: dos más tres al cuadrado es veinticinco, no trece."))

D.append(dato(f"💡 Las probabilidades «y» se multiplican, las «o» se suman 🎲 Guárdalo 📌 {H} #Probabilidad #TipsPAES",
  "💡 DATO PAES", "«Y» multiplica, «o» suma", "Dato PAES: cuándo multiplicar y cuándo sumar probabilidades.", "«Y» y «o»",
  [(["«Y» (independientes): multiplica", r"$P(A \text{ y } B) = P(A) \cdot P(B)$"], "Si te piden que ocurra una cosa y también la otra, y son independientes, multiplicas."),
   (["Ej.: dos caras seguidas", r"$\dfrac{1}{2} \cdot \dfrac{1}{2} = \dfrac{1}{4}$"], "Por ejemplo, cara y cara en dos lanzamientos: un medio por un medio, un cuarto."),
   (["«O» (excluyentes): suma", r"$P(1 \text{ o } 2) = \dfrac{1}{6} + \dfrac{1}{6} = \dfrac{1}{3}$"], "Si te piden una cosa o la otra, y no pueden pasar juntas, sumas. Sacar uno o dos en un dado: un tercio.")],
  "Y → × · O → +", "Y si los eventos pueden pasar juntos, recuerda restar la intersección."))

D.append(dato(f"💡 Seno de 30°, 45° y 60° sin memorizar una tabla 🤯 Guárdalo 📌 {H} #Trigonometria #PAESM2 #TipsPAES",
  "💡 TRUCO PAES", "Seno de 30°, 45° y 60°", "Truco PAES para M2: los senos de treinta, cuarenta y cinco y sesenta grados, sin tabla.", "Senos notables",
  [(["Raíces de 1, 2 y 3 sobre 2", r"$\dfrac{\sqrt{1}}{2},\ \dfrac{\sqrt{2}}{2},\ \dfrac{\sqrt{3}}{2}$"], "Escribe raíz de uno, raíz de dos y raíz de tres, todas divididas en dos."),
   (["Senos de 30°, 45°, 60°", r"$\sin 30^\circ = \tfrac{1}{2}$"], "Esos son los senos de treinta, cuarenta y cinco y sesenta grados. Raíz de uno es uno: seno de treinta es un medio."),
   (["El coseno, al revés", r"$\cos 60^\circ = \tfrac{1}{2}$"], "Para el coseno, se leen al revés: coseno de sesenta es un medio, y coseno de treinta, raíz de tres medios.")],
  "√1 · √2 · √3 ÷ 2", "Con eso armas la tangente: seno dividido en coseno."))

D.append(dato(f"💡 Estima antes de calcular y descarta alternativas en segundos ⏱️ Guárdalo 📌 {H} #TipsPAES #Estimacion",
  "💡 TRUCO PAES", "Estima antes de calcular", "Truco PAES: estimar antes de calcular te ahorra tiempo y errores.", "Estimar primero",
  [(["Redondea", r"$19{,}8 \cdot 5{,}1 \approx 20 \cdot 5$"], "Redondea los números a valores cómodos: diecinueve coma ocho es casi veinte, y cinco coma uno es casi cinco."),
   (["Calcula fácil", r"$20 \cdot 5 = 100$"], "Veinte por cinco es cien. El resultado real tiene que estar cerca de cien."),
   (["Descarta lo lejano", r"$\text{Si ves } 10{,}1 \text{ o } 1.010\text{: fuera}$"], "Si una alternativa dice diez o mil, la descartas al tiro, sin calcular.")],
  "Redondea y descarta", "Estimar no reemplaza el cálculo, pero te avisa cuando algo salió mal."))

D.append(dato(f"💡 Leyes de logaritmos en 30 segundos 📈 Las que más salen en M2. Guárdalas 📌 {H} #Logaritmos #PAESM2 #TipsPAES",
  "💡 DATO PAES", "Las 3 leyes de logaritmos", "Dato PAES para M2: las tres leyes de logaritmos que tienes que manejar.", "Leyes de logaritmos",
  [(["Producto: se suman", r"$\log(ab) = \log a + \log b$"], "El logaritmo de un producto es la suma de los logaritmos."),
   (["Cociente: se restan", r"$\log\left(\dfrac{a}{b}\right) = \log a - \log b$"], "El logaritmo de una división es la resta de los logaritmos."),
   (["Potencia: el exponente baja", r"$\log\left(a^n\right) = n \log a$"], "Y el exponente baja multiplicando. Ojo: logaritmo de a más be no tiene fórmula.")],
  "Suma · Resta · Baja", "Repásalas con ejemplos: logaritmo de dos más logaritmo de cinco es logaritmo de diez, o sea uno."))

# ---------------- CUENTA REGRESIVA (solo tips de estudio, sin datos nuevos de la prueba)
C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: arma tu cuaderno de errores ✍️ {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: arma tu cuaderno de errores.", "Tip: tus errores",
  [(["Anota cada ejercicio que fallas"], "Cada vez que te equivoques en un ejercicio, anótalo en un cuaderno aparte."),
   (["Escribe por qué te equivocaste"], "Al lado, escribe por qué: ¿leíste mal, olvidaste una fórmula o fue un error de cálculo?"),
   (["Repásalo el fin de semana"], "El fin de semana, vuelve a resolverlos sin mirar la solución.")],
  "Anota · Entiende · Repite", "Tus errores son tu mejor guía de estudio. Sigue a math paes punto c, ele."))

C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: estudia en bloques cortos ⏱️ {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: estudia en bloques cortos.", "Tip: bloques cortos",
  [(["25 minutos de foco"], "Pon un temporizador de veinticinco minutos y estudia solo matemática, con el celular lejos."),
   (["5 minutos de pausa"], "Después, descansa cinco minutos: párate, toma agua, estira las piernas."),
   (["Repite tres o cuatro veces"], "Repite el ciclo tres o cuatro veces. Rinde más que tres horas a medias.")],
  "25 de foco · 5 de pausa", "Poco y concentrado le gana a mucho y distraído. Sigue a math paes punto c, ele."))

C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: ¿qué te están preguntando? 🔎 {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: antes de calcular, identifica qué te preguntan.", "Tip: la pregunta",
  [(["Lee primero la pregunta final"], "Lee primero la última frase del enunciado: ahí está lo que te piden."),
   (["Anota qué buscas"], "Anota qué buscas: ¿un precio, un porcentaje, un ángulo, una probabilidad?"),
   (["Al final, ¿respondiste eso?"], "Cuando termines, revisa que tu resultado responda exactamente eso.")],
  "¿Qué me piden? ✅", "Muchos puntos se pierden por responder otra cosa. Sigue a math paes punto c, ele."))

C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: haz un dibujo ✏️ {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: si te enredas, haz un dibujo.", "Tip: dibuja",
  [(["Geometría: dibuja la figura"], "En geometría, dibuja la figura y anota las medidas que te dan."),
   (["Probabilidad: una tabla"], "En probabilidad, una tabla o un diagrama de árbol ordena todos los casos."),
   (["Funciones: un bosquejo"], "En funciones, un bosquejo rápido del gráfico te muestra si la respuesta tiene sentido.")],
  "Dibuja · Ordena · Comprueba", "Un dibujo de diez segundos ahorra minutos de confusión. Sigue a math paes punto c, ele."))

C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: prueba las alternativas 🔁 {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: a veces conviene probar las alternativas.", "Tip: prueba",
  [(["Reemplaza en la ecuación"], "Si te piden el valor de equis, puedes reemplazar cada alternativa en la ecuación."),
   (["La que cumple, es"], "La alternativa que hace verdadera la igualdad es la correcta."),
   (["Úsalo para comprobar"], "Y aunque lo hayas resuelto, reemplazar tu respuesta es la mejor forma de comprobarla.")],
  "Reemplaza y comprueba", "Las alternativas también son una herramienta. Sigue a math paes punto c, ele."))

C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: si te bloqueas, respira y sigue 🧘 {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: qué hacer si te bloqueas en una pregunta.", "Tip: no te bloquees",
  [(["Respira hondo tres veces"], "Si te bloqueas, suelta el lápiz y respira hondo tres veces."),
   (["Marca la pregunta y sigue"], "Marca la pregunta y pasa a la siguiente. No te quedes pegado."),
   (["Vuelve con la mente fresca"], "Cuando vuelvas al final, muchas veces la respuesta aparece sola.")],
  "Respira · Marca · Vuelve", "Una pregunta difícil no define tu prueba. Sigue a math paes punto c, ele."))

E = []
for i in range(7):
    E.append(S[i])
    if i < 6:
        E.append(D[i]); E.append(C[i])
for k, e in enumerate(E, 1):
    e["tipo"] = "especial"; e["uid"] = f"s1102-{k:02d}"
json.dump(E, open(os.path.join(AQUI, "especiales_2026-11-02.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(E), "especiales")
