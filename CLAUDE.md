# Se Apri il Cuore · sito di Paolo Furini

Sito Jekyll pubblicato da GitHub Pages (branch `main`, cartella root). Ogni push su `main` va online in un paio di minuti. Indirizzo: https://paolofurini.it (dominio su Aruba, DNS verso GitHub Pages). seapriilcuore.it e romanzidellinvisibile.it reindirizzano qui (paolofurini.com non è nostro: registrato da terzi, scade il 4/12/2026).

## Struttura
- `index.html` home · `romanzi/` collana e pagina di ogni libro · `blog/index.html` elenco articoli · `autore.md`
- `_posts/AAAA-MM-GG-slug.md` articoli del blog
- `_layouts/`, `_includes/`, `assets/css/site.css` (mondo visivo: blu notte, ambra, carta calda; font Newsreader + Instrument Sans, self-hosted)
- Usare sempre il filtro `relative_url` per i link interni: `baseurl` è `""`.

## Pubblicare un articolo
Ordine fisso: 1) Claude scrive la bozza e i due prompt per l'immagine (skill images-rdi); 2) Paolo crea l'immagine e la manda; 3) Claude la ridimensiona (-900/-1600, jpg e webp) e solo allora pubblica l'articolo con la copertina. Mai pubblicare un articolo senza immagine.

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

## Newsletter (Brevo)
- Ogni nuovo file in `_posts/` con data di oggi (o degli ultimi 3 giorni) fa partire da solo la lettera agli iscritti della lista Brevo "Se Apri il Cuore" (`.github/workflows/newsletter.yml` + `scripts/newsletter.py`, chiave nel segreto GitHub `BREVO_API_KEY`).
- **Interruttore:** `.github/newsletter/config.yml` → `live: false` (attuale) significa che le lettere arrivano SOLO a Paolo come prova. Non mettere `live: true` senza una richiesta esplicita di Paolo.
- **Invio approvato:** quando Paolo, dopo aver letto articolo ed email di prova, dice esplicitamente di inviare, scrivere lo slug dell'articolo come ultima riga di `.github/newsletter/approva` e fare push: parte la lettera alla lista solo per quell'articolo.
- Per non inviarla per un singolo articolo: `newsletter: false` nel front matter.
- Prova: modificare `.github/newsletter/test-request`; l'esito si legge in `.github/newsletter/log.md`.
- Il modulo d'iscrizione è `_includes/newsletter.html` (doppia conferma).

## SEO e ricerca con IA (da rispettare in ogni articolo)
- `title` chiaro, con la parola chiave principale, max 60 caratteri circa. `description` max 155 caratteri: dice di cosa parla l'articolo, non è uno slogan.
- `tema` sempre uno dei temi in `_data/temi.yml` (ogni tema ha la sua pagina in `temi/`).
- Il primo paragrafo risponde subito alla domanda dell'articolo. Quando è naturale, i titoli H2 sono domande vere ("Cos'è…", "Come…").
- **Digital Feng Shui è il tema di punta del sito**: obiettivo essere il riferimento in Italia. La pagina pilastro è `/digital-feng-shui/` (`temi/digital-feng-shui.md`, schema in `_includes/schema-dfs.html`). Ogni articolo che tocca telefono, notifiche, attenzione o schermi linka la pagina pilastro con il testo "Digital Feng Shui"; quando nasce un articolo DFS nuovo, aggiungerlo anche nella sezione "Da dove comincio?" della pagina pilastro se è una buona porta d'ingresso.
- Almeno un link interno a un altro articolo, a una pagina tema o alla pagina del libro.
- Immagini con `alt` descrittivo in italiano.
- `sitemap.xml`, `robots.txt` (aperto anche ai crawler IA) e `llms.txt` si aggiornano da soli a ogni build.

## Voce di Paolo (prima persona)
- Asciutta e diretta, poco poetica, con il Cuore aperto ma senza sdolcinature. Frasi concrete, esperienze vere, niente prediche.
- Mantenere le maiuscole della terminologia spirituale: Cuore, Coscienza, Noi, Funzione, Innocuità, Raggio, Anima, Servizio.
- Mostrare, non dire. Niente termini esoterici usati in modo didascalico.
- Niente fatti inventati su Paolo, sul libro (data d'uscita, prezzo, editore) o sulla Scuola. Se un dato non è certo, non scriverlo.
- Niente lineette lunghe come intercalare, niente elenchi di tre aggettivi, niente formule da IA ("in un mondo in cui", "scopriamo insieme").
- Chiusura: l'articolo termina con il testo; la firma "Paolo" la aggiunge il layout.
- Nelle lettere e nelle email ai lettori il saluto è "Caro/a," (mai "Ciao").

## Design
Le regole di design vengono dalla skill Impeccable (`.claude/skills/impeccable`, Apache 2.0, di Paul Bakaus). Prima di modificare l'aspetto del sito leggere `reference/craft-floor.md`. Niente eyebrow sopra i titoli, niente card tutte uguali, niente gradienti nel testo, movimento minimo.
