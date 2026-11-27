import html, re

C = "#2E7D32"      # verd
CL = "#DCEDDC"     # verd clar per a capçaleres de taula
RAW = "https://raw.githubusercontent.com/paumartinezps5-netizen/repo-para-claudia-/claude/busy-newton-dsqx1y/memoria_tasca8/"
P = 'style="line-height:1.15;margin:0 0 7pt 0;"'
LI = 'style="line-height:1.15;margin:0 0 2pt 0;"'
VID = "https://drive.google.com/file/d/1C1Yyn5y2V5U1RfgWP6419OddZYwYJQkM/view?usp=sharing"


def h2(t): return f'<h2 style="font-size:14pt;font-weight:bold;color:{C};margin:14pt 0 6pt 0;">{t}</h2>'
def h3(t): return f'<h3 style="font-size:12pt;font-weight:bold;color:{C};margin:10pt 0 4pt 0;">{t}</h3>'
def p(t): return f"<p {P}>{t}</p>"
def ul(items): return "<ul>" + "".join(f"<li {LI}>{i}</li>" for i in items) + "</ul>"
def cw(t): return html.escape(t)                      # sense lletra de codi dins del text
SP = '<p style="line-height:1.15;margin:0;">&nbsp;</p>'


def table(rows, widths, center=None):
    out = '<table style="border-collapse:collapse;" cellpadding="0" cellspacing="0">'
    for r, row in enumerate(rows):
        out += "<tr>"
        for c, (cell, w) in enumerate(zip(row, widths)):
            bg = f"background-color:{CL};" if r == 0 else ""
            b = "font-weight:bold;" if r == 0 or (center and c in center) else ""
            al = "text-align:center;" if center and c in center else ""
            out += (f'<td width="{w}" style="{bg}border:1px solid #BFBFBF;padding:2pt 6pt;vertical-align:top;">'
                    f'<p style="font-size:10.5pt;margin:0;{b}{al}">{cell}</p></td>')
        out += "</tr>"
    return out + "</table>" + SP


def imgs(items):
    out = '<table style="border-collapse:collapse;margin:0 auto;" cellpadding="0" cellspacing="0"><tr>'
    for f, w, h, cap in items:
        out += (f'<td width="{w + 16}" style="border:1px solid #FFFFFF;padding:0 6pt;vertical-align:bottom;">'
                f'<p style="text-align:center;margin:0;"><img src="{RAW}{f}" width="{w}" height="{h}" alt="{cap}"></p>'
                f'<p style="font-size:9.5pt;color:#555555;text-align:center;margin:2pt 0 0 0;">{cap}</p></td>')
    return out + "</tr></table>" + SP


KW = [("void", "#00979C"), ("int", "#00979C"), ("setup", "#5E6D03"), ("loop", "#5E6D03"),
      ("if", "#5E6D03"), ("switch", "#5E6D03"), ("case", "#5E6D03"), ("break", "#5E6D03"),
      ("pinMode", "#D35400"), ("digitalWrite", "#D35400"), ("digitalRead", "#D35400"), ("delay", "#D35400"), ("randomSeed", "#D35400"), ("random", "#D35400"), ("analogRead", "#D35400"),
      ("OUTPUT", "#00979C"), ("INPUT", "#00979C"), ("HIGH", "#00979C"), ("LOW", "#00979C")]


def lines_html(lines):
    out = []
    for l in lines:
        l = html.escape(l.rstrip(), quote=False)
        parts = re.split(r'(".*?"|//.*$)', l)
        for i in range(0, len(parts), 2):
            for k, col in KW:
                parts[i] = re.sub(rf"\b{k}\b", f'<span style="color:{col};">{k}</span>', parts[i])
        for i in range(1, len(parts), 2):
            if parts[i].startswith("//"):
                parts[i] = f'<span style="color:#95A5A6;">{parts[i]}</span>'
        out.append(("".join(parts) or "&nbsp;").replace("  ", "&nbsp;&nbsp;"))
    return "<br>".join(out)


def code(lines, size=9.5):
    return (f'<p style="font-family:Courier New;font-size:{size}pt;color:#434F54;margin:0 0 10pt 0;line-height:1.0;">'
            + lines_html(lines) + "</p>")


def code_cols(cols, size=9, w=214):
    out = '<table style="border-collapse:collapse;" cellpadding="0" cellspacing="0"><tr>'
    for c in cols:
        out += (f'<td width="{w}" style="border:1px solid #FFFFFF;padding:0 4pt;vertical-align:top;">'
                f'<p style="font-family:Courier New;font-size:{size}pt;color:#434F54;margin:0;line-height:1.0;">'
                + lines_html(c) + "</p></td>")
    return out + "</tr></table>" + SP


GROC, VERD, VERM, OFF = "#E6A800", "#2E9E3E", "#D62828", "#D3D3D3"
ORDRE = [(12, "groc", GROC), (11, "verd", VERD), (10, "vermell", VERM), (9, "verd", VERD), (8, "groc", GROC), (7, "vermell", VERM)]


def dot(col, size=13): return f'<span style="color:{col};font-size:{size}pt;">●</span>'


def steps(items):
    out = '<table style="border-collapse:collapse;" cellpadding="0" cellspacing="0">'
    for i, t in enumerate(items, 1):
        out += (f'<tr><td width="26" style="background-color:{C};border:2px solid #FFFFFF;padding:3pt 0;vertical-align:middle;">'
                f'<p style="font-size:13pt;font-weight:bold;color:#FFFFFF;text-align:center;margin:0;">{i}</p></td>'
                f'<td width="455" style="background-color:#F1F7F1;border:2px solid #FFFFFF;padding:3pt 7pt;vertical-align:middle;">'
                f'<p style="margin:0;line-height:1.15;">{t}</p></td></tr>')
    return out + "</table>" + SP


def snippet(lines, new=()):
    out = []
    for i, l in enumerate(lines):
        h = lines_html([l])
        if i in new:
            h = f'<span style="background-color:{CL};">{h}</span>'
        out.append(h)
    return ('<p style="font-family:Courier New;font-size:9pt;color:#434F54;margin:0;line-height:1.0;">'
            + "<br>".join(out) + "</p>")


def compare(a, b):
    def cell(title, body):
        return (f'<td width="232" style="border:1px solid #BFBFBF;padding:4pt 8pt;vertical-align:top;">'
                f'<p style="font-size:10.5pt;font-weight:bold;color:{C};margin:0 0 3pt 0;">{title}</p>{body}</td>')
    return ('<table style="border-collapse:collapse;" cellpadding="0" cellspacing="0"><tr>'
            + cell(*a) + cell(*b) + "</tr></table>" + SP)


src = open("../tasca8/Dau.ino", encoding="utf-8").read().splitlines()
cs = [i for i, l in enumerate(src) if l.strip().startswith("case")]
assert len(cs) == 6, cs
# 2 columnes (amb 3 les línies es partien); tall just abans del case 4
cols = code_cols([src[:cs[3]], src[cs[3]:]], w=321)

ABANS = ["case 2:", "  digitalWrite(12, HIGH);", "  digitalWrite(11, HIGH);", "  break;"]
ARA = ["case 2:", "  digitalWrite(12, HIGH);", "  digitalWrite(11, HIGH);", "  delay(2000);",
       "  digitalWrite(12, LOW);", "  digitalWrite(11, LOW);", "  break;"]
assert all(l.strip() in [s.strip() for s in src] for l in ARA)

muntatge = [["Element", "On va connectat"]]
muntatge += [[f"{dot(col, 11)} Led {nom}", f"Port {port}"] for port, nom, col in ORDRE]
muntatge += [["Pota curta dels leds", "Línia de menys → resistència de 220 Ω → GND"],
             ["Polsador", "Una pota a 5V i l'altra al port 13, amb la seva resistència"]]

dau = [["Surt"] + [str(p) for p, _, _ in ORDRE]]
dau += [[str(n)] + [dot(col if i < n else OFF, 12) for i, (_, _, col) in enumerate(ORDRE)] for n in range(1, 7)]

body = f"""
<h1 style="font-size:24pt;font-weight:bold;color:{C};margin:0 0 2pt 0;">Tasca 8 – Dau electrònic</h1>
<p style="font-size:12pt;margin:0 0 6pt 0;">Premem el polsador i s'encenen tants leds com el número que ha sortit</p>
<p style="font-size:10.5pt;color:#555555;margin:0;">Pau Martínez Cuadra i Enric Vinyes Huguet</p>
<p style="font-size:10.5pt;color:#555555;margin:0 0 6pt 0;">Robòtica · 1r Batxillerat · 27/11/2026</p>
{h2("1. Descripció de la pràctica")}
{p("Havíem de fer un dau electrònic amb 6 leds: prems el polsador i surt un número de l'1 al 6, com un dau normal.")}
{p("L'enunciat deixava triar entre encendre només el led del número (manera A) o encendre tants leds com el número (manera B). Nosaltres hem fet la B: si surt un 3, s'encenen tres leds.")}
{h2("2. Material")}
{ul(["Arduino UNO i cable USB", "Protoboard", "6 leds: 2 grocs, 2 verds i 2 vermells", "2 resistències: una per als leds (220 Ω) i una per al polsador", "1 polsador", "Cables", "Ordinador amb l'Arduino IDE"])}
{h2("3. Muntatge")}
{p("Els sis leds estan en fila a la part de baix de la protoboard. La pota llarga va al port i la curta a la línia de menys, que va a GND amb una resistència. El polsador està a dalt, entre 5V i el port 13.")}
{table(muntatge, [190, 291])}
{p("El primer led que s'encén és el groc del port 12, el de l'extrem de la fila, i a partir d'aquí van seguint cap a l'altra punta.")}
{imgs([("foto_dalt.jpg", 94, 125, "Vista des de dalt"), ("foto_leds.jpg", 167, 125, "Els sis leds"), ("foto_placa.jpg", 167, 125, "L'Arduino i el polsador")])}
{h2("4. Com hem arribat al codi final")}
{steps(["Vam partir del codi del dau que el Pau va fer l'any passat i el vam deixar amb switch i case, com al Morse de la Tasca 6, perquè ens és més fàcil de seguir que un for.",
        "Quan el provàvem, el led del port 12 es quedava sempre encès. Com que s'encén amb tots els números, no es veia quan acabava una tirada i començava la següent, i això creava confusió. El professor ens va dir que els leds s'havien d'apagar després de cada tirada.",
        "Primer vam posar el delay(2000) i els LOW al final, després del switch, però els leds no s'apagaven.",
        "Al final els vam posar dins de cada case, apagant només els leds que s'havien encès. Així sí que funciona, però com que hi ha sis case els vam haver de canviar un per un, i va ser una mica pesat."])}
{p("Per exemple, el case 2 abans i ara (en verd, el que hi hem afegit):")}
{compare(("Abans", snippet(ABANS)), ("Ara", snippet(ARA, new={3, 4, 5})))}
{h2("5. Descripció i funcionament")}
{h3("5.1. El codi")}
{cols}
{p("Al setup diem que el 13 és d'entrada (el polsador) i del 12 al 7 són de sortida (els leds). El randomSeed(analogRead(0)) llegeix el pin A0, que no té res connectat, i així els números no surten sempre en el mateix ordre quan engeguem la placa.")}
{p("Al loop, si premem el polsador, random(1, 7) treu un número de l'1 al 6 i el guarda a n. El switch mira quin número és i va al case que toca. Cada case encén els seus leds, espera 2 segons i els apaga. El break fa que no segueixi amb el case de sota.")}
{p("Així queden els leds per a cada número:")}
{table(dau, [60] + [50] * 6, center=set(range(7)))}
{p("Mentre dura el delay l'Arduino no mira el polsador, o sigui que si el premem durant aquests 2 segons no passa res.")}
{h3("5.2. El vídeo")}
{p("Al vídeo tirem el dau quatre vegades: surten un 2, un 4 i dos 2 més, i es veu com els leds s'apaguen sols als 2 segons. Al final el gravem de costat perquè es vegin bé els sis leds.")}
{imgs([("video_3.0.jpg", 102, 114, "Surt un 2"), ("video_5.0.jpg", 102, 114, "Surt un 4"), ("video_6.6.jpg", 102, 114, "Als 2 s s'apaguen"), ("video_12.5.jpg", 102, 114, "De costat")])}
{p('Enllaç al vídeo: <a href="' + VID + '">Vídeo Tasca 8 - Dau</a>')}
{h2("6. Opinió personal i possibles millores")}
{p("Aquesta pràctica ens ha sigut bastant fàcil, perquè vam recuperar el codi del dau que el Pau va fer l'any passat. L'hem retocat una mica perquè els leds s'apaguin després de dos segons, ja que el primer led sempre es quedava encès i creava confusió. Canviar-ho ha sigut una mica pesat, però ara es veu clar quan surt cada número.")}
{p("Coses que es podrien millorar:")}
{ul(["Que abans de sortir el número els leds s'encenguin i s'apaguin ràpid uns quants cops, com si el dau rodés.",
     "Fer el codi més curt amb un for, perquè ara cada case repeteix els mateixos digitalWrite."])}
"""

open("memoria.html", "w", encoding="utf-8").write(
    '<!DOCTYPE html><html lang="ca"><head><meta charset="utf-8"><title>Memòria Tasca 8 Dau</title></head><body>'
    + body.strip() + "</body></html>")
print("ok", len(body))
