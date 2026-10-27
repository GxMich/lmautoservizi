# L.M. Autoservizi di Miglietta Luca — sito

Sito statico dell'officina di Luca Miglietta a Frassineto Po (AL), in italiano e in inglese. Nasce dalla "versione semplice" della demo (`siti demo/LMautoservizi-demo-motion`, `docs/semplice/`) e ne mantiene aspetto e comportamento: caselle dei servizi, tendina con la scelta del mezzo e invio su WhatsApp, tema scuro e chiaro, animazioni GSAP + ScrollTrigger + Lenis.

- Anteprima (GitHub Pages): https://gxmich.github.io/lmautoservizi/
- Dominio definitivo: https://www.lmautoservizi.it

## Struttura

```
sorgente/
  contenuti.py        dati dell'attività (telefono, P.IVA, foto, attestati, dati ancora da completare)
  testi_legali.py     testi HTML di privacy, garanzia, vettura di cortesia e nota sulle recensioni (bozze, vedi "Testi legali")
  sito.py             nucleo: configurazione, lingua, registro delle pagine, link, icone, testata, piede, tendina WhatsApp
  pagine/             un modulo per argomento, ognuno con costruisci()
  stile/*.css         uniti in ordine di nome in docs/assets/sito.css
  script/*.js         uniti in ordine di nome in docs/assets/sito.js
  genera.py           genera tutto docs/
  controlla_link.py   controlla link, risorse e frammenti del sito generato
  controlla_seo.py    controlla titoli, descrizioni, hreflang, canonical, immagini, dati strutturati e note interne
  foto.py             prepara le foto vere
docs/                 sito generato, pubblicato così com'è
materiali/            foto originali e PDF del cliente (fuori dal repository), testi-legali/, da-completare.md
```

Indirizzi puliti, a cartelle: `servizi/meccanica/`, `ritiro-e-consegna/`, `chi-sono/`… L'inglese sta sotto `en/` con gli stessi percorsi. Tutti i link interni sono relativi, così il sito funziona sotto `/lmautoservizi/` su GitHub Pages, in locale e sul dominio definitivo; solo la pagina 404 usa indirizzi assoluti (GitHub la serve a percorsi qualsiasi).

## Generare e provare

```sh
python sorgente/genera.py
python sorgente/controlla_link.py
python sorgente/controlla_seo.py
python -m http.server 8080 --directory docs
```

Poi aprire http://localhost:8080/ . In locale la 404 carica stili e script dall'indirizzo pubblico (`LM_URL`).

`genera.py` scrive le 32 pagine (16 per lingua), `sitemap.xml`, `robots.txt`, `.nojekyll`, `site.webmanifest`, i pacchetti `assets/sito.css` e `assets/sito.js` (con `?v=` di versione nelle pagine) e `materiali/da-completare.md`, l'elenco dei dati e delle foto che mancano. In produzione scrive anche `llms.txt`, `_redirects` e `_headers` (vedi "Pubblicare").

## Controlli

- `controlla_link.py` esce con errore se un link, un'immagine o un `#frammento` non esiste. Controlla anche gli `url()` del CSS, le icone del manifest, la sitemap e, in produzione, i link di `llms.txt` e le destinazioni di `_redirects`.
- `controlla_seo.py` controlla ogni pagina generata: un solo `<h1>`; `<title>` di al massimo 65 caratteri e diverso per ogni pagina della stessa lingua; meta description tra 70 e 160 caratteri; `<html lang>`; hreflang `it`, `en` e `x-default` reciproci; canonical in produzione e `noindex` in anteprima; `alt`, `width` e `height` su ogni `<img>`; JSON-LD leggibile, senza `Review` né `AggregateRating`; nessuna nota interna ("DA VERIFICARE", "TODO", "None", commenti HTML). Stampa una tabella per pagina; esce con errore solo per i problemi gravi (h1 mancante, JSON-LD rotto, note interne pubblicate), gli altri sono avvisi. Controlla quello che c'è in `docs/`: dopo una generazione di produzione verifica la produzione.

Prima di ogni pubblicazione: generare, lanciare i due controlli e guardare che entrambi finiscano senza errori.

## Aggiungere o modificare una pagina

1. Registrare la pagina in `PAGINE` in `sorgente/sito.py` (id, percorso, nome in italiano e inglese); `NAV` e `PIEDE_PAGINE` decidono dove compare nei menu.
2. In un modulo di `sorgente/pagine/`, dentro `costruisci()`: `inizia("id")`, poi `scrivi(head(...) + testata() + ... + finale() + piede())`. I link si fanno con `href("id")`, i file con `risorsa("assets/...")`. L'elenco completo è in cima a `sito.py`.
3. Gli stili nuovi vanno in un file a parte in `sorgente/stile/` (per esempio `20-servizi.css`), gli script in `sorgente/script/`: `00-base.*` resta quello della versione semplice.

`genera.py` importa da solo tutti i moduli di `pagine/` e si ferma se una pagina registrata non viene generata.

## Pubblicare

Oggi GitHub Pages pubblica `main:/docs` come anteprima. Dopo ogni modifica: generare, controllare e includere `docs/` nel commit. La generazione normale è sempre un'anteprima: `noindex` in ogni pagina e `robots.txt` che blocca tutto.

Variabili per la pubblicazione definitiva:

- `LM_URL`: indirizzo pubblico del sito, usato da canonical, hreflang, anteprime social, sitemap, dati strutturati, `llms.txt` e pagina 404 (predefinito `https://gxmich.github.io/lmautoservizi/`).
- `LM_PRODUZIONE=1`: attiva canonical e indicizzazione; `robots.txt` apre il sito a tutti, con un permesso esplicito per Googlebot, Bingbot e i robot di ricerca degli assistenti (OAI-SearchBot, Claude-SearchBot, PerplexityBot), e rimanda alla sitemap. Scrive anche `llms.txt`, `_redirects` e `_headers`.
- `LM_GOATCOUNTER` (facoltativa): codice del sito su GoatCounter, per le statistiche senza cookie (vedi sotto). Senza, il sito non ha statistiche.

```sh
LM_PRODUZIONE=1 LM_URL=https://www.lmautoservizi.it/ python sorgente/genera.py
python sorgente/controlla_link.py
python sorgente/controlla_seo.py
```

(In PowerShell: `$env:LM_PRODUZIONE="1"; $env:LM_URL="https://www.lmautoservizi.it/"; python sorgente/genera.py`, e poi `Remove-Item Env:LM_PRODUZIONE, Env:LM_URL` per tornare all'anteprima.) Una generazione senza `LM_PRODUZIONE` cancella da `docs/` `llms.txt`, `_redirects` e `_headers`, così un'anteprima non porta mai in giro i file della produzione.

### Dove ospitare il sito definitivo

Il sito è di un'attività commerciale, e questo conta per la scelta:

- **Netlify** (piano gratuito) o **Cloudflare Pages** (gratuito): ammettono siti commerciali e leggono `_redirects` e `_headers`. Cartella da pubblicare: `docs/`, nessun comando di build (il sito si genera in locale e si carica già pronto). Il dominio `www.lmautoservizi.it` si collega dal pannello del servizio, dove si impostano anche HTTPS e il passaggio da `lmautoservizi.it` a `www`.
- **Vercel**: il piano Hobby è solo per uso personale e non commerciale; per questo sito servirebbe il piano Pro, a pagamento. Vercel non legge `_redirects` e `_headers` (usa `vercel.json`).
- **GitHub Pages**: va bene per l'anteprima. Per usarlo anche in produzione serve il file `docs/CNAME` con dentro `www.lmautoservizi.it` (una riga), da aggiungere a mano: `genera.py` non lo scrive e non lo cancella. GitHub Pages ignora `_redirects` e `_headers`, quindi i vecchi indirizzi WordPress finirebbero sulla 404.

### File per l'hosting (solo produzione)

- `_redirects`: porta con un 301 gli indirizzi del vecchio sito WordPress a una sola pagina (`/index.php`, `/wp-login.php`, `/wp-admin/*`, `/feed/*`, `/comments/feed/*`, `/sitemap_index.xml`, `/page-sitemap.xml`, `/wp-sitemap.xml`, `/privacy-policy`) alla home, alla sitemap o alla privacy. Così Google aggiorna i vecchi risultati e i robot che cercano WordPress non riempiono i log di 404. L'elenco è in `genera.py`.
- `_headers`: intestazioni di sicurezza su tutte le pagine (`X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy` che spegne fotocamera, microfono e posizione) e cache lunga per `assets/`: un anno per `sito.css`, `sito.js` (cambiano `?v=` a ogni modifica) e il carattere, 30 giorni per foto e librerie, che tengono lo stesso nome quando vengono sostituite. Le regole sulla cache non si sovrappongono, perché Netlify e Cloudflare unirebbero due `Cache-Control`.
- `llms.txt`: riassunto dell'attività (cosa fa, contatti, orari, zona) e l'elenco delle pagine con la loro descrizione, letto da alcuni assistenti di ricerca. È facoltativo e innocuo; le descrizioni vengono dalle meta description delle pagine, quindi restano allineate da sole.

Netlify e Cloudflare usano lo stesso formato per questi due file; GitHub Pages li pubblica come file normali e non li applica.

### Statistiche senza cookie (facoltative, spente)

Con `LM_GOATCOUNTER=<codice>` (il nome scelto su goatcounter.com) ogni pagina carica lo script di GoatCounter da `gc.zgo.at` e `script/40-statistiche.js` conta come eventi i clic su Chiama (`tel:`), sui link WhatsApp e gli invii della tendina e dei moduli gomme e ricambi, senza mai mandare il testo dei messaggi. L'informativa privacy cambia da sola: toglie "niente statistiche" e mostra il paragrafo sulle statistiche. Prima di accenderle (vedi `materiali/testi-legali/LEGGIMI.md`): firmare l'accordo art. 28 con Luca, compilarne l'Allegato 1, far verificare al professionista se serve comunque il consenso, aggiornare `AGGIORNAMENTO` in `sorgente/pagine/legale.py`.

## Testi legali

Le bozze complete e commentate sono in `materiali/testi-legali/` (informativa privacy, messaggi WhatsApp, vettura di cortesia, garanzia, note legali e prezzi, accordo art. 28, permessi per recensioni e foto); `LEGGIMI.md` spiega chi usa cosa ed elenca tutti i punti DA VERIFICARE. **Sono bozze, non un parere legale: prima di pubblicare il sito definitivo vanno fatte rivedere a un consulente privacy o a un avvocato** (e la parte sulla vettura di cortesia anche all'assicuratore).

Il sito prende i testi da `sorgente/testi_legali.py` (se cambia un testo lì, va cambiato anche il file `.md`, e viceversa):

- `privacy/`: `PRIVACY_IT` e `PRIVACY_EN` con i dati veri di `contenuti.py` e la data `AGGIORNAMENTO` di `sorgente/pagine/legale.py`, da cambiare a ogni modifica dei testi. Indice dei titoli a lato sui computer e a tendina sul telefono.
- `garanzia-e-condizioni/`: i riassunti `GARANZIA_SITO_*` e `VETTURA_CORTESIA_*`; le condizioni complete si firmano in officina alla consegna dell'auto.
- `nota_recensioni()` in `sito.py`: `RECENSIONI_NOTA_*` da mettere sotto le recensioni della home.
- Piede di ogni pagina: ditta, sede legale, P.IVA, REA (appena c'è in `contenuti.py`), PEC e link a "Garanzia e condizioni" e "Privacy e cookie".

I commenti `<!-- DA VERIFICARE ... -->` dei testi sono note interne: `senza_commenti()` li toglie prima di scrivere le pagine e `controlla_seo.py` si ferma se una nota arriva comunque nel sito. Nei dati strutturati non ci sono `Review` né `AggregateRating`: Google non mostra le stelle per le recensioni pubblicate dall'attività stessa.

## Foto vere

Gli scatti vanno in `materiali/foto/` con i nomi indicati in `materiali/foto/LEGGIMI.md`, poi:

```sh
python sorgente/foto.py
python sorgente/genera.py
```

Ogni foto vera sostituisce da sola quella stock e toglie la scritta "Foto di esempio". Gli originali restano fuori dal repository. `foto.py` richiede Pillow (`pip install pillow`).

## Dati da completare

I dati che Luca deve ancora darci sono in `sorgente/contenuti.py` con valore `None` (indirizzo dell'officina, coordinate, REA, Instagram, link per le recensioni Google, prezzi). Finché restano `None` il sito li omette; `genera.py` li elenca a ogni generazione, con una riga di spiegazione, anche in `materiali/da-completare.md`.

## Immagini

Le fonti delle immagini stock sono in `docs/assets/img/campione/FONTI.json`. Il pneumatico è un render illustrativo. Le immagini campione sono dichiarate nel sito e non rappresentano fotografie dell'attività. Il PDF con i servizi del cliente resta in locale in `materiali/` ed è escluso dal repository.
