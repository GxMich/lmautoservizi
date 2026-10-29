"""Pagina 404: servita a indirizzi qualsiasi, quindi link e risorse sono assoluti (vedi ASSOLUTE in sito.py)."""
from sito import inizia, scrivi, head, testata, intro, piede, href, I, TEL, tel_txt


def costruisci():
    inizia("404")
    scrivi(head("Pagina non trovata | L.M. Autoservizi",
                "La pagina che cerchi non esiste: torna alla home di L.M. Autoservizi o chiama Luca.",
                noindex=True) + testata()
           + intro("Pagina non trovata", "Questa pagina non esiste. Torna alla home oppure chiamami: ti rimetto in carreggiata.") + f'''
<section class="sezione"><div class="wrap"><div class="azioni"><a class="btn btn--arancio" href="{href("home")}">Torna alla home {I["freccia"]}</a><a class="btn btn--vuoto" href="tel:{TEL}">{I["tel"]}{tel_txt()}</a></div></div></section>''' + piede())
