# Traspàs de context: Pau i les memòries de Robòtica

Aquest fitxer és per al Claude que treballi en local amb la Pau (xat de Robòtica, INS 2026-2027). Ho ha escrit el Claude que va fer la feina al núvol. Llegeix-lo sencer abans de fer res i després llegeix també `CLAUDE.md` (la guia d'estil, que és la part més important).

## 1. Qui és la Pau i com vol que li treballis

- Pau Martínez Cuadra, 16 anys, 1r de Batxillerat. Fa memòries de Robòtica amb el seu company **Enric Vinyes Huguet**. Fa un mes que ha començat a emprendre.
- **Li parles en castellà.** Les memòries i tot el que s'entrega van **en català**.
- Ho va deixar escrit com a preferència: **sigues crític amb tot, no li donis la raó sempre**. Si alguna cosa del que demana és mala idea o té un error, li ho dius. També va dir que si et demana una cosa la facis, i això inclou coses que no et semblin bé; si no és legal o pot perjudicar algú, digues-li-ho clar abans.
- No li has de demanar permís per cada pas petit (ho va dir quan li demanava confirmació abans de moure fitxers al Drive). Sí que has de confirmar coses que no es poden desfer o que surten fora (esborrar, compartir públicament, enviar).
- Treballa amb pocs tokens. Respostes curtes i que vagin al gra. No li facis resums llargs de tot el que has fet.
- Li agrada que li expliquis el codi de manera senzilla, amb taules i exemples petits (li va servir molt l'explicació de `Serial.available()`, de `print` contra `println` i de `i<n` contra `i<=n`).

## 2. Què li agrada de les memòries (el més important)

Tot el detall és a `CLAUDE.md`. Resum del que més li importa:

- Que **no es noti que ho ha fet una IA**. Ho ha repetit moltes vegades: text amb paraules d'ells ("o sigui", "els que toquen", "ens va costar"), frases curtes, primera persona del plural, res massa perfecte, **cap anècdota inventada**. Els problemes que expliquen ells (per exemple, el SOS que no parava) es posen amb les seves paraules.
- Que s'expliqui **tot bé, sobretot el que ells han entès i com ho han entès**.
- Estil "punt mig entre senzill i amb color": res de capçaleres amb fons de color, quadres destacats, esquemes inventats ni gràfics decoratius. Cada memòria té un **color principal diferent** (1.1 blau `#1F5C99`, Tasques 2 i 3 lila `#6A3D9A`, la següent taronja `#D9480F`, després verd `#2E7D32`).
- Títol amb el color, subtítol, noms i "Robòtica · 1r Batxillerat · data" en gris. Apartats numerats. Taules grises amb capçalera en to clar del color.
- **Codi amb els colors de l'Arduino IDE, sense quadre ni fons, i sense comentaris.**
- **Fotos reals** (muntatge) i **captures dels vídeos**, retallades perquè es vegi el led encès o apagat.
- Un vídeo del funcionament enllaçat des de la memòria (MP4, perquè el professor l'ha de poder obrir a l'institut).
- Google Doc **A4**, comprovat exportant a PDF perquè no hi hagi res tallat entre pàgines. Pàgines en blanc, taules o codi partits per la meitat li molesten.
- Un cop acabat, ell baixa el PDF i el penja al **Moodle**.

## 3. Quan et posa codi o es queixa del codi

- **Fes el codi tan senzill com el seu.** Quan vaig arreglar el semàfor amb variables amb nom i comentaris, va dir: "has complicat massa el codi i has afegit explicacions en gris que no m'agraden, perquè es nota massa que ho has fet tu". Després de dir-ho, ho vaig deixar com el seu codi original amb només els pins canviats i els errors corregits.
- Mantén **el seu format** (`// C++ code` de Tinkercad, `digitalWrite(10,HIGH);` amb números, sense sagnat), els seus noms i la seva estructura. Només canvia el que és un error o el que es demana.
- Si l'enunciat del professor demana comentaris al codi (com al semàfor), **digues-li que els ha d'escriure ell amb les seves paraules** i no els posis tu.
- El codi s'ha de **provar abans de donar-lo**. Jo simulava l'Arduino compilant el `.ino` a l'ordinador amb un `delay`, `digitalWrite` i `Serial` falsos per veure la seqüència. No ho he pogut provar a la placa real, i li ho he dit sempre.

## 4. El muntatge (el que tenen a la protoboard)

- Arduino UNO + protoboard. De la Tasca 1.1 (7 leds) i del semàfor (1.3) tenen els leds posats.
- **Semàfor (1.3), pins:** vermell cotxes 13, groc cotxes 12, verd cotxes 11, vermell vianants 9, verd vianants 8. Dues resistències. Els vianants porten la massa a la fila "+" de la protoboard connectada a GND (funciona però confon).
- **Polsador (Tasques 2 i 3):** led vermell al port 10; polsador de 4 potes amb una pota a 5V, l'altra al port 2 i a la resistència cap a GND (pull-down).
- **Tasca 5:** fa servir el pin 13 (el vermell dels cotxes, que també encén el led "L" de la placa).

## 5. Què hem fet (cronològic)

| Tasca | Estat | On és |
|---|---|---|
| 1.1 LEDs | Memòria feta, Google Doc, blau | Drive `Robòtica`, plantilla a `memoria_tasca1_1/memoria.html` |
| 2 SOS amb polsador | Fet, dos codis (amb `for` i sense `for`) | `Tasca2_SOS_for/`, `Tasca2_SOS/` |
| 3 Polsador com a interruptor | Fet | `Tasca3_Interruptor/` |
| Memòria Tasques 2 i 3 (una sola) | **Feta i entregable**, lila, 6 pàgines, vídeos MP4 enllaçats | Google Doc id `1OSitvfxTBpIPHvLqVoSLO-YGThzo9jxR32x70aZDjCo`; PDF a `memoria_tasca2_3/` |
| 1.3 Semàfor (Tasca 4) | **Codi arreglat. Memòria encara per fer** (faltaria foto del muntatge real, vídeo, i els seus comentaris al codi) | `memoria_tasca1_3/Tasca1_3_Semafor.ino` |
| 5 Led tantes vegades com el número del monitor sèrie | Codi fet i explicat. Memòria per fer | `tasca5/Tasca5_Monitor.ino` |
| 6 Codi Morse (A, B, C amb `switch` i `Serial`) | **No començada.** Ell va dir: "primer fes la 5". Té ja el codi de partida del professor, amb subrutines `punt()`/`ratlla()` i `switch`, que fa servir `led13`. | pendent |

## 6. Coses que van sortir malament i has de saber

- **El SOS que no parava mai:** va ser amb `INPUT_PULLUP` mirant si estava a LOW, però amb la resistència cap a GND ja estava a LOW sense apretar. És el problema real que expliquen a la memòria.
- **Memòria semàfor:** el seu esborrany d'opinió personal barreja singular i plural ("vaig fer" / "hem") i li falten accents. Ha d'anar tot en plural. Li vaig dir que ho deixaria amb les seves paraules però corregit.
- **Tinkercad del semàfor:** a la captura que em va passar hi havia un cable lila, un led rojo solt fora de la protoboard i una sola resistència, que no coincideix amb l'esquema. Li vaig avisar que ha d'entregar el circuit bo.
- El Google Doc es va editar a mà pel Pau després de generar-lo. **Mai no sobreescriguis el text del Doc**; si has de canviar alguna cosa, llegeix el Doc de nou i canvia només el que toca (per exemple, enllaços o una sola paraula).
- Vaig corregir un sol error de català en un text seu: "Te vam ensenyar" → "Et vam ensenyar".

## 7. Drive (compte de la Pau, `pau.martinezps5@gmail.com`)

Carpeta `Robòtica` (id `1vuOz8LaBaQFVSh0lWEjkQaKMDCQ2bnJ_`), dins `1r Batxillerat (2026-27)`:

- A l'arrel: les memòries bones (`Memòria LED 1.1-…`, `Memòria Polsador 2 i 3-…`).
- `Vídeos Tasques 2 i 3`: els dos MP4 editats.
- `Fotos i vídeos originals`: els originals del mòbil i els de WhatsApp.
- `Versions antigues`: la primera versió duplicada de la memòria 1.1.
- **Pendent seu:** posar la carpeta `Vídeos Tasques 2 i 3` com a "Qualsevol persona amb l'enllaç" (lector). El connector del Drive només comparteix amb correus concrets, no ho pot fer. Sense això el professor no podrà obrir els vídeos.
- Limitació del connector del Drive: només baixa fitxers de **menys de 10 MB**. Els vídeos del mòbil s'han de passar per WhatsApp (els comprimeix) i pujar al Drive. Els fitxers grans (mp4) no es poden pujar pel connector; ha de ser ell.
- `drive.google.com` pot estar bloquejat des de l'entorn del núvol i en alguns instituts. Els enllaços de vídeo de la memòria van al Drive.

## 8. Com es fa una memòria (flux ja provat)

1. Plantilla `memoria_tasca1_1/memoria.html` (o la de `memoria_tasca2_3/`, més recent). Generada amb Python.
2. Les imatges es pugen a aquest repo (branca `claude/busy-newton-dsqx1y`) i es posen amb enllaç `raw.githubusercontent.com`, perquè Google les ha de poder carregar.
3. L'HTML es puja al Drive amb `create_file` amb `text/html`; es converteix a Google Doc.
4. Mida A4 amb l'API de Docs; `pageBreakBefore` en lloc de salts de pàgina inserits (si no, queden pàgines en blanc quan el text creix).
5. Exportar a PDF, passar a imatges i mirar-les per comprovar que no hi ha res tallat.
6. Si hi ha captures: retallades i sense el fons groc heretat (si surt groc, treure `backgroundColor`).

## 9. Vídeos (si cal tornar-ne a fer)

- `eines/editar_video.sh entrada sortida inici final "Tasca N" "Subtítol" "drawtext extra"`: estabilitza, neteja el soroll, cartell amb el color de la memòria, música i MP4 en H.264 Main + AAC (obre a qualsevol ordinador).
- `eines/musica.py` genera la música de fons sense drets d'autor. Necessita `ffmpeg` i `python3` amb `numpy`.
- El vídeo ha de ser curt (6-8 s) i els rètols han de ser amb el color de la memòria.

## 10. Què hauries de fer ara

1. Fer la **Tasca 6** (Morse). Parteix del codi del professor; ha d'anar amb el pin 13, i el professor només hi té A, B i C. Si vol ampliar-ho amb més lletres o amb el `for`, que sigui seu.
2. **Memòries** de la 1.3, la 5 i la 6, amb l'estil de la secció 2. Pregunta-li pels textos d'ells, que no et surtin inventats.
3. Recordar-li el que està pendent a la secció 7.

## 11. Configuració i compactació

- Al repo hi ha `.claude/settings.json` amb `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=30` (compacta el context al 30 %). Això només serveix en local si fa servir aquest repo; al núvol no es va aplicar mai. Un 30 % és molt baix: compactar perd detalls (índexs del Doc, ordres exactes). Un 50-60 % va millor.
- Les imatges i vídeos pesats (mp4, jpg) són al repo, no al xat.

## 12. Per posar-te al dia en local

```
git clone https://github.com/paumartinezps5-netizen/repo-para-claudia-.git
cd repo-para-claudia-
git checkout claude/busy-newton-dsqx1y
```
Llegeix `CLAUDE.md` i aquest fitxer. Si vols tocar el Drive, necessites el connector de Google Drive i Google Docs a l'altre Claude.
