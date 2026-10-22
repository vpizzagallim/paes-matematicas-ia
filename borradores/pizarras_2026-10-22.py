# Guiones de voz y hoja manuscrita para los posts del lote 22-oct (003-037).
# Cada entrada: pasos [(lineas, voz)], respuesta hablada, idea clave hablada.
import json, os

LET = {"A": "a", "B": "be", "C": "ce", "D": "de", "E": "e"}
S = {}

S["003"] = ([(["Misma base: se suman los exponentes", "$2^3 \\cdot 2^5 = 2^8$"], "Cuando multiplicas potencias de igual base, sumas los exponentes. Dos elevado a tres por dos elevado a cinco es dos elevado a ocho."),
             (["Al dividir se restan", "$2^8 \\div 2^6 = 2^2 = 4$"], "Y al dividir, restas. Ocho menos seis da dos, y dos al cuadrado es cuatro.")],
            "cuatro", "Multiplicar suma exponentes, dividir los resta.")
S["004"] = ([(["Con IVA = 119% del neto", "$P \\cdot 1{,}19 = 11.900$"], "El precio con IVA es el ciento diecinueve por ciento del precio neto. O sea, el neto por uno coma diecinueve da once mil novecientos."),
             (["Despejamos", "$P = 11.900 \\div 1{,}19 = 10.000$"], "Para despejar, divides once mil novecientos por uno coma diecinueve, y te da diez mil pesos.")],
            "diez mil pesos", "Para quitar un porcentaje ya aplicado, se divide, no se resta.")
S["005"] = ([(["Buscamos cuadrados perfectos", "$\\sqrt{50} = 5\\sqrt{2} \\quad \\sqrt{18} = 3\\sqrt{2}$"], "Descompón cada raíz buscando un cuadrado perfecto. Raíz de cincuenta es cinco raíz de dos, y raíz de dieciocho es tres raíz de dos."),
             (["Ahora son semejantes", "$5\\sqrt{2} + 3\\sqrt{2} = 8\\sqrt{2}$"], "Ahora sí se pueden sumar, como términos semejantes: cinco más tres, ocho raíz de dos.")],
            "ocho raíz de dos", "La raíz de una suma no es la suma de las raíces.")
S["006"] = ([(["3 : 5 → 8 partes", "$40 \\div 8 = 5$"], "La razón tres es a cinco reparte el curso en ocho partes iguales. Cuarenta dividido en ocho da cinco alumnos por parte."),
             (["Mujeres = 5 partes", "$5 \\cdot 5 = 25$"], "Las mujeres son cinco de esas partes, así que cinco por cinco: veinticinco mujeres.")],
            "veinticinco", "En una razón, el total se reparte en la suma de sus partes.")
S["007"] = ([(["Parte sobre total", "$12 \\div 80 = 0{,}15$"], "Para saber qué porcentaje de ochenta es doce, divides la parte por el total: doce dividido en ochenta da cero coma quince."),
             (["Por 100", "$0{,}15 \\cdot 100 = 15\\%$"], "Lo multiplicas por cien, y te da quince por ciento.")],
            "quince por ciento", "Siempre es la parte dividida por el total, por cien.")
S["008"] = ([(["Primero multiplicar", "$\\tfrac{3}{4} \\cdot \\tfrac{2}{3} = \\tfrac{1}{2}$"], "Ojo con el orden: primero va la multiplicación. Tres cuartos por dos tercios da un medio."),
             (["Después sumar", "$\\tfrac{1}{4} + \\tfrac{1}{2} = \\tfrac{3}{4}$"], "Cero coma veinticinco es un cuarto. Un cuarto más un medio da tres cuartos.")],
            "tres cuartos", "Multiplicación y división van antes que la suma.")
S["009"] = ([(["Pasamos a notación científica", "$4{,}2 \\cdot 10^{-4} \\cdot 3 \\cdot 10^{5}$"], "Escribe cero coma cero cero cero cuarenta y dos como cuatro coma dos por diez a la menos cuatro."),
             (["Multiplicamos y ajustamos", "$12{,}6 \\cdot 10^{1} = 1{,}26 \\cdot 10^{2}$"], "Cuatro coma dos por tres da doce coma seis, y diez a la menos cuatro por diez a la cinco es diez a la uno. Ajustando, queda uno coma veintiséis por diez al cuadrado.")],
            "uno coma veintiséis por diez al cuadrado", "Si achicas el coeficiente, el exponente sube.")
S["010"] = ([(["Distribuimos el 3", "$3x - 6 = x + 8$"], "Primero distribuye el tres a todo el paréntesis: tres equis menos seis igual equis más ocho."),
             (["Despejamos", "$2x = 14 \\Rightarrow x = 7$"], "Pasamos las equis a un lado y los números al otro: dos equis igual catorce, así que equis vale siete.")],
            "siete", "El número fuera del paréntesis multiplica a todo lo de adentro.")
S["011"] = ([(["Planteamos el sistema", "$2a + 3n = 17.000$", "$a + n = 7.000$"], "Llama a al precio de adulto y ene al de niño. Dos a más tres ene es diecisiete mil, y a más ene es siete mil."),
             (["Restamos y reemplazamos", "$n = 3.000 \\Rightarrow a = 4.000$"], "Multiplica la segunda por dos y resta: ene da tres mil. Entonces el adulto cuesta siete mil menos tres mil, cuatro mil pesos.")],
            "cuatro mil pesos", "Relee qué te preguntan: adulto o niño.")
S["012"] = ([(["3 km = 15 tramos de 200 m", "$3.000 \\div 200 = 15$"], "Tres kilómetros son tres mil metros, o sea quince tramos de doscientos metros."),
             (["Costo fijo + variable", "$500 + 150 \\cdot 15 = 2.750$"], "El costo es quinientos de bajada de bandera, más ciento cincuenta por cada tramo: dos mil setecientos cincuenta pesos.")],
            "dos mil setecientos cincuenta pesos", "Función afín: un costo fijo más un costo por unidad.")
S["013"] = ([(["Agrupamos las x", "$-x < 6$"], "Pasa las equis a un lado: dos equis menos tres equis es menos equis, y menos equis es menor que seis."),
             (["Multiplicar por −1 invierte", "$x > -6$"], "Al multiplicar por menos uno, la desigualdad se da vuelta. Queda equis mayor que menos seis.")],
            "equis mayor que menos seis", "Multiplicar por un negativo invierte la desigualdad.")
S["014"] = ([(["Vértice", "$x_v = \\tfrac{6}{2} = 3$"], "La parábola abre hacia arriba, así que el mínimo está en el vértice. Equis del vértice: menos be partido dos a, seis partido dos, tres."),
             (["Evaluamos", "$f(3) = 9 - 18 + 5 = -4$"], "Ahora evalúa la función en tres: nueve menos dieciocho más cinco, menos cuatro.")],
            "menos cuatro", "El valor mínimo es la función evaluada en el vértice.")
S["015"] = ([(["Suma por diferencia", "$a^2 - b^2 = (a+b)(a-b)$"], "No necesitas despejar a ni be. A al cuadrado menos be al cuadrado es la suma por la diferencia."),
             (["Reemplazamos", "$10 \\cdot 4 = 40$"], "La suma es diez y la diferencia es cuatro. Diez por cuatro, cuarenta.")],
            "cuarenta", "Busca productos notables antes de hacer cuentas largas.")
S["016"] = ([(["Desarrollamos cada cuadrado", "$x^2 + 6x + 9 \\quad x^2 - 6x + 9$"], "Desarrolla cada cuadrado de binomio, sin olvidar el término del medio: más seis equis en uno, menos seis equis en el otro."),
             (["Restamos", "$6x - (-6x) = 12x$"], "Al restar, los equis al cuadrado y los nueves se cancelan, y queda seis equis menos menos seis equis: doce equis.")],
            "doce equis", "El doble producto es el término que más se olvida.")
S["017"] = ([(["Pendiente", "$m = \\tfrac{11 - 5}{3 - 1} = 3$"], "Con dos puntos sacas la pendiente: once menos cinco, partido tres menos uno, da tres."),
             (["Coeficiente de posición", "$3 + n = 5 \\Rightarrow n = 2$"], "Usa efe de uno igual cinco: tres más ene es cinco, ene es dos. Y efe de cero es justamente ene.")],
            "dos", "Efe de cero es el corte con el eje i griega.")
S["018"] = ([(["Escalera = hipotenusa", "$h^2 + 5^2 = 13^2$"], "La escalera es la hipotenusa del triángulo rectángulo. Altura al cuadrado más cinco al cuadrado igual trece al cuadrado."),
             (["Despejamos", "$h^2 = 144 \\Rightarrow h = 12$"], "Ciento sesenta y nueve menos veinticinco da ciento cuarenta y cuatro, y su raíz es doce metros.")],
            "doce metros", "La hipotenusa siempre es el lado más largo.")
S["019"] = ([(["Áreas", "$20 \\cdot 15 = 300 \\quad 10 \\cdot 8 = 80$"], "El terreno mide veinte por quince, trescientos metros cuadrados. La casa, diez por ocho, ochenta."),
             (["Restamos", "$300 - 80 = 220$"], "Lo que queda libre es trescientos menos ochenta: doscientos veinte metros cuadrados.")],
            "doscientos veinte metros cuadrados", "Área libre: total menos lo ocupado.")
S["020"] = ([(["Triángulos semejantes", "$\\tfrac{h}{18} = \\tfrac{3}{2}$"], "El sol forma triángulos semejantes. La altura es a su sombra como tres es a dos."),
             (["Despejamos", "$h = 18 \\cdot 1{,}5 = 27$"], "Dieciocho por tres medios da veintisiete metros.")],
            "veintisiete metros", "En semejanza, compara altura con altura y sombra con sombra.")
S["021"] = ([(["Volumen del cilindro", "$V = \\pi r^2 h$"], "El volumen de un cilindro es pi por radio al cuadrado por altura."),
             (["Reemplazamos", "$\\pi \\cdot 9 \\cdot 10 = 90\\pi$"], "Tres al cuadrado es nueve, por diez, noventa pi centímetros cúbicos.")],
            "noventa pi", "No olvides elevar el radio al cuadrado.")
S["022"] = ([(["Rotación 90° antihoraria", "$(x, y) \\to (-y, x)$"], "Rotar noventa grados en sentido antihorario cambia equis i griega por menos i griega, equis."),
             (["Aplicamos", "$(2, -3) \\to (3, 2)$"], "Con dos, menos tres, queda tres, dos.")],
            "tres coma dos", "Antihorario: menos i griega, equis. Horario: i griega, menos equis.")
S["023"] = ([(["Ponderamos u", "$2\\vec{u} = (4, -2)$"], "Primero multiplica u por dos: cuatro, menos dos."),
             (["Sumamos componente a componente", "$(4 - 3,\\; -2 + 4) = (1, 2)$"], "Luego suma con ve, componente a componente: uno, dos.")],
            "uno coma dos", "Los vectores se operan componente a componente.")
S["024"] = ([(["Suma necesaria", "$5 \\cdot 5{,}5 = 27{,}5$"], "Para tener promedio cinco coma cinco con cinco notas, la suma tiene que ser veintisiete coma cinco."),
             (["Lo que falta", "$27{,}5 - 22{,}0 = 5{,}5$"], "Tus cuatro notas suman veintidós. Te falta un cinco coma cinco.")],
            "cinco coma cinco", "Promedio por cantidad de notas da la suma que necesitas.")
S["025"] = ([(["Ordenamos", "$2, 3, 5, 7, 8, 10$"], "Para la mediana, lo primero es ordenar los datos de menor a mayor."),
             (["Par de datos: promedio central", "$\\tfrac{5 + 7}{2} = 6$"], "Hay seis datos, así que promedias los dos del centro: cinco y siete. Da seis.")],
            "seis", "Siempre ordena antes de buscar la mediana.")
S["026"] = ([(["36 casos posibles", "$6 \\cdot 6 = 36$"], "Con dos dados hay treinta y seis resultados igual de probables."),
             (["Suman 7: seis casos", "$\\tfrac{6}{36} = \\tfrac{1}{6}$"], "Suman siete: uno seis, dos cinco, tres cuatro, y al revés. Seis casos de treinta y seis: un sexto.")],
            "un sexto", "Cuenta casos igual de probables, no sumas posibles.")
S["027"] = ([(["Primera roja", "$\\tfrac{4}{10}$"], "La primera bolita roja tiene probabilidad cuatro de diez."),
             (["Segunda roja, sin reposición", "$\\tfrac{4}{10} \\cdot \\tfrac{3}{9} = \\tfrac{2}{15}$"], "Sin reposición queda una roja menos y una bolita menos: tres de nueve. Multiplicando, dos quinceavos.")],
            "dos quinceavos", "Sin reposición cambian el numerador y el denominador.")
S["028"] = ([(["Juegan al menos uno", "$25 + 18 - 8 = 35$"], "Suma los de fútbol y básquetbol, pero resta los ocho que juegan ambos para no contarlos dos veces: treinta y cinco."),
             (["No juegan ninguno", "$\\tfrac{40 - 35}{40} = \\tfrac{1}{8}$"], "Quedan cinco que no juegan nada. Cinco de cuarenta es un octavo.")],
            "un octavo", "En la unión, la intersección se resta una vez.")
S["029"] = ([(["Cada logaritmo", "$\\log_2 8 = 3 \\quad \\log_3 \\tfrac{1}{9} = -2$"], "Logaritmo en base dos de ocho es tres, porque dos al cubo es ocho. Y logaritmo en base tres de un noveno es menos dos."),
             (["Sumamos", "$3 + (-2) = 1$"], "Tres más menos dos: uno.")],
            "uno", "El logaritmo de un número entre cero y uno es negativo.")
S["030"] = ([(["Duplicaciones", "$12 \\div 3 = 4$"], "En doce horas hay cuatro periodos de tres horas, o sea cuatro duplicaciones."),
             (["Modelo exponencial", "$500 \\cdot 2^4 = 8.000$"], "Quinientos por dos a la cuarta, que es dieciséis: ocho mil bacterias.")],
            "ocho mil", "Duplicar es multiplicar por dos cada periodo, no sumar.")
S["031"] = ([(["Altura = cateto opuesto", "$\\sin 30^\\circ = \\tfrac{h}{8}$"], "La rampa es la hipotenusa y la altura es el cateto opuesto al ángulo. Usamos seno."),
             (["Seno de 30° = 1/2", "$h = 8 \\cdot \\tfrac{1}{2} = 4$"], "Seno de treinta grados es un medio. Ocho por un medio: cuatro metros.")],
            "cuatro metros", "Opuesto con seno, adyacente con coseno.")
S["032"] = ([(["Sin cargos: no importa el orden", "$\\binom{7}{3}$"], "Como el comité no tiene cargos, el orden no importa. Son combinaciones de siete en tres."),
             (["Calculamos", "$\\tfrac{7 \\cdot 6 \\cdot 5}{3 \\cdot 2 \\cdot 1} = 35$"], "Siete por seis por cinco, dividido por tres factorial: treinta y cinco comités.")],
            "treinta y cinco", "Si el orden no importa, son combinaciones.")
S["033"] = ([(["Con lentes", "$0{,}18 + 0{,}08 = 0{,}26$"], "Mujeres con lentes: cero coma seis por cero coma tres, cero coma dieciocho. Hombres con lentes: cero coma cero ocho. En total, cero coma veintiséis."),
             (["Condicional", "$\\tfrac{0{,}18}{0{,}26} = \\tfrac{9}{13}$"], "De los que usan lentes, la fracción de mujeres es cero coma dieciocho partido cero coma veintiséis: nueve treceavos.")],
            "nueve treceavos", "En la condicional, divide por la probabilidad de la condición.")
S["034"] = ([(["Formas de ubicar 2 caras", "$\\binom{4}{2} = 6$"], "Hay seis formas de ubicar dos caras en cuatro lanzamientos."),
             (["Cada secuencia vale 1/16", "$6 \\cdot \\tfrac{1}{16} = \\tfrac{3}{8}$"], "Cada secuencia tiene probabilidad un dieciseisavo. Seis dieciseisavos es tres octavos.")],
            "tres octavos", "Binomial: combinaciones por probabilidad de cada secuencia.")
S["035"] = ([(["Pendiente", "$m = \\tfrac{8 - 2}{3 - 1} = 3$"], "La pendiente es ocho menos dos, partido tres menos uno: tres."),
             (["Ecuación y corte", "$y = 3x - 1 \\Rightarrow n = -1$"], "Con el punto uno, dos, la recta es i griega igual tres equis menos uno. Corta al eje i griega en menos uno.")],
            "menos uno", "El corte con el eje i griega es el ene de i griega igual eme equis más ene.")
S["036"] = ([(["Media", "$\\bar{x} = \\tfrac{20}{4} = 5$"], "La media de dos, cuatro, seis y ocho es cinco."),
             (["Desviaciones al cuadrado", "$\\tfrac{9 + 1 + 1 + 9}{4} = 5$"], "Las desviaciones al cuadrado son nueve, uno, uno y nueve. Suman veinte, y divididas en cuatro dan cinco.")],
            "cinco", "La desviación estándar es la raíz de la varianza.")
S["037"] = ([(["Interés compuesto", "$1.000.000 \\cdot 1{,}1^2$"], "Con interés compuesto, cada año ganas sobre lo acumulado. El capital se multiplica por uno coma uno dos veces."),
             (["Resultado", "$1.000.000 \\cdot 1{,}21 = 1.210.000$"], "Uno coma uno al cuadrado es uno coma veintiuno. Te quedan un millón doscientos diez mil pesos.")],
            "un millón doscientos diez mil pesos", "Compuesto multiplica, simple suma.")


def pizarra(pid, letra):
    pasos, resp, clave = S[pid]
    return {"pasos": [{"lineas": l, "voz": v} for l, v in pasos],
            "cierre": {"voz": f"La respuesta correcta es la {LET[letra]}: {resp}. {clave} Sigue a math paes punto c, ele."}}


if __name__ == "__main__":
    salida = {}
    for pid in S:
        salida[pid] = S[pid]
    json.dump({k: [[list(a), b] for a, b in v[0]] + [v[1], v[2]] for k, v in S.items()},
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "pizarras_2026-10-22.json"), "w"), ensure_ascii=False)
