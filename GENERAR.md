# Instrucciones para la generación semanal de problemas

Este archivo lo lee la tarea programada semanal de Claude. Objetivo: dejar en `cola/` suficientes posts para 7 días (4 por día = 28), sin repetir problemas ya publicados.

## Pasos

1. Clonar el repo y contar los posts en `cola/`. Generar los que falten para llegar a **28** (más un 15% extra, porque algunos se rechazan en la verificación).
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

- 5 alternativas, una sola correcta. Los distractores deben salir de errores típicos reales, no ser números al azar.
- `verificacion` resuelve el problema **de forma independiente**, desde los datos del enunciado. No basta con copiar el valor correcto.
- `pasos`: entre 2 y 4 pasos cortos. `trampa`: el error más común. `clave`: la idea general reutilizable.
- **Espacio en las láminas:** enunciado de hasta ~45 palabras; cada paso de hasta ~30 palabras más una fórmula.
- Decimales con coma (`0{,}8` en LaTeX) y miles con punto, como en Chile.
- `gancho`: una frase corta para el comienzo del texto del post.
- Problemas originales: no copiar ítems liberados del DEMRE.
