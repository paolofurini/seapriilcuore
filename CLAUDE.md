# Se Apri il Cuore · sito di Paolo Furini

Sito Jekyll pubblicato da GitHub Pages (branch `main`, cartella root). Ogni push su `main` va online in un paio di minuti. Indirizzo: https://paolofurini.it (dominio su Aruba, DNS verso GitHub Pages). paolofurini.com, seapriilcuore.it e romanzidellinvisibile.it reindirizzano qui.

## Struttura
- `index.html` home · `romanzi/` collana e pagina di ogni libro · `blog/index.html` elenco articoli · `autore.md`
- `_posts/AAAA-MM-GG-slug.md` articoli del blog
- `_layouts/`, `_includes/`, `assets/css/site.css` (mondo visivo: blu notte, ambra, carta calda; font Newsreader + Instrument Sans, self-hosted)
- Usare sempre il filtro `relative_url` per i link interni: `baseurl` è `""`.

## Pubblicare un articolo
Front matter:
```yaml
---
title: "Titolo"
description: "Sottotitolo in una riga"
tema: "Digital Feng Shui" | "Digital Detox" | "I Romanzi dell'Invisibile" | "Matrix"
cover: /assets/img/nome      # facoltativa: servono nome-900.jpg/.webp e nome-1600.jpg/.webp
cover_alt: "Descrizione dell'immagine"
image: /assets/img/nome-1600.jpg   # anteprima social; se manca usa og-default.jpg
---
```
Prima di pubblicare: `jekyll build` deve passare senza errori.

## Voce di Paolo (prima persona)
- Asciutta e diretta, poco poetica, con il Cuore aperto ma senza sdolcinature. Frasi concrete, esperienze vere, niente prediche.
- Mantenere le maiuscole della terminologia spirituale: Cuore, Coscienza, Noi, Funzione, Innocuità, Raggio, Anima, Servizio.
- Mostrare, non dire. Niente termini esoterici usati in modo didascalico.
- Niente fatti inventati su Paolo, sul libro (data d'uscita, prezzo, editore) o sulla Scuola. Se un dato non è certo, non scriverlo.
- Niente lineette lunghe come intercalare, niente elenchi di tre aggettivi, niente formule da IA ("in un mondo in cui", "scopriamo insieme").
- Chiusura: l'articolo termina con il testo; la firma "Paolo" la aggiunge il layout.

## Design
Le regole di design vengono dalla skill Impeccable (`.claude/skills/impeccable`, Apache 2.0, di Paul Bakaus). Prima di modificare l'aspetto del sito leggere `reference/craft-floor.md`. Niente eyebrow sopra i titoli, niente card tutte uguali, niente gradienti nel testo, movimento minimo.
