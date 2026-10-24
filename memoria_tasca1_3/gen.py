import html, re

C = "#D9480F"      # taronja
CL = "#FBE3D6"     # to clar per a capçaleres de taula
RAW = "https://raw.githubusercontent.com/paumartinezps5-netizen/repo-para-claudia-/claude/busy-newton-dsqx1y/memoria_tasca1_3/"
P = 'style="line-height:1.15;margin:0 0 7pt 0;"'
LI = 'style="line-height:1.15;margin:0 0 2pt 0;"'
VID = "https://drive.google.com/file/d/1Ob4sw5UbXOHw9vyGgA10awgyx2JbU93W/view?usp=sharing"
PEND = '<span style="background-color:#FFF200;">[{}]</span>'


def h2(t): return f'<h2 style="font-size:14pt;font-weight:bold;color:{C};margin:14pt 0 6pt 0;">{t}</h2>'
def h3(t): return f'<h3 style="font-size:12pt;font-weight:bold;color:{C};margin:10pt 0 4pt 0;">{t}</h3>'
def p(t): return f"<p {P}>{t}</p>"
def ul(items): return "<ul>" + "".join(f"<li {LI}>{i}</li>" for i in items) + "</ul>"
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


KW = [("void", "#00979C"), ("setup", "#5E6D03"), ("loop", "#5E6D03"), ("pinMode", "#D35400"),
      ("digitalWrite", "#D35400"), ("delay", "#D35400"), ("OUTPUT", "#00979C"), ("HIGH", "#00979C"), ("LOW", "#00979C")]


def code(lines, size=10):
    out = []
    for l in lines:
        l = html.escape(l)
        for k, col in KW:
            l = re.sub(rf"\b{k}\b", f'<span style="color:{col};">{k}</span>', l)
        out.append(l or "&nbsp;")
    return (f'<p style="font-family:Courier New;font-size:{size}pt;color:#434F54;margin:0 0 10pt 0;line-height:1.0;">'
            + "<br>".join(out) + "</p>")


src = open("Tasca1_3_Semafor.ino", encoding="utf-8").read().splitlines()
src = [l for l in src if not l.startswith("//")]          # sense comentaris a la memòria
cut = src.index("digitalWrite(8,HIGH);") + 2                # parteix el codi en dues columnes
cols = (f'<table style="border-collapse:collapse;" cellpadding="0" cellspacing="0"><tr>'
        f'<td width="260" style="border:1px solid #FFFFFF;padding:0 6pt 0 0;vertical-align:top;">{code(src[:cut])}</td>'
        f'<td width="260" style="border:1px solid #FFFFFF;padding:0 6pt 0 0;vertical-align:top;">{code(src[cut:])}</td>'
        f"</tr></table>")

body = f"""
<h1 style="font-size:24pt;font-weight:bold;color:{C};margin:0 0 2pt 0;">Tasca 4 – Semàfor</h1>
<p style="font-size:12pt;margin:0 0 6pt 0;">1.3 Semàfor de cotxes i vianants (nivell bàsic)</p>
<p style="font-size:10.5pt;color:#555555;margin:0;">Pau Martínez Cuadra i Enric Vinyes Huguet</p>
<p style="font-size:10.5pt;color:#555555;margin:0 0 6pt 0;">Robòtica · 1r Batxillerat · 23/10/2026</p>
{h2("1. Descripció de la pràctica")}
{p("En aquesta pràctica fem un semàfor amb cinc leds: tres per als cotxes (vermell, groc i verd) i dos per als vianants (vermell i verd). Primer el vam fer al Tinkercad i després el vam muntar a la protoboard amb l'Arduino.")}
{p("El semàfor comença amb el verd dels cotxes i el vermell dels vianants. Després els cotxes passen a groc i a vermell, i llavors s'encén el verd dels vianants. Abans de tornar a vermell, el verd dels vianants fa pampallugues per avisar que s'acaba. Després torna a començar i el cicle es va repetint.")}
{h2("2. Material")}
{ul(["Arduino UNO i cable USB", "Protoboard", "5 leds: 2 vermells, 2 verds i 1 groc", "Resistències", "Cables", "Ordinador amb l'Arduino IDE i el Tinkercad"])}
{h2("3. Muntatge")}
{p("Vam aprofitar la protoboard de les tasques anteriors. El polsador que surt a les fotos és de les tasques 2 i 3, en aquesta no el fem servir. Cada led té la pota llarga connectada a un port de l'Arduino:")}
{table([["Led", "Port"], ["Vermell dels cotxes", "13"], ["Groc dels cotxes", "12"], ["Verd dels cotxes", "11"], ["Vermell dels vianants", "9"], ["Verd dels vianants", "8"]], [190, 80])}
{imgs([("muntatge_costat.jpg", 204, 153, "Els cinc leds: a l'esquerra els dels cotxes i a la dreta els dels vianants"), ("muntatge_dalt.jpg", 115, 153, "El muntatge sencer")])}
{h3("3.1. Circuit al Tinkercad")}
{p("Abans de muntar-lo de veritat, vam tornar a provar al Tinkercad el circuit que ja teníem de 4t d'ESO, amb els mateixos ports. A la dreta de la captura hi ha el codi, que és el mateix que després vam passar a l'Arduino.")}
{imgs([("tinkercad.png", 540, 279, "El circuit i el codi al Tinkercad")])}
{h2("4. Descripció i funcionament")}
{h3("4.1. El codi")}
{cols}
{p("Al setup posem els cinc ports dels leds com a OUTPUT amb pinMode. Això només es fa una vegada, quan s'engega l'Arduino.")}
{p("Al loop hi ha tot el semàfor. Només fem servir dues funcions: digitalWrite, que encén un led amb HIGH o l'apaga amb LOW, i delay, que fa esperar l'Arduino els mil·lisegons que li diem (1000 ms és 1 segon). Mentre està al delay, els leds es queden com estaven. Quan arriba al final del loop, torna a començar per dalt i el cicle es repeteix sol.")}
{h3("4.2. Les fases del semàfor")}
{table([["Fase", "Cotxes", "Vianants", "Temps"],
        ["1", "Verd", "Vermell", "5 s"],
        ["2", "Groc", "Vermell", "1,5 s"],
        ["3", "Vermell", "Vermell", "1 s"],
        ["4", "Vermell", "Verd", "3 s"],
        ["5", "Vermell", "Verd fent pampallugues", "1,2 s"],
        ["6", "Vermell", "Vermell", "1 s"]], [40, 90, 170, 60])}
{p("Les pampallugues de la fase 5 són apagar i encendre el verd dels vianants (port 8) dues vegades, amb un delay(300) entre cada canvi. O sigui, 4 × 300 = 1200 ms.")}
{p("A les fases 3 i 6 els dos vermells estan encesos a la vegada. Així no hi ha mai cap moment en què cotxes i vianants tinguin verd junts. Un cicle sencer dura 5 + 1,5 + 1 + 3 + 1,2 + 1 = 12,7 segons.")}
{imgs([("cap_verd_cotxes.jpg", 120, 120, "Fase 1"), ("cap_groc.jpg", 120, 120, "Fase 2"), ("cap_vermell.jpg", 120, 120, "Fase 3"), ("cap_verd_vianants.jpg", 120, 120, "Fase 4")])}
{p('Vídeo del funcionament: <a href="' + VID + '">' + VID + "</a>")}
{h2("5. Opinió personal i possibles millores")}
{p("Aquesta pràctica ens ha agradat més que les anteriors, perquè al final tens una cosa que s'assembla a un semàfor de veritat. El codi no té res de nou, només digitalWrite i delay, però s'ha de pensar bé l'ordre. Si un led no s'apaga quan toca, ja tens dos colors encesos alhora i el semàfor no té sentit.")}
{p("També hem vist que en un semàfor el més important és que no hi hagi mai verd per a tots dos. Per això deixem un segon amb els dos vermells encesos abans de cada canvi.")}
{p("A més, ens ha estat més fàcil perquè l'any passat, a 4t d'ESO, ja vam fer aquesta pràctica (o una de molt semblant) amb el mateix professor, i hem aprofitat el circuit i el codi que teníem al Tinkercad.")}
{p("Possibles millores:")}
{ul(["Posar un polsador perquè els vianants demanin passar, i que el semàfor només canviï quan l'apretin.",
     "Afegir un brunzidor que soni mentre els vianants tenen verd.",
     "Posar una resistència a cada led, d'uns 220 Ω, perquè no hi passi massa corrent."])}
"""

open("memoria.html", "w", encoding="utf-8").write(
    '<!DOCTYPE html><html lang="ca"><head><meta charset="utf-8"><title>Memòria Tasca 4 Semàfor</title></head><body>'
    + body.strip() + "</body></html>")
print("ok", len(body))
