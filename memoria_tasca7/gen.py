import html, re

C = "#6A3D9A"      # lila
CL = "#E8DFF2"     # lila clar per a capçaleres de taula
RAW = "https://raw.githubusercontent.com/paumartinezps5-netizen/repo-para-claudia-/claude/busy-newton-dsqx1y/memoria_tasca7/"
P = 'style="line-height:1.15;margin:0 0 7pt 0;"'
LI = 'style="line-height:1.15;margin:0 0 2pt 0;"'
VID = "https://drive.google.com/file/d/13URCd0k92le8KIF0xQNIHirZ0gmgZJLJ/view?usp=sharing"
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


def code_cols(cols, size=9):
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
{p("Aquesta vegada havíem de fer un pas de vianants amb dos semàfors: un per als cotxes (vermell, groc i verd) i un per als vianants (vermell i verd). Normalment els cotxes tenen verd i els vianants vermell. Quan algú prem el polsador, el semàfor dels cotxes passa a groc i després a vermell, i els vianants es posen en verd.")}
{p("A més, mentre els vianants tenen verd el brunzidor fa pitets, com els semàfors de veritat per a les persones cegues. Al final el verd parpelleja cada cop més ràpid i el brunzidor pita al mateix ritme, per avisar que s'acaba el temps per creuar.")}
{p("No vam trobar el codi de l'any passat, i aquesta versió a més demanava més coses, així que l'hem fet de zero. També l'hem passat al Tinkercad.")}
{h2("2. Material")}
{ul(["Arduino UNO i cable USB", "Protoboard", "5 leds: 2 vermells, 1 groc i 2 verds", "2 resistències de 220 Ω", "1 polsador", "1 brunzidor", "Cables", "Ordinador amb l'Arduino IDE i el Tinkercad"])}
{h2("3. Muntatge")}
{p("Els leds dels cotxes van a la part de dalt de la protoboard i els dels vianants una mica més a la dreta. La pota llarga de cada led va al seu port i la curta a la línia de menys. Cada semàfor té la seva resistència de 220 Ω, que va de la línia de menys a GND, i així amb dues resistències en tenim prou per als cinc leds.")}
{table([["Element", "On va connectat"],
        ["Led vermell dels cotxes", "Port 13"],
        ["Led groc dels cotxes", "Port 12"],
        ["Led verd dels cotxes", "Port 11"],
        ["Led vermell dels vianants", "Port 9"],
        ["Led verd dels vianants", "Port 8"],
        ["Pota curta dels leds", "Línia de menys → resistència de 220 Ω → GND (una per semàfor)"],
        ["Polsador", "Una pota a 5V i l'altra al port 7"],
        ["Brunzidor", "Port 3 i GND"]], [170, 311])}
{p("Amb tants cables era fàcil equivocar-se, però l'Enric munta molt bé i ho va deixar tot ordenat, i això ens va ajudar molt a l'hora de buscar errors.")}
{imgs([("foto_dalt.jpg", 155, 116, "Vista des de dalt"), ("foto2.jpg", 87, 116, "Leds i resistències"), ("foto3.jpg", 155, 116, "Amb el brunzidor i el polsador")])}
{h2("4. El Tinkercad")}
{p("Hem copiat al Tinkercad el mateix circuit que vam muntar a classe: els cinc leds als mateixos ports, una resistència per a cada semàfor, el polsador entre 5V i el port 7 i el brunzidor al port 3. Hem posat colors als cables per entendre'l millor: negre per a GND, vermell per a 5V i un color diferent per a cada led.")}
{imgs([("tk_circuit2.jpg", 330, 227, "El circuit al Tinkercad")])}
{imgs([("tk_cotxes.jpg", 230, 93, "Simulació: verd per als cotxes, vermell per als vianants"), ("tk_vianants.jpg", 230, 93, "Simulació: vermell per als cotxes, verd per als vianants")])}
{p("Hi ha dues coses diferents del muntatge real. A la nostra protoboard la línia de menys està partida pel mig i al Tinkercad no, així que hem fet servir la de dalt per als cotxes i la de baix per als vianants. I el brunzidor del Tinkercad només sona amb " + cw("tone()") + ", així que a la simulació els pitets no se senten, tot i que els leds funcionen igual.")}
{p('Enllaç al Tinkercad: <a href="' + TK + '">' + TK + "</a>")}
{h2("5. Els problemes que hem tingut")}
{p("El polsador i els bucles " + cw("for") + " ja els havíem fet servir abans, així que la part del codi no ens va costar gaire. El problema gros va ser el brunzidor.")}
{p("Quan ho vam provar el primer cop, els leds anaven bé però el brunzidor no sonava. Vam pensar que era el codi i vam estar una bona estona canviant-lo i provant versions diferents, però no sonava amb cap. Al final vam veure que el codi estava bé i que el que fallava era el brunzidor, i el professor ens en va deixar un altre.")}
{p("Amb el brunzidor nou encara teníem un problema: al pin 2 no funcionava, així que el vam passar al pin 3 i allà sí. Després vam provar de fer-lo sonar amb " + cw("tone()") + ", però sonava molt fluix. Amb " + cw("digitalWrite()") + " sonava bé, i per això el codi final el fa servir.")}
{p("D'aquí ens quedem amb una cosa: quan alguna cosa no funciona, no sempre és culpa del codi. La pròxima vegada, abans de passar-nos tanta estona canviant el programa, primer provarem el component sol per saber si funciona.")}
<br style="page-break-before:always;clear:both">
{h2("6. Descripció i funcionament")}
{h3("6.1. El codi")}
{cols}
{p("Al setup posem els ports dels leds i del brunzidor com a OUTPUT i el del polsador com a INPUT. Al loop encenem el verd dels cotxes (port 11) i el vermell dels vianants (port 9). Aquesta és la posició de repòs, i s'hi queda fins que algú prem el polsador.")}
{p("Quan " + cw("digitalRead(7)") + " llegeix HIGH, el programa fa tota la seqüència. Per a les pampallugues hem fet tres " + cw("for") + " seguits, cada un més ràpid que l'anterior, i dins de cada un encenem i apaguem el led i el brunzidor a la vegada perquè vagin junts:")}
{table([["Pas", "Cotxes", "Vianants", "Brunzidor", "Temps"],
        ["1", "Verd", "Vermell", "–", "2 s d'espera"],
        ["2", "Groc", "Vermell", "–", "1,5 s"],
        ["3", "Vermell", "Vermell", "–", "1 s (seguretat)"],
        ["4", "Vermell", "Verd", "3 pitets", "200 ms sí, 600 ms no"],
        ["5", "Vermell", "Verd que fa pampallugues", "Pita amb el led", "4 × 300, 6 × 150, 8 × 75 ms"],
        ["6", "Vermell", "Verd fix", "Pitet llarg", "1 s"],
        ["7", "Vermell", "Vermell", "–", "1 s (seguretat)"],
        ["8", "Verd", "Vermell", "–", "Torna al repòs"]], [42, 68, 118, 105, 148], center={0})}
{p("Els dos moments en què tots dos semàfors estan en vermell són de seguretat, perquè ningú creui mentre l'altre encara passa.")}
{h3("6.2. El vídeo")}
{p("Al vídeo es veu el semàfor dels cotxes passant a groc i a vermell, i els vianants en verd mentre el brunzidor pita cada cop més ràpid. Hi hem afegit un zoom als leds, perquè des de lluny costaven de veure, i hem tret el soroll de la classe perquè només se senti el brunzidor, amb una mica de música de fons.")}
{imgs([("video_groc.jpg", 232, 149, "Els cotxes passen a groc"), ("video_vianants.jpg", 232, 149, "Vermell per als cotxes i verd per als vianants")])}
{p('Vídeo: <a href="' + VID + '">' + VID + "</a>")}
{h2("7. Opinió personal i possibles millores")}
{p("Aquesta pràctica ens ha costat bastant, sobretot per culpa del brunzidor. Vam perdre molt de temps buscant un error al codi que no hi era, i això fa ràbia. Però quan per fi vam sentir els pitets i vam veure el semàfor fent tota la seqüència, va valer la pena. És la pràctica més completa que hem fet fins ara i n'estem contents.")}
{p("També hem vist que, quan hi ha tants cables, tenir el muntatge ben fet és mitja feina. En això l'Enric és molt bo, i gràcies a ell no hem hagut de buscar errors de connexions.")}
{p("Possibles millores:")}
{ul(["Afegir un display de 7 segments amb un compte enrere, perquè els vianants sàpiguen quants segons els queden per creuar.",
     "Fer que els cotxes tinguin un temps mínim de verd. Ara, si algú prem el polsador just quan s'acaba la seqüència, els cotxes tornen a parar de seguida.",
     "Posar un sensor de llum (LDR) perquè a la nit el semàfor dels cotxes quedi en groc intermitent, com passa en alguns semàfors de veritat."])}
"""

open("memoria.html", "w", encoding="utf-8").write(
    '<!DOCTYPE html><html lang="ca"><head><meta charset="utf-8"><title>Memòria Tasca 7 Semàfor</title></head><body>'
    + body.strip() + "</body></html>")
print("ok", len(body))
