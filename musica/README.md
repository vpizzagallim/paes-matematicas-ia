# Musica de los Reels

20 temas de rock reales de Pixabay Music (Pixabay Content License: uso libre, tambien comercial y en redes, sin atribucion obligatoria).
Se guarda solo el tramo mas fuerte (~60 s) de cada tema, mono, volumen normalizado (-14 LUFS).
Los datos de cada tema (titulo, autor, link) estan en `pistas.json`. `scripts/musica_rock.py` elige un tema distinto por post
(rotan los 20 antes de repetir) y un tramo al azar. Para sacar un tema (p. ej. si Instagram lo marca), borrar su .mp3 y su entrada en pistas.json.
