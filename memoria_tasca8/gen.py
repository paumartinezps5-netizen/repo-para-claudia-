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


def code_cols(cols, size=9):
    out = '<table style="border-collapse:collapse;" cellpadding="0" cellspacing="0"><tr>'
    for c in cols:
        out += (f'<td width="214" style="border:1px solid #FFFFFF;padding:0 4pt;vertical-align:top;">'
                f'<p style="font-family:Courier New;font-size:{size}pt;color:#434F54;margin:0;line-height:1.0;">'
                + lines_html(c) + "</p></td>")
    return out + "</tr></table>" + SP


src = open("../tasca8/Dau.ino", encoding="utf-8").read().splitlines()
cs = [i for i, l in enumerate(src) if l.strip().startswith("case")]
assert len(cs) == 6, cs
# talla just abans d'un case, perquè cap case quedi partit entre columnes
cols = code_cols([src[:cs[2]], src[cs[2]:cs[4]], src[cs[4]:]])

body = f"""
<h1 style="font-size:24pt;font-weight:bold;color:{C};margin:0 0 2pt 0;">Tasca 8 – Dau electrònic</h1>
<p style="font-size:12pt;margin:0 0 6pt 0;">Premem el polsador i s'encenen tants leds com el número que ha sortit</p>
<p style="font-size:10.5pt;color:#555555;margin:0;">Pau Martínez Cuadra i Enric Vinyes Huguet</p>
<p style="font-size:10.5pt;color:#555555;margin:0 0 6pt 0;">Robòtica · 1r Batxillerat · 27/11/2026</p>
{h2("1. Descripció de la pràctica")}
{p("En aquesta tasca havíem de fer un dau electrònic amb 6 leds. Quan premem el polsador, ha de sortir un número de l'1 al 6, com si tiréssim un dau de sis cares.")}
{p("Es podia fer de dues maneres: que s'encengués només el led del número que surt, o que s'encenguessin tants leds com el número. Nosaltres hem triat la segona: si surt un 3, s'encenen tres leds.")}
{p("Per començar vam recuperar el codi del dau que el Pau va fer l'any passat, i després l'hem retocat perquè els leds s'apaguin sols al cap de dos segons.")}
{h2("2. Material")}
{ul(["Arduino UNO i cable USB", "Protoboard", "6 leds: 2 vermells, 2 grocs i 2 verds", "2 resistències: una per als leds (220 Ω) i una per al polsador", "1 polsador", "Cables", "Ordinador amb l'Arduino IDE"])}
{h2("3. Muntatge")}
{p("Els sis leds van en fila a la part de baix de la protoboard. La pota llarga de cada led va al seu port i la curta a la línia de menys, que està connectada a GND amb una resistència. El polsador està a la part de dalt i va connectat a 5V i al port 13.")}
{table([["Element", "On va connectat"],
        ["Led groc (el primer que s'encén)", "Port 12"],
        ["Led verd", "Port 11"],
        ["Led vermell", "Port 10"],
        ["Led verd", "Port 9"],
        ["Led groc", "Port 8"],
        ["Led vermell (l'últim)", "Port 7"],
        ["Pota curta dels leds", "Línia de menys → resistència de 220 Ω → GND"],
        ["Polsador", "Una pota a 5V i l'altra al port 13, amb la seva resistència"]], [190, 291])}
{p("L'ordre dels ports és important: els leds s'encenen sempre començant pel 12, així que el número es llegeix comptant des del led groc del final de la fila. L'Enric, que munta molt bé, ho va deixar tot ben ordenat.")}
{imgs([("foto_dalt.jpg", 87, 116, "Vista des de dalt"), ("foto_leds.jpg", 155, 116, "Els sis leds"), ("foto_placa.jpg", 155, 116, "L'Arduino i el polsador")])}
{h2("4. Els problemes que hem tingut")}
{p("Aquesta pràctica ens ha anat bastant bé, perquè ja teníem la base del codi de l'any passat. El que vam haver de canviar va ser que, quan tiràvem el dau, el primer led es quedava sempre encès. Com que el led del port 12 s'encén amb tots els números, no quedava clar quan acabava una tirada i començava la següent, i això creava confusió.")}
{p("El professor ens va dir que els leds s'havien d'apagar després de cada tirada. Per fer-ho, a cada " + cw("case") + " hi hem afegit un " + cw("delay(2000)") + " i després hem apagat amb " + cw("LOW") + " els mateixos leds que havíem encès. Com que hi ha sis " + cw("case") + " i cadascun encén un nombre diferent de leds, ho vam haver de canviar un per un, i va ser una mica pesat.")}
<br style="page-break-before:always;clear:both">
{h2("5. Descripció i funcionament")}
{h3("5.1. El codi")}
{cols}
{p("Al setup, a més de dir quins ports són de sortida i quin d'entrada, hi ha " + cw("randomSeed(analogRead(0))") + ". Això fa servir el soroll del pin A0, que no està connectat a res, perquè cada vegada que engeguem la placa els números no surtin en el mateix ordre.")}
{p("Al loop, quan premem el polsador, " + cw("random(1, 7)") + " tria un número entre l'1 i el 6 (el 7 no hi entra mai) i el guarda a " + cw("n") + ". Després, el " + cw("switch") + " mira quin número ha sortit i va al " + cw("case") + " que toca. Cada " + cw("case") + " encén els seus leds, espera dos segons i els torna a apagar. El " + cw("break") + " fa que el programa surti del " + cw("switch") + " i no continuï amb el " + cw("case") + " de sota.")}
{table([["Número", "Leds que s'encenen", "Ports"],
        ["1", "1 led", "12"],
        ["2", "2 leds", "12 i 11"],
        ["3", "3 leds", "12, 11 i 10"],
        ["4", "4 leds", "12, 11, 10 i 9"],
        ["5", "5 leds", "12, 11, 10, 9 i 8"],
        ["6", "Tots 6", "12, 11, 10, 9, 8 i 7"]], [70, 160, 251], center={0})}
{p("Mentre dura el " + cw("delay(2000)") + " l'Arduino no llegeix el polsador, així que si el premem durant aquests dos segons no passa res. Quan els leds s'apaguen, ja es pot tornar a tirar.")}
{h3("5.2. El vídeo")}
{p("Al vídeo tirem el dau unes quantes vegades. Surten un 2, un 4 i dos 2 més, i es veu com els leds s'apaguen sols al cap de dos segons. Al final també el gravem de costat.")}
{imgs([("video_3.0.jpg", 130, 146, "Surt un 2: s'encenen 2 leds"), ("video_5.0.jpg", 130, 146, "Surt un 4: s'encenen 4 leds")])}
{p('Vídeo: <a href="' + VID + '">' + VID + "</a>")}
{h2("6. Opinió personal i possibles millores")}
{p("Aquesta pràctica ens ha sigut bastant fàcil, perquè vam recuperar el codi del dau que el Pau va fer l'any passat. L'hem retocat una mica perquè els leds s'apaguin al cap de dos segons, ja que el primer led sempre es quedava encès i creava confusió. Aquest canvi l'hem fet nosaltres, i ha sigut una mica pesat, però ara el dau s'entén molt millor.")}
{p("Possibles millores:")}
{ul(["Fer que el dau «rodi»: abans de mostrar el número, encendre leds a l'atzar durant un segon, com si el dau estigués girant.",
     "Escriure cada número que surt al monitor sèrie i, després de moltes tirades, comprovar que tots els números surten més o menys les mateixes vegades.",
     "Escurçar el codi amb un " + cw("for") + " que encengui els leds del 12 cap avall. Així, si s'ha de canviar alguna cosa, no caldria fer-ho als sis " + cw("case") + "."])}
"""

open("memoria.html", "w", encoding="utf-8").write(
    '<!DOCTYPE html><html lang="ca"><head><meta charset="utf-8"><title>Memòria Tasca 8 Dau</title></head><body>'
    + body.strip() + "</body></html>")
print("ok", len(body))
