"""Chi sono: Luca, il suo percorso e gli attestati (si aprono a grandezza piena)."""
from contenuti import ATT
from sito import (inizia, scrivi, head, testata, intro, finale, piede, foto, azienda, briciole, risorsa,
                  t, tt, attr, lingua, I)

ATT_EN = {"qualifica-professionale": ("Vehicle electromechanical repair technician", "Professional qualification, 400 hours, 2010"),
          "responsabile-revisioni": ("Technical manager for periodic vehicle inspections", "Certificate of competence"),
          "gas-fluorurati": ("F-gas recovery in vehicles", "Car air conditioning, Reg. EC 307/2008, 2012"),
          "diploma": ("Scientific-technological high school diploma", "IIS A. Sobrero, Casale Monferrato, 2009"),
          "sicurezza-generale": ("Workplace safety: general and specific training", "Legislative Decree 81/2008, 8 hours"),
          "sicurezza-specifica": ("Workplace safety: specific training", "Legislative Decree 81/2008, 4 hours"),
          "inglese": ("English language, level 2", "Certificate of attendance and achievement, 2011"),
          "gran-turismo": ("Grand touring car driving", "Puresport")}


def costruisci():
    inizia("chi")
    voci_att = [(f, *(ATT_EN[f] if lingua() == "en" else (titolo, sotto))) for f, titolo, sotto in ATT]
    attestati = "".join(f'''<li><button type="button" data-lightbox="{risorsa(f"assets/img/attestati/{f}.webp")}" data-titolo="{attr(titolo)}"><img src="{risorsa(f"assets/img/attestati/{f}-thumb.webp")}" alt="" loading="lazy" decoding="async" width="340" height="480"><span>{titolo}<small>{sotto}</small></span></button></li>''' for f, titolo, sotto in voci_att)
    lightbox = f'''<dialog class="lightbox" id="lightbox" aria-labelledby="lightbox-t" data-lenis-prevent>
  <figure><figcaption id="lightbox-t"></figcaption></figure>
  <button class="lightbox-chiudi" type="button" aria-label="{t("Chiudi", "Close")}" data-chiudi>{I["chiudi"]}</button>
</dialog>
'''
    cronologia = [("2009", ("Diploma di liceo scientifico tecnologico a Casale Monferrato.", "Scientific-technological high school diploma in Casale Monferrato.")),
                  ("2010", ("Qualifica di operatore di riparazioni elettromeccaniche per l'autoveicolo.", "Qualification as vehicle electromechanical repair technician.")),
                  ("2012", ("Formazione per il recupero dei gas fluorurati degli impianti di climatizzazione.", "Training in F-gas recovery from air-conditioning systems.")),
                  (("Oggi", "Today"), ("Titolare di L.M. Autoservizi, con officina a Frassineto Po, ritiro e consegna e officina mobile.", "Owner of L.M. Autoservizi, with a workshop in Frassineto Po, pick-up and delivery, and a mobile workshop."))]
    crono = "".join(f'<li><b>{tt(anno)}</b><span>{tt(testo)}</span></li>' for anno, testo in cronologia)
    scrivi(head(t("Chi sono: Luca Miglietta | L.M. Autoservizi", "About me: Luca Miglietta | L.M. Autoservizi"),
                t("Luca Miglietta, titolare di L.M. Autoservizi: qualifica in riparazioni elettromeccaniche, responsabile tecnico delle revisioni, oltre dieci anni multimarca.",
                  "Luca Miglietta, owner of L.M. Autoservizi: qualified in vehicle electromechanical repairs, technical manager for inspections, over ten years on all makes."),
                [azienda(), briciole()], immagine="luca") + testata()
           + intro(t("Chi sono", "About me"), t("Mi chiamo Luca Miglietta. Lavoro da solo: il mezzo che mi affidi lo segue una persona sola, dall'inizio alla fine.",
                                                "My name is Luca Miglietta. I work alone: the vehicle you leave with me is looked after by one person, from start to finish.")) + f'''
<section class="sezione">
  <div class="wrap chi-griglia">
    {foto("luca", "(max-width: 899px) 100vw, 45vw", "foto chi-foto")}
    <div>
      <dl class="tessera">
        <div><dt>{t("Titolare", "Owner")}</dt><dd>Luca Miglietta</dd></div>
        <div><dt>{t("Officina", "Workshop")}</dt><dd>Frassineto Po (AL)</dd></div>
        <div><dt>{t("Esperienza", "Experience")}</dt><dd>{t("Più di dieci anni, multimarca", "Over ten years, all makes")}</dd></div>
        <div><dt>{t("Abilitazione", "Qualification")}</dt><dd>{t("Responsabile tecnico delle revisioni", "Technical manager for vehicle inspections")}</dd></div>
      </dl>
      <h2>{t("Il mio percorso", "My background")}</h2>
      <ol class="cronologia" data-cronologia>{crono}</ol>
    </div>
  </div>
</section>
<section class="sezione sezione--asfalto">
  <div class="wrap">
    <h2>{t("Attestati", "Certificates")}</h2>
    <p class="piccolo">{t("Tocca un attestato per vederlo a grandezza piena.", "Tap a certificate to see it full size.")}</p>
    <ul class="attestati">{attestati}</ul>
  </div>
</section>''' + finale() + piede(lightbox))
