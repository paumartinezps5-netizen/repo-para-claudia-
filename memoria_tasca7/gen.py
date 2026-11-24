import html, re

C = "#6A3D9A"      # lila
CL = "#E8DFF2"     # lila clar per a capçaleres de taula
RAW = "https://raw.githubusercontent.com/paumartinezps5-netizen/repo-para-claudia-/claude/busy-newton-dsqx1y/memoria_tasca7/"
P = 'style="line-height:1.15;margin:0 0 7pt 0;"'
LI = 'style="line-height:1.15;margin:0 0 2pt 0;"'
VID = "https://drive.google.com/file/d/1fLu978DHVbCbbsImocNNSJvtHuRM5CR-/view?usp=sharing"
TK = "https://www.tinkercad.com/things/f1VX2OMWFiM-dazzling-habbi"


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
      ("if", "#5E6D03"), ("for", "#5E6D03"),
      ("pinMode", "#D35400"), ("digitalWrite", "#D35400"), ("digitalRead", "#D35400"), ("delay", "#D35400"),
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


def code_cols(cols, size=7.5):
    out = '<table style="border-collapse:collapse;" cellpadding="0" cellspacing="0"><tr>'
    for c in cols:
        out += (f'<td width="214" style="border:1px solid #FFFFFF;padding:0 4pt;vertical-align:top;">'
                f'<p style="font-family:Courier New;font-size:{size}pt;color:#434F54;margin:0;line-height:1.0;">'
                + lines_html(c) + "</p></td>")
    return out + "</tr></table>" + SP


src = open("../tasca7/Semafor_Polsador_Brunzidor.ino", encoding="utf-8").read().splitlines()
fors = [i for i, l in enumerate(src) if l.strip().startswith("for")]
assert len(fors) == 4, fors
# talla just abans d'un for, perquè cap bucle quedi partit entre columnes
cols = code_cols([src[:fors[0]], src[fors[0]:fors[3]], src[fors[3]:]])

ex = ["for (i=0; i<4; i++) {", " digitalWrite(8,HIGH);", " digitalWrite(3,HIGH);", " delay(300);",
      " digitalWrite(8,LOW);", " digitalWrite(3,LOW);", " delay(300);", "}"]

body = f"""
<h1 style="font-size:24pt;font-weight:bold;color:{C};margin:0 0 2pt 0;">Tasca 7 – Semàfor amb polsador i brunzidor</h1>
<p style="font-size:12pt;margin:0 0 6pt 0;">Un semàfor de cotxes i un de vianants que canvien quan premem el polsador</p>
<p style="font-size:10.5pt;color:#555555;margin:0;">Pau Martínez Cuadra i Enric Vinyes Huguet</p>
<p style="font-size:10.5pt;color:#555555;margin:0 0 6pt 0;">Robòtica · 1r Batxillerat · 24/11/2026</p>
{h2("1. Descripció de la pràctica")}
{p("En aquesta pràctica fem un pas de vianants amb dos semàfors: un per als cotxes (vermell, groc i verd) i un per als vianants (vermell i verd). Normalment els cotxes tenen verd i els vianants vermell. Quan un vianant prem el polsador, el semàfor dels cotxes passa a groc i després a vermell, i els vianants es posen en verd.")}
{p("Mentre els vianants tenen verd, el brunzidor fa uns pitets, com els semàfors de veritat per a les persones cegues. Al final, el verd dels vianants fa pampallugues cada cop més ràpides i el brunzidor pita al mateix ritme, per avisar que s'acaba el temps per creuar.")}
{p("No vam trobar el codi de l'any passat d'aquesta pràctica, i a més aquesta versió demanava més coses. Per això l'hem fet de zero. També l'hem passat al Tinkercad.")}
{h2("2. Material")}
{ul(["Arduino UNO i cable USB", "Protoboard", "5 leds: 2 vermells, 1 groc i 2 verds", "2 resistències de 220 Ω", "1 polsador", "1 brunzidor", "Cables", "Ordinador amb l'Arduino IDE i el Tinkercad"])}
{h2("3. Muntatge")}
{p("Els leds dels cotxes van a la part de dalt de la protoboard i els dels vianants una mica més a la dreta. La pota llarga de cada led va al seu port i la curta va a la línia de menys. Cada semàfor té la seva resistència de 220 Ω, que va de la línia de menys fins a GND. Així, amb dues resistències en tenim prou per als cinc leds.")}
{table([["Element", "On va connectat"],
        ["Led vermell dels cotxes", "Port 13"],
        ["Led groc dels cotxes", "Port 12"],
        ["Led verd dels cotxes", "Port 11"],
        ["Led vermell dels vianants", "Port 9"],
        ["Led verd dels vianants", "Port 8"],
        ["Pota curta dels leds", "Línia de menys → resistència de 220 Ω → GND (una per semàfor)"],
        ["Polsador", "Una pota a 5V i l'altra al port 7"],
        ["Brunzidor", "Port 3 i GND"]], [170, 311])}
{p("L'Enric munta molt bé, i amb tants cables això ens ha ajudat molt.")}
{imgs([("foto_dalt.jpg", 155, 116, "Vista des de dalt"), ("foto2.jpg", 87, 116, "Leds i resistències"), ("foto3.jpg", 155, 116, "Amb el brunzidor i el polsador")])}
{h2("4. El Tinkercad")}
{p("El Tinkercad és una pàgina web on es poden muntar circuits amb Arduino i simular-los sense tenir la placa. Hi posem els components, els connectem amb cables i hi enganxem el codi. Quan cliquem «Inicia la simulació», el circuit funciona com si fos de veritat i, en aquest cas, podem prémer el polsador amb el ratolí.")}
{p("Hem copiat al Tinkercad el mateix circuit que vam muntar a classe: els cinc leds als mateixos ports, una sola resistència per a cada semàfor, el polsador entre 5V i el port 7 i el brunzidor al port 3. Hem posat colors als cables per entendre'l millor: negre per a GND, vermell per a 5V i un color diferent per a cada led.")}
{imgs([("tk_circuit2.jpg", 330, 227, "El circuit al Tinkercad")])}
{imgs([("tk_cotxes.jpg", 230, 93, "Simulació: verd per als cotxes, vermell per als vianants"), ("tk_vianants.jpg", 230, 93, "Simulació: vermell per als cotxes, verd per als vianants")])}
{p("Hi ha dues diferències amb el muntatge real. A la protoboard de classe la línia de menys està partida pel mig, i per això cada semàfor té la seva resistència. Al Tinkercad la línia és sencera, i per separar-los hem fet servir la línia de menys de dalt per als cotxes i la de baix per als vianants. L'altra és el brunzidor: el del Tinkercad és un piezo passiu, que només sona si li enviem una nota amb " + cw("tone()") + ". Amb " + cw("digitalWrite()") + ", com al nostre codi, a la simulació no se sent. El nostre brunzidor de classe sí que sona amb " + cw("digitalWrite()") + ", perquè ja fa el so ell sol.")}
{p('Enllaç al Tinkercad: <a href="' + TK + '">' + TK + "</a>")}
{h2("5. Què hem après")}
{h3("5.1. Llegir un polsador")}
{p("Fins ara només havíem fet servir els ports com a sortida. Aquí el port 7 és una entrada (" + cw("pinMode(7,INPUT)") + "). Amb " + cw("digitalRead(7)") + " l'Arduino mira si hi arriba corrent: quan premem el polsador hi arriben els 5V i llegeix HIGH. L'" + cw("if") + " fa que tota la seqüència del semàfor només passi quan es compleix això.")}
{h3("5.2. Els bucles for")}
{p("Per fer les pampallugues hauríem d'escriure les mateixes línies moltes vegades. Amb un " + cw("for") + " les escrivim un cop i li diem quantes vegades les ha de repetir. La variable " + cw("i") + " comença a 0 i va pujant d'un en un fins que arriba al número que posem.")}
{code(ex)}
{p("Aquest bloc encén i apaga el verd dels vianants i el brunzidor 4 vegades, amb 300 ms cada cop. Després n'hi ha un altre de 6 vegades amb 150 ms i un altre de 8 vegades amb 75 ms. Així les pampallugues van cada cop més ràpid.")}
{h3("5.3. Sincronitzar el led i el brunzidor")}
{p("Perquè el led i el brunzidor vagin junts, els encenem i els apaguem a les mateixes línies, sense cap " + cw("delay") + " entre mig. Com que l'Arduino fa les instruccions tan ràpid, sembla que passin a la vegada.")}
<p style="page-break-before:always;margin:0;"></p>
{h2("6. Descripció i funcionament")}
{h3("6.1. El codi")}
{cols}
{p("Al setup posem els ports dels leds i del brunzidor com a OUTPUT i el del polsador com a INPUT. Al loop, primer encenem el verd dels cotxes (port 11) i el vermell dels vianants (port 9). Aquesta és la posició de repòs, i s'hi queda fins que algú prem el polsador.")}
{p("Quan " + cw("digitalRead(7)") + " llegeix HIGH, el programa fa tota la seqüència:")}
{table([["Pas", "Cotxes", "Vianants", "Brunzidor", "Temps"],
        ["1", "Verd", "Vermell", "–", "2 s d'espera"],
        ["2", "Groc", "Vermell", "–", "1,5 s"],
        ["3", "Vermell", "Vermell", "–", "1 s (seguretat)"],
        ["4", "Vermell", "Verd", "3 pitets", "200 ms sí, 600 ms no"],
        ["5", "Vermell", "Verd que fa pampallugues", "Pita amb el led", "4 × 300, 6 × 150, 8 × 75 ms"],
        ["6", "Vermell", "Verd fix", "Pitet llarg", "1 s"],
        ["7", "Vermell", "Vermell", "–", "1 s (seguretat)"],
        ["8", "Verd", "Vermell", "–", "Torna al repòs"]], [42, 68, 118, 105, 148], center={0})}
{p("Els segons en què els dos semàfors estan en vermell són de seguretat, perquè ningú creui mentre l'altre encara passa. Quan acaba la seqüència, el loop torna a començar i el semàfor queda en repòs fins que tornem a prémer el polsador.")}
{h3("6.2. El vídeo")}
{p("Al vídeo es veu com premem el polsador, el semàfor dels cotxes passa a groc i a vermell, i els vianants es posen en verd mentre el brunzidor pita cada cop més ràpid.")}
{imgs([("video_groc.jpg", 232, 149, "Hem premut el polsador: els cotxes passen a groc"), ("video_vianants.jpg", 232, 149, "Vermell per als cotxes i verd per als vianants")])}
{p('Vídeo: <a href="' + VID + '">' + VID + "</a>")}
{h2("7. Opinió personal i possibles millores")}
{p("Aquesta pràctica ens ha costat bastant. És la més llarga que hem fet fins ara, amb molts cables i moltes coses a la vegada: cinc leds, un polsador i un brunzidor. El que més ens va costar va ser el brunzidor.")}
{p("Al principi el brunzidor no sonava i no aconseguíem que funcionés. Pensàvem que el problema era del codi i en vam provar diverses versions, però al final el problema era el brunzidor, i el professor ens en va deixar un altre. També el vam passar del pin 2 al 3, perquè al 2 no funcionava. Després vam provar de fer-lo sonar amb " + cw("tone()") + ", però sonava molt fluix. Amb " + cw("digitalWrite()") + " sona bé, i per això el codi final el fa servir.")}
{p("El muntatge va anar bé gràcies a l'Enric, que munta molt bé. Al final el semàfor fa tot el que demanava la pràctica i n'estem contents.")}
{p("Possibles millores:")}
{ul(["Posar una resistència a cada led. Amb una sola per semàfor, quan n'hi ha dos d'encesos alhora brillen una mica menys.",
     "Posar una resistència de 10 kΩ del port 7 a GND (resistència de pull-down) o fer servir " + cw("INPUT_PULLUP") + ". Ara, quan no premem, el port 7 queda a l'aire i a vegades pot llegir HIGH sense que ningú premi.",
     "Fer una versió del codi amb " + cw("tone()") + " només per al Tinkercad, perquè allà el piezo només sona així."])}
"""

open("memoria.html", "w", encoding="utf-8").write(
    '<!DOCTYPE html><html lang="ca"><head><meta charset="utf-8"><title>Memòria Tasca 7 Semàfor</title></head><body>'
    + body.strip() + "</body></html>")
print("ok", len(body))
