import html, re

C = "#1F5C99"      # blau
CL = "#DCE6F2"     # blau clar per a capçaleres de taula
RAW = "https://raw.githubusercontent.com/paumartinezps5-netizen/repo-para-claudia-/claude/busy-newton-dsqx1y/memoria_tasca5/"
P = 'style="line-height:1.15;margin:0 0 7pt 0;"'
LI = 'style="line-height:1.15;margin:0 0 2pt 0;"'
VID = "https://drive.google.com/file/d/1jE-KkDh4eZrnJPrO563vu6umI3AsbYl3/view?usp=sharing"   # vídeo de la Tasca 5


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
      ("pinMode", "#D35400"), ("digitalWrite", "#D35400"), ("delay", "#D35400"),
      ("Serial", "#D35400"), ("begin", "#D35400"), ("available", "#D35400"), ("read", "#D35400"),
      ("println", "#D35400"), ("OUTPUT", "#00979C"), ("HIGH", "#00979C"), ("LOW", "#00979C")]


def lines_html(lines):
    out = []
    for l in lines:
        l = html.escape(l.rstrip(), quote=False)
        # no pintar paraules dins dels textos entre cometes
        parts = re.split(r'(".*?")', l)
        for i in range(0, len(parts), 2):
            for k, col in KW:
                parts[i] = re.sub(rf"\b{k}\b", f'<span style="color:{col};">{k}</span>', parts[i])
        out.append(("".join(parts) or "&nbsp;").replace("  ", "&nbsp;&nbsp;"))
    return "<br>".join(out)


def code(lines, size=9.5):
    return (f'<p style="font-family:Courier New;font-size:{size}pt;color:#434F54;margin:0 0 10pt 0;line-height:1.0;">'
            + lines_html(lines) + "</p>")


def code_cols(lines, n=3, size=7.5):
    # talla només entre blocs (línies en blanc), perquè cap case quedi partit entre columnes
    blocks, cur = [], []
    for l in lines:
        if l.strip():
            cur.append(l)
        elif cur:
            blocks.append(cur); cur = []
    blocks.append(cur)
    total = sum(len(b) for b in blocks)
    cols, cur = [], []
    for b in blocks:
        if cur and len(cols) < n - 1 and len(cur) + len(b) / 2 > total / n:
            cols.append(cur); cur = []
        cur += b
    cols.append(cur)
    out = '<table style="border-collapse:collapse;" cellpadding="0" cellspacing="0"><tr>'
    for c in cols:
        out += (f'<td width="214" style="border:1px solid #FFFFFF;padding:0 4pt;vertical-align:top;">'
                f'<p style="font-family:Courier New;font-size:{size}pt;color:#434F54;margin:0;line-height:1.0;">'
                + lines_html(c) + "</p></td>")
    return out + "</tr></table>" + SP


src = open("../tasca6/Tasca6_Morse_AZ.ino", encoding="utf-8").read().splitlines()
cols = code_cols(src)

ex = ["case 'A':", "case 'a':", "  punt();", "  ratlla();", "  delay(PausaLletra);", "  break;"]

MORSE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
         "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",
         "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.."}
def mc(c): return " ".join("·" if k == "." else "–" for k in c)
ks = list(MORSE)
mrows = [["Lletra", "Codi"] * 4]
for i in range(7):
    row = []
    for g in range(4):
        j = g * 7 + i
        row += [ks[j], mc(MORSE[ks[j]])] if j < len(ks) else ["", ""]
    mrows.append(row)

body = f"""
<h1 style="font-size:24pt;font-weight:bold;color:{C};margin:0 0 2pt 0;">Tasca 6 – Codi Morse</h1>
<p style="font-size:12pt;margin:0 0 6pt 0;">El led fa en Morse la lletra que escrivim al monitor sèrie</p>
<p style="font-size:10.5pt;color:#555555;margin:0;">Pau Martínez Cuadra i Enric Vinyes Huguet</p>
<p style="font-size:10.5pt;color:#555555;margin:0 0 6pt 0;">Robòtica · 1r Batxillerat · 10/11/2026</p>
{h2("1. Descripció de la pràctica")}
{p("En aquesta pràctica fem que el led del port 13 faci en codi Morse la lletra que escrivim al monitor sèrie. Cada lletra és una combinació de punts (el led s'encén poca estona) i ratlles (s'encén més estona). A més, el monitor ens va escrivint «punt» o «ratlla» cada vegada.")}
{p("El professor ens va donar un codi d'exemple que només feia la A, la B i la C. Nosaltres l'hem ampliat amb totes les lletres fins a la Z.")}
{h2("2. Material")}
{ul(["Arduino UNO i cable USB", "Protoboard", "1 led vermell", "1 resistència", "Cables", "Ordinador amb l'Arduino IDE (monitor sèrie)"])}
{h2("3. Muntatge")}
{p("El muntatge és el mateix que el de la Tasca 5: un led amb una resistència, amb la pota llarga al port 13 i la curta a GND. El led L de la placa també està connectat al port 13, així que també fa el Morse.")}
{table([["Element", "On va connectat"], ["Led vermell (amb resistència)", "Port 13 i GND"], ["Comunicació amb l'ordinador", "Cable USB (pins 0 RX i 1 TX)"]], [200, 200])}
{p("Aquesta vegada se'ns va oblidar fer fotos i gravar el vídeo a classe. Com que el muntatge és exactament el mateix, hem reaprofitat les fotos de la Tasca 5.")}
{imgs([("muntatge.jpg", 128, 230, "El muntatge (foto de la Tasca 5, és el mateix)"), ("general.jpg", 330, 184, "L'ordinador i la placa (a la pantalla hi ha el codi de la Tasca 5)")])}
{h2("4. Què hem après")}
{h3("4.1. El codi Morse")}
{p("Abans d'aquesta pràctica no sabíem com funcionava el Morse. Cada lletra té assignada la seva combinació de punts i ratlles. Per exemple, la A és un punt i una ratlla, i la S són tres punts. Per fer el codi vam haver de buscar la de cada lletra:")}
{table(mrows, [55, 65] * 4, center={0, 2, 4, 6})}
{h3("4.2. El que ja sabíem de la Tasca 5")}
{p("Tota la part del port sèrie ja la coneixíem de la pràctica anterior, i aquí només l'hem hagut d'aplicar: " + cw("Serial.begin(9600)") + " per engegar la comunicació, " + cw("Serial.available()") + " per saber si hem escrit alguna cosa, " + cw("Serial.read()") + " per llegir el que hem escrit i " + cw("Serial.println()") + " per escriure al monitor.")}
{p("Aquí " + cw("Serial.read()") + " ens va bé, perquè cada lletra és un sol caràcter. I com que el que arriba és el caràcter, als " + cw("case") + " la lletra va entre cometes (" + cw("'A'") + "), igual que a la Tasca 5 vam veure que " + cw("'5'") + " entre cometes no és el mateix que " + cw("5") + ".")}
{h3("4.3. El que és nou: switch, case i break")}
{p("El " + cw("switch") + " mira el valor de la variable " + cw("val") + ", que és la lletra que hem escrit, i salta directament al " + cw("case") + " d'aquella lletra. Dins de cada " + cw("case") + " cridem " + cw("punt()") + " i " + cw("ratlla()") + " en l'ordre que toca.")}
{code(ex)}
{p("El " + cw("break") + " serveix per sortir del " + cw("switch") + " quan la lletra ja està feta. Si no el poséssim, l'Arduino continuaria fent les lletres que hi ha a sota.")}
{p("Cada lletra té dos " + cw("case") + " seguits, un per a la majúscula i un per a la minúscula. Com que el primer no té res a dins, passa directament al segon, i així funciona tant si escrivim A com a.")}
{h2("5. Descripció i funcionament")}
{h3("5.1. El codi")}
{cols}
{p("A dalt de tot hi ha les variables dels temps: el punt dura 100 ms, la ratlla 200 ms i entre lletra i lletra hi ha una pausa d'1 segon. Després hi ha les dues subrutines, " + cw("punt()") + " i " + cw("ratlla()") + ": encenen el led, esperen, l'apaguen, esperen el mateix temps i escriuen «punt» o «ratlla» al monitor. Així no hem de repetir aquestes línies a cada lletra.")}
{p("Al setup posem el port 13 com a OUTPUT i engeguem el port sèrie a 9600. Al loop, si hem escrit alguna cosa, " + cw("Serial.read()") + " llegeix la lletra, la guarda a " + cw("val") + " i el " + cw("switch") + " fa el " + cw("case") + " que toca.")}
{p("Si escrivim una paraula sencera, les lletres arriben una darrere l'altra i l'Arduino les va fent per ordre. Si escrivim un número o un símbol, no hi ha cap " + cw("case") + " per a ell i no passa res.")}
{h3("5.2. Què fa amb cada lletra")}
{table([["Escrivim", "Què fa el led", "Què surt al monitor"],
        ["A", "1 curta i 1 llarga", "punt, ratlla"],
        ["E", "1 curta", "punt"],
        ["T", "1 llarga", "ratlla"],
        ["S", "3 curtes", "punt, punt, punt"],
        ["O", "3 llargues", "ratlla, ratlla, ratlla"],
        ["SOS", "3 curtes, 3 llargues i 3 curtes", "punt ×3, ratlla ×3, punt ×3"]], [90, 210, 181])}
{p("Escrivint SOS fem el mateix que a la Tasca 2, però ara des del monitor sèrie i sense haver de fer un programa només per a això.")}
{p("Com que se'ns va oblidar gravar el vídeo, posem el de la Tasca 5, que té el mateix muntatge i també fa servir el monitor sèrie. La diferència és que allà escrivíem un número i aquí escrivim una lletra.")}
{p('Vídeo (Tasca 5): <a href="' + VID + '">' + VID + "</a>")}
{h2("6. Opinió personal i possibles millores")}
{p("Aquesta pràctica ens ha semblat bastant fàcil, perquè tota la part del port sèrie ja la vam aprendre a la Tasca 5 i només l'hem hagut d'aplicar. El que sí que era nou eren el " + cw("switch") + ", el " + cw("case") + " i el " + cw("break") + ", que els hem après en aquesta sessió.")}
{p("També vam haver de mirar com era el codi Morse, perquè no sabíem que cada lletra té els seus punts i ratlles assignats. Un cop ho vam tenir, afegir les lletres de la D a la Z era anar seguint el mateix patró.")}
{p("Se'ns va oblidar gravar el vídeo i fer fotos. La pròxima vegada ho farem a classe mateix.")}
{p("Possibles millores:")}
{ul(["Fer la ratlla més llarga, de 300 ms (el triple del punt, com en el Morse de veritat), perquè amb 100 i 200 ms costa distingir el punt de la ratlla.",
     "Afegir els números del 0 al 9.",
     "Que el monitor, a més de «punt» i «ratlla», escrigui quina lletra està fent.",
     "Fer una pausa més llarga quan escrivim un espai, per separar les paraules."])}
"""

open("memoria.html", "w", encoding="utf-8").write(
    '<!DOCTYPE html><html lang="ca"><head><meta charset="utf-8"><title>Memòria Tasca 6 Codi Morse</title></head><body>'
    + body.strip() + "</body></html>")
print("ok", len(body))
