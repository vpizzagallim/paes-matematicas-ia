# Instrucciones para la generación semanal de problemas

Este archivo lo lee la tarea programada semanal de Claude. Objetivo: dejar en `cola/` suficientes posts para 7 días, sin repetir problemas ya publicados. Desde el 26-oct-2026 salen **12 publicaciones al día (84 por semana)**; de esas, los videos promocionales del Método 500 (promo/plan.json, unos 10 a 14 por semana) reemplazan posts de la cola, así que la cola necesita **unos 74 por semana**.

## Pasos

1. Clonar el repo y contar los posts en `cola/`. Generar los que falten para llegar a **74** (más un 10% extra, porque algunos se rechazan en la verificación).
2. Revisar `publicados/*/post.json` y `cola/*/post.json` para no repetir temas ni enunciados recientes.
3. Escribir el lote en `borradores/lote_AAAA-MM-DD.json` (lista JSON) con el formato de `borradores/lote_inicial.json`.
4. Ejecutar `python3 scripts/preparar_lote.py borradores/lote_AAAA-MM-DD.json`. Los rechazados se corrigen o se descartan; nunca se fuerza un problema que no pasa la verificación.
5. Mirar al menos 3 de las imágenes generadas (texto cortado, fórmulas montadas, desbordes). Si alguna lámina se desborda, acortar el texto y volver a renderizar.
6. Hacer commit y push a `main`.

## Mezcla y nivel

- **70% M1 y 30% M2.** Rotar los ejes: Números, Álgebra y funciones, Geometría, Probabilidad y estadística.
- **Temario PAES vigente (DEMRE).** M1: porcentajes, proporcionalidad, potencias y raíces, ecuaciones e inecuaciones lineales, sistemas 2x2, función lineal y afín, función cuadrática, perímetros, áreas y volúmenes, Pitágoras, semejanza, homotecia, vectores en el plano, transformaciones isométricas, medidas de tendencia central y posición, gráficos, probabilidad clásica y regla aditiva/multiplicativa. M2: números reales y logaritmos, matemática financiera simple, función exponencial, logarítmica y potencia, trigonometría en el triángulo rectángulo, rectas en el plano (ecuación y posiciones relativas), medidas de dispersión, combinatoria, probabilidad condicional y variable aleatoria / modelo binomial.
- **Dificultad variada**, la mayoría intermedia. Usar contextos chilenos: pesos chilenos con punto de miles, Metro, feria, cuentas de la luz, etc.

## Reglas de calidad

- **4 alternativas (A, B, C y D), igual que la PAES real** (instrucciones oficiales DEMRE), una sola correcta. Los distractores deben salir de errores típicos reales, no ser números al azar.
- `verificacion` resuelve el problema **de forma independiente**, desde los datos del enunciado. No basta con copiar el valor correcto.
- `pasos`: entre 2 y 4 pasos cortos. `trampa`: el error más común. `clave`: la idea general reutilizable.
- **Espacio en las láminas:** enunciado de hasta ~45 palabras; cada paso de hasta ~30 palabras más una fórmula.
- Decimales con coma (`0{,}8` en LaTeX) y miles con punto, como en Chile.
- `gancho`: una frase corta para el comienzo del texto del post.
- Problemas originales: no copiar ítems liberados del DEMRE.

## Reels (desde el 22-oct-2026 se publican Reels con voz, no carruseles)

Cada problema debe traer además el campo `pizarra`, que es el guion del video:

```json
"pizarra": {
  "pasos": [
    {"lineas": ["Texto corto manuscrito", "$formula$"], "voz": "Lo que dice la voz en este paso."},
    {"lineas": ["...", "$...$"], "voz": "..."}
  ],
  "cierre": {"voz": "La respuesta correcta es la be: treinta y ocho mil cuatrocientos pesos. <idea clave en una frase>. Sigue a math paes punto c, ele."}
}
```

- 2 o 3 pasos. Cada paso lleva 1 o 2 líneas: un texto corto (hasta ~32 caracteres) y una fórmula que no sea muy ancha. Si una fórmula es larga, se divide en dos líneas. En las fórmulas, usar `\dfrac`, no `\tfrac`.
- `voz` se escribe **para ser leída en voz alta**: números en palabras ("treinta y dos mil", "cero coma ocho"), sin símbolos, con 1 o 2 frases por paso. Las letras de las alternativas van como "a, be, ce, de, e".
- Duración: el total hablado debe quedar entre 25 y 35 segundos (unas 70 a 100 palabras sumando pasos y cierre).
- El cierre siempre nombra la letra correcta tal como quedó después de mezclar las alternativas.
- `preparar_lote.py` rechaza el problema si la hoja no cabe; en ese caso hay que acortarla.
- Las láminas de carrusel se siguen generando, porque son el respaldo si el Reel falla.


## Cada 3 videos normales, 1 especial (desde el 23-oct-2026)

En la cola, después de cada 3 problemas normales va 1 video especial (`"tipo": "especial"`), que GitHub arma al publicar con `scripts/armar_especial.py`. Modelo: `borradores/especiales_2026-10-23.py`. Hay tres formatos, y conviene rotarlos:

- **sketch** (música de payaso): 3 o 4 escenas cómicas cortas con Benja (estudiante) y/o la Profe Pi (`personaje`: benja o profe; `expresion`: feliz, nervioso, llora o sorpresa; `fondo`: aula, pieza o pizarra; `entrada`: caminando o derecha; `cartel`; `efecto`: boing, trombon, redoble, tictac, bocina o ding). Termina con un `problema` de 4 alternativas, con `verificacion` y `pizarra`.
- **dato**: la Profe explica una propiedad, un atajo o un truco útil (`pizarra_dato`: cartel, subtítulo, intro_voz, título, 2 o 3 pasos con líneas y voz, remate y cierre).
- **cuenta**: "Faltan N días para la PAES" (N se calcula al publicar; la PAES regular es el 30-nov-2026) + tip del día en `pizarra_dato`.
- **Duración:** menos de 59 segundos (la historia de Instagram admite 60). El campo `texto_post` es el texto del Reel, con hashtags.
- **Datos factuales** (reglas de la prueba, fechas): solo los confirmados en fuentes oficiales del DEMRE.
- **Horario (desde el 26-oct-2026):** todos los días 12 publicaciones (Chile): 08:07, 09:27, 10:47, 12:07, 13:27, 14:47, 16:07, 17:27, 18:47, 20:07, 21:27 y 22:47. Unas 74 desde la cola por semana: ~55 problemas normales y ~19 especiales. Solo las promos y los especiales se publican además como historia.
- **Nombres de carpeta en la cola:** números de 3 cifras correlativos, mayores al máximo de cola/ y publicados/.
