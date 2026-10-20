# Memòries de Robòtica (1r Batxillerat)

Pau Martínez Cuadra i Enric Vinyes Huguet. Les memòries van al Drive de la Pau, carpeta "Robòtica" (id `1vuOz8LaBaQFVSh0lWEjkQaKMDCQ2bnJ_`), com a Google Doc A4.

## Estil triat (a partir de la Tasca 1.1)

- Punt mig entre senzill i amb color. Res de capçaleres amb fons de color, quadres destacats, esquemes inventats ni gràfics decoratius.
- Cada memòria té un color principal diferent:
  - 1.1 LEDs: blau `#1F5C99`.
  - Les següents (en ordre): verd `#2E7D32`, taronja `#D9480F`, lila `#6A3D9A`, i després es torna a començar.
- Títol a l'esquerra amb el color principal, subtítol a sota, i noms + "Robòtica · 1r Batxillerat · data" en gris.
- Apartats numerats ("1. Objectiu", "2. Material"...) amb el color principal. No cal fer servir sempre els mateixos apartats; s'ha d'adaptar a la pràctica.
- Taules senzilles amb vores grises i la fila de títols amb un to clar del color principal.
- El codi va amb els colors de l'Arduino IDE, sense quadre ni fons. No hi ha d'haver comentaris al codi.
- Hi ha d'haver fotos reals: la del muntatge i captures del vídeo si n'hi ha.

## Com s'han d'escriure

- En català, en primera persona del plural ("vam posar", "ens va costar"), com si ho haguessin escrit ells.
- Frases curtes i vocabulari normal ("o sigui", "els que toquen"). Res de frases fetes de IA ni de text massa perfecte.
- Les explicacions han de ser concretes de la seva pràctica. Els problemes que expliquin ells (per exemple, un led que no funcionava) s'han de posar amb les seves paraules. No s'han d'inventar anècdotes que no han passat.

## Com es fa

`memoria_tasca1_1/memoria.html` és la plantilla. Les imatges han de ser públiques perquè Google les pugui carregar, i per això es pugen a aquest repo i es fa servir l'enllaç `raw.githubusercontent.com`. L'HTML es puja al Drive (create_file amb `text/html`), es posa la mida A4 amb l'API de Docs, i s'exporta a PDF per comprovar que no hi ha res tallat entre pàgines.

## Pendent per a la memòria de la Tasca 2 (SOS amb polsador)

- Color: verd `#2E7D32`.
- Van ensenyar dos codis al professor i a la memòria hi han de sortir els dos, cadascun amb la seva explicació:
  - `Tasca2_SOS_for/Tasca2_SOS_for.ino`: versió amb bucles `for`. Guarda com està el botó sense prémer (`repos`) i fa l'SOS quan la lectura canvia.
  - `Tasca2_SOS/Tasca2_SOS.ino`: versió sense `for`, amb `if (digitalRead(polsador)==HIGH)` i el botó amb resistència pull-down. És la que van triar perquè s'entén millor.
- Es pot comentar que la versió sense `for` és més llarga però més fàcil de llegir, i que la del `for` és més curta.

## Pendent per a la memòria de la Tasca 3 (polsador com a interruptor)

- Color: taronja `#D9480F`.
- Codi: `Tasca3_Interruptor/Tasca3_Interruptor.ino`. Mateix muntatge que la Tasca 2 (polsador al pin 2 amb pull-down, led al pin 10).
