# Tasca 8 (dau): targeta -> vídeo vertical centrat amb fons difuminat, etiquetes animades
# a la dreta i cara del dau a l'esquerra -> targeta final. So original + música suau.
# Ús: python editar_video_tasca8.py <carpeta amb v.mp4 i musica.wav> <sortida.mp4>
import subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont

D, OUT = sys.argv[1], sys.argv[2]
FF = os.environ["FFMPEG"]
FB, FR, FE = "C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arial.ttf", "C:/Windows/Fonts/seguiemj.ttf"
W, H, FPS, XF, CARD, END = 1280, 720, 30, 0.5, 2.6, 2.6
GREEN = (46, 125, 50)
SRC_END = 18.83
HOLD = 1.2  # congela la cara del final perquè es vegi

# temps del vídeo original (mesurats a partir de la brillantor dels leds)
LABELS = [  # (inici, final, emoji, text; | = salt de línia)
    (0.2, 2.05, "👆", "Premem el|polsador"),
    (2.1, 4.05, "🎲", "Surt un 2:|s'encenen 2 leds"),
    (4.3, 5.6, "🎲", "Ara surt un 4:|4 leds encesos"),
    (5.6, 6.85, "⏱", "Als 2 segons|s'apaguen sols"),
    (6.9, 8.85, "🎲", "Tornem a tirar:|un altre 2"),
    (9.2, 11.15, "🎲", "I un altre 2!"),
    (11.4, 16.2, "👀", "Els 6 leds|vistos de costat"),
    (17.4, SRC_END + HOLD, "😂", "Cameo final"),
]
DICE = [(2.1, 4.05, 2), (4.3, 6.25, 4), (6.9, 8.85, 2), (9.2, 11.15, 2)]


def label_png(path, emo, text):
    fe, ft = ImageFont.truetype(FE, 54), ImageFont.truetype(FB, 34)
    lines = text.split("|")
    h = max(96, 30 + 44 * len(lines))
    im = Image.new("RGBA", (410, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, 409, h - 1), 22, fill=GREEN + (235,))
    d.text((16, (h - 66) // 2), emo, font=fe, embedded_color=True)
    y = (h - 44 * len(lines)) // 2 + 2
    for ln in lines:
        d.text((94, y), ln, font=ft, fill="white"); y += 44
    im.save(path)


def dice_png(path, n):
    s = 210
    im = Image.new("RGBA", (s, s + 60), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, s - 1, s - 1), 34, fill=(255, 255, 255, 245), outline=GREEN, width=8)
    a, b, c = 52, s // 2, s - 52
    pos = {1: [(b, b)], 2: [(a, a), (c, c)], 3: [(a, a), (b, b), (c, c)],
           4: [(a, a), (c, a), (a, c), (c, c)], 5: [(a, a), (c, a), (b, b), (a, c), (c, c)],
           6: [(a, a), (c, a), (a, b), (c, b), (a, c), (c, c)]}[n]
    for x, y in pos:
        d.ellipse((x - 19, y - 19, x + 19, y + 19), fill=GREEN)
    ft = ImageFont.truetype(FB, 32)
    t = f"{n} leds"
    d.rounded_rectangle((0, s + 12, s - 1, s + 58), 14, fill=GREEN + (235,))
    d.text(((s - ft.getlength(t)) / 2, s + 17), t, font=ft, fill="white")
    im.save(path)


def card_png(path, big, small, emo):
    im = Image.new("RGB", (W, H), GREEN)
    d = ImageDraw.Draw(im)
    d.text((90, 205), big, font=ImageFont.truetype(FB, 96), fill="white")
    d.rectangle((90, 330, 180, 336), fill="white")
    d.text((90, 365), small, font=ImageFont.truetype(FR, 48), fill="white")
    d.text((90, 620), "Pau Martínez i Enric Vinyes · Robòtica · 1r Batxillerat",
           font=ImageFont.truetype(FR, 28), fill=(220, 235, 220))
    im.save(path)
    e = Image.new("RGBA", (190, 190), (0, 0, 0, 0))
    ImageDraw.Draw(e).text((10, 10), emo, font=ImageFont.truetype(FE, 150), embedded_color=True)
    e.save(path.replace(".png", "_e.png"))


os.makedirs(f"{D}/ov", exist_ok=True)
card_png(f"{D}/ov/card.png", "Tasca 8", "Dau electrònic", "🎲")
card_png(f"{D}/ov/end.png", "Premem el botó", "i s'encenen tants leds com el número", "🎲")
for i, (s, e, emo, t) in enumerate(LABELS):
    label_png(f"{D}/ov/l{i}.png", emo, t)
for i, (s, e, n) in enumerate(DICE):
    dice_png(f"{D}/ov/d{i}.png", n)

p = lambda x: round(x, 3)
O1 = p(CARD - XF)            # inici del clip principal al vídeo final
O2 = p(O1 + SRC_END + HOLD - XF)    # inici de la targeta final
TOT = p(O2 + END)

inputs = ["-i", f"{D}/v.mp4"]
fc = []
LOOK = "eq=contrast=1.06:saturation=1.1,unsharp=5:5:0.5,fps=30,format=yuv420p,setsar=1"
fc.append(f"[0:v]setpts=PTS-STARTPTS,split[x][y];"
          f"[x]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=22:2,eq=brightness=-0.10[bg];"
          f"[y]scale=-2:{H}:flags=lanczos[fg];[bg][fg]overlay=(W-w)/2:0,format=rgba[m0]")
k, last = 1, "m0"


def add_ov(png, s, e, xt, y, slide):
    global k, last
    dur = p(e - s)
    inputs.extend(["-loop", "1", "-t", str(dur), "-i", png])
    fc.append(f"[{k}:v]format=rgba,fade=in:st=0:d=0.25:alpha=1,fade=out:st={p(dur - 0.25)}:d=0.25:alpha=1,"
              f"setpts=PTS-STARTPTS+{s}/TB[o{k}]")
    x = f"'{xt}+{slide}*pow(max(0,1-(t-{s})/0.35),2)'"
    fc.append(f"[{last}][o{k}]overlay=x={x}:y={y}:eof_action=pass[m{k}]")
    last = f"m{k}"; k += 1


for i, (s, e, emo, t) in enumerate(LABELS):
    add_ov(f"{D}/ov/l{i}.png", s, e, 855, "(H-h)/2", 160)
for i, (s, e, n) in enumerate(DICE):
    add_ov(f"{D}/ov/d{i}.png", s, e, 115, 215, -160)
fc.append(f"[{last}]tpad=stop_mode=clone:stop_duration={HOLD},{LOOK}[main]")

# targetes amb el dau que gira
for name, d in (("card", CARD), ("end", END)):
    inputs.extend(["-loop", "1", "-t", str(d), "-i", f"{D}/ov/{name}.png",
                   "-loop", "1", "-t", str(d), "-i", f"{D}/ov/{name}_e.png"])
    fc.append(f"[{k + 1}:v]format=rgba,rotate='0.35*sin(2*PI*t/1.3)':c=none:ow=270:oh=270[r{k}];"
              f"[{k}:v][r{k}]overlay=x=930:y=(H-h)/2-20,fps=30,format=yuv420p,setsar=1[{name}]")
    k += 2

inputs.extend(["-i", f"{D}/musica.wav"])
mus = k
fc.append(f"[card]settb=1/30[c0];[main]settb=1/30[c1];[end]settb=1/30[c2];"
          f"[c0][c1]xfade=transition=fade:duration={XF}:offset={O1}[v1];"
          f"[v1][c2]xfade=transition=fade:duration={XF}:offset={O2},fade=t=out:st={p(TOT - 0.6)}:d=0.6,format=yuv420p[v]")
D1 = int(O1 * 1000)
fc.append(f"[0:a]afade=t=in:d=0.3,afade=t=out:st={p(SRC_END - 0.4)}:d=0.4,adelay={D1}|{D1},apad,atrim=0:{TOT}[orig];"
          f"[{mus}:a]atrim=0:{TOT},asetpts=PTS-STARTPTS,volume=0.32,afade=t=in:d=0.8,afade=t=out:st={p(TOT - 1.5)}:d=1.5[mu];"
          f"[orig][mu]amix=inputs=2:normalize=0,loudnorm=I=-16:TP=-1.5,aresample=44100[a]")

cmd = [FF, "-hide_banner", "-loglevel", "error", "-y", *inputs, "-filter_complex", ";".join(fc),
       "-map", "[v]", "-map", "[a]", "-t", str(TOT), "-c:v", "libx264", "-preset", "medium", "-crf", "20",
       "-profile:v", "main", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", OUT]
subprocess.run(cmd, check=True)
print("ok", TOT)
