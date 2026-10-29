"""Gomme e ricambi: i due moduli che preparano la richiesta su WhatsApp (misura della gomma, pezzo di ricambio)."""
import math
from sito import (inizia, scrivi, head, testata, intro, finale, piede, spunte, azienda, briciole, risorsa,
                  attr, I)

TARGA_UE = ('<span class="targa-ue" aria-hidden="true"><svg viewBox="0 0 44 64" width="44" height="64">'
            + "".join(f'<circle cx="{22 + 11 * math.cos(math.radians(a * 30)):.1f}" cy="{19 + 11 * math.sin(math.radians(a * 30)):.1f}" r="1.35" fill="#f2c230"/>' for a in range(12))
            + '<text x="22" y="53" text-anchor="middle" font-family="Archivo,Arial,sans-serif" font-weight="700" font-size="17" fill="#fff">I</text></svg></span>')


def costruisci():
    inizia("gomme")
    scrivi(head("Gomme e ricambi a Frassineto Po | L.M. Autoservizi",
                "Vendita di pneumatici e ricambi, con montaggio, equilibratura e convergenza in officina. Scrivi la misura e ti rispondo con disponibilità e prezzo.",
                [azienda(), briciole("Gomme e ricambi")], immagine="servizio-gommista") + testata()
           + intro("Gomme e ricambi", "Dimmi la misura o la targa: ti rispondo con disponibilità e prezzo. Al montaggio penso io.") + f'''
<section class="sezione">
  <div class="wrap gomme-griglia">
    <div>
      <h2 id="gomme-t">Vendita pneumatici</h2>
      <p class="lead">Estive, invernali e quattro stagioni. La misura è scritta sul fianco, per esempio 205/55 R16: se non la trovi, dimmi la targa e la ricavo io.</p>
      <form class="modulo" data-wa data-intro="{attr("Ciao Luca, vorrei un preventivo per delle gomme.")}" novalidate aria-labelledby="gomme-t">
        <fieldset class="campo">
          <legend>Misura della gomma</legend>
          <div class="misura">
            <label><span class="sr">Larghezza</span><input name="larghezza" inputmode="numeric" maxlength="3" placeholder="205" required autocomplete="off"></label><i aria-hidden="true">/</i>
            <label><span class="sr">Spalla</span><input name="spalla" inputmode="numeric" maxlength="2" placeholder="55" required autocomplete="off"></label><i aria-hidden="true">R</i>
            <label><span class="sr">Cerchio in pollici</span><input name="cerchio" inputmode="numeric" maxlength="2" placeholder="16" required autocomplete="off"></label>
          </div>
          <p class="errore" aria-live="polite"></p>
        </fieldset>
        <div class="campi-due">
          <div class="campo"><label for="g-stagione">Che gomme cerchi</label><select id="g-stagione" name="stagione" data-etichetta="Stagione"><option>Estive</option><option>Invernali</option><option>Quattro stagioni</option><option>Non lo so, consigliami tu</option></select></div>
          <div class="campo"><label for="g-mezzo">Mezzo <span>(facoltativo)</span></label><input id="g-mezzo" name="mezzo" data-etichetta="Mezzo" placeholder="Es. Fiat Panda 2015"></div>
        </div>
        <button class="btn btn--arancio btn--pieno" type="submit">{I["chat"]}Chiedi disponibilità su WhatsApp</button>
        <p class="nota">Ti rispondo con disponibilità e prezzo. Il montaggio si fa in officina.</p>
        <p class="esito" role="status" hidden></p>
      </form>
      {spunte(["Montaggio ed equilibratura in officina", "Convergenza e campanatura", "Riparazione delle forature, anche da te"])}
    </div>
    <figure class="gomma">
      <div class="gomma-foto"><img src="{risorsa("assets/img/3d/pneumatico-realista-v1.webp")}" width="1254" height="1254" alt="Render illustrativo di un pneumatico con cerchio in lega" loading="lazy" decoding="async"></div>
      <figcaption class="gomma-dati"><div><span data-misura-etichetta>Esempio di misura</span><strong data-misura-testo>205/55 R16</strong></div><p>Immagine illustrativa</p></figcaption>
    </figure>
  </div>
</section>
<section class="sezione sezione--asfalto">
  <div class="wrap gomme-griglia">
    <div>
      <h2>Vendita ricambi</h2>
      <p class="lead">Ricambi per veicoli di tutte le marche. Dimmi la targa e il pezzo che ti serve: ti rispondo con disponibilità e preventivo, e se vuoi lo monto io.</p>
      {spunte(["Ricambi per tutte le marche", "Preventivo gratuito", "Montaggio in officina"])}
    </div>
    <form class="modulo modulo--riquadro" data-wa data-intro="{attr("Ciao Luca, vorrei un preventivo per un ricambio.")}" novalidate aria-labelledby="rc-t">
      <h2 id="rc-t">Chiedi un ricambio</h2>
      <div class="campo"><label for="rc-targa">Targa <span>(facoltativa)</span></label>
        <div class="targa">{TARGA_UE}<input id="rc-targa" name="targa" class="targa-campo" data-etichetta="Targa" autocomplete="off" autocapitalize="characters" spellcheck="false" maxlength="8" placeholder="AB123CD"></div>
        <p class="aiuto">Serve solo a trovare il pezzo giusto.</p></div>
      <div class="campo"><label for="rc-pezzo">Che pezzo ti serve</label><input id="rc-pezzo" name="pezzo" data-etichetta="Pezzo" required placeholder="Es. pastiglie dei freni anteriori"><p class="errore" aria-live="polite"></p></div>
      <div class="campo"><label for="rc-mezzo">Mezzo <span>(facoltativo)</span></label><input id="rc-mezzo" name="mezzo" data-etichetta="Mezzo" placeholder="Es. Fiat Panda 2015"></div>
      <button class="btn btn--arancio btn--pieno" type="submit">{I["chat"]}Chiedi su WhatsApp</button>
      <p class="nota">Si apre WhatsApp con il messaggio già scritto. L'invio lo confermi tu.</p>
      <p class="esito" role="status" hidden></p>
    </form>
  </div>
</section>''' + finale("Non sai cosa ti serve?", "Descrivimi il problema: ti dico io cosa serve.") + piede())
