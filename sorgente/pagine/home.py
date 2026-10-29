"""Home: "Riparti sereno.", le caselle dei servizi con la tendina WhatsApp, i tre modi alla pari (officina, ritiro
e consegna, domicilio), l'officina a Frassineto Po, Luca, recensioni, dove e quando. Testi nuovi in testi_pagine.HOME."""
from contenuti import RECENSIONI, RECENSIONI_GOOGLE, RECENSIONI_CON_PERMESSO, GEAR_PIENO
from testi_pagine import HOME
from pagine.officina import ICO
from sito import (inizia, scrivi, head, testata, piede, orari, griglia_servizi, foto, img, foto_info, nota_foto, azienda,
                  href, I, VANTAGGI_ICO, TEL, EMAIL, MAPS, tel_txt, wa, nota_recensioni, indirizzo_officina, anni_esperienza)


def costruisci():
    inizia("home")
    # L'officina: tre punti con le icone che si disegnano (gancio .vantaggi-lista di 00-base.js).
    punti = "".join(f'<li>{ICO[ico]}<h3>{titolo}</h3><p>{testo}</p></li>'
                    for ico, (titolo, testo) in zip(("orario", "cortesia", "preventivo"), HOME["officina_punti"]))
    # I tre modi, alla pari: stesse carte, stesso peso, ognuna porta alla sua pagina.
    modi = "".join(f'<li>{ico}<p class="modi-etichetta">{etichetta}</p><h3>{titolo}</h3><p>{testo}</p>'
                   f'<a class="link" href="{link}">{azione} {I["freccia"]}</a></li>'
                   for (ico, link, azione), (titolo, etichetta, testo) in zip(
                       ((ICO["officina"], href("officina"), "Scopri l'officina"), (VANTAGGI_ICO["rotta"], href("ritiro"), "Come funziona"),
                        (VANTAGGI_ICO["mobile"], href("mobile"), "Cosa faccio sul posto")), HOME["modi_voci"]))
    # Il titolo dà per scontato il risultato (il mezzo riparte) e fa sentire lo stato d'animo: niente negazioni.
    riga_a, riga_b = "Riparti", "sereno"
    caratteri = max(len(riga_a), len(riga_b) + 1)
    recensioni = "".join(f'<figure class="voce"><blockquote lang="it"><p>{testo}</p></blockquote><figcaption>{nome}</figcaption></figure>' for testo, nome in RECENSIONI)
    tutte = f'<a class="link" href="{MAPS}" target="_blank" rel="noopener">Tutte le recensioni su Google {I["esterno"]}</a>'
    if RECENSIONI_GOOGLE:  # con il link diretto, i due collegamenti stanno in riga
        tutte = f'<div class="azioni">{tutte}<a class="link" href="{RECENSIONI_GOOGLE}" target="_blank" rel="noopener">Lascia una recensione {I["esterno"]}</a></div>'
    eroe_stock = foto_info("eroe")[4]
    scrivi(head("Meccanico di fiducia a Frassineto Po | L.M. Autoservizi",
                "L'officina di Luca Miglietta a Frassineto Po: meccanica, elettrauto, gomme, carrozzeria e diagnosi, multimarca. Orario continuato, vettura di cortesia gratuita.",
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
      <p>Quando il tuo mezzo ha un problema, vuoi qualcuno che ti ascolti, ti spieghi cosa serve e lo sistemi. <strong>Sono Luca Miglietta</strong>: vedi il preventivo prima di iniziare e dalla prima telefonata alla riconsegna parli sempre con me.</p>
      <div class="azioni">
        <a class="btn btn--arancio" href="#servizi">Cosa ti serve? {I["giu"]}</a>
        <a class="btn btn--vuoto eroe-chiama" href="tel:{TEL}">{I["tel"]}{tel_txt()}</a>
      </div>
    </div>
    <div class="eroe-info"><p class="stato" data-stato></p>{f'<p class="nota-foto">Foto di esempio</p>' if eroe_stock else ""}</div>
  </div>
</section>

<section class="servizi" id="servizi" aria-labelledby="servizi-t">
  <div class="wrap">
    <div class="servizi-testa">
      <h2 id="servizi-t">Cosa ti serve?</h2>
      <div class="servizi-testa-lato">
        <p class="lead">Tocca il servizio, scegli il mezzo e scrivimi due righe. Ti rispondo io, di persona.</p>
        <a class="link" href="{href("servizi")}">Tutti i servizi nel dettaglio {I["freccia"]}</a>
      </div>
    </div>
    {griglia_servizi()}
  </div>
</section>

<section class="modi" aria-labelledby="modi-t">
  <div class="wrap">
    <div class="modi-testa">
      <h2 id="modi-t">{HOME["modi_titolo"]}</h2>
      <p class="lead">{HOME["modi_testo"]}</p>
    </div>
    <ul class="vantaggi-lista modi-lista">{modi}</ul>
  </div>
</section>

<section class="officina-home" aria-labelledby="officina-t">
  <div class="wrap">
    <div class="officina-home-griglia">
      <div class="officina-home-testo">
        <h2 id="officina-t">{HOME["officina_titolo"].replace(", ", ",<br>", 1)}</h2>
        <p class="lead">{HOME["officina_testo"]}</p>
        <div class="azioni">
          <a class="btn btn--arancio" href="{href("officina")}">Scopri l'officina {I["freccia"]}</a>
          <a class="link" href="{MAPS}" target="_blank" rel="noopener">Apri in Google Maps {I["esterno"]}</a>
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
      <h2 id="luca-t">Un solo riferimento, dall'inizio alla fine.</h2>
      <p class="lead">Mi chiamo Luca Miglietta. Lavoro da solo: il tuo mezzo lo segue una persona sola, e al telefono rispondo io.</p>
      <p>Prima ascolto il problema, poi ti dico cosa serve e quanto costa. Il preventivo è gratuito e si parte solo quando ti va bene.</p>
      <dl class="fatti">
        <div><dt>Esperienza</dt><dd>{anni_esperienza()} anni, tutte le marche</dd></div>
        <div><dt>Abilitazione</dt><dd>Responsabile tecnico delle revisioni</dd></div>
        <div><dt>Qualifica</dt><dd>Riparazioni elettromeccaniche dell'autoveicolo</dd></div>
        <div><dt>Climatizzatori</dt><dd>Recupero dei gas fluorurati, Reg.&nbsp;CE&nbsp;307/2008</dd></div>
      </dl>
      <a class="link" href="{href("chi")}">Conosci Luca {I["freccia"]}</a>
    </div>
  </div>
</section>

<section class="recensioni" aria-labelledby="rec-t">
  <div class="wrap">
    <h2 id="rec-t">Chi si è già affidato a Luca</h2>
    <div class="voci">{recensioni}</div>
    {nota_recensioni() if RECENSIONI_CON_PERMESSO else f'<p class="piccolo recensioni-fonte">Recensioni scelte da Luca tra quelle pubblicate su Google</p>'}
    {tutte}
  </div>
</section>

<section class="contatti-home" id="contatti" aria-labelledby="contatti-t">
  <div class="wrap contatti-home-griglia">
    <div>
      <h2 id="contatti-t">Dove e quando</h2>
      <p class="contatti-luogo">Officina: {indirizzo_officina()}</p>
      {orari()}
      <p class="stato" data-stato></p>
      <div class="contatti-home-link">
        <a class="link" href="{href("officina")}">Tutto sull'officina {I["freccia"]}</a>
        <a class="link" href="{MAPS}" target="_blank" rel="noopener">Apri in Google Maps {I["esterno"]}</a>
      </div>
    </div>
    <div class="contatti-diretti">
      <a class="numerone" href="tel:{TEL}">{tel_txt()}</a>
      <p>Chiamami o scrivimi: ti dico quando puoi portarmi il mezzo o quando posso passare a ritirarlo.</p>
      <div class="azioni">
        <a class="btn btn--arancio" href="{wa()}" target="_blank" rel="noopener">{I["chat"]}Scrivi su WhatsApp</a>
        <a class="btn btn--vuoto" href="mailto:{EMAIL}">{I["mail"]}Email</a>
      </div>
    </div>
  </div>
</section>
''' + piede())
