import html, re

C = "#2E7D32"      # verd
CL = "#E3F1E4"     # verd clar per a capçaleres de taula
RAW = "https://raw.githubusercontent.com/paumartinezps5-netizen/repo-para-claudia-/claude/busy-newton-dsqx1y/memoria_tasca5/"
P = 'style="line-height:1.15;margin:0 0 7pt 0;"'
LI = 'style="line-height:1.15;margin:0 0 2pt 0;"'
VID = "https://drive.google.com/file/d/1jE-KkDh4eZrnJPrO563vu6umI3AsbYl3/view?usp=sharing"


def h2(t): return f'<h2 style="font-size:14pt;font-weight:bold;color:{C};margin:14pt 0 6pt 0;">{t}</h2>'
def h3(t): return f'<h3 style="font-size:12pt;font-weight:bold;color:{C};margin:10pt 0 4pt 0;">{t}</h3>'
def p(t): return f"<p {P}>{t}</p>"
def ul(items): return "<ul>" + "".join(f"<li {LI}>{i}</li>" for i in items) + "</ul>"
def cw(t): return html.escape(t)                      # sense lletra de codi dins del text
SP = '<p style="line-height:1.15;margin:0;">&nbsp;</p>'


def table(rows, widths):
    out = '<table style="border-collapse:collapse;" cellpadding="0" cellspacing="0">'
    for r, row in enumerate(rows):
        out += "<tr>"
        for cell, w in zip(row, widths):
            bg = f"background-color:{CL};" if r == 0 else ""
            b = "font-weight:bold;" if r == 0 else ""
            out += (f'<td width="{w}" style="{bg}border:1px solid #BFBFBF;padding:2pt 6pt;vertical-align:top;">'
                    f'<p style="font-size:10.5pt;margin:0;{b}">{cell}</p></td>')
        out += "</tr>"
    return out + "</table>" + SP


def imgs(items):
    out = '<table style="border-collapse:collapse;margin:0 auto;" cellpadding="0" cellspacing="0"><tr>'
    for f, w, h, cap in items:
        out += (f'<td width="{w + 16}" style="border:1px solid #FFFFFF;padding:0 6pt;vertical-align:bottom;">'
                f'<p style="text-align:center;margin:0;"><img src="{RAW}{f}" width="{w}" height="{h}" alt="{cap}"></p>'
                f'<p style="font-size:9.5pt;color:#555555;text-align:center;margin:2pt 0 0 0;">{cap}</p></td>')
    return out + "</tr></table>" + SP


KW = [("void", "#00979C"), ("int", "#00979C"), ("char", "#00979C"), ("setup", "#5E6D03"), ("loop", "#5E6D03"),
      ("if", "#5E6D03"), ("for", "#5E6D03"), ("pinMode", "#D35400"), ("digitalWrite", "#D35400"), ("delay", "#D35400"),
      ("Serial", "#D35400"), ("begin", "#D35400"), ("available", "#D35400"), ("read", "#D35400"),
      ("parseInt", "#D35400"), ("print", "#D35400"), ("println", "#D35400"),
      ("OUTPUT", "#00979C"), ("HIGH", "#00979C"), ("LOW", "#00979C")]


def code(lines, size=10):
    out = []
    for l in lines:
        l = html.escape(l, quote=False)
        # no pintar paraules dins dels textos entre cometes
        parts = re.split(r'(".*?")', l)
        for i in range(0, len(parts), 2):
            for k, col in KW:
                parts[i] = re.sub(rf"\b{k}\b", f'<span style="color:{col};">{k}</span>', parts[i])
        out.append(("".join(parts) or "&nbsp;").replace("  ", "&nbsp;&nbsp;"))
    return (f'<p style="font-family:Courier New;font-size:{size}pt;color:#434F54;margin:0 0 10pt 0;line-height:1.0;">'
            + "<br>".join(out) + "</p>")


src = open("../tasca5/Tasca5_Monitor.ino", encoding="utf-8").read().splitlines()
src = [l for l in src if not l.strip().startswith("//")]   # sense comentaris a la memòria
cols = code(src, 9.5)

pdf = ["char option = Serial.read();",
       "if (option >= '1' && option <= '9') {",
       "  option -= '0';",
       "  for(int i=0;i<option;i++){ ... }"]

body = f"""
<h1 style="font-size:24pt;font-weight:bold;color:{C};margin:0 0 2pt 0;">Tasca 5 – Led i monitor sèrie</h1>
<p style="font-size:12pt;margin:0 0 6pt 0;">1.4 Port sèrie: el led s'encén tantes vegades com el número que escrivim</p>
<p style="font-size:10.5pt;color:#555555;margin:0;">Pau Martínez Cuadra i Enric Vinyes Huguet</p>
<p style="font-size:10.5pt;color:#555555;margin:0 0 6pt 0;">Robòtica · 1r Batxillerat · 03/11/2026</p>
{h2("1. Descripció de la pràctica")}
{p("En aquesta pràctica fem servir el port sèrie perquè l'ordinador i l'Arduino es puguin passar informació. Escrivim un número al monitor sèrie de l'Arduino IDE i el led del port 13 s'encén i s'apaga tantes vegades com el número que hem escrit.")}
{p("A més, l'Arduino ens contesta pel mateix monitor. Ens diu quantes vegades s'encendrà el led i, quan acaba, ens demana un altre número.")}
{h2("2. Material")}
{ul(["Arduino UNO i cable USB", "Protoboard", "1 led vermell", "1 resistència", "Cables", "Ordinador amb l'Arduino IDE (monitor sèrie)"])}
{h2("3. Muntatge")}
{p("El muntatge és el més senzill de totes les tasques: només hi ha un led amb una resistència. La pota llarga del led va al port 13 i la curta a GND. El polsador que surt a les fotos és de tasques anteriors, en aquesta no el fem servir.")}
{table([["Element", "On va connectat"], ["Led vermell (amb resistència)", "Port 13 i GND"], ["Comunicació amb l'ordinador", "Cable USB (pins 0 RX i 1 TX)"]], [200, 200])}
{p("La placa també té un led petit, el L, que està connectat per dins al port 13. Per això, quan el nostre led s'encén, aquest també s'encén.")}
{imgs([("muntatge.jpg", 128, 230, "El muntatge: el led amb la resistència"), ("general.jpg", 330, 184, "El codi i el monitor sèrie a l'ordinador")])}
{h2("4. El port sèrie: què hem après")}
{p("La teoria la vam treure del PDF del port sèrie del Moodle. Aquí expliquem el que vam entendre i també el que ens va costar més.")}
{h3("4.1. Què és el port sèrie")}
{p("Un port és la connexió entre dos aparells per passar-se informació. En un port sèrie els bits van un darrere l'altre per un sol canal, i fa falta una línia per enviar (TX) i una per rebre (RX). En un port paral·lel, en canvi, s'envien per diversos canals alhora. L'USB també és un port sèrie.")}
{p("A l'Arduino UNO el port sèrie fa servir els pins 0 (RX) i 1 (TX), i mentre l'estem fent servir no podem fer servir aquests pins per a res més. Va pel mateix cable USB amb què el programem. Per veure què passa obrim el monitor sèrie de l'IDE, que té una part per escriure i enviar i una altra on surt el que ens envia l'Arduino.")}
{h3("4.2. Les instruccions noves")}
{table([["Instrucció", "Què fa"],
        [cw("Serial.begin(9600)"), "Engega la comunicació. El 9600 és la velocitat, en bits per segon. El monitor sèrie ha d'estar a la mateixa velocitat."],
        [cw("Serial.available()"), "Diu quants caràcters han arribat que encara no hem llegit. Si és més gran que 0, vol dir que hem escrit alguna cosa."],
        [cw("Serial.read()"), "Llegeix un sol caràcter, el primer que ha arribat."],
        [cw("Serial.print()"), "Escriu al monitor sèrie i es queda a la mateixa línia."],
        [cw("Serial.println()"), "Escriu al monitor sèrie i després salta de línia."],
        [cw("Serial.parseInt()"), "Llegeix el número sencer que hem escrit (per exemple 12) i ens el dona com a número de veritat."]], [200, 441])}
{h3("4.3. El que més ens va costar: el codi ASCII")}
{p("Primer vam fer els exemples del PDF. En el primer, la variable " + cw("option") + " guarda el que llegim amb " + cw("Serial.read()") + ". Si és una " + cw("'a'") + " el led s'apaga i si és una " + cw("'b'") + " s'encén. Això ho vam entendre bé.")}
{p("El que ens va fer donar més voltes va ser l'exemple dels números. Quan escrivim un 5 al monitor, l'Arduino no rep el número 5, sinó el caràcter " + cw("'5'") + ". L'ordinador guarda cada caràcter amb un número de la taula ASCII, i el " + cw("'5'") + " hi val 53. Per tant, si féssim el " + cw("for") + " amb " + cw("option") + " tal com arriba, el led faria 53 pampallugues en lloc de 5.")}
{table([["Caràcter que escrivim", "'0'", "'1'", "'5'", "'9'", "'a'", "'b'"],
        ["Valor ASCII que rep l'Arduino", "48", "49", "53", "57", "97", "98"]], [201, 73, 73, 73, 73, 73, 73])}
{p("Per això l'exemple del PDF fa " + cw("option -= '0';") + ". Com que a la taula ASCII els números van seguits, si al " + cw("'5'") + " (53) li restem el " + cw("'0'") + " (48) ens queda 5, que és el valor real.")}
{code(pdf, 9.5)}
{p("Aquí vam entendre la diferència entre posar les cometes o no: " + cw("'5'") + " entre cometes és el caràcter, que val 53, i " + cw("5") + " sense cometes és el número. Si al codi escrivíssim " + cw("option == 5") + " sense cometes, no es compliria mai, perquè el que arriba és el 53.")}
{p("Però aquest sistema té un problema: " + cw("Serial.read()") + " només llegeix un caràcter cada vegada. Si escrivim 12, primer llegeix el " + cw("'1'") + " i després el " + cw("'2'") + ", i el led faria 1 pampallugues i després 2. Per això l'exemple només funciona del 1 al 9.")}
{h3("4.4. La solució que vam trobar: Serial.parseInt()")}
{p("Buscant per internet vam trobar " + cw("Serial.parseInt()") + ". Aquesta funció llegeix tots els caràcters del número i ja ens dona el valor real. Si escrivim 12, ens dona 12, sense haver de restar " + cw("'0'") + " ni pensar en la taula ASCII. Així el codi queda més curt i a més funciona amb números de més d'una xifra. Per això al nostre programa vam fer servir aquesta.")}
{h2("5. Descripció i funcionament")}
{h3("5.1. El codi")}
{cols}
{p("Al setup posem el port 13 com a OUTPUT, engeguem el port sèrie a 9600 i escrivim «Escriu un numero:», perquè sapiguem que ja podem escriure.")}
{p("Al loop, l'" + cw("if") + " amb " + cw("Serial.available()") + " mira si hem escrit alguna cosa. Si és que sí, " + cw("Serial.parseInt()") + " llegeix el número i el guarda a la variable " + cw("n") + ". Si " + cw("n") + " és més gran que 0, l'Arduino ens contesta amb tres instruccions seguides: el text, el número i «vegades». Les dues primeres són " + cw("print") + " perquè tot surti a la mateixa línia, i l'última és " + cw("println") + " per saltar de línia.")}
{p("Després el " + cw("for") + " es repeteix " + cw("n") + " vegades: encén el led, espera 500 ms, l'apaga i espera 500 ms més. Cada pampallugues dura 1 segon. Quan acaba, ens demana un altre número. Si escrivim un 0 o una lletra, " + cw("parseInt") + " dona 0 i, com que no és més gran que 0, no passa res.")}
{h3("5.2. Proves")}
{table([["Número que escrivim", "Què contesta l'Arduino", "Pampallugues", "Temps"],
        ["3", "El led s'encendra 3 vegades", "3", "3 s"],
        ["1", "El led s'encendra 1 vegades", "1", "1 s"],
        ["9", "El led s'encendra 9 vegades", "9", "9 s"],
        ["10", "El led s'encendra 10 vegades", "10", "10 s"],
        ["12", "El led s'encendra 12 vegades", "12", "12 s"],
        ["19", "El led s'encendra 19 vegades", "19", "19 s"]], [137, 275, 151, 79])}
{p("Amb els números de dues xifres també funciona, que era el que no podíem fer amb l'exemple del PDF.")}
{imgs([("cap_on.jpg", 140, 140, "Led encès"), ("cap_off.jpg", 140, 140, "Led apagat"), ("monitor.jpg", 200, 140, "El que ens contesta l'Arduino")])}
{p('Vídeo del funcionament: <a href="' + VID + '">' + VID + "</a>")}
{h2("6. Opinió personal i possibles millores")}
{p("En aquesta pràctica, per primera vegada, l'ordinador i l'Arduino es passen informació, i ja no només fem encendre i apagar leds. Hem après a fer servir " + cw("Serial.begin") + ", " + cw("Serial.available") + ", " + cw("Serial.read") + " i " + cw("Serial.print") + ".")}
{p("El que més ens va costar va ser entendre el codi ASCII de l'exemple del PDF: que el que arriba no és el número sinó un caràcter, que " + cw("'5'") + " i " + cw("5") + " no són el mateix i per què s'havia de restar " + cw("'0'") + ". Hi vam donar moltes voltes. Després vam trobar " + cw("Serial.parseInt()") + ", que agafa directament el valor real i ho fa tot molt més fàcil. Tot i així, creiem que ha estat útil entendre-ho, perquè ara sabem què passa quan l'Arduino llegeix el que escrivim.")}
{p("Possibles millores:")}
{ul(["Que quan el número sigui 1 escrigui «vegada» i no «vegades».",
     "Posar un límit, per exemple 20, perquè si algú escriu 1000 no s'hagi d'esperar més d'un quart d'hora.",
     "Avisar pel monitor quan el que escrivim no és un número.",
     "Fer servir el polsador que ja tenim a la protoboard perquè l'Arduino enviï un missatge a l'ordinador quan l'apretem."])}
"""

open("memoria.html", "w", encoding="utf-8").write(
    '<!DOCTYPE html><html lang="ca"><head><meta charset="utf-8"><title>Memòria Tasca 5 Port sèrie</title></head><body>'
    + body.strip() + "</body></html>")
print("ok", len(body))
