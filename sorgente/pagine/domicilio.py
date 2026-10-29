"""Ritiro e consegna (gratis entro 20 km) e assistenza a domicilio (solo gli interventi veloci): dal 29/10/2026 stanno
alla pari con l'officina. I lavori lunghi si fanno nell'officina di Frassineto Po: entrambe le pagine rimandano a href("officina")
e l'una all'altra. Le frasi su zona e vettura di cortesia vengono da contenuti.py (ZONA_TESTO, CORTESIA_TESTO)."""
from contenuti import FAQ_R, ZONA_TESTO, CORTESIA_TESTO
from sito import (inizia, scrivi, head, testata, intro, finale, piede, foto, spunte, azienda, briciole, url, zona_servita,
                  href, I, TEL, tel_txt, apri, apri_servizio, ZONA)


def costruisci():
    pagina_ritiro()
    pagina_mobile()


def schema_servizio(tipo, nome, descrizione):
    return {"@context": "https://schema.org", "@type": "Service", "serviceType": tipo, "name": nome, "description": descrizione,
            "provider": {"@id": azienda()["@id"]}, "url": url(), "areaServed": zona_servita()}


def cta(pulsante, nota="Il messaggio si apre su WhatsApp, già pronto: l'invio lo confermi tu."):
    """Pulsanti subito sotto l'introduzione: chi arriva su queste pagine ha già deciso, non deve scorrere per chiedere."""
    return f'''
<div class="servizio-cta">
  <div class="wrap">
    <div class="azioni">{pulsante}<a class="btn btn--vuoto" href="tel:{TEL}">{I["tel"]}Chiama {tel_txt()}</a></div>
    <p class="piccolo">{nota}</p>
  </div>
</div>'''


def pagina_ritiro():
    inizia("ritiro")
    tappe_dati = [("Mi chiami o mi scrivi", "Mi dici dov'è il mezzo e cosa non va."),
                  ("Passo a ritirarlo", "Vengo a casa o al lavoro, gratis entro 20 km. Se ti serve e se è libera, ti lascio la vettura di cortesia."),
                  ("Diagnosi e preventivo", "Controllo il mezzo in officina e ti dico cosa serve e quanto costa, prima di iniziare."),
                  ("Lo riparo", "Nella mia officina a Frassineto Po, con il ponte e le attrezzature giuste."),
                  ("Te lo riporto", "Riparato, dove vuoi. Paghi alla riconsegna.")]
    tappe = "".join(f'<li class="tappa"><span class="tappa-n">{i + 1}</span><div><h3>{titolo}</h3><p>{testo}</p></div></li>' for i, (titolo, testo) in enumerate(tappe_dati))
    faq = "".join(f'<details><summary>{d}</summary><div class="faq-risposta"><p>{r}</p></div></details>' for d, r in FAQ_R)
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": d, "acceptedAnswer": {"@type": "Answer", "text": r}} for d, r in FAQ_R]}
    comuni = "".join(f"<li>{c}</li>" for c in ZONA)
    descrizione = "Passo a prendere il mezzo a casa o al lavoro, gratis entro 20 km da Frassineto Po, lo riparo in officina e te lo riporto. Chiedi il ritiro su WhatsApp."
    scrivi(head("Ritiro auto gratis, Frassineto Po e Casale | L.M. Autoservizi", descrizione,
                [azienda(), schema_servizio("Ritiro e consegna del veicolo", "Ritiro e consegna gratis entro 20 km", descrizione),
                 faq_schema, briciole("Ritiro e consegna")], immagine="ritiro") + testata()
           + intro("Ritiro e consegna gratis", "Se non puoi portarmi il mezzo, passo io a prenderlo a casa o al lavoro e te lo riporto riparato. È gratis entro 20 km da Frassineto Po. La riparazione la faccio nella mia officina.")
           # dal menu si arriva qui anche per il domicilio (voce "Ritiro e domicilio"): il collegamento sta subito sotto i pulsanti
           + cta(apri("ritiro", "Chiedi il ritiro"),
                 f'Ti serve solo una batteria, una diagnosi o la gomma bucata riparata? <a class="link" href="{href("mobile")}">Arrivo io, a domicilio {I["freccia"]}</a>') + f'''
<section class="sezione">
  <div class="wrap ritiro-griglia">
    <div>
      <h2>Come funziona</h2>
      <div class="percorso" data-percorso><span class="percorso-linea" aria-hidden="true"><span></span></span><ol class="percorso-tappe">{tappe}</ol></div>
      <div class="rimando-officina">
        <p>Se preferisci portarmelo tu, l'officina è aperta dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato. Per batteria, diagnosi e gomma bucata arrivo io, dove sei.</p>
        <div class="azioni"><a class="link" href="{href("officina")}">Scopri l'officina {I["freccia"]}</a><a class="link" href="{href("mobile")}">Assistenza a domicilio {I["freccia"]}</a></div>
      </div>
    </div>
    {foto("ritiro", "(max-width: 899px) 100vw, 40vw", "foto ritiro-foto")}
  </div>
</section>
<section class="sezione sezione--stretta" id="dove" aria-labelledby="dove-t">
  <div class="wrap">
    <h2 id="dove-t">Dove arrivo</h2>
    <p class="lead">Ritiro e riconsegno {ZONA_TESTO}. Questi sono i comuni più vicini: se il tuo non c'è, chiamami.</p>
    <ul class="comuni">{comuni}</ul>
  </div>
</section>
<section class="sezione sezione--asfalto" id="domande">
  <div class="wrap ritiro-dettagli">
    <div><h2>Domande frequenti</h2><div class="faq">{faq}</div></div>
    <div class="riquadro">
      <h2>Chiedi il ritiro</h2>
      <p>Dimmi dove si trova il mezzo e cosa non va: il resto lo sistemiamo su WhatsApp. {CORTESIA_TESTO}</p>
      {apri("ritiro", "Chiedi il ritiro")}
      <a class="link" href="tel:{TEL}">{I["tel"]}Oppure chiama {tel_txt()}</a>
    </div>
  </div>
</section>''' + piede())


def pagina_mobile():
    inizia("mobile")
    descrizione = "Cambio della batteria, diagnosi con il computer e gomma bucata riparata dove si trova il mezzo, entro 20 km da Frassineto Po, vicino a Casale."
    scrivi(head("Meccanico a domicilio, Frassineto Po e Casale | L.M. Autoservizi", descrizione,
                [azienda(), schema_servizio("Assistenza a domicilio", "Assistenza a domicilio per gli interventi veloci", descrizione), briciole()],
                immagine="officina-mobile") + testata()
           + intro("Assistenza a domicilio", "Per gli interventi veloci arrivo io, dove si trova il mezzo: cambio la batteria, faccio la diagnosi con il computer, riparo la gomma bucata. Il resto lo riparo nella mia officina a Frassineto Po.")
           + cta(apri_servizio("soccorso", "Chiedi assistenza a domicilio")) + f'''
<section class="sezione">
  <div class="wrap mobile-griglia">
    <div class="mobile-presentazione">
      <h2>Arrivo io, dove sei.</h2>
      <p class="lead">Batteria, diagnosi e gomma bucata li sistemo sul posto. Per il resto porto il mezzo in officina.</p>
      {foto("officina-mobile", "(max-width: 899px) 100vw, 50vw", "foto mobile-foto")}
    </div>
    <div class="mobile-dettagli">
      <h2>Cosa faccio sul posto</h2>
      {spunte(["Cambio della batteria", "Diagnosi con il computer e lettura delle spie", "Riparazione della gomma bucata"])}
      <h2>E quando serve l'officina</h2>
      <p>Se il lavoro richiede il ponte o tempi lunghi, ritiro il mezzo gratis e te lo riporto riparato. Il preventivo è gratuito e te lo do prima di iniziare.</p>
      <div class="azioni"><a class="link" href="{href("ritiro")}">Come funziona il ritiro {I["freccia"]}</a><a class="link" href="{href("officina")}">Scopri l'officina {I["freccia"]}</a></div>
      <p class="piccolo">Arrivo {ZONA_TESTO}. Se non sei sicuro, chiamami.</p>
    </div>
  </div>
</section>''' + finale() + piede())
