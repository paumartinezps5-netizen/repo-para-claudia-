# Memòries de Robòtica (1r Batxillerat)

Pau Martínez Cuadra i Enric Vinyes Huguet. Les memòries van al Drive de la Pau, carpeta "Robòtica" (id `1vuOz8LaBaQFVSh0lWEjkQaKMDCQ2bnJ_`), com a Google Doc A4.

## Estil triat (a partir de la Tasca 1.1)

- Punt mig entre senzill i amb color. Res de capçaleres amb fons de color, quadres destacats, esquemes inventats ni gràfics decoratius.
- Cada memòria té un color principal diferent:
  - 1.1 LEDs: blau `#1F5C99`.
  - Tasques 2 i 3 (una sola memòria): lila `#6A3D9A`. Van demanar un color que no recordés el semàfor.
  - Les següents (en ordre): taronja `#D9480F`, verd `#2E7D32`, blau, lila, i després es torna a començar. Si la memòria parla de leds de colors, millor un color que no sigui verd/groc/vermell.
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

## Tasques 2 i 3 (fet, una sola memòria)

- Google Doc "Memòria Polsador 2 i 3-Pau Martínez i Enric Vinyes" (id `1OSitvfxTBpIPHvLqVoSLO-YGThzo9jxR32x70aZDjCo`), fitxers a `memoria_tasca2_3/`.
- Surten els dos codis de la Tasca 2 (`Tasca2_SOS_for` i `Tasca2_SOS`) i el de la Tasca 3 (`Tasca3_Interruptor`), cadascun amb la seva explicació.
- Té salts de pàgina abans de "4.1" perquè el codi no quedi partit.
- Vídeos editats (cartell lila, rètols, música pròpia, soroll reduït) a `memoria_tasca2_3/tasca2_sos.mp4` i `tasca3_interruptor.mp4`. A la memòria s'enllacen amb jsDelivr (`https://cdn.jsdelivr.net/gh/paumartinezps5-netizen/repo-para-claudia-@<commit>/...`), que es reprodueix al navegador; raw.githubusercontent els descarrega.

## Vídeos

- El connector del Drive només baixa fitxers de menys de 10 MB. Els vídeos del mòbil s'han de passar per WhatsApp (els comprimeix) i pujar al Drive.
- `eines/musica.py` genera la música de fons (sense drets d'autor) i `eines/editar_video.sh` fa l'edició (necessita `musica.m4a` a `MUSICA_DIR`).
