import sys
import wave

import numpy as np

out = sys.argv[1]
SR = 44100
BPM = 92
beat = 60 / BPM
bar = 4 * beat
CHORDS = [
    [57, 60, 64, 69],
    [53, 57, 60, 65],
    [48, 52, 55, 60],
    [55, 59, 62, 67],
]
BARS = 24
n = int(BARS * bar * SR) + SR
mix = np.zeros(n)


def hz(m):
    return 440 * 2 ** ((m - 69) / 12)


def add(sig, start):
    i = int(start * SR)
    j = min(n, i + len(sig))
    mix[i:j] += sig[: j - i]


def pad(freq, dur):
    t = np.arange(int(dur * SR)) / SR
    s = sum(np.sin(2 * np.pi * freq * k * t + k) / k ** 1.6 for k in range(1, 6))
    s += 0.5 * np.sin(2 * np.pi * freq * 1.003 * t)
    env = np.minimum(1, t / 0.6) * np.minimum(1, (dur - t) / 0.8)
    return s * env


def pluck(freq, dur):
    t = np.arange(int(dur * SR)) / SR
    s = np.sin(2 * np.pi * freq * t) + 0.3 * np.sin(4 * np.pi * freq * t)
    return s * np.exp(-t * 5)


def kick():
    t = np.arange(int(0.35 * SR)) / SR
    f = 50 + 70 * np.exp(-t * 25)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)


def hat():
    t = np.arange(int(0.06 * SR)) / SR
    s = np.random.default_rng(1).standard_normal(len(t))
    s = np.diff(s, prepend=0)
    return s * np.exp(-t * 70)


for b in range(BARS):
    ch = CHORDS[b % 4]
    t0 = b * bar
    for m in ch:
        add(0.10 * pad(hz(m), bar + 0.4), t0)
    add(0.16 * pad(hz(ch[0] - 12), bar + 0.4), t0)
    arp = [ch[0], ch[2], ch[3] + 0, ch[1] + 12, ch[2] + 12, ch[3], ch[1], ch[2]]
    for k, m in enumerate(arp):
        add(0.07 * pluck(hz(m + 12), beat), t0 + k * beat / 2)
    if b >= 2:
        for k in range(4):
            if k in (0, 2):
                add(0.45 * kick(), t0 + k * beat)
            add(0.05 * hat(), t0 + k * beat + beat / 2)

mix /= np.max(np.abs(mix)) * 1.15
fade = int(3 * SR)
mix[:SR] *= np.linspace(0, 1, SR)
mix[-fade:] *= np.linspace(1, 0, fade)
pcm = (mix * 32767).astype(np.int16)
with wave.open(out, "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print(out, len(pcm) / SR)
