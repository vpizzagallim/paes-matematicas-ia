"""Musica hard rock original y distinta en cada video (estilo riff de guitarra con power chords).

rock_variado(total_segundos, semilla) -> np.array mono (44.1 kHz) normalizado a [-1, 1].
Guitarra con sintesis de cuerda pulsada (Karplus-Strong), rasgueo con desfase entre cuerdas,
palm mute, distorsion y bateria. Tempo, tono, progresion, riff y bateria cambian con la semilla.
"""
import zlib
import numpy as np
from scipy.signal import lfilter, butter

SR = 44100

PROGRESIONES = [  # semitonos desde la tonica, por compas
    [0, 0, 5, 5], [0, -2, 5, 0], [0, 5, 7, 5], [0, -2, -4, -2], [0, 3, 5, 0],
    [0, 0, -2, 5], [0, 7, 5, 0], [0, -5, -2, 0],
]
TONICAS = {"E": 82.41, "A": 110.0, "G": 98.0, "D": 73.42, "C": 65.41}
RIFFS = [  # 8 corcheas: C acorde abierto, m palm mute, x rasguido apagado, - silencio
    "C-mmC-mm", "Cmm-Cmm-", "C--mC-mm", "mmCmmmCm", "C-m-C-mx", "CmCmCm-x", "C--C--C-", "mmmCmmmC",
    "C-xmC-xm", "Cm-mCm-C",
]
BATERIAS = [  # por corchea: k bombo, s caja, h hihat, b bombo+hihat
    "bhsbbhsh", "bhshbhsh", "bbsbhbsh", "bhshbbsh", "bhsbhbsb",
]


def _cuerda(f, dur, brillo=1.0, apagada=False, rng=None):
    n = int(dur * SR)
    N = max(2, int(round(SR / f)))
    x = np.zeros(n)
    exc = rng.uniform(-1, 1, N)
    if brillo < 1.0:  # pulso mas oscuro
        exc = lfilter([1 - brillo], [1, -brillo], exc)
    x[:N] = exc
    g = 0.94 if apagada else 0.996
    a = np.zeros(N + 2); a[0] = 1; a[N] = -g / 2; a[N + 1] = -g / 2
    y = lfilter([1.0], a, x)
    if apagada:
        y *= np.exp(-np.arange(n) / SR * 18)
    return y


def _rasgueo(raiz, dur, tipo, rng, abajo=True):
    if tipo == "x":  # rasguido apagado (scratch)
        y = rng.standard_normal(int(0.05 * SR)) * np.exp(-np.arange(int(0.05 * SR)) / SR * 90) * 0.5
        return y
    notas = [raiz, raiz * 1.4983, raiz * 2] + ([raiz * 2.9966] if tipo == "C" else [])
    if not abajo:
        notas = notas[::-1]
    n = int(dur * SR)
    y = np.zeros(n)
    for i, f in enumerate(notas):
        retardo = int(i * rng.uniform(0.006, 0.011) * SR)
        c = _cuerda(f, dur, brillo=0.5 if tipo == "m" else 0.15, apagada=(tipo == "m"), rng=rng)
        y[retardo:] += c[:n - retardo] * (0.9 if tipo == "m" else 1.0)
    return y


def _distorsion(y, ganancia):
    y = np.tanh(y * ganancia)
    b, a = butter(2, 4800 / (SR / 2), "low"); y = lfilter(b, a, y)
    b, a = butter(1, 90 / (SR / 2), "high"); y = lfilter(b, a, y)
    return y


def _bateria(n_total, beat, patron, compases_fill, rng):
    y = np.zeros(n_total)
    def poner(s, t):
        i = int(t * SR); m = min(len(s), n_total - i)
        if m > 0: y[i:i + m] += s[:m]
    tk = np.arange(int(0.25 * SR)) / SR
    kick = 0.9 * np.sin(2 * np.pi * (50 + 110 * np.exp(-tk * 35)) * tk) * np.exp(-tk * 10)
    ts = np.arange(int(0.2 * SR)) / SR
    snare = (0.5 * rng.standard_normal(len(ts)) + 0.4 * np.sin(2 * np.pi * 185 * ts)) * np.exp(-ts * 18)
    th = np.arange(int(0.05 * SR)) / SR
    hh = rng.standard_normal(len(th)); hh = (hh - np.convolve(hh, np.ones(5) / 5, "same")) * 0.22 * np.exp(-th * 70)
    tc = np.arange(int(1.2 * SR)) / SR
    crash = rng.standard_normal(len(tc)); crash = (crash - np.convolve(crash, np.ones(3) / 3, "same")) * 0.25 * np.exp(-tc * 3)
    t, k = 0.0, 0
    paso = beat / 2
    while t < n_total / SR:
        compas = k // 8
        if k % 32 == 0: poner(crash, t)
        if compas % 4 == 3 and k % 8 >= 4 and compases_fill:  # redoble al final de cada 4 compases
            poner(snare * 0.8, t); poner(snare * 0.6, t + paso / 2)
        else:
            c = patron[k % 8]
            if c in "kb": poner(kick, t)
            if c == "s": poner(snare, t)
            if c in "hb": poner(hh, t)
        t += paso; k += 1
    return y


def rock_variado(total, semilla=0):
    rng = np.random.default_rng(zlib.crc32(str(semilla).encode()))
    bpm = int(rng.integers(116, 146))
    beat = 60 / bpm
    tonica = TONICAS[list(TONICAS)[rng.integers(len(TONICAS))]]
    prog = PROGRESIONES[rng.integers(len(PROGRESIONES))]
    riff_a = RIFFS[rng.integers(len(RIFFS))]
    riff_b = RIFFS[rng.integers(len(RIFFS))]
    bat = BATERIAS[rng.integers(len(BATERIAS))]
    ganancia = rng.uniform(6, 14)
    n_total = int(total * SR)
    guitarra = np.zeros(n_total)
    paso = beat / 2
    t, k = 0.0, 0
    while t < total:
        compas = k // 8
        raiz = tonica * 2 ** (prog[compas % 4] / 12)
        riff = riff_a if (compas // 4) % 2 == 0 else riff_b
        tipo = riff[k % 8]
        if tipo != "-":
            dur = paso * (3 if tipo == "C" else 1.05)
            s = _rasgueo(raiz, dur, tipo, rng, abajo=(k % 2 == 0))
            i = int(t * SR); m = min(len(s), n_total - i)
            # humanizar: pequeno adelanto/atraso y dinamica
            guitarra[i:i + m] += s[:m] * rng.uniform(0.85, 1.0)
        t += paso; k += 1
    guitarra = _distorsion(guitarra / max(1e-9, np.abs(guitarra).max()), ganancia)
    # doble toma (izq/der simulada con leve retardo) para que suene mas gorda
    d = int(0.012 * SR)
    guitarra = 0.6 * guitarra + 0.4 * np.concatenate([np.zeros(d), guitarra[:-d]])
    bateria = _bateria(n_total, beat, bat, True, rng)
    bajo = np.zeros(n_total)
    t, k = 0.0, 0
    while t < total:  # bajo en corcheas siguiendo la raiz
        raiz = tonica * 2 ** (prog[(k // 8) % 4] / 12) / 2
        nt = np.arange(int(paso * SR)) / SR
        s = np.sin(2 * np.pi * raiz * nt) * np.exp(-nt * 6) * 0.5
        i = int(t * SR); m = min(len(s), n_total - i); bajo[i:i + m] += s[:m]
        t += paso; k += 1
    y = 0.55 * guitarra + 0.45 * bateria + 0.35 * bajo
    return y / max(1e-9, np.abs(y).max())


def descripcion(semilla=0):
    rng = np.random.default_rng(zlib.crc32(str(semilla).encode()))
    return f"{int(rng.integers(116, 146))} bpm"
