---
layout: guida
title: "Digital Feng Shui: cos'è e come si pratica"
tema: Digital Feng Shui
permalink: /digital-feng-shui/
description: "Cos'è il Digital Feng Shui, che differenza c'è con il Digital Detox e le 3 Regole d'Oro per armonizzare telefono e computer, ogni giorno."
schema: schema-dfs.html
etichetta: Guida
cover: /assets/img/blog/digital-feng-shui-guida-cover
cover_alt: "Una stanza in ordine al tramonto, con una lampada accesa, una teiera e il telefono sul tavolino; fuori dalla finestra la città blu, e una persona di spalle sulla soglia"
image: /assets/img/blog/digital-feng-shui-guida-cover-1600.jpg
---
{% capture freccia %}<svg class="g-freccia" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>{% endcapture %}

## Cos'è il Digital Feng Shui?

Il Digital Feng Shui è l'arte di armonizzare i propri dispositivi digitali perché siano strumenti al nostro servizio e non padroni della nostra attenzione. Prende il principio del Feng Shui, l'antica arte orientale di disporre gli spazi perché l'energia scorra senza ostacoli, e lo applica agli spazi in cui oggi passiamo più tempo: lo smartphone e il computer.

<p class="g-autore">Per più di trent'anni ho lavorato nel marketing di grandi aziende della tecnologia, costruendo sistemi pensati per catturare l'attenzione delle persone. Qui racconto le regole che uso su di me per non farmene stritolare. <a href="{{ '/autore/' | relative_url }}">Chi sono</a></p>

## Quali sono le 3 Regole d'Oro del Digital Feng Shui?

<div class="g-regole g-wide">
  <div class="g-regola"><span class="g-num" aria-hidden="true">1</span><h3>Chiudere le porte</h3><p>Nessuna macchina ha il diritto di interromperti. Disattiva tutte le notifiche non umane, social, news, shopping, e lascia attive solo le chiamate e i messaggi di persone vere. Se un'informazione ti serve, vai tu a cercarla, quando decidi tu.</p></div>
  <div class="g-regola"><span class="g-num" aria-hidden="true">2</span><h3>Lasciare spazio vuoto</h3><p>Sulla prima schermata del telefono tieni solo gli strumenti essenziali, calendario, note, mappe, e un'immagine che ti dia pace. Per aprire i social o la posta devi scorrere o cercare l'app: quel secondo di attrito è lo spazio in cui la volontà si riprende il comando.</p></div>
  <div class="g-regola"><span class="g-num" aria-hidden="true">3</span><h3>Respirare prima del click</h3><p>Prima di aprire la posta o un social, fermati tre secondi. Entra con un'intenzione chiara, fai quello che devi fare ed esci, senza farti trascinare dal flusso: in quei tre secondi smetti di essere un automa e torni a essere una persona che sceglie.</p></div>
</div>

<p class="g-link"><a href="{{ '/blog/oltre-il-digital-detox-cose-il-digital/' | relative_url }}">Le tre regole spiegate per intero, con gli studi {{ freccia }}</a></p>

## Le stanze della casa digitale

<p class="g-intro">Una stanza alla volta: ogni articolo ne rimette in ordine una.</p>

<ul class="g-stanze g-wide">
{% for s in site.data.stanze_dfs %}{% if s.url %}  <li><a href="{{ s.url | relative_url }}"><span class="g-stanza">{{ s.nome }}</span><span class="g-frase">{{ s.frase }}</span><span class="g-articolo">{{ s.articolo }}</span>{{ freccia }}</a></li>
{% endif %}{% endfor %}</ul>

<p class="g-prossime">Prossime stanze: {% assign prossime = site.data.stanze_dfs | where_exp: "s", "s.url == nil" %}{% for s in prossime %}{{ s.nome | downcase }}{% unless forloop.last %} · {% endunless %}{% endfor %}</p>

<div class="g-inizio g-wide">
<h2>Da dove comincio?</h2>
<p>Da una sera e una tazza di tè. Stasera spegni tutte le notifiche che non vengono da una persona: bastano pochi minuti, ed è la prima regola. Poi, quando vuoi, scegli una stanza e rimettila in ordine.</p>
</div>

## Domande e risposte sul Digital Feng Shui

<div class="g-faq">
{% for q in site.data.faq_dfs %}{% unless q.solo_schema %}<details><summary><h3>{{ q.domanda }}</h3></summary><p>{{ q.risposta }}</p></details>
{% endunless %}{% endfor %}</div>

<p class="g-nota">Gli studi citati, con i link, sono nell'articolo <a href="{{ '/blog/oltre-il-digital-detox-cose-il-digital/' | relative_url }}">Cos'è il Digital Feng Shui e perché il Digital Detox non basta</a>.</p>

## Che differenza c'è tra Digital Feng Shui e Digital Detox?

Il Digital Detox è la pausa: spegni tutto per un fine settimana, cammini in un bosco, respiri. Funziona, e ne abbiamo bisogno. Ma il lunedì mattina lo schermo si riaccende, e in pochi minuti l'ansia smaltita nel bosco torna addosso.

Il Digital Feng Shui è quello che fai il lunedì. Se il Detox è la cura, il Feng Shui digitale è la prevenzione: un ordine quotidiano che ti permette di stare dentro la tecnologia, perché lì lavoriamo e viviamo, senza farti prosciugare. Il Detox è l'Oasi nel deserto; il Digital Feng Shui è l'armatura che indossi quando dall'Oasi devi uscire. Se vuoi capire perché staccare è così difficile, leggi [Dall'altra parte dello schermo non c'è un amico]({{ '/blog/dallaltra-parte-dello-schermo-non/' | relative_url }}).

## Tutti gli articoli sul Digital Feng Shui

{% assign articoli = site.posts | where: "tema", "Digital Feng Shui" %}
<ul class="post-list">
{% for x in articoli %}  <li><a href="{{ x.url | relative_url }}"><span class="pl-title">{{ x.title }}</span><span class="pl-date">{% include data-it.html date=x.date %}</span></a></li>
{% endfor %}</ul>

<div class="g-newsletter">
<h2>Una stanza alla volta, nella posta</h2>
<p>Quando esce un nuovo articolo ti scrivo una lettera, e niente altro.</p>
{% include newsletter.html %}
</div>
