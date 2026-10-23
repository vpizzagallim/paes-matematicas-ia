"""Musica de rock para los videos.

Desde el 23-oct-2026 se usan temas de rock reales (grabados por musicos, licencia libre de Pixabay)
guardados en musica/ (tramos de ~60 s). Cada video toma un tema distinto (rotan los 20 antes de
repetir) y un tramo al azar. Si la carpeta no esta, se usa la musica sintetizada de abajo.

Respaldo: musica de hard rock clasico original y distinta en cada video (rasgueo de guitarra estilo anos 70-80).

rock_variado(total_segundos, semilla) -> np.array mono (44.1 kHz) normalizado a [-1, 1].

Guitarra con acordes abiertos de verdad (6 cuerdas en afinacion estandar, sintesis de cuerda pulsada
Karplus-Strong), rasgueo con desfase entre cuerdas, golpes acentuados que se dejan sonar, apagados,
saturacion suave tipo amplificador a valvulas + simulacion de parlante, dos tomas (como en un estudio)
y una sala corta. Bateria acustica simple y bajo. Tempo, tono, progresion, ritmo y bateria cambian con
la semilla, asi que cada video suena distinto.
"""
import json
import os
import subprocess
import zlib
import numpy as np
from scipy.signal import lfilter, butter, fftconvolve

SR = 44100

# Afinacion estandar E2 A2 D3 G3 B3 E4
CUERDAS = [82.41, 110.00, 146.83, 196.00, 246.94, 329.63]
# Acordes abiertos clasicos (traste por cuerda, None = no se toca)
ACORDES = {
    "E": [0, 2, 2, 1, 0, 0], "A": [None, 0, 2, 2, 2, 0], "D": [None, None, 0, 2, 3, 2],
    "G": [3, 2, 0, 0, 0, 3], "C": [None, 3, 2, 0, 1, 0], "B": [None, 2, 4, 4, 4, 2],
    "E5": [0, 2, 2, None, None, None], "A5": [None, 0, 2, 2, None, None], "D5": [None, None, 0, 2, 3, None],
    "G5": [3, 5, 5, None, None, None], "F#": [2, 4, 4, 3, 2, 2], "Bm": [None, 2, 4, 4, 3, 2],
    "C5": [None, 3, 5, 5, None, None], "B5": [None, 2, 4, 4, None, None], "F#5": [2, 4, 4, None, None, None],
    "F5": [1, 3, 3, None, None, None],
}
PROGRESIONES = [  # un acorde por compas, 4 compases
    ["E", "D", "A", "E"], ["A", "G", "D", "A"], ["E", "A", "E", "B"], ["G", "C", "D", "G"],
    ["A", "D", "E", "A"], ["E", "G", "A", "E"], ["D", "C", "G", "D"], ["A", "C", "D", "A"],
    ["E5", "G5", "A5", "E5"], ["A", "D", "A", "E"], ["G", "D", "C", "G"], ["E", "D", "A", "B"],
    ["E5", "D5", "C5", "B5"], ["A5", "C5", "D5", "A5"], ["E5", "F#5", "G5", "A5"], ["E5", "G5", "D5", "A5"],
    ["E5", "C5", "D5", "E5"], ["A5", "G5", "F5", "E5"],
]
# 8 corcheas por compas: X golpe acentuado que suena, x golpe corto, m apagado (palm mute),
# k rasguido muerto (chuk), . silencio / dejar sonar
RITMOS = [
    "X..X..X.", "X.X...x.", "X...X.kX", "X..k.XX.", "XX..X...", "X.mmX.mm", "X..X.kx.",
    "X...Xk.X", "X.kX.kX.", "Xm.mX.k.", "X..XX.k.", "X.x.X.kx",
    # mas pesados: galope y palm mute
    "XmmXmmXm", "mmmmX.mX", "X.mmm.X.", "mmXmmXmX", "XmmmXmXm", "Xm.XmmX.",
]
BATERIAS = [  # por corchea: k bombo, s caja, h hihat, b bombo+hihat, o hihat abierto
    "bhshbhsh", "bhshbbsh", "bhsbhbsh", "bhshbhso", "bbshbhsh",
]


def _cuerda(f, dur, rng, apagada=False, brillo=0.5):
    n = int(dur * SR)
    N = max(2, int(round(SR / f)))
    exc = rng.uniform(-1, 1, N)
    p = max(1, int(N * rng.uniform(0.12, 0.2)))  # posicion de la pua: quita armonicos como una cuerda real
    exc = exc - np.roll(exc, p)
    exc = lfilter([1 - brillo], [1, -brillo], exc)  # pua mas o menos brillante
    x = np.zeros(n); x[:N] = exc
    g = 0.90 if apagada else 0.997
    a = np.zeros(N + 2); a[0] = 1; a[N] = -g / 2; a[N + 1] = -g / 2
    y = lfilter([1.0], a, x)
    if apagada:
        y *= np.exp(-np.arange(n) / SR * 22)
    return y


def _rasgueo(acorde, dur, tipo, rng, abajo=True):
    n = int(dur * SR)
    if tipo == "k":  # chuk: cuerdas apagadas con la mano
        m = int(0.06 * SR)
        r = rng.standard_normal(m)
        b, a = butter(2, [250 / (SR / 2), 2500 / (SR / 2)], "band"); r = lfilter(b, a, r)
        return r * np.exp(-np.arange(m) / SR * 70) * 0.9
    trastes = ACORDES[acorde]
    notas = [CUERDAS[i] * 2 ** (t / 12) for i, t in enumerate(trastes) if t is not None]
    if tipo == "m":
        notas = notas[:3]  # palm mute: solo las graves
    if not abajo:
        notas = notas[::-1][:4]  # hacia arriba: agudas y mas suave
    y = np.zeros(n)
    vel = rng.uniform(0.010, 0.018) if tipo == "X" else rng.uniform(0.006, 0.010)
    for i, f in enumerate(notas):
        r = int(i * vel * SR / max(1, len(notas) - 1) * 2)
        f *= 2 ** (rng.normal(0, 0.03) / 12)  # afinacion humana
        c = _cuerda(f, dur, rng, apagada=(tipo == "m"), brillo=0.35 if tipo == "X" else 0.55)
        amp = (1.0 if abajo else 0.6) * rng.uniform(0.85, 1.0)
        y[r:] += c[:n - r] * amp
    m = int(0.012 * SR)  # ruido de la pua contra las cuerdas
    pua = rng.standard_normal(m) * np.exp(-np.arange(m) / SR * 400)
    b, a = butter(2, [1500 / (SR / 2), 6000 / (SR / 2)], "band")
    y[:min(m, n)] += lfilter(b, a, pua)[:min(m, n)] * (0.35 if tipo == "X" else 0.2)
    if tipo == "x":  # golpe corto: se apaga con la mano
        corte = int(min(n, 0.6 * n))
        env = np.ones(n); env[corte:] = np.exp(-np.arange(n - corte) / SR * 40)
        y *= env
    return y


def _biquad_pico(f0, q, db):
    A = 10 ** (db / 40); w = 2 * np.pi * f0 / SR; al = np.sin(w) / (2 * q)
    b = [1 + al * A, -2 * np.cos(w), 1 - al * A]; a = [1 + al / A, -2 * np.cos(w), 1 - al / A]
    return np.array(b) / a[0], np.array(a) / a[0]


def _amplificador(y, ganancia):
    """Amplificador a valvulas en dos etapas (como un Marshall) + parlante 4x12."""
    b, a = butter(1, 140 / (SR / 2), "high"); y = lfilter(b, a, y)          # apretar graves antes de saturar
    y = np.tanh(y * ganancia + 0.2) - np.tanh(0.2)                          # etapa 1 (asimetrica, como valvula)
    b, a = butter(1, 5500 / (SR / 2), "low"); y = lfilter(b, a, y)          # entre etapas se pierde brillo
    y = np.tanh(y * 2.2)                                                    # etapa 2
    y = y / max(1e-9, np.abs(y).max())
    # parlante: resonancia grave, medios algo hundidos, presencia y caida brusca de agudos
    for f0, q, db in [(110, 1.0, 4.0), (450, 0.8, -3.0), (1600, 1.0, 2.5), (3000, 1.2, 3.0)]:
        b, a = _biquad_pico(f0, q, db); y = lfilter(b, a, y)
    b, a = butter(6, 4800 / (SR / 2), "low"); y = lfilter(b, a, y)
    b, a = butter(2, 75 / (SR / 2), "high"); y = lfilter(b, a, y)
    return y


def _sala(y, rng, seg=0.45, mezcla=0.14):
    m = int(seg * SR)
    ir = rng.standard_normal(m) * np.exp(-np.arange(m) / SR * 9)
    b, a = butter(2, 5000 / (SR / 2), "low"); ir = lfilter(b, a, ir)
    ir[:int(0.012 * SR)] = 0  # pre-delay
    ir /= np.sqrt(np.sum(ir ** 2))
    hum = fftconvolve(y, ir)[:len(y)]
    return (1 - mezcla) * y + mezcla * hum * (np.abs(y).max() / max(1e-9, np.abs(hum).max()))


def _guitarra(total, beat, prog, ritmo_a, ritmo_b, ganancia, rng):
    n_total = int(total * SR)
    g = np.zeros(n_total)
    paso = beat / 2
    t, k = 0.0, 0
    while t < total:
        compas = k // 8
        acorde = prog[compas % 4]
        ritmo = ritmo_a if (compas // 4) % 2 == 0 else ritmo_b
        tipo = ritmo[k % 8]
        if tipo != ".":
            # el acentuado suena hasta el proximo golpe
            j = 1
            while tipo == "X" and j < 8 and ritmo[(k + j) % 8] == ".":
                j += 1
            dur = paso * j * 1.05 + 0.05
            s = _rasgueo(acorde, dur, tipo, rng, abajo=(k % 2 == 0) or tipo == "X")
            i = int((t + rng.normal(0, 0.004)) * SR); i = max(0, i)
            m = min(len(s), n_total - i)
            if m > 0:
                g[i:i + m] += s[:m] * (1.0 if tipo == "X" else 0.75)
        t += paso; k += 1
    return _amplificador(g / max(1e-9, np.abs(g).max()), ganancia)


def _bateria(n_total, beat, patron, rng):
    y = np.zeros(n_total)
    def poner(s, t, v=1.0):
        i = int(max(0, t + rng.normal(0, 0.003)) * SR); m = min(len(s), n_total - i)
        if m > 0: y[i:i + m] += s[:m] * v * rng.uniform(0.9, 1.0)
    def banda(x, lo, hi):
        b, a = butter(2, [lo / (SR / 2), hi / (SR / 2)], "band"); return lfilter(b, a, x)
    tk = np.arange(int(0.35 * SR)) / SR
    kick = np.sin(2 * np.pi * (52 * tk + 60 / 30 * (1 - np.exp(-tk * 30)))) * np.exp(-tk * 9)
    click = banda(rng.standard_normal(len(tk)), 1500, 5000) * np.exp(-tk * 250) * 0.3
    kick = 0.95 * kick + click
    ts = np.arange(int(0.3 * SR)) / SR
    snare = (0.35 * np.sin(2 * np.pi * 190 * ts) + 0.2 * np.sin(2 * np.pi * 330 * ts)) * np.exp(-ts * 22) \
        + 0.6 * banda(rng.standard_normal(len(ts)), 1200, 9000) * np.exp(-ts * 14)
    th = np.arange(int(0.08 * SR)) / SR
    hh = banda(rng.standard_normal(len(th)), 7000, 14000) * np.exp(-th * 55) * 0.35
    to = np.arange(int(0.35 * SR)) / SR
    hho = banda(rng.standard_normal(len(to)), 6000, 14000) * np.exp(-to * 9) * 0.3
    tc = np.arange(int(1.8 * SR)) / SR
    crash = banda(rng.standard_normal(len(tc)), 3000, 13000) * np.exp(-tc * 2.2) * 0.35
    t, k = 0.0, 0
    paso = beat / 2
    while t < n_total / SR:
        compas = k // 8
        if k % 32 == 0:
            poner(crash, t); poner(kick, t)
        if compas % 4 == 3 and k % 8 >= 6:  # pequeno redoble al cerrar la frase
            poner(snare, t, 0.8); poner(snare, t + paso / 2, 0.65)
        else:
            c = patron[k % 8]
            if c in "kb": poner(kick, t)
            if c == "s": poner(snare, t)
            if c in "hb": poner(hh, t, 0.9 if k % 2 == 0 else 0.6)
            if c == "o": poner(hho, t)
        t += paso; k += 1
    return _sala(y, rng, 0.35, 0.18)


def _bajo(total, beat, prog, rng):
    n_total = int(total * SR)
    y = np.zeros(n_total)
    paso = beat / 2
    t, k = 0.0, 0
    while t < total:
        acorde = prog[(k // 8) % 4]
        raiz = CUERDAS[next(i for i, f in enumerate(ACORDES[acorde]) if f is not None)] * \
            2 ** (next(f for f in ACORDES[acorde] if f is not None) / 12)
        while raiz > 70: raiz /= 2
        nt = np.arange(int(paso * 0.95 * SR)) / SR
        s = sum(np.sin(2 * np.pi * raiz * h * nt) / h ** 1.6 for h in range(1, 6))
        s *= (1 - np.exp(-nt * 300)) * np.exp(-nt * 3) * 0.6
        i = int(t * SR); m = min(len(s), n_total - i); y[i:i + m] += s[:m]
        t += paso; k += 1
    y = np.tanh(2.0 * y / max(1e-9, np.abs(y).max()))
    b, a = butter(2, 900 / (SR / 2), "low")
    return lfilter(b, a, y)


def _rock_sintetico(total, semilla=0):
    rng = np.random.default_rng(zlib.crc32(str(semilla).encode()))
    bpm = int(rng.integers(104, 136))
    beat = 60 / bpm
    prog = PROGRESIONES[rng.integers(len(PROGRESIONES))]
    ritmo_a = RITMOS[rng.integers(len(RITMOS))]
    ritmo_b = RITMOS[rng.integers(len(RITMOS))]
    bat = BATERIAS[rng.integers(len(BATERIAS))]
    ganancia = rng.uniform(5.0, 8.0)  # hard rock: mas pesado que crunch, sin llegar a metal
    # dos tomas de guitarra distintas (como grabar dos veces): suena gordo y humano
    g1 = _guitarra(total, beat, prog, ritmo_a, ritmo_b, ganancia, np.random.default_rng(rng.integers(1 << 30)))
    g2 = _guitarra(total, beat, prog, ritmo_a, ritmo_b, ganancia * 0.9, np.random.default_rng(rng.integers(1 << 30)))
    guitarra = _sala(0.55 * g1 + 0.45 * g2, rng, 0.5, 0.12)
    bateria = _bateria(int(total * SR), beat, bat, rng)
    bajo = _bajo(total, beat, prog, rng)
    norm = lambda v: v / max(1e-9, np.abs(v).max())
    y = 0.64 * norm(guitarra) + 0.42 * norm(bateria) + 0.34 * norm(bajo)
    y = np.tanh(1.2 * y)  # pegamento final suave
    return y / max(1e-9, np.abs(y).max())


def descripcion(semilla=0):
    rng = np.random.default_rng(zlib.crc32(str(semilla).encode()))
    return f"{int(rng.integers(104, 136))} bpm"


MUSICA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "musica")


def _pistas():
    try:
        return [p for p in json.load(open(os.path.join(MUSICA, "pistas.json"), encoding="utf-8"))
                if os.path.exists(os.path.join(MUSICA, p["id"] + ".mp3"))]
    except Exception:
        return []


def elegir_pista(semilla):
    """Tema para este video: los posts correlativos recorren todos los temas antes de repetir."""
    pistas = _pistas()
    if not pistas:
        return None
    orden = np.random.default_rng(20261023).permutation(len(pistas))
    s = str(semilla)
    n = int(s) if s.isdigit() else zlib.crc32(s.encode())
    return pistas[orden[n % len(pistas)]]


def _leer(ruta, desde, dur):
    r = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{desde:.2f}", "-t", f"{dur:.2f}", "-i", ruta,
                        "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32).astype(np.float64)


def rock_variado(total, semilla=0):
    p = elegir_pista(semilla)
    if p is None:
        return _rock_sintetico(total, semilla)
    try:
        ruta = os.path.join(MUSICA, p["id"] + ".mp3")
        rng = np.random.default_rng(zlib.crc32(("tramo" + str(semilla)).encode()))
        largo = float(p.get("dur", 60))
        n = int(total * SR)
        if largo >= total + 0.5:
            y = _leer(ruta, rng.uniform(0, largo - total - 0.2), total + 0.1)
        else:  # el video es mas largo que el tramo: se repite con un cruce suave
            y = _leer(ruta, 0, largo)
            cruce = int(1.0 * SR)
            while len(y) < n:
                rampa = np.linspace(0, 1, cruce)
                y = np.concatenate([y[:-cruce], y[-cruce:] * (1 - rampa) + y[:cruce] * rampa, y[cruce:]])
        y = y[:n]
        if len(y) < n:
            y = np.pad(y, (0, n - len(y)))
        fi, fo = int(0.25 * SR), int(1.5 * SR)
        y[:fi] *= np.linspace(0, 1, fi)
        y[-fo:] *= np.linspace(1, 0, fo)
        print(f"Musica: {p['titulo']} - {p['autor']} (Pixabay)")
        return y / max(1e-9, np.abs(y).max())
    except Exception as e:
        print(f"::warning::No se pudo usar el tema real ({e}); va la musica sintetizada")
        return _rock_sintetico(total, semilla)
