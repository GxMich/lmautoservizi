/* Statistiche senza cookie (GoatCounter): attive solo se il sito è generato con LM_GOATCOUNTER,
   che aggiunge nella <head> lo script di gc.zgo.at. Qui si contano come eventi i clic su Chiama e WhatsApp
   e gli invii dei messaggi preparati (tendina e moduli gomme e ricambi). Senza window.goatcounter non fa niente.
   Non parte mai il contenuto dei messaggi: solo il nome dell'evento e la zona della pagina. */
(function () {
  "use strict";
  if (!document.querySelector("script[data-goatcounter]")) return;

  function zona(el) {
    var zone = [[".testata", "testata"], [".menu", "menu"], [".barra", "barra"], [".scheda", "tendina"], [".piede", "piede"], [".finale", "finale"]];
    for (var i = 0; i < zone.length; i++) if (el.closest(zone[i][0])) return zone[i][1];
    return "pagina";
  }
  function conta(evento, el) {
    var gc = window.goatcounter;
    if (!gc || typeof gc.count !== "function") return;
    try { gc.count({ path: evento, title: zona(el) + " · " + location.pathname, event: true }); } catch (e) { /* le statistiche non devono mai bloccare il sito */ }
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href^="tel:"], a[href*="wa.me"]');
    if (a) conta(a.getAttribute("href").indexOf("tel:") === 0 ? "clic-chiama" : "clic-whatsapp", a);
  });
  // I moduli fermano l'invio se manca un campo: si conta solo quando non resta nessun campo segnato come errato.
  document.addEventListener("submit", function (e) {
    var form = e.target;
    if (!form.closest || !(form.closest(".scheda") || form.hasAttribute("data-wa"))) return;
    if (form.querySelector('[aria-invalid="true"]')) return;
    conta(form.closest(".scheda") ? "invio-whatsapp-tendina" : "invio-whatsapp-modulo", form);
  });
})();
