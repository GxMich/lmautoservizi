# Da completare

Elenco rigenerato da `python sorgente/genera.py` a ogni generazione: non serve modificarlo a mano.

## Dati mancanti in `sorgente/contenuti.py`

Finché un valore resta `None`, il sito lo omette.

- `FACEBOOK`: la pagina è di Luca ma per scelta non va sul sito: resta None (non serve completarlo).
- `INSTAGRAM`: Luca dice di non avere Instagram: resta None finché non apre un profilo.
- `RECENSIONI_GOOGLE`: link diretto «scrivi una recensione» dal Profilo dell'attività su Google (Chiedi recensioni): aggiunge il pulsante sotto le recensioni.
- `PREZZI`: Luca preferisce solo il preventivo, senza prezzi sul sito (29/10/2026): resta None (non serve completarlo).
- `NOLEGGIO_LINK`: il link del noleggio a lungo termine, dal PDF «QR NOLEGGIO LUNGO TERMINE» di Luca (29/10/2026): con il link compaiono la casella in home e la scheda in Servizi. Il QR va salvato in docs/assets/img/noleggio-qr.png.
- `RECENSIONI_CON_PERMESSO`: conferma che le recensioni in home vengono da Google e che gli autori sono d'accordo: con True compare la nota del Codice del Consumo (nota_recensioni).

## Foto ancora di esempio

Gli scatti vanno in `materiali/foto/` con i nomi di `materiali/foto/LEGGIMI.md`, poi `python sorgente/foto.py` e `python sorgente/genera.py`.

- `eroe`
- `luca`
- `officina`
- `ingresso`
- `officina-mobile`
- `ritiro`
- `servizio-meccanica`
- `servizio-elettrauto`
- `servizio-gommista`
- `servizio-carrozzeria`
- `servizio-diagnosi`
- `servizio-soccorso`
- `servizio-ricambi`
- `servizio-allestimenti`
- `allestimento-1`
- `allestimento-2`
- `allestimento-3`
- `allestimento-4`
- `allestimento-5`
- `allestimento-6`
