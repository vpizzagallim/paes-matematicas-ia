# paes-matematicas-ia

Publicación automática de problemas PAES (M1 y M2) en Instagram, en la cuenta [@paes_matematicas_ia](https://www.instagram.com/paes_matematicas_ia/).

- `cola/`: posts listos para publicar (3 imágenes + texto). Se publican en orden.
- `publicados/`: posts ya publicados.
- `.github/workflows/publicar.yml`: publica el siguiente post 4 veces al día (09:00, 15:00, 21:00 y 03:00, hora de Chile).
- `.github/workflows/renovar-token.yml`: renueva el token de Instagram dos veces al mes.
- `scripts/preparar_lote.py`: verifica cada problema con sympy y genera las imágenes (`render/`).
- `GENERAR.md`: instrucciones de la generación semanal.

Secretos del repositorio: `IG_TOKEN` (token de Instagram) y `GH_PAT` (llave de GitHub del bot).
