"""Gomme e ricambi: il catalogo per macro aree (ogni casella apre la tendina WhatsApp sulla sua categoria), come funziona
l'ordine (niente spedizioni, si ritira in officina dopo il pagamento) e i due moduli che preparano la richiesta su WhatsApp
(misura della gomma, pezzo di ricambio)."""
import math
from sito import (inizia, scrivi, head, testata, intro, finale, piede, spunte, azienda, briciole, risorsa, svg, dati_servizio,
                  attr, I, ICONE)

TARGA_UE = ('<span class="targa-ue" aria-hidden="true"><svg viewBox="0 0 44 64" width="44" height="64">'
            + "".join(f'<circle cx="{22 + 11 * math.cos(math.radians(a * 30)):.1f}" cy="{19 + 11 * math.sin(math.radians(a * 30)):.1f}" r="1.35" fill="#f2c230"/>' for a in range(12))
            + '<text x="22" y="53" text-anchor="middle" font-family="Archivo,Arial,sans-serif" font-weight="700" font-size="17" fill="#fff">I</text></svg></span>')

# Le macro aree che Luca vuole mostrare (29/10/2026): niente prodotti o modelli specifici, si chiede su WhatsApp.
# (nome, descrizione, icona, tipo della tendina: "gomme" chiede la misura, "ricambi" cosa serve; esempio per il campo)
CATALOGO = [
    ("Ricambi", "Freni, filtri, cinghie e altri pezzi, per tutte le marche", ICONE["ricambi"], "ricambi", "Es. pastiglie dei freni anteriori"),
    ("Gomme", "Estive, invernali e quattro stagioni", ICONE["gommista"], "gomme", ""),
    ("Lubrificanti", "Olio motore, olio del cambio e liquidi", svg(
        '<path d="M12 3.2c3.3 4.2 6 7.6 6 10.8a6 6 0 0 1-12 0c0-3.2 2.7-6.6 6-10.8z"/><path class="pieno" d="M9.3 13.6a2.9 2.9 0 0 0 2.7 3.6v-1.7a1.3 1.3 0 0 1-1.2-1.9z"/>'),
     "ricambi", "Es. olio motore 5W-30, 5 litri"),
    ("Additivi", "Per motore, carburante e radiatore", svg(
        '<path d="M9.5 2.8h5v3.4l1.8 2.3c.5.6.7 1.3.7 2v9.2a1.5 1.5 0 0 1-1.5 1.5H8.5A1.5 1.5 0 0 1 7 19.7v-9.2c0-.7.2-1.4.7-2l1.8-2.3z"/>'
        '<path d="M9.5 6.2h5M7 12.5h10"/><path class="pieno" d="M9.5 14.6h5v2.8h-5z"/>'),
     "ricambi", "Es. additivo per pulire gli iniettori diesel"),
    ("Accessori", "Lampadine LED, spazzole tergicristallo, tappetini", svg(
        '<path d="M9 17.5h6M9.8 20.5h4.4"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.6.5 1 1.2 1 2v1.7h5.2v-1.7c0-.8.4-1.5 1-2A6 6 0 0 0 12 3z"/>'
        '<path class="pieno" d="M11 7.8h2l-.5 3.8h-1z"/>'),
     "ricambi", "Es. lampadine LED H7"),
    ("Carrozzeria", "Ricambi di carrozzeria e prodotti per la cura", ICONE["carrozzeria"], "ricambi", "Es. specchietto destro"),
    ("Batterie", "Per auto, furgoni e camper, con il montaggio", ICONE["elettrauto"], "ricambi", "Es. batteria 70 Ah per Fiat Ducato"),
    ("Non lo trovi qui?", "Scrivimi cosa cerchi: se si trova, te lo procuro", ICONE["altro"], "ricambi", "Es. tappo del serbatoio"),
]
ORDINE = [("Mi scrivi cosa ti serve", "Ti rispondo con disponibilità e prezzo."),
          ("Paghi in officina", "Dopo il pagamento ordino il pezzo."),
          ("Lo ritiri in officina", "A Frassineto Po. Se vuoi, te lo monto io.")]


def casella_catalogo(nome, desc, icona, tipo, esempio):
    nota = "Marca, modello e anno del mezzo aiutano a trovare il pezzo giusto." if tipo == "ricambi" else ""
    extra = f' data-tipo="{tipo}"' + (f' data-esempio="{attr(esempio)}"' if esempio else "")
    return f'''<li><button type="button" class="servizio servizio--largo" {dati_servizio(nome, nota, "vendita")}{extra}>
  <span class="servizio-ico" aria-hidden="true">{icona}</span>
  <span class="servizio-testo"><span class="servizio-nome">{nome}</span><span class="servizio-desc">{desc}</span></span>
</button></li>'''


def costruisci():
    inizia("gomme")
    catalogo = "".join(casella_catalogo(*voce) for voce in CATALOGO)
    ordine = "".join(f'<li><span class="ordine-n" aria-hidden="true">{i + 1}</span><div><h3>{titolo}</h3><p>{testo}</p></div></li>'
                     for i, (titolo, testo) in enumerate(ORDINE))
    scrivi(head("Vendita gomme e ricambi a Frassineto Po | L.M. Autoservizi",
                "Ricambi, gomme, lubrificanti, additivi, accessori e batterie: chiedi su WhatsApp disponibilità e prezzo, poi ritiri in officina a Frassineto Po.",
                [azienda(), briciole("Gomme e ricambi")], immagine="servizio-gommista") + testata()
           + intro("Gomme e ricambi", "Dimmi cosa ti serve: ti rispondo con disponibilità e prezzo. Lo ritiri in officina, e al montaggio penso io.") + f'''
<section class="sezione" aria-labelledby="catalogo-t">
  <div class="wrap">
    <h2 id="catalogo-t">Cosa trovi</h2>
    <p class="lead catalogo-lead">Tocca la categoria e scrivimi cosa cerchi: il messaggio si apre su WhatsApp, già pronto.</p>
    <ul class="servizi-griglia catalogo">{catalogo}
    </ul>
    <div class="ordine" aria-labelledby="ordine-t">
      <h3 id="ordine-t">Come funziona l'ordine</h3>
      <ol class="ordine-passi">{ordine}</ol>
      <p class="ordine-nota"><strong>Niente spedizioni:</strong> gomme e ricambi si ritirano solo in officina, e ordino il pezzo dopo il pagamento.</p>
    </div>
  </div>
</section>
<section class="sezione sezione--asfalto">
  <div class="wrap gomme-griglia">
    <div>
      <h2 id="gomme-t">Vendita pneumatici</h2>
      <p class="lead">Estive, invernali e quattro stagioni. La misura è scritta sul fianco, per esempio 205/55 R16: se non la trovi, dimmi la targa e la ricavo io.</p>
      <form class="modulo" data-wa data-intro="{attr("Ciao Luca, vorrei un preventivo per delle gomme.")}" data-misura-o-targa novalidate aria-labelledby="gomme-t">
        <fieldset class="campo">
          <legend>Misura della gomma <span>(oppure la targa, qui sotto)</span></legend>
          <div class="misura">
            <label><span class="sr">Larghezza</span><input name="larghezza" inputmode="numeric" maxlength="3" placeholder="205" autocomplete="off"></label><i aria-hidden="true">/</i>
            <label><span class="sr">Spalla</span><input name="spalla" inputmode="numeric" maxlength="2" placeholder="55" autocomplete="off"></label><i aria-hidden="true">R</i>
            <label><span class="sr">Cerchio in pollici</span><input name="cerchio" inputmode="numeric" maxlength="2" placeholder="16" autocomplete="off"></label>
          </div>
          <p class="errore" aria-live="polite"></p>
        </fieldset>
        <div class="campo"><label for="g-targa">Targa <span>(se non trovi la misura)</span></label>
          <div class="targa">{TARGA_UE}<input id="g-targa" name="targa" class="targa-campo" data-etichetta="Targa" autocomplete="off" autocapitalize="characters" spellcheck="false" maxlength="8" placeholder="AB123CD"></div></div>
        <div class="campi-due">
          <div class="campo"><label for="g-stagione">Che gomme cerchi</label><select id="g-stagione" name="stagione" data-etichetta="Stagione"><option>Estive</option><option>Invernali</option><option>Quattro stagioni</option><option>Non lo so, consigliami tu</option></select></div>
          <div class="campo"><label for="g-mezzo">Mezzo <span>(facoltativo)</span></label><input id="g-mezzo" name="mezzo" data-etichetta="Mezzo" placeholder="Es. Fiat Panda 2015"></div>
        </div>
        <button class="btn btn--arancio btn--pieno" type="submit">{I["chat"]}Chiedi disponibilità su WhatsApp</button>
        <p class="nota">Ti rispondo con disponibilità e prezzo. Il montaggio si fa in officina.</p>
        <p class="esito" role="status" hidden></p>
      </form>
      {spunte(["Montaggio ed equilibratura in officina", "Convergenza e campanatura", "Deposito delle gomme che non usi, fino al prossimo cambio", "Riparazione delle forature, anche da te"])}
    </div>
    <figure class="gomma">
      <div class="gomma-foto"><img src="{risorsa("assets/img/3d/pneumatico-realista-v1.webp")}" srcset="{risorsa("assets/img/3d/pneumatico-realista-v1-640.webp")} 640w, {risorsa("assets/img/3d/pneumatico-realista-v1.webp")} 1254w" sizes="(max-width: 899px) 90vw, 520px" width="1254" height="1254" alt="Render illustrativo di un pneumatico con cerchio in lega" loading="lazy" decoding="async"></div>
      <figcaption class="gomma-dati"><div><span data-misura-etichetta>Esempio di misura</span><strong data-misura-testo>205/55 R16</strong></div><p>Immagine illustrativa</p></figcaption>
    </figure>
  </div>
</section>
<section class="sezione">
  <div class="wrap gomme-griglia">
    <div>
      <h2>Vendita ricambi</h2>
      <p class="lead">Ricambi per veicoli di tutte le marche. Dimmi la targa e il pezzo che ti serve: ti rispondo con disponibilità e preventivo, e se vuoi lo monto io.</p>
      {spunte(["Ricambi per tutte le marche", "Preventivo gratuito", "Ritiro e montaggio in officina"])}
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
