"""Home: "Riparti sereno.", le caselle dei servizi con la tendina WhatsApp, l'officina a Frassineto Po (il centro),
Luca, recensioni, le comodità in più (ritiro, officina mobile, imprese), dove e quando. Testi nuovi in testi_pagine.HOME."""
from contenuti import RECENSIONI, RECENSIONI_GOOGLE, RECENSIONI_CON_PERMESSO, GEAR_PIENO
from testi_pagine import HOME
from pagine.officina import ICO
from sito import (inizia, scrivi, head, testata, piede, orari, griglia_servizi, foto, img, foto_info, nota_foto, azienda,
                  t, tt, lingua, href, I, VANTAGGI_ICO, TEL, EMAIL, MAPS, tel_txt, wa, nota_recensioni)


def costruisci():
    inizia("home")
    # L'officina: tre punti con le icone che si disegnano (gancio .vantaggi-lista di 00-base.js).
    punti = "".join(f'<li>{ICO[ico]}<h3>{tt(titolo)}</h3><p>{tt(testo)}</p></li>'
                    for ico, (titolo, testo) in zip(("orario", "cortesia", "preventivo"), HOME["officina_punti"]))
    # Le comodità in più: righe leggere, ognuna porta alla sua pagina.
    extra = "".join(f'<li><a class="extra-voce" href="{link}"><span class="extra-ico" aria-hidden="true">{ico}</span>'
                    f'<div><h3>{tt(titolo)}</h3><p>{tt(testo)}</p></div>{I["freccia"]}</a></li>'
                    for (ico, link), (titolo, testo) in zip(((VANTAGGI_ICO["rotta"], href("ritiro")), (VANTAGGI_ICO["mobile"], href("mobile")),
                                                            (VANTAGGI_ICO["aziende"], href("servizi", frammento="aziende"))), HOME["extra_voci"]))
    # Il titolo dà per scontato il risultato (il mezzo riparte) e fa sentire lo stato d'animo: niente negazioni.
    riga_a, riga_b = t("Riparti", "Drive away"), t("sereno", "worry-free")
    caratteri = max(len(riga_a), len(riga_b) + 1)
    recensioni = "".join(f'<figure class="voce"><blockquote lang="it"><p>{testo}</p></blockquote><figcaption>{nome}</figcaption></figure>' for testo, nome in RECENSIONI)
    tutte = f'<a class="link" href="{MAPS}" target="_blank" rel="noopener">{t("Tutte le recensioni su Google", "All reviews on Google")} {I["esterno"]}</a>'
    if RECENSIONI_GOOGLE:  # con il link diretto, i due collegamenti stanno in riga
        tutte = f'<div class="azioni">{tutte}<a class="link" href="{RECENSIONI_GOOGLE}" target="_blank" rel="noopener">{t("Lascia una recensione", "Leave a review")} {I["esterno"]}</a></div>'
    eroe_stock = foto_info("eroe")[4]
    scrivi(head(t("Meccanico di fiducia a Frassineto Po | L.M. Autoservizi", "Trusted mechanic in Frassineto Po | L.M. Autoservizi"),
                t("L'officina di Luca Miglietta a Frassineto Po: meccanica, elettrauto, gomme, carrozzeria e diagnosi, multimarca. Orario continuato, vettura di cortesia gratuita.",
                  "Luca Miglietta's workshop in Frassineto Po, Italy: mechanics, auto electrics, tyres, bodywork and diagnostics, all makes. Open all day, free courtesy car."),
                [azienda()], immagine="officina") + testata() + f'''
<section class="eroe" aria-labelledby="eroe-t">
  <div class="eroe-fascio" aria-hidden="true"></div>
  <div class="eroe-scena" aria-hidden="true">
    <div class="eroe-ingranaggio">
      <svg class="eroe-aloni" viewBox="-400 -400 800 800"><circle r="340"/><circle r="390"/></svg>
      <div class="eroe-finestra">{img("eroe", "(max-width: 899px) 46vw, 24vw", priorita=True, alt="")}</div>
      <svg class="eroe-anello" viewBox="-300 -300 600 600"><path fill="currentColor" fill-rule="evenodd" d="{GEAR_PIENO}"/></svg>
    </div>
  </div>
  <div class="eroe-righe">
    <h1 id="eroe-t" style="--car: {caratteri}"><span class="riga riga-a"><span>{riga_a}</span></span><span class="riga riga-b"><span>{riga_b}<em>.</em></span></span></h1>
  </div>
  <div class="eroe-basso wrap">
    <div class="eroe-testo">
      <p>{t("Quando il tuo mezzo ha un problema, vuoi qualcuno che ti ascolti, ti spieghi cosa serve e lo sistemi. <strong>Sono Luca Miglietta</strong>: vedi il preventivo prima di iniziare e dalla prima telefonata alla riconsegna parli sempre con me.",
              "When your vehicle has a problem, you want someone who listens, explains what's needed and fixes it. <strong>I'm Luca Miglietta</strong>: you see the quote before any work starts, and from the first call to the hand-back you always deal with me.")}</p>
      <div class="azioni">
        <a class="btn btn--arancio" href="#servizi">{t("Cosa ti serve?", "What do you need?")} {I["giu"]}</a>
        <a class="btn btn--vuoto eroe-chiama" href="tel:{TEL}">{I["tel"]}{tel_txt()}</a>
      </div>
    </div>
    <div class="eroe-info"><p class="stato" data-stato></p>{f'<p class="nota-foto">{t("Foto di esempio", "Example photo")}</p>' if eroe_stock else ""}</div>
  </div>
</section>

<section class="servizi" id="servizi" aria-labelledby="servizi-t">
  <div class="wrap">
    <div class="servizi-testa">
      <h2 id="servizi-t">{t("Cosa ti serve?", "What do you need?")}</h2>
      <div class="servizi-testa-lato">
        <p class="lead">{t("Tocca il servizio, scegli il mezzo e scrivimi due righe. Ti rispondo io, di persona.", "Tap the service, choose your vehicle and send me a couple of lines. I'll answer personally.")}</p>
        <a class="link" href="{href("servizi")}">{t("Tutti i servizi nel dettaglio", "All services in detail")} {I["freccia"]}</a>
      </div>
    </div>
    {griglia_servizi()}
  </div>
</section>

<section class="officina-home" aria-labelledby="officina-t">
  <div class="wrap">
    <div class="officina-home-griglia">
      <div class="officina-home-testo">
        <h2 id="officina-t">{tt(HOME["officina_titolo"]).replace(", ", ",<br>", 1)}</h2>
        <p class="lead">{tt(HOME["officina_testo"])}</p>
        <div class="azioni">
          <a class="btn btn--arancio" href="{href("officina")}">{t("Scopri l'officina", "Discover the workshop")} {I["freccia"]}</a>
          <a class="link" href="{MAPS}" target="_blank" rel="noopener">{t("Apri in Google Maps", "Open in Google Maps")} {I["esterno"]}</a>
        </div>
      </div>
      <figure class="foto officina-home-foto" data-iride>{img("officina", "(max-width: 899px) 100vw, 50vw")}<p class="stato" data-stato></p>{nota_foto("officina")}</figure>
    </div>
    <ul class="vantaggi-lista officina-punti">{punti}</ul>
  </div>
</section>

<section class="luca" aria-labelledby="luca-t">
  <div class="wrap luca-griglia">
    {foto("luca", "(max-width: 899px) 100vw, 45vw", "foto luca-foto")}
    <div class="luca-testo">
      <h2 id="luca-t">{t("Un solo riferimento, dall'inizio alla fine.", "One point of contact, from start to finish.")}</h2>
      <p class="lead">{t("Mi chiamo Luca Miglietta. Lavoro da solo: il tuo mezzo lo segue una persona sola, e al telefono rispondo io.", "My name is Luca Miglietta. I work alone: one person looks after your vehicle, and I'm the one who answers the phone.")}</p>
      <p>{t("Prima ascolto il problema, poi ti dico cosa serve e quanto costa. Il preventivo è gratuito e si parte solo quando ti va bene.", "First I listen to the problem, then I tell you what's needed and what it costs. The quote is free and work starts only when you're happy with it.")}</p>
      <dl class="fatti">
        <div><dt>{t("Esperienza", "Experience")}</dt><dd>{t("Più di dieci anni, tutte le marche", "Over ten years, all makes")}</dd></div>
        <div><dt>{t("Abilitazione", "Qualification")}</dt><dd>{t("Responsabile tecnico delle revisioni", "Technical manager for vehicle inspections")}</dd></div>
        <div><dt>{t("Qualifica", "Training")}</dt><dd>{t("Riparazioni elettromeccaniche dell'autoveicolo", "Vehicle electromechanical repairs")}</dd></div>
        <div><dt>{t("Climatizzatori", "Air conditioning")}</dt><dd>{t("Recupero dei gas fluorurati, Reg.&nbsp;CE&nbsp;307/2008", "F-gas recovery, Reg.&nbsp;EC&nbsp;307/2008")}</dd></div>
      </dl>
      <a class="link" href="{href("chi")}">{t("Conosci Luca", "About Luca")} {I["freccia"]}</a>
    </div>
  </div>
</section>

<section class="recensioni" aria-labelledby="rec-t">
  <div class="wrap">
    <h2 id="rec-t">{t("Chi si è già affidato a Luca", "What customers say")}</h2>
    {"" if lingua() == "it" else '<p class="lead recensioni-nota">Original reviews in Italian, from Google.</p>'}
    <div class="voci">{recensioni}</div>
    {nota_recensioni() if RECENSIONI_CON_PERMESSO else f'<p class="piccolo recensioni-fonte">{t("Recensioni scelte da Luca tra quelle pubblicate su Google", "Reviews chosen by Luca from those published on Google")}</p>'}
    {tutte}
  </div>
</section>

<section class="extra" aria-labelledby="extra-t">
  <div class="wrap extra-griglia">
    <div class="extra-testa">
      <h2 id="extra-t">{tt(HOME["extra_titolo"])}</h2>
      <p>{tt(HOME["extra_testo"])}</p>
    </div>
    <ul class="extra-lista">{extra}</ul>
  </div>
</section>

<section class="contatti-home" id="contatti" aria-labelledby="contatti-t">
  <div class="wrap contatti-home-griglia">
    <div>
      <h2 id="contatti-t">{t("Dove e quando", "Where and when")}</h2>
      <p class="contatti-luogo">{t("Officina a Frassineto Po (AL)", "Workshop in Frassineto Po (AL), Italy")}</p>
      {orari()}
      <p class="stato" data-stato></p>
      <div class="contatti-home-link">
        <a class="link" href="{href("officina")}">{t("Tutto sull'officina", "All about the workshop")} {I["freccia"]}</a>
        <a class="link" href="{MAPS}" target="_blank" rel="noopener">{t("Apri in Google Maps", "Open in Google Maps")} {I["esterno"]}</a>
      </div>
    </div>
    <div class="contatti-diretti">
      <a class="numerone" href="tel:{TEL}">{tel_txt()}</a>
      <p>{t("Chiamami o scrivimi: ti dico quando puoi portarmi il mezzo o quando posso passare a ritirarlo.", "Call or message me: I'll tell you when you can bring the vehicle in or when I can collect it. WhatsApp is the easiest way to reach me if you don't speak Italian.")}</p>
      <div class="azioni">
        <a class="btn btn--arancio" href="{wa()}" target="_blank" rel="noopener">{I["chat"]}{t("Scrivi su WhatsApp", "Message on WhatsApp")}</a>
        <a class="btn btn--vuoto" href="mailto:{EMAIL}">{I["mail"]}Email</a>
      </div>
    </div>
  </div>
</section>
''' + piede())
