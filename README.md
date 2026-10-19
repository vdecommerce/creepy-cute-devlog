# Creepy Cute: The Forgotten Garden · devblog

Publieke website: https://vdecommerce.github.io/creepy-cute-devlog/

Een zelfstandig Nederlands ontwikkeldagboek met geselecteerde beelden. De
Roblox-bron en spelmodellen staan in een afzonderlijke private repository.
De website maakt de game niet openbaar; Hoofdstuk I is in een besloten test.

## Lokaal werken

Node.js 22 of nieuwer is voldoende. Er zijn geen package-afhankelijkheden.

```sh
npm run build
npm run check
npm run dev
```

De preview toont dezelfde `/creepy-cute-devlog/`-paden als GitHub Pages.

## Nieuwe mijlpalen

Voeg een artikel toe aan `content/posts.json`. Werk de actuele ontwikkelstand in
`content/site.json` bij wanneer een gecontroleerde mijlpaal dat rechtvaardigt.
Houd historische artikelen herkenbaar als de stand bij hun eigen datum.

Beelden staan in `public/assets/media/` met herkomstlabels, afmetingen en
alternatieve teksten in `content/media.json`. De optionele lokale media-import
gebruikt `scripts/prepare-media.py --game-root <private-game-checkout>` en
ImageMagick. Alleen de geselecteerde beelden komen op de website; de originele
modellen, builds en private referentiefoto's worden niet gepubliceerd.

Conceptart is AI-gegenereerd. Blender-renders zijn geen gameplay. Native
Studio-inspecties worden apart gelabeld; ze bewijzen geen fysieke telefoon-FPS.
Er is geen open-source- of hergebruiklicentie voor artwork of spelmodellen.

## Publicatie

Na review en merge: voer op een schone main `npm run publish` uit. Dit bouwt en
controleert de site en schrijft uitsluitend de gegenereerde bestanden naar de
aparte gh-pages-branch. GitHub Pages serveert die branch. Dist blijft ongevolgd
op bronbranches. Deze route werkt met de bestaande GitHub-koppeling, die geen
Actions-workflow mag toevoegen. Er zijn geen providerkeys of eigen tracking nodig.

Deze opzet volgt de aparte devblogrepository van Arcana: Echoes of the Stars.
