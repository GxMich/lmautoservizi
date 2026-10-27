"""Genera il sito in docs/: python sorgente/genera.py
Pagine: ogni modulo di sorgente/pagine/ con costruisci(), chiamato una volta per lingua (italiano in docs/, inglese in docs/en/).
Poi scrive sitemap.xml, robots.txt, .nojekyll, site.webmanifest, i pacchetti assets/sito.css e assets/sito.js
(tutti i file di sorgente/stile e sorgente/script, in ordine di nome) e l'elenco dei dati da completare.
LM_URL dà l'indirizzo pubblico (predefinito: GitHub Pages); LM_PRODUZIONE=1 attiva canonical e indicizzazione.
Solo in produzione scrive anche llms.txt (riassunto per gli assistenti di ricerca), _redirects (vecchi indirizzi
WordPress) e _headers (intestazioni di sicurezza e cache): li leggono Netlify e Cloudflare Pages, GitHub Pages li ignora.
In anteprima questi tre file vengono cancellati da docs/, se ci sono."""
import html, importlib, json, os, pkgutil, re, sys
from urllib.parse import urlsplit
sys.stdout.reconfigure(encoding="utf-8")
import contenuti, pagine, sito
from sito import DOCS, RADICE, PAGINE, LINGUE, NON_INDICIZZATE, URL, PRODUZIONE, url


def scrivi_file(relativo, testo):
    file = os.path.join(DOCS, *relativo.split("/"))
    os.makedirs(os.path.dirname(file), exist_ok=True)
    with open(file, "w", encoding="utf-8", newline="\n") as f:
        f.write(testo)
    print("scritto", relativo, len(testo))


# ---------------------------------------------------------------- pagine
MODULI = [importlib.import_module("pagine." + m.name) for m in pkgutil.iter_modules(pagine.__path__)]
for lingua in LINGUE:
    sito.imposta_lingua(lingua)
    for modulo in MODULI:
        if hasattr(modulo, "costruisci"):
            modulo.costruisci()
mancanti = [f"{l}:{p}" for l in LINGUE for p in PAGINE if (l, p) not in sito.SCRITTE]
if mancanti:
    sys.exit("pagine registrate ma non generate: " + ", ".join(mancanti))

# pagine rimaste da un registro precedente: si segnalano, non si cancellano
for cartella, sotto, file in os.walk(DOCS):
    sotto[:] = [s for s in sotto if s != "assets"]
    for nome in file:
        if nome.endswith(".html") and os.path.normpath(os.path.join(cartella, nome)) not in sito.FILE_SCRITTI:
            print("attenzione: pagina non più generata, da cancellare a mano:", os.path.relpath(os.path.join(cartella, nome), RADICE))

# ---------------------------------------------------------------- sitemap, robots, manifest
voci = []
for p in PAGINE:
    if p in NON_INDICIZZATE:
        continue
    alternative = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{a}" href="{url(p, a)}"/>' for a in LINGUE)
    alternative += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{url(p, "it")}"/>'
    voci += [f"  <url>\n    <loc>{url(p, l)}</loc>{alternative}\n  </url>\n" for l in LINGUE]
scrivi_file("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "".join(voci) + "</urlset>\n")
# In produzione tutto aperto, con un permesso esplicito per i motori di ricerca e per i robot degli assistenti
# che cercano e citano le fonti (per gli altri robot vale la regola generale).
CERCATORI = ["Googlebot", "Bingbot", "OAI-SearchBot", "Claude-SearchBot", "PerplexityBot"]
if PRODUZIONE:
    robots = ("# L.M. Autoservizi: sito aperto ai motori di ricerca e agli assistenti che citano le fonti.\n"
              "User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {c}\n" for c in CERCATORI) + f"Allow: /\n\nSitemap: {URL}sitemap.xml\n")
else:
    robots = "User-agent: *\nDisallow: /\n"
scrivi_file("robots.txt", robots)
scrivi_file(".nojekyll", "")
scrivi_file("site.webmanifest", json.dumps({
    "name": "L.M. Autoservizi", "short_name": "LM Autoservizi", "lang": "it", "start_url": "./", "scope": "./", "display": "standalone",
    "background_color": "#0b0d10", "theme_color": "#0b0d10",
    "icons": [{"src": "assets/img/favicon-192.png", "sizes": "192x192", "type": "image/png"},
              {"src": "assets/img/favicon-180.png", "sizes": "180x180", "type": "image/png"}]}, ensure_ascii=False, indent=2) + "\n")

# ---------------------------------------------------------------- stili e script
scrivi_file("assets/sito.css", sito.CSS)
scrivi_file("assets/sito.js", sito.JS)

# ---------------------------------------------------------------- solo produzione: llms.txt, _redirects, _headers
BASE = urlsplit(URL).path or "/"        # "/" sul dominio definitivo
SOLO_PRODUZIONE = ("llms.txt", "_redirects", "_headers")


def descrizione(pagina, lingua):
    """Meta description della pagina appena generata: llms.txt resta allineato ai testi delle pagine."""
    relativo = sito.percorso(pagina, lingua)
    with open(os.path.join(DOCS, *(relativo + "index.html").split("/")), encoding="utf-8") as f:
        trovata = re.search(r'<meta name="description" content="([^"]*)">', f.read())
    return html.unescape(trovata.group(1)) if trovata else ""


def voce_llms(pagina, lingua):
    nome_pagina = PAGINE[pagina][1][LINGUE.index(lingua)]
    return f"- [{nome_pagina}]({url(pagina, lingua)}): {descrizione(pagina, lingua)}"


if PRODUZIONE:
    legali = ["privacy", "condizioni"]
    principali = [p for p in PAGINE if p not in NON_INDICIZZATE and p not in legali]
    officina = sito.indirizzo_officina()
    llms = ["# L.M. Autoservizi", "",
            "> Officina multimarca di Luca Miglietta a Frassineto Po (AL), vicino a Casale Monferrato: meccanica, elettrauto, gommista, "
            "carrozzeria, diagnosi e pre-revisione. Vettura di cortesia gratuita, ritiro e consegna dell'auto, officina mobile.", "",
            f"L.M. Autoservizi di Miglietta Luca, ditta individuale, P.IVA {contenuti.PIVA}. Sito in italiano, con la versione inglese sotto /en/.", "",
            f"- Telefono e WhatsApp: +39 {contenuti.TEL_TXT}",
            f"- Email: {contenuti.EMAIL}",
            "- Orari: dal lunedì al venerdì 7:30–19:30, orario continuato; sabato e domenica chiuso",
            f"- Officina: {officina}; mappa: {contenuti.MAPS}",
            f"- Zona servita: {', '.join(sito.ZONA)} e paesi vicini",
            "- Pagamenti: contanti, carta o bancomat, alla riconsegna", "",
            "## Pagine", ""] + [voce_llms(p, "it") for p in principali]
    llms += ["", "## English", ""] + [voce_llms(p, "en") for p in ("home", "servizi", "ritiro", "contatti")]
    llms += ["", "## Optional", ""] + [voce_llms(p, "it") for p in legali]
    scrivi_file("llms.txt", "\n".join(llms) + "\n")

    # Vecchio sito WordPress (una sola pagina): gli indirizzi che motori e robot conoscono ancora, verso quelli nuovi.
    vecchi = [("/index.php", ""), ("/index.php/*", ""), ("/wp-login.php", ""), ("/wp-admin", ""), ("/wp-admin/*", ""),
              ("/feed", ""), ("/feed/*", ""), ("/comments/feed", ""), ("/comments/feed/*", ""),
              ("/sitemap_index.xml", "sitemap.xml"), ("/page-sitemap.xml", "sitemap.xml"), ("/post-sitemap.xml", "sitemap.xml"),
              ("/wp-sitemap.xml", "sitemap.xml"), ("/privacy-policy", "privacy/"), ("/privacy-policy/*", "privacy/")]
    scrivi_file("_redirects", "# Vecchi indirizzi del sito WordPress -> sito nuovo, 301 permanenti.\n"
                "# Formato di Netlify e Cloudflare Pages; GitHub Pages ignora questo file.\n"
                + "".join(f"{da:<22} {BASE + a:<16} 301\n" for da, a in vecchi))

    # Sicurezza per tutte le pagine; cache di un anno solo per i file che cambiano nome (o ?v=) quando cambiano.
    # Le regole sulla cache non si sovrappongono: Netlify e Cloudflare unirebbero due Cache-Control con una virgola.
    cache_lunga, cache_media = "public, max-age=31536000, immutable", "public, max-age=2592000"
    intestazioni = ["# Intestazioni HTTP per Netlify e Cloudflare Pages; GitHub Pages ignora questo file.",
                    f"{BASE}*", "  X-Content-Type-Options: nosniff", "  Referrer-Policy: strict-origin-when-cross-origin",
                    "  Permissions-Policy: camera=(), microphone=(), geolocation=()", "",
                    "# sito.css e sito.js hanno ?v= con l'impronta del contenuto; il carattere non cambia",
                    f"{BASE}assets/sito.css", f"  Cache-Control: {cache_lunga}", f"{BASE}assets/sito.js", f"  Cache-Control: {cache_lunga}",
                    f"{BASE}assets/fonts/*", f"  Cache-Control: {cache_lunga}", "",
                    "# foto e librerie tengono lo stesso nome quando vengono sostituite: 30 giorni",
                    f"{BASE}assets/img/*", f"  Cache-Control: {cache_media}", f"{BASE}assets/js/*", f"  Cache-Control: {cache_media}"]
    scrivi_file("_headers", "\n".join(intestazioni) + "\n")
else:
    for nome_file in SOLO_PRODUZIONE:
        if os.path.exists(os.path.join(DOCS, nome_file)):
            os.remove(os.path.join(DOCS, nome_file))
            print("cancellato", nome_file, "(serve solo in produzione)")

# ---------------------------------------------------------------- da completare
segnaposto = [(n, contenuti.DA_COMPLETARE.get(n, "valore da inserire.")) for n, v in vars(contenuti).items() if n.isupper() and v is None]
stock = [s for s in contenuti.FOTO_SLOT if sito.foto_info(s)[4]]
righe = ["# Da completare", "", "Elenco rigenerato da `python sorgente/genera.py` a ogni generazione: non serve modificarlo a mano.", "",
         "## Dati mancanti in `sorgente/contenuti.py`", "", "Finché un valore resta `None`, il sito lo omette.", ""]
righe += [f"- `{n}`: {spiegazione}" for n, spiegazione in segnaposto] or ["- Nessuno: tutti i dati sono completi."]
righe += ["", "## Foto ancora di esempio", "",
          "Gli scatti vanno in `materiali/foto/` con i nomi di `materiali/foto/LEGGIMI.md`, poi `python sorgente/foto.py` e `python sorgente/genera.py`.", ""]
righe += [f"- `{s}`" for s in stock] or ["- Nessuna: tutte le foto sono vere."]
os.makedirs(os.path.join(RADICE, "materiali"), exist_ok=True)
with open(os.path.join(RADICE, "materiali", "da-completare.md"), "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(righe) + "\n")

print(f"\n{len(sito.SCRITTE)} pagine, {'PRODUZIONE (indicizzabile)' if PRODUZIONE else 'anteprima (noindex)'}, indirizzo {URL}, "
      + (f"statistiche GoatCounter ({sito.STATISTICHE})" if sito.STATISTICHE else "senza statistiche"))
print("\nDA COMPLETARE (sorgente/contenuti.py, elenco anche in materiali/da-completare.md):")
for n, spiegazione in segnaposto:
    print(f"- {n}: {spiegazione}")
if stock:
    print(f"- foto ancora di esempio: {', '.join(stock)}")
