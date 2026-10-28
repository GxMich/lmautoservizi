"""Controlla i collegamenti del sito generato: python sorgente/controlla_link.py
Per ogni pagina HTML in docs/ verifica che ogni href, src, srcset e data-lightbox relativo porti a un file esistente
(una cartella vale se contiene index.html) e che ogni #frammento esista nella pagina di arrivo.
Gli indirizzi assoluti che cominciano con l'indirizzo pubblico del sito (LM_URL: canonical, hreflang, og:image, pagina 404)
si controllano allo stesso modo sui file locali; gli altri indirizzi esterni, mailto: e tel: si saltano.
Controlla anche gli url() di assets/sito.css, le icone di site.webmanifest e la sitemap; in produzione anche
i link di llms.txt e le destinazioni di _redirects. Esce con errore se trova problemi."""
import json, os, posixpath, re, sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
from sito import DOCS, URL

sys.stdout.reconfigure(encoding="utf-8")
ATTRIBUTI = ("href", "src", "srcset", "data-lightbox")
ESTERNI = ("mailto:", "tel:", "javascript:", "data:", "http:", "https:", "//")


class Pagina(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.id, self.link = set(), []

    def handle_starttag(self, tag, attrs):
        for nome, valore in attrs:
            if valore is None:
                continue
            if nome == "id":
                self.id.add(valore)
            elif nome == "srcset":
                self.link += [(tag, nome, parte.strip().split()[0]) for parte in valore.split(",") if parte.strip()]
            elif nome in ATTRIBUTI:
                self.link.append((tag, nome, valore))


_cache = {}


def leggi(file):
    if file not in _cache:
        p = Pagina()
        with open(file, encoding="utf-8") as f:
            p.feed(f.read())
        _cache[file] = p
    return _cache[file]


def destinazione(cartella, valore):
    """(file locale o None se esterno, frammento). cartella: posizione della pagina rispetto a docs/."""
    if valore.startswith(URL):
        cartella, valore = "", "./" + valore[len(URL):]
    elif valore.startswith(ESTERNI):
        return None, ""
    parti = urlsplit(valore)
    percorso = unquote(parti.path)
    if not percorso:
        return "", parti.fragment  # stessa pagina
    unito = posixpath.normpath(posixpath.join(cartella, percorso))
    if unito.startswith(".."):
        return "../" + unito, parti.fragment
    file = os.path.join(DOCS, *unito.split("/")) if unito != "." else DOCS
    if percorso.endswith("/") or os.path.isdir(file):
        file = os.path.join(file, "index.html")
    return file, parti.fragment


problemi, contati = [], {"pagine": 0, "riferimenti": 0, "assoluti": 0, "frammenti": 0}
for radice, sotto, nomi in os.walk(DOCS):
    sotto[:] = sorted(s for s in sotto if s not in ("assets", "domande"))  # domande/: questionario a sé, solo in anteprima
    for nome in sorted(nomi):
        if not nome.endswith(".html"):
            continue
        file = os.path.join(radice, nome)
        relativo = os.path.relpath(file, DOCS).replace(os.sep, "/")
        cartella = posixpath.dirname(relativo)
        pagina = leggi(file)
        contati["pagine"] += 1
        for tag, attributo, valore in pagina.link:
            arrivo, frammento = destinazione(cartella, valore)
            if arrivo is None:
                continue
            contati["riferimenti"] += 1
            contati["assoluti"] += valore.startswith(URL)
            if arrivo == "":
                arrivo = file
            if arrivo.startswith("../") or not os.path.isfile(arrivo):
                problemi.append(f"{relativo}: <{tag} {attributo}=\"{valore}\"> porta a un file che non esiste")
                continue
            if frammento:
                contati["frammenti"] += 1
                if arrivo.endswith(".html") and frammento not in leggi(arrivo).id:
                    problemi.append(f"{relativo}: <{tag} {attributo}=\"{valore}\"> il frammento #{frammento} non esiste")

# url() del foglio di stile, icone del manifest, indirizzi della sitemap
css = os.path.join(DOCS, "assets", "sito.css")
if os.path.isfile(css):
    for valore in re.findall(r'url\(["\']?([^"\')]+)["\']?\)', open(css, encoding="utf-8").read()):
        arrivo, _ = destinazione("assets", valore)
        if arrivo is not None:
            contati["riferimenti"] += 1
            if arrivo.startswith("../") or not os.path.isfile(arrivo):
                problemi.append(f"assets/sito.css: url({valore}) porta a un file che non esiste")
manifest = os.path.join(DOCS, "site.webmanifest")
if os.path.isfile(manifest):
    for icona in json.load(open(manifest, encoding="utf-8")).get("icons", []):
        contati["riferimenti"] += 1
        if not os.path.isfile(destinazione("", icona["src"])[0]):
            problemi.append(f"site.webmanifest: l'icona {icona['src']} non esiste")
sitemap = os.path.join(DOCS, "sitemap.xml")
if os.path.isfile(sitemap):
    for valore in re.findall(r'(?:<loc>|href=")([^<"]+)', open(sitemap, encoding="utf-8").read()):
        arrivo, _ = destinazione("", valore)
        contati["riferimenti"] += 1
        contati["assoluti"] += 1
        if arrivo is None or not os.path.isfile(arrivo):
            problemi.append(f"sitemap.xml: {valore} non corrisponde a una pagina generata")

# solo in produzione: link di llms.txt (assoluti) e destinazioni di _redirects (dalla radice del dominio)
llms = os.path.join(DOCS, "llms.txt")
if os.path.isfile(llms):
    for valore in re.findall(r"\]\((https?://[^)\s]+)\)", open(llms, encoding="utf-8").read()):
        arrivo, _ = destinazione("", valore)
        contati["riferimenti"] += 1
        if arrivo is None:
            problemi.append(f"llms.txt: {valore} non è un indirizzo di {URL}")
        elif not os.path.isfile(arrivo):
            problemi.append(f"llms.txt: {valore} non corrisponde a una pagina generata")
redirects = os.path.join(DOCS, "_redirects")
if os.path.isfile(redirects):
    base = urlsplit(URL).path or "/"
    for riga in open(redirects, encoding="utf-8"):
        parti = riga.split("#", 1)[0].split()
        if not parti:
            continue
        contati["riferimenti"] += 1
        if len(parti) < 2 or not parti[1].startswith(base):
            problemi.append(f"_redirects: riga non valida o fuori dal sito: {riga.strip()}")
            continue
        arrivo, _ = destinazione("", "./" + parti[1][len(base):])
        if not os.path.isfile(arrivo):
            problemi.append(f"_redirects: {parti[0]} porta a {parti[1]}, che non esiste")

for p in problemi:
    print("PROBLEMA", p)
print(f"{contati['pagine']} pagine HTML, {contati['riferimenti']} riferimenti controllati "
      f"({contati['assoluti']} assoluti verso {URL}), {contati['frammenti']} frammenti: "
      + (f"{len(problemi)} problemi" if problemi else "nessun problema"))
sys.exit(1 if problemi else 0)
