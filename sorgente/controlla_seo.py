"""Controlla la SEO tecnica del sito generato: python sorgente/controlla_seo.py
Per ogni pagina HTML in docs/:
- un solo <h1>;
- <title> presente, al massimo 65 caratteri e diverso da quello delle altre pagine della stessa lingua;
- meta description tra 70 e 160 caratteri, anche questa diversa per ogni pagina della stessa lingua;
- <html lang> presente e coerente con la cartella (en/ in inglese);
- hreflang it, en e x-default, reciproci: la pagina nell'altra lingua esiste e rimanda a questa; x-default è l'italiano;
- in produzione (robots.txt con "Sitemap:") canonical presente e uguale all'indirizzo della pagina; in anteprima noindex;
- ogni <img> ha alt (anche vuoto, per le immagini decorative), width e height;
- ogni blocco JSON-LD si legge; niente Review o AggregateRating (recensioni autoreferenziali), niente valori null;
- nessuna nota interna: "DA VERIFICARE" o "TODO" nel sorgente, "None" nel testo o negli attributi, commenti HTML.
L'indirizzo pubblico si ricava dagli hreflang della home: il controllo vale per la generazione che c'è in docs/.
Stampa una tabella dei problemi per pagina. Esce con errore solo per i problemi gravi (h1 mancante, JSON-LD rotto,
note interne pubblicate); gli avvisi vanno letti ma non fermano la pubblicazione."""
import json, os, re, sys
from collections import defaultdict
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding="utf-8")
# Si può controllare anche un'altra cartella: python sorgente/controlla_seo.py percorso/della/cartella
DOCS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
TITOLO_MAX, DESCRIZIONE_MIN, DESCRIZIONE_MAX = 65, 70, 160
NOTE_INTERNE = ("DA VERIFICARE", "TODO")
VIETATI = {"Review", "AggregateRating"}


class Pagina(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang, self.h1, self.titolo, self.descrizione, self.robots, self.canonical = None, 0, None, None, "", None
        self.alternative, self.immagini, self.ld, self.testo, self.attributi, self.commenti = {}, [], [], [], [], 0
        self._in, self._buffer = None, []

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        self.attributi += [v for k, v in attrs if v and k not in ("src", "srcset", "href", "d", "viewBox")]
        if tag == "html":
            self.lang = a.get("lang")
        elif tag == "h1":
            self.h1 += 1
        elif tag == "title" and self.titolo is None:
            self._in, self._buffer = "title", []
        elif tag == "meta" and a.get("name") == "description":
            self.descrizione = a.get("content", "")
        elif tag == "meta" and a.get("name") == "robots":
            self.robots = a.get("content", "")
        elif tag == "link" and "canonical" in a.get("rel", "").split():
            self.canonical = a.get("href")
        elif tag == "link" and "alternate" in a.get("rel", "").split() and "hreflang" in a:
            self.alternative.setdefault(a["hreflang"], []).append(a.get("href", ""))
        elif tag == "img":
            self.immagini.append(a)
        elif tag == "script":
            self._in, self._buffer = ("ld" if a.get("type") == "application/ld+json" else "script"), []
        elif tag == "style":
            self._in = "style"

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        if self._in == "title" and tag == "title":
            self.titolo = "".join(self._buffer).strip()
            self.testo.append(self.titolo)
        elif self._in == "ld" and tag == "script":
            self.ld.append("".join(self._buffer))
        if tag in ("title", "script", "style"):
            self._in = None

    def handle_data(self, data):
        if self._in in ("title", "ld"):
            self._buffer.append(data)
        elif self._in not in ("script", "style"):
            self.testo.append(data)

    def handle_comment(self, data):
        self.commenti += 1


def leggi(file):
    p = Pagina()
    with open(file, encoding="utf-8") as f:
        sorgente = f.read()
    p.feed(sorgente)
    p.sorgente = sorgente
    return p


def tipi(dato):
    """Tutti i valori di @type e i null di un blocco JSON-LD, anche annidati."""
    trovati, nulli = set(), 0
    if isinstance(dato, dict):
        t = dato.get("@type")
        trovati |= set(t) if isinstance(t, list) else {t} if t else set()
        for v in dato.values():
            if v is None:
                nulli += 1
            else:
                a, b = tipi(v)
                trovati, nulli = trovati | a, nulli + b
    elif isinstance(dato, list):
        for v in dato:
            a, b = tipi(v)
            trovati, nulli = trovati | a, nulli + b
    return trovati, nulli


# ---------------------------------------------------------------- pagine
pagine = {}
for radice, sotto, nomi in os.walk(DOCS):
    sotto[:] = sorted(s for s in sotto if s != "assets")
    for nome in sorted(nomi):
        if nome.endswith(".html"):
            file = os.path.join(radice, nome)
            pagine[os.path.relpath(file, DOCS).replace(os.sep, "/")] = leggi(file)
if "index.html" not in pagine:
    sys.exit("docs/index.html non c'è: generare prima il sito con python sorgente/genera.py")

URL = (pagine["index.html"].alternative.get("it") or [""])[0]
robots_txt = os.path.join(DOCS, "robots.txt")
PRODUZIONE = os.path.isfile(robots_txt) and "Sitemap:" in open(robots_txt, encoding="utf-8").read()


def indirizzo(relativo):
    """Indirizzo pubblico di un file di docs/: le cartelle finiscono con /, la 404 resta un file."""
    return URL + (relativo[:-len("index.html")] if relativo.endswith("index.html") else relativo)


def file_di(indirizzo_pubblico):
    if not URL or not indirizzo_pubblico.startswith(URL):
        return None
    resto = indirizzo_pubblico[len(URL):]
    return resto + "index.html" if resto == "" or resto.endswith("/") else resto


problemi = defaultdict(list)       # pagina -> [(livello, testo)]


def errore(pagina, testo):
    problemi[pagina].append(("ERRORE", testo))


def avviso(pagina, testo):
    problemi[pagina].append(("avviso", testo))


titoli, descrizioni = defaultdict(list), defaultdict(list)
for rel, p in pagine.items():
    lingua_cartella = "en" if rel.startswith("en/") else "it"
    proprio = indirizzo(rel)
    noindex = "noindex" in p.robots

    # titoli
    if p.h1 == 0:
        errore(rel, "manca l'<h1>")
    elif p.h1 > 1:
        avviso(rel, f"{p.h1} <h1> nella pagina (ne serve uno)")
    if not p.titolo:
        avviso(rel, "manca il <title>")
    else:
        if len(p.titolo) > TITOLO_MAX:
            avviso(rel, f"<title> di {len(p.titolo)} caratteri (massimo {TITOLO_MAX}): «{p.titolo}»")
        titoli[(lingua_cartella, p.titolo)].append(rel)
    if p.descrizione is None:
        avviso(rel, "manca la meta description")
    else:
        if not DESCRIZIONE_MIN <= len(p.descrizione) <= DESCRIZIONE_MAX:
            avviso(rel, f"meta description di {len(p.descrizione)} caratteri (da {DESCRIZIONE_MIN} a {DESCRIZIONE_MAX})")
        descrizioni[(lingua_cartella, p.descrizione)].append(rel)

    # lingua e alternative
    if not p.lang:
        avviso(rel, "manca <html lang>")
    elif p.lang != lingua_cartella:
        avviso(rel, f'<html lang="{p.lang}"> in una pagina della cartella {lingua_cartella}')
    for l in ("it", "en", "x-default"):
        valori = p.alternative.get(l, [])
        if len(valori) != 1:
            avviso(rel, f"hreflang {l}: {len(valori)} link (ne serve uno)")
    if p.alternative.get(lingua_cartella, [None])[0] not in (None, proprio):
        avviso(rel, f"l'hreflang {lingua_cartella} non punta alla pagina stessa ({p.alternative[lingua_cartella][0]})")
    if p.alternative.get("x-default") and p.alternative.get("it") and p.alternative["x-default"][0] != p.alternative["it"][0]:
        avviso(rel, "x-default diverso dalla versione italiana")
    altra = "it" if lingua_cartella == "en" else "en"
    for href in p.alternative.get(altra, [])[:1]:
        arrivo = file_di(href)
        if arrivo not in pagine:
            avviso(rel, f"hreflang {altra} porta a una pagina che non esiste: {href}")
        elif pagine[arrivo].alternative.get(lingua_cartella, [None])[0] != proprio:
            avviso(rel, f"hreflang non reciproco: {arrivo} non rimanda a questa pagina")

    # canonical e indicizzazione
    if PRODUZIONE and not noindex:
        if not p.canonical:
            avviso(rel, "manca il canonical (generazione di produzione)")
        elif p.canonical != proprio:
            avviso(rel, f"canonical diverso dall'indirizzo della pagina: {p.canonical}")
    if PRODUZIONE and noindex and not rel.endswith("404.html"):
        avviso(rel, "noindex in una generazione di produzione")
    if not PRODUZIONE and not noindex:
        avviso(rel, "anteprima senza noindex")

    # immagini
    for img in p.immagini:
        nome_img = img.get("src", "?").rsplit("/", 1)[-1]
        mancano = [a for a in ("alt", "width", "height") if a not in img]
        if mancano:
            avviso(rel, f"<img {nome_img}> senza {', '.join(mancano)}")

    # dati strutturati
    for i, blocco in enumerate(p.ld, 1):
        try:
            dato = json.loads(blocco)
        except json.JSONDecodeError as e:
            errore(rel, f"JSON-LD n. {i} non si legge: {e}")
            continue
        trovati, nulli = tipi(dato)
        if trovati & VIETATI:
            avviso(rel, f"JSON-LD n. {i} contiene {', '.join(sorted(trovati & VIETATI))}: da togliere (recensioni autoreferenziali)")
        if nulli:
            avviso(rel, f"JSON-LD n. {i} ha {nulli} valori null")

    # note interne
    for nota in NOTE_INTERNE:
        if nota in p.sorgente:
            errore(rel, f"nota interna «{nota}» nel sorgente pubblicato")
    if re.search(r"\bNone\b", " ".join(p.testo + p.attributi)):
        errore(rel, "«None» nel testo o negli attributi: un dato mancante finito nella pagina")
    if p.commenti:
        avviso(rel, f"{p.commenti} commenti HTML nel sorgente pubblicato")

for (lingua_pagina, titolo), elenco in titoli.items():
    if len(elenco) > 1:
        for rel in elenco:
            avviso(rel, f"<title> uguale a quello di {', '.join(r for r in elenco if r != rel)}")
for (lingua_pagina, testo), elenco in descrizioni.items():
    if len(elenco) > 1:
        for rel in elenco:
            avviso(rel, f"meta description uguale a quella di {', '.join(r for r in elenco if r != rel)}")

# ---------------------------------------------------------------- tabella
errori = sum(1 for v in problemi.values() for livello, _ in v if livello == "ERRORE")
avvisi = sum(len(v) for v in problemi.values()) - errori
if problemi:
    larghezza = max(len(r) for r in problemi)
    print(f"{'PAGINA':<{larghezza}}  LIVELLO  PROBLEMA")
    for rel in sorted(problemi):
        for livello, testo in sorted(problemi[rel]):
            print(f"{rel:<{larghezza}}  {livello:<7}  {testo}")
    print()
print(f"{len(pagine)} pagine, generazione {'di PRODUZIONE' if PRODUZIONE else 'di anteprima'} per {URL or '(indirizzo sconosciuto)'}: "
      f"{errori} errori, {avvisi} avvisi" + (" (gli avvisi non fermano la pubblicazione)" if avvisi and not errori else ""))
sys.exit(1 if errori else 0)
