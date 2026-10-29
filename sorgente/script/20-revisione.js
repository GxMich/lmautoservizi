/* Diagnosi e pre-revisione: quando scade la revisione.
   Prima revisione entro la fine del mese di prima immatricolazione + 4 anni, poi ogni 2 anni entro il mese dell'ultima.
   Tutto si calcola nel browser: il promemoria .ics nasce qui e nessun dato parte dalla pagina. */
(function () {
  "use strict";
  var form = document.querySelector("[data-revisione]");
  if (!form) return;
  var $ = function (s) { return form.querySelector(s); };
  var MESI = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"];
  var T = {
    prima: "Prima revisione entro la fine di", prossima: "Prossima revisione entro la fine di", eraPrima: "La prima revisione era entro la fine di", era: "La revisione era entro la fine di",
    resta: ". Prima della revisione ti controllo il mezzo gratis.", questoMese: "Scade questo mese: prenota adesso il controllo gratuito.",
    chiedi: "Questa data è passata. Dopo la prima, la revisione si rifà ogni due anni: aggiungi mese e anno dell'ultima e ti dico la prossima scadenza.",
    scaduta: "La revisione è scaduta: conviene prenotarla subito. Prima ti controllo il mezzo gratis.",
    erroreOrdine: "L'ultima revisione non può essere prima dell'immatricolazione: controlla le date.", erroreFuturo: "Questa data è nel futuro: controlla mese e anno.",
    anno: ["anno", "anni"], mese: ["mese", "mesi"], e: " e ",
    titolo: "Revisione auto entro ", nota: "Revisione in scadenza: ", notaScaduta: "Revisione scaduta: ",
    descrizione: "Prima della revisione ti controllo il mezzo gratis e te la prenoto. Luca, L.M. Autoservizi: ", file: "promemoria-revisione-",
    pronto: "Promemoria pronto: apri il file scaricato per aggiungerlo al calendario."
  };

  /* ---------- calcolo (date come {a: anno, m: mese 1-12}) ---------- */
  function scadenza(imm, ultima, oggi) {
    var n = function (d) { return d.a * 12 + d.m - 1; };
    if (n(imm) > n(oggi) || (ultima && n(ultima) > n(oggi))) return { errore: "futuro" };
    if (ultima && n(ultima) < n(imm)) return { errore: "ordine" };
    var k = ultima ? n(ultima) + 24 : n(imm) + 48, oggiN = n(oggi);
    var stato = k > oggiN ? "ok" : k === oggiN ? "mese" : ultima ? "scaduta" : "chiedi";
    return { scadenza: { a: Math.floor(k / 12), m: k % 12 + 1 }, stato: stato, mesi: k - oggiN, prima: !ultima };
  }
  function durata(mesi) {
    var a = Math.floor(mesi / 12), m = mesi % 12, parti = [];
    var conta = function (x, nomi) { return x === 1 ? "un " + nomi[0] : x + " " + nomi[1]; };
    if (a) parti.push(conta(a, T.anno));
    if (m) parti.push(conta(m, T.mese));
    var testo = parti.join(T.e);
    return (mesi === 1 || mesi === 12 ? "Manca " : "Mancano ") + testo;
  }
  function inParole(d) { return MESI[d.m - 1] + " " + d.a; }
  // fine calcolo

  /* ---------- modulo ---------- */
  var esito = $("[data-esito-revisione]"), azioni = $("[data-azioni-revisione]"), promemoriaEsito = $("[data-promemoria-esito]");
  var bottonePromemoria = $("[data-promemoria]"), gruppoUltima = $("[data-gruppo='ult']");
  var risultato = null;
  var annoOggi = new Date().getFullYear();
  Array.prototype.forEach.call(form.querySelectorAll("[data-anni]"), function (s) {
    for (var a = annoOggi; a >= 1980; a--) s.add(new Option(String(a), String(a)));
  });
  form.hidden = false;

  function leggi(chiave) {
    var m = parseInt(form.elements[chiave + "-m"].value, 10), a = parseInt(form.elements[chiave + "-a"].value, 10);
    return m && a ? { a: a, m: m } : null;
  }
  function riga(classe, testo) {
    var p = document.createElement("p");
    p.className = classe;
    p.textContent = testo;
    return p;
  }
  function aggiorna() {
    var imm = leggi("imm"), ultima = leggi("ult"), ora = new Date();
    risultato = imm ? scadenza(imm, ultima, { a: ora.getFullYear(), m: ora.getMonth() + 1 }) : null;
    esito.textContent = "";
    esito.className = "calcolo-esito" + (risultato ? " calcolo-esito--" + (risultato.errore ? "errore" : risultato.stato) : "");
    gruppoUltima.classList.toggle("calcolo-data--chiesta", !!risultato && risultato.stato === "chiedi");
    promemoriaEsito.textContent = "";
    azioni.hidden = !risultato || !!risultato.errore || risultato.stato === "chiedi";
    bottonePromemoria.hidden = !risultato || risultato.stato !== "ok";
    if (!risultato) return;
    if (risultato.errore) { esito.appendChild(riga("calcolo-nota", risultato.errore === "ordine" ? T.erroreOrdine : T.erroreFuturo)); return; }
    var s = risultato.stato;
    esito.appendChild(riga("calcolo-etichetta", s === "chiedi" ? T.eraPrima : s === "scaduta" ? T.era : risultato.prima ? T.prima : T.prossima));
    esito.appendChild(riga("calcolo-mese", inParole(risultato.scadenza)));
    esito.appendChild(riga("calcolo-nota", s === "ok" ? durata(risultato.mesi) + T.resta : s === "mese" ? T.questoMese : s === "chiedi" ? T.chiedi : T.scaduta));
  }
  form.addEventListener("change", aggiorna);
  form.addEventListener("submit", function (e) { e.preventDefault(); });
  window.addEventListener("pageshow", aggiorna);
  aggiorna();

  /* ---------- promemoria .ics: un giorno intero, il primo del mese prima della scadenza ---------- */
  function ics(s) {
    var oggi = new Date(); oggi.setHours(0, 0, 0, 0);
    var giorno = new Date(s.a, s.m - 2, 1);
    if (giorno < oggi) giorno = oggi;  // scadenza vicina: il promemoria cade oggi
    var dopo = new Date(giorno.getFullYear(), giorno.getMonth(), giorno.getDate() + 1);
    var data = function (d) { return d.getFullYear() + String(d.getMonth() + 1).padStart(2, "0") + String(d.getDate()).padStart(2, "0"); };
    var testo = function (x) { return x.replace(/\\/g, "\\\\").replace(/([,;])/g, "\\$1").replace(/\n/g, "\\n"); };
    // le righe oltre 75 byte si spezzano e continuano con uno spazio (RFC 5545)
    var piega = function (r) {
      var fuori = "", byte = 0, enc = new TextEncoder();
      Array.from(r).forEach(function (c) {
        var b = enc.encode(c).length;
        if (byte + b > 75) { fuori += "\r\n "; byte = 1; }
        fuori += c; byte += b;
      });
      return fuori;
    };
    var titolo = T.titolo + inParole(s);
    return ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//L.M. Autoservizi//Revisione//IT", "CALSCALE:GREGORIAN", "METHOD:PUBLISH",
      "BEGIN:VEVENT", "UID:revisione-" + data(giorno) + "-" + Date.now().toString(36) + "@lmautoservizi.it",
      "DTSTAMP:" + new Date().toISOString().replace(/[-:]/g, "").replace(/\.\d+/, ""),
      "DTSTART;VALUE=DATE:" + data(giorno), "DTEND;VALUE=DATE:" + data(dopo),
      "SUMMARY:" + testo(titolo), "DESCRIPTION:" + testo(T.descrizione + form.getAttribute("data-tel")),
      "URL:" + form.getAttribute("data-pagina"), "TRANSP:TRANSPARENT",
      "BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:" + testo(titolo), "TRIGGER:PT9H", "END:VALARM",
      "END:VEVENT", "END:VCALENDAR"].map(piega).join("\r\n") + "\r\n";
  }
  bottonePromemoria.addEventListener("click", function () {
    if (!risultato || risultato.stato !== "ok") return;
    var s = risultato.scadenza;
    var a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([ics(s)], { type: "text/calendar;charset=utf-8" }));
    a.download = T.file + MESI[s.m - 1].toLowerCase() + "-" + s.a + ".ics";
    document.body.appendChild(a);
    a.click();
    a.remove();
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 10000);
    promemoriaEsito.textContent = T.pronto;
  });

  /* ---------- "Prenota il controllo gratuito": la tendina della diagnosi si apre (00-base.js) con le note già scritte ---------- */
  document.addEventListener("click", function (e) {
    if (!e.target.closest || !e.target.closest("[data-prenota-revisione]") || !risultato || !risultato.scadenza) return;
    var note = document.getElementById("scheda-note");
    if (!note) return;
    var testo = (risultato.stato === "scaduta" ? T.notaScaduta : T.nota) + inParole(risultato.scadenza);
    // questo ascoltatore è registrato dopo quello che apre la tendina (e svuota le note se cambia servizio): si scrive dopo.
    // La riga della revisione va in cima; quello che il cliente ha già scritto resta.
    var scrivi = function () {
      var resto = note.value.split("\n").filter(function (r) { return r.indexOf(T.nota) !== 0 && r.indexOf(T.notaScaduta) !== 0; });
      note.value = [testo].concat(resto).join("\n").trim();
    };
    scrivi();
    requestAnimationFrame(scrivi);
  });
})();
