"""Chi sono: Luca, il suo percorso e gli attestati (si aprono a grandezza piena)."""
from contenuti import ATT, ANNI_ESPERIENZA
from sito import (inizia, scrivi, head, testata, intro, finale, piede, foto, azienda, briciole, risorsa,
                  attr, anni_esperienza, abilitazioni, lightbox, indirizzo_officina, I)

def costruisci():
    inizia("chi")
    attestati = "".join(f'''<li><button type="button" data-lightbox="{risorsa(f"assets/img/attestati/{f}.webp")}" data-titolo="{attr(titolo)}"><img src="{risorsa(f"assets/img/attestati/{f}-thumb.webp")}" alt="" loading="lazy" decoding="async" width="340" height="480"><span>{titolo}<small>{sotto}</small></span></button></li>''' for f, titolo, sotto in ATT)
    cronologia = [("2009", "Diploma di liceo scientifico tecnologico a Casale Monferrato."),
                  ("2010", "Qualifica di operatore di riparazioni elettromeccaniche per l'autoveicolo."),
                  ("2012", "Formazione per il recupero dei gas fluorurati degli impianti di climatizzazione."),
                  ("Oggi", "Titolare di L.M. Autoservizi, con officina a Frassineto Po, ritiro e consegna e assistenza a domicilio.")]
    crono = "".join(f'<li><b>{anno}</b><span>{testo}</span></li>' for anno, testo in cronologia)
    scrivi(head("Chi sono: Luca Miglietta | L.M. Autoservizi",
                f"Luca Miglietta, titolare di L.M. Autoservizi: qualifica in riparazioni elettromeccaniche, responsabile tecnico delle revisioni, {ANNI_ESPERIENZA} anni multimarca.",
                [azienda(), briciole()], immagine="luca") + testata()
           + intro("Chi sono", "Mi chiamo Luca Miglietta. Lavoro da solo: il mezzo che mi affidi lo segue una persona sola, dall'inizio alla fine.") + f'''
<section class="sezione">
  <div class="wrap chi-griglia">
    {foto("luca", "(max-width: 899px) 100vw, 45vw", "foto chi-foto")}
    <div>
      <dl class="tessera">
        <div><dt>Titolare</dt><dd>Luca Miglietta</dd></div>
        <div><dt>Officina</dt><dd>{indirizzo_officina()}</dd></div>
        <div><dt>Esperienza</dt><dd>{anni_esperienza()} anni, multimarca</dd></div>
        <div><dt>Mezzi</dt><dd>Auto, fuoristrada, furgoni e camper</dd></div>
        <div><dt>Officina abilitata</dt><dd>{abilitazioni().capitalize()}</dd></div>
        <div><dt>Revisioni</dt><dd>Responsabile tecnico delle revisioni</dd></div>
      </dl>
      <h2>Il mio percorso</h2>
      <ol class="cronologia" data-cronologia>{crono}</ol>
    </div>
  </div>
</section>
<section class="sezione sezione--asfalto">
  <div class="wrap">
    <h2>Attestati</h2>
    <p class="piccolo">Tocca un attestato per vederlo a grandezza piena.</p>
    <ul class="attestati">{attestati}</ul>
  </div>
</section>''' + finale() + piede(lightbox()))
