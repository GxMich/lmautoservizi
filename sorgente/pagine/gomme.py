"""Gomme e ricambi: i due moduli che preparano la richiesta su WhatsApp (misura della gomma, pezzo di ricambio)."""
import math
from sito import (inizia, scrivi, head, testata, intro, finale, piede, spunte, azienda, briciole, risorsa,
                  t, attr, I)

TARGA_UE = ('<span class="targa-ue" aria-hidden="true"><svg viewBox="0 0 44 64" width="44" height="64">'
            + "".join(f'<circle cx="{22 + 11 * math.cos(math.radians(a * 30)):.1f}" cy="{19 + 11 * math.sin(math.radians(a * 30)):.1f}" r="1.35" fill="#f2c230"/>' for a in range(12))
            + '<text x="22" y="53" text-anchor="middle" font-family="Archivo,Arial,sans-serif" font-weight="700" font-size="17" fill="#fff">I</text></svg></span>')


def costruisci():
    inizia("gomme")
    scrivi(head(t("Gomme e ricambi a Frassineto Po | L.M. Autoservizi", "Tyres and parts in Frassineto Po | L.M. Autoservizi"),
                t("Vendita di pneumatici e ricambi, con montaggio, equilibratura e convergenza in officina. Scrivi la misura e ti rispondo con disponibilità e prezzo.",
                  "Tyre and parts sales with fitting, balancing and alignment in the workshop. Enter the size and I'll reply with availability and price."),
                [azienda(), briciole(t("Gomme e ricambi", "Tyres and parts"))], immagine="servizio-gommista") + testata()
           + intro(t("Gomme e ricambi", "Tyres and parts"), t("Dimmi la misura o la targa: ti rispondo con disponibilità e prezzo. Al montaggio penso io.",
                                                             "Tell me the size or the number plate: I'll reply with availability and price. I'll take care of fitting.")) + f'''
<section class="sezione">
  <div class="wrap gomme-griglia">
    <div>
      <h2 id="gomme-t">{t("Vendita pneumatici", "Tyre sales")}</h2>
      <p class="lead">{t("Estive, invernali e quattro stagioni. La misura è scritta sul fianco, per esempio 205/55 R16: se non la trovi, dimmi la targa e la ricavo io.",
                         "Summer, winter and all-season. The size is written on the sidewall, for example 205/55 R16: if you can't find it, tell me the number plate and I'll work it out.")}</p>
      <form class="modulo" data-wa data-intro="{attr(t("Ciao Luca, vorrei un preventivo per delle gomme.", "Hi Luca, I'd like a quote for tyres (preventivo gomme)."))}" novalidate aria-labelledby="gomme-t">
        <fieldset class="campo">
          <legend>{t("Misura della gomma", "Tyre size")}</legend>
          <div class="misura">
            <label><span class="sr">{t("Larghezza", "Width")}</span><input name="larghezza" inputmode="numeric" maxlength="3" placeholder="205" required autocomplete="off"></label><i aria-hidden="true">/</i>
            <label><span class="sr">{t("Spalla", "Profile")}</span><input name="spalla" inputmode="numeric" maxlength="2" placeholder="55" required autocomplete="off"></label><i aria-hidden="true">R</i>
            <label><span class="sr">{t("Cerchio in pollici", "Rim size in inches")}</span><input name="cerchio" inputmode="numeric" maxlength="2" placeholder="16" required autocomplete="off"></label>
          </div>
          <p class="errore" aria-live="polite"></p>
        </fieldset>
        <div class="campi-due">
          <div class="campo"><label for="g-stagione">{t("Che gomme cerchi", "Which tyres")}</label><select id="g-stagione" name="stagione" data-etichetta="{t("Stagione", "Season (stagione)")}"><option>{t("Estive", "Summer")}</option><option>{t("Invernali", "Winter")}</option><option>{t("Quattro stagioni", "All-season")}</option><option>{t("Non lo so, consigliami tu", "Not sure, please advise")}</option></select></div>
          <div class="campo"><label for="g-mezzo">{t("Mezzo", "Vehicle")} <span>({t("facoltativo", "optional")})</span></label><input id="g-mezzo" name="mezzo" data-etichetta="{t("Mezzo", "Vehicle (mezzo)")}" placeholder="{t("Es.", "E.g.")} Fiat Panda 2015"></div>
        </div>
        <button class="btn btn--arancio btn--pieno" type="submit">{I["chat"]}{t("Chiedi disponibilità su WhatsApp", "Ask for availability on WhatsApp")}</button>
        <p class="nota">{t("Ti rispondo con disponibilità e prezzo. Il montaggio si fa in officina.", "I'll reply with availability and price. Fitting is done in the workshop.")}</p>
        <p class="esito" role="status" hidden></p>
      </form>
      {spunte([("Montaggio ed equilibratura in officina", "Fitting and balancing in the workshop"), ("Convergenza e campanatura", "Alignment and camber"), ("Riparazione delle forature, anche da te", "Puncture repair, also at your place")])}
    </div>
    <figure class="gomma">
      <div class="gomma-foto"><img src="{risorsa("assets/img/3d/pneumatico-realista-v1.webp")}" width="1254" height="1254" alt="{t("Render illustrativo di un pneumatico con cerchio in lega", "Illustrative render of a tyre with an alloy rim")}" loading="lazy" decoding="async"></div>
      <figcaption class="gomma-dati"><div><span data-misura-etichetta>{t("Esempio di misura", "Example size")}</span><strong data-misura-testo>205/55 R16</strong></div><p>{t("Immagine illustrativa", "Illustrative image")}</p></figcaption>
    </figure>
  </div>
</section>
<section class="sezione sezione--asfalto">
  <div class="wrap gomme-griglia">
    <div>
      <h2>{t("Vendita ricambi", "Parts sales")}</h2>
      <p class="lead">{t("Ricambi per veicoli di tutte le marche. Dimmi la targa e il pezzo che ti serve: ti rispondo con disponibilità e preventivo, e se vuoi lo monto io.",
                         "Parts for vehicles of all makes. Tell me the number plate and the part you need: I'll reply with availability and a quote, and I can fit it if you like.")}</p>
      {spunte([("Ricambi per tutte le marche", "Parts for all makes"), ("Preventivo gratuito", "Free quote"), ("Montaggio in officina", "Fitting in the workshop")])}
    </div>
    <form class="modulo modulo--riquadro" data-wa data-intro="{attr(t("Ciao Luca, vorrei un preventivo per un ricambio.", "Hi Luca, I'd like a quote for a part (preventivo ricambio)."))}" novalidate aria-labelledby="rc-t">
      <h2 id="rc-t">{t("Chiedi un ricambio", "Ask for a part")}</h2>
      <div class="campo"><label for="rc-targa">{t("Targa", "Number plate")} <span>({t("facoltativa", "optional")})</span></label>
        <div class="targa">{TARGA_UE}<input id="rc-targa" name="targa" class="targa-campo" data-etichetta="{t("Targa", "Plate (targa)")}" autocomplete="off" autocapitalize="characters" spellcheck="false" maxlength="8" placeholder="AB123CD"></div>
        <p class="aiuto">{t("Serve solo a trovare il pezzo giusto.", "Only used to find the right part.")}</p></div>
      <div class="campo"><label for="rc-pezzo">{t("Che pezzo ti serve", "Which part do you need")}</label><input id="rc-pezzo" name="pezzo" data-etichetta="{t("Pezzo", "Part (pezzo)")}" required placeholder="{t("Es. pastiglie dei freni anteriori", "E.g. front brake pads")}"><p class="errore" aria-live="polite"></p></div>
      <div class="campo"><label for="rc-mezzo">{t("Mezzo", "Vehicle")} <span>({t("facoltativo", "optional")})</span></label><input id="rc-mezzo" name="mezzo" data-etichetta="{t("Mezzo", "Vehicle (mezzo)")}" placeholder="{t("Es.", "E.g.")} Fiat Panda 2015"></div>
      <button class="btn btn--arancio btn--pieno" type="submit">{I["chat"]}{t("Chiedi su WhatsApp", "Ask on WhatsApp")}</button>
      <p class="nota">{t("Si apre WhatsApp con il messaggio già scritto. L'invio lo confermi tu.", "WhatsApp opens with the message already written. You just tap Send.")}</p>
      <p class="esito" role="status" hidden></p>
    </form>
  </div>
</section>''' + finale(t("Non sai cosa ti serve?", "Not sure what you need?"), t("Descrivimi il problema: ti dico io cosa serve.", "Describe the problem: I'll tell you what's needed.")) + piede())
