"""Comodità in più, per chi non può portare il mezzo in officina: ritiro e consegna con vettura di cortesia, officina mobile.
La riparazione vera si fa nell'officina di Frassineto Po: entrambe le pagine lo dicono e rimandano a href("officina")."""
from contenuti import FAQ_R
from sito import (inizia, scrivi, head, testata, intro, finale, piede, foto, spunte, azienda, briciole,
                  t, tt, lingua, href, I, TEL, tel_txt, apri, apri_servizio)

FAQ_EN = [("How much does pick-up cost?", "Tell me where the vehicle is: I'll tell you straight away whether there's a charge and how much, before I set off."),
          ("How far do you go?", "I collect and deliver in Casale Monferrato and nearby villages. Call to check whether I can reach you."),
          ("How much is the courtesy car?", "Nothing: it's always free. I leave it fuelled, clean and sanitised, for as long as you need it."),
          ("What if the repair takes several days?", "The courtesy car stays with you for the whole repair. I keep you updated on progress."),
          ("How do I pay?", "In cash or by card, on delivery.")]


def costruisci():
    pagina_ritiro()
    pagina_mobile()


def pagina_ritiro():
    inizia("ritiro")
    tappe_dati = [(("Mi chiami o mi scrivi", "You call or message me"), ("Mi dici dov'è il mezzo e cosa non va. Nessun giro di telefonate.", "Tell me where the vehicle is and what's wrong. No endless phone calls.")),
                  (("Passo a ritirarlo", "I collect it"), ("Vengo a casa o al lavoro e ti lascio una vettura di cortesia gratuita.", "I come to your home or workplace and leave you a free courtesy car.")),
                  (("Diagnosi e preventivo", "Diagnosis and quote"), ("Controllo il mezzo in officina e ti dico cosa serve e quanto costa, prima di iniziare.", "I check the vehicle in the workshop and tell you what's needed and what it costs, before starting.")),
                  (("Lo riparo", "I repair it"), ("Nella mia officina a Frassineto Po, con il ponte e le attrezzature giuste.", "In my workshop in Frassineto Po, with the lift and the right equipment.")),
                  (("Te lo riporto", "I bring it back"), ("Riparato, pulito e igienizzato, dove vuoi. Paghi alla riconsegna.", "Repaired, clean and sanitised, wherever you like. You pay on delivery."))]
    tappe = "".join(f'<li class="tappa"><span class="tappa-n">{i + 1}</span><div><h3>{tt(titolo)}</h3><p>{tt(testo)}</p></div></li>' for i, (titolo, testo) in enumerate(tappe_dati))
    domande = FAQ_EN if lingua() == "en" else [(d, r.replace("dove si trova l'auto", "dove si trova il mezzo")) for d, r in FAQ_R]
    faq = "".join(f'<details><summary>{d}</summary><div class="faq-risposta"><p>{r}</p></div></details>' for d, r in domande)
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": d, "acceptedAnswer": {"@type": "Answer", "text": r}} for d, r in domande]}
    scrivi(head(t("Ritiro e consegna con vettura di cortesia | L.M. Autoservizi", "Pick-up and delivery with courtesy car | L.M. Autoservizi"),
                t("Ritiro il mezzo a casa o al lavoro, lo riparo nella mia officina a Frassineto Po e te lo riporto. Vettura di cortesia gratuita per tutta la riparazione.",
                  "I collect your vehicle from home or work, repair it in my workshop in Frassineto Po and bring it back. Free courtesy car for the whole repair."),
                [azienda(), faq_schema, briciole(t("Ritiro e consegna", "Pick-up and delivery"))], immagine="ritiro") + testata()
           + intro(t("Ritiro e consegna", "Pick-up and delivery"), t("Se non puoi portarmi il mezzo, passo io a prenderlo a casa o al lavoro e te lo riporto riparato. La riparazione la faccio nella mia officina a Frassineto Po, e intanto hai una vettura di cortesia gratuita.",
                                                                     "If you can't bring me the vehicle, I collect it from your home or workplace and bring it back repaired. The repair itself is done in my workshop in Frassineto Po, and in the meantime you have a free courtesy car.")) + f'''
<section class="sezione">
  <div class="wrap ritiro-griglia">
    <div>
      <h2>{t("Come funziona", "How it works")}</h2>
      <div class="percorso" data-percorso><span class="percorso-linea" aria-hidden="true"><span></span></span><ol class="percorso-tappe">{tappe}</ol></div>
      <div class="rimando-officina">
        <p>{t("Se preferisci portarmelo tu, l'officina è aperta dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato.", "If you'd rather bring it in yourself, the workshop is open Monday to Friday, 7:30 to 19:30, with no lunch break.")}</p>
        <a class="link" href="{href("officina")}">{t("Scopri l'officina", "Discover the workshop")} {I["freccia"]}</a>
      </div>
    </div>
    {foto("ritiro", "(max-width: 899px) 100vw, 40vw", "foto ritiro-foto")}
  </div>
</section>
<section class="sezione sezione--asfalto" id="domande">
  <div class="wrap ritiro-dettagli">
    <div><h2>{t("Domande frequenti", "Frequently asked questions")}</h2><div class="faq">{faq}</div></div>
    <div class="riquadro">
      <h2>{t("Chiedi il ritiro", "Request a pick-up")}</h2>
      <p>{t("Dimmi dove si trova il mezzo e cosa non va: il resto lo sistemiamo su WhatsApp.", "Tell me where the vehicle is and what's wrong: we'll sort out the rest on WhatsApp.")}</p>
      {apri("ritiro", t("Chiedi il ritiro", "Request a pick-up"))}
      <a class="link" href="tel:{TEL}">{I["tel"]}{t("Oppure chiama", "Or call")} {tel_txt()}</a>
    </div>
  </div>
</section>''' + piede())


def pagina_mobile():
    inizia("mobile")
    scrivi(head(t("Officina mobile a domicilio | L.M. Autoservizi", "Mobile workshop at your home | L.M. Autoservizi"),
                t("Forature, cambio delle ruote montate, diagnosi e avviamento direttamente dove si trova il mezzo, a Casale Monferrato e nei paesi vicini.",
                  "Punctures, changing mounted wheels, diagnostics and starting problems fixed where your vehicle is, in Casale Monferrato and nearby villages."),
                [azienda(), briciole()], immagine="officina-mobile") + testata()
           + intro(t("Officina mobile", "Mobile workshop"), t("Se non puoi portarmi il mezzo e il lavoro si può fare sul posto, arrivo io con il furgone attrezzato. Tutto il resto lo riparo nella mia officina a Frassineto Po.",
                                                             "If you can't bring me the vehicle and the job can be done on site, I come to you with my equipped van. Everything else I repair in my workshop in Frassineto Po.")) + f'''
<section class="sezione">
  <div class="wrap mobile-griglia">
    <div class="mobile-presentazione">
      <h2>{t("L'officina arriva da te.", "The workshop comes to you.")}</h2>
      <p class="lead">{t("Un intervento sul posto, quando si può. Il ritiro in officina, quando serve.", "A repair on the spot when possible. Collection to the workshop when needed.")}</p>
      {foto("officina-mobile", "(max-width: 899px) 100vw, 50vw", "foto mobile-foto")}
    </div>
    <div class="mobile-dettagli">
      <h2>{t("Cosa faccio sul posto", "What I do on site")}</h2>
      {spunte([("Riparazione delle forature", "Puncture repair"), ("Cambio delle ruote già montate sui cerchi", "Changing wheels already mounted on rims"),
               ("Diagnosi elettronica e lettura delle spie", "Electronic diagnostics and warning lights"), ("Problemi elettrici e di avviamento, nei casi semplici", "Electrical and starting problems, in simple cases")])}
      <h2>{t("E quando serve l'officina", "When the workshop is needed")}</h2>
      <p>{t("Se il lavoro richiede il ponte o tempi lunghi, ritiro il mezzo e ti lascio una vettura di cortesia gratuita. Il preventivo è sempre gratuito e arriva prima di iniziare.",
              "If the job needs the lift or more time, I collect the vehicle and leave you a free courtesy car. The quote is always free and comes before any work starts.")}</p>
      <a class="link" href="{href("officina")}">{t("Scopri l'officina", "Discover the workshop")} {I["freccia"]}</a>
      <div class="azioni">{apri_servizio("soccorso", t("Chiedi assistenza a domicilio", "Request at-home assistance"))}<a class="btn btn--vuoto" href="tel:{TEL}">{I["tel"]}{t("Chiama", "Call")} {tel_txt()}</a></div>
      <p class="piccolo">{t("Lavoro a Casale Monferrato e nei paesi vicini. Chiama per sapere se arrivo anche da te.", "I work in Casale Monferrato and nearby villages. Call to check whether I can reach you.")}</p>
    </div>
  </div>
</section>''' + finale() + piede())
