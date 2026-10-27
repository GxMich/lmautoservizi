"""Pagina 404: servita a indirizzi qualsiasi, quindi link e risorse sono assoluti (vedi ASSOLUTE in sito.py)."""
from sito import inizia, scrivi, head, testata, intro, piede, t, href, I, TEL, tel_txt


def costruisci():
    inizia("404")
    scrivi(head(t("Pagina non trovata | L.M. Autoservizi", "Page not found | L.M. Autoservizi"),
                t("La pagina che cerchi non esiste: torna alla home di L.M. Autoservizi o chiama Luca.", "The page you're looking for doesn't exist: go back to the L.M. Autoservizi home page or call Luca."),
                noindex=True) + testata()
           + intro(t("Pagina non trovata", "Page not found"), t("Questa pagina non esiste. Torna alla home oppure chiamami: ti rimetto in carreggiata.", "This page doesn't exist. Go back to the home page or give me a call: I'll get you back on the road.")) + f'''
<section class="sezione"><div class="wrap"><div class="azioni"><a class="btn btn--arancio" href="{href("home")}">{t("Torna alla home", "Back to the home page")} {I["freccia"]}</a><a class="btn btn--vuoto" href="tel:{TEL}">{I["tel"]}{tel_txt()}</a></div></div></section>''' + piede())
