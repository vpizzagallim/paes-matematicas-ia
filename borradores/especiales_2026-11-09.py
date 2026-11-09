# Videos especiales del 09-nov-2026 (sketch con musica de payaso, dato util y cuenta regresiva).
# Orden de publicacion: dato (cola 296) y cuenta (cola 300), continuando la rotacion sketch-dato-cuenta.
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


D, C = [], []

D.append(dato(f"💡 Truco: 21 × 19 de cabeza en 3 segundos 🤯 Suma por diferencia. Guárdalo 📌 {H} #CalculoMental #TipsPAES",
  "💡 TRUCO PAES", "21 × 19 sin calculadora", "Truco PAES: multiplicar veintiuno por diecinueve en tres segundos, sin calculadora.", "Suma por diferencia",
  [(["Busca el número del medio", r"$21 \cdot 19 = (20 + 1)(20 - 1)$"], "Veintiuno y diecinueve están a uno de distancia del veinte. Es veinte más uno, por veinte menos uno."),
   (["Suma por diferencia", r"$(a + b)(a - b) = a^2 - b^2$"], "Y la suma por su diferencia es el primero al cuadrado menos el segundo al cuadrado."),
   (["Listo", r"$20^2 - 1^2 = 400 - 1 = 399$"], "Veinte al cuadrado es cuatrocientos, menos uno: trescientos noventa y nueve.")],
  "(a + b)(a − b) = a² − b²", "Prueba con treinta y dos por veintiocho: novecientos menos dieciséis, ochocientos ochenta y cuatro. Sigue a math paes punto c, ele."))

C.append(cuenta(f"⏳ Cuenta regresiva PAES. Tip del día: revisa las unidades 📏 {H} #CuentaRegresivaPAES #TipsPAES",
  "Tip del día: antes de responder, revisa las unidades.", "Tip: las unidades",
  [(["¿Metros o centímetros?"], "Antes de calcular, revisa que todos los datos estén en la misma unidad: metros con metros, minutos con minutos."),
   (["Convierte al principio"], "Si vienen mezclados, convierte todo al principio, no al final."),
   (["¿En qué unidad te preguntan?"], "Y al terminar, fíjate en qué unidad está la respuesta que te piden.")],
  "Revisa las unidades ✅", "Muchas alternativas incorrectas son el resultado correcto en otra unidad. Sigue a math paes punto c, ele."))

E = [D[0], C[0]]
for k, e in enumerate(E, 1):
    e["tipo"] = "especial"; e["uid"] = f"s1109-{k:02d}"
json.dump(E, open(os.path.join(AQUI, "especiales_2026-11-09.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(E), "especiales")
