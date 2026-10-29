"""Comodità in più, per chi non può portare il mezzo in officina: ritiro e consegna con vettura di cortesia, officina mobile.
La riparazione vera si fa nell'officina di Frassineto Po: entrambe le pagine lo dicono e rimandano a href("officina")."""
from contenuti import FAQ_R
from sito import (inizia, scrivi, head, testata, intro, finale, piede, foto, spunte, azienda, briciole,
                  href, I, TEL, tel_txt, apri, apri_servizio)

def costruisci():
    pagina_ritiro()
    pagina_mobile()


def pagina_ritiro():
    inizia("ritiro")
    tappe_dati = [("Mi chiami o mi scrivi", "Mi dici dov'è il mezzo e cosa non va. Nessun giro di telefonate."),
                  ("Passo a ritirarlo", "Vengo a casa o al lavoro e ti lascio una vettura di cortesia gratuita."),
                  ("Diagnosi e preventivo", "Controllo il mezzo in officina e ti dico cosa serve e quanto costa, prima di iniziare."),
                  ("Lo riparo", "Nella mia officina a Frassineto Po, con il ponte e le attrezzature giuste."),
                  ("Te lo riporto", "Riparato, pulito e igienizzato, dove vuoi. Paghi alla riconsegna.")]
    tappe = "".join(f'<li class="tappa"><span class="tappa-n">{i + 1}</span><div><h3>{titolo}</h3><p>{testo}</p></div></li>' for i, (titolo, testo) in enumerate(tappe_dati))
    domande = [(d, r.replace("dove si trova l'auto", "dove si trova il mezzo")) for d, r in FAQ_R]
    faq = "".join(f'<details><summary>{d}</summary><div class="faq-risposta"><p>{r}</p></div></details>' for d, r in domande)
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": d, "acceptedAnswer": {"@type": "Answer", "text": r}} for d, r in domande]}
    scrivi(head("Ritiro e consegna con vettura di cortesia | L.M. Autoservizi",
                "Ritiro il mezzo a casa o al lavoro, lo riparo nella mia officina a Frassineto Po e te lo riporto. Vettura di cortesia gratuita per tutta la riparazione.",
                [azienda(), faq_schema, briciole("Ritiro e consegna")], immagine="ritiro") + testata()
           + intro("Ritiro e consegna", "Se non puoi portarmi il mezzo, passo io a prenderlo a casa o al lavoro e te lo riporto riparato. La riparazione la faccio nella mia officina a Frassineto Po, e intanto hai una vettura di cortesia gratuita.") + f'''
<section class="sezione">
  <div class="wrap ritiro-griglia">
    <div>
      <h2>Come funziona</h2>
      <div class="percorso" data-percorso><span class="percorso-linea" aria-hidden="true"><span></span></span><ol class="percorso-tappe">{tappe}</ol></div>
      <div class="rimando-officina">
        <p>Se preferisci portarmelo tu, l'officina è aperta dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato.</p>
        <a class="link" href="{href("officina")}">Scopri l'officina {I["freccia"]}</a>
      </div>
    </div>
    {foto("ritiro", "(max-width: 899px) 100vw, 40vw", "foto ritiro-foto")}
  </div>
</section>
<section class="sezione sezione--asfalto" id="domande">
  <div class="wrap ritiro-dettagli">
    <div><h2>Domande frequenti</h2><div class="faq">{faq}</div></div>
    <div class="riquadro">
      <h2>Chiedi il ritiro</h2>
      <p>Dimmi dove si trova il mezzo e cosa non va: il resto lo sistemiamo su WhatsApp.</p>
      {apri("ritiro", "Chiedi il ritiro")}
      <a class="link" href="tel:{TEL}">{I["tel"]}Oppure chiama {tel_txt()}</a>
    </div>
  </div>
</section>''' + piede())


def pagina_mobile():
    inizia("mobile")
    scrivi(head("Officina mobile a domicilio | L.M. Autoservizi",
                "Forature, cambio delle ruote montate, diagnosi e avviamento direttamente dove si trova il mezzo, a Casale Monferrato e nei paesi vicini.",
                [azienda(), briciole()], immagine="officina-mobile") + testata()
           + intro("Officina mobile", "Se non puoi portarmi il mezzo e il lavoro si può fare sul posto, arrivo io con il furgone attrezzato. Tutto il resto lo riparo nella mia officina a Frassineto Po.") + f'''
<section class="sezione">
  <div class="wrap mobile-griglia">
    <div class="mobile-presentazione">
      <h2>L'officina arriva da te.</h2>
      <p class="lead">Un intervento sul posto, quando si può. Il ritiro in officina, quando serve.</p>
      {foto("officina-mobile", "(max-width: 899px) 100vw, 50vw", "foto mobile-foto")}
    </div>
    <div class="mobile-dettagli">
      <h2>Cosa faccio sul posto</h2>
      {spunte(["Riparazione delle forature", "Cambio delle ruote già montate sui cerchi",
               "Diagnosi elettronica e lettura delle spie", "Problemi elettrici e di avviamento, nei casi semplici"])}
      <h2>E quando serve l'officina</h2>
      <p>Se il lavoro richiede il ponte o tempi lunghi, ritiro il mezzo e ti lascio una vettura di cortesia gratuita. Il preventivo è sempre gratuito e arriva prima di iniziare.</p>
      <a class="link" href="{href("officina")}">Scopri l'officina {I["freccia"]}</a>
      <div class="azioni">{apri_servizio("soccorso", "Chiedi assistenza a domicilio")}<a class="btn btn--vuoto" href="tel:{TEL}">{I["tel"]}Chiama {tel_txt()}</a></div>
      <p class="piccolo">Lavoro a Casale Monferrato e nei paesi vicini. Chiama per sapere se arrivo anche da te.</p>
    </div>
  </div>
</section>''' + finale() + piede())
