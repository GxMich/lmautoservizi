# Da completare

Elenco rigenerato da `python sorgente/genera.py` a ogni generazione: non serve modificarlo a mano.

## Dati mancanti in `sorgente/contenuti.py`

Finché un valore resta `None`, il sito lo omette.

- `INDIRIZZO_OFFICINA`: via e numero civico dell'officina (il biglietto riporta solo la sede legale): va in Contatti, nel piede e nei dati strutturati per Google.
- `GEO`: coordinate dell'officina (latitudine, longitudine), da Google Maps: tasto destro sul punto e clic sui numeri.
- `REA`: numero REA della Camera di Commercio (visura camerale), da mostrare nel piede accanto alla partita IVA.
- `INSTAGRAM`: indirizzo del profilo Instagram, se esiste; se non c'è resta None e il sito non lo mostra.
- `RECENSIONI_GOOGLE`: link diretto «scrivi una recensione» dal Profilo dell'attività su Google (Chiedi recensioni): aggiunge il pulsante sotto le recensioni.
- `PREZZI`: fascia di prezzo o listino indicativo: per ora il sito non mostra prezzi.
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
