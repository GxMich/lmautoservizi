# Foto originali

Qui vanno gli scatti originali (JPEG o PNG; HEIC solo con `pip install pillow-heif`). Restano fuori dal repository.

Ogni file prende il nome dello spazio in cui finirà (gli spazi sono in `FOTO_SLOT`, in `sorgente/contenuti.py`):

| File | Spazio | Formato |
|---|---|---|
| `eroe.jpg` | Apertura della home, dentro l'ingranaggio | verticale 2:3, soggetto al centro |
| `luca.jpg` | Ritratto di Luca (home e Chi sono) | verticale 4:5 |
| `officina.jpg` | Interno dell'officina (pagina L'officina, fascia della pagina Servizi, anteprima social) | orizzontale 3:2 |
| `ingresso.jpg` | Ingresso dell'officina (Contatti) | orizzontale 3:2 |
| `officina-mobile.jpg` | Furgone dell'officina mobile | orizzontale 3:2 |
| `ritiro.jpg` | Consegna delle chiavi / vettura di cortesia | orizzontale 3:2 |
| `servizio-meccanica.jpg` | Casella Meccanica e pagina Meccanica | orizzontale 3:2 |
| `servizio-elettrauto.jpg` | Casella Elettrauto e pagina Elettrauto | orizzontale 3:2 |
| `servizio-gommista.jpg` | Casella Gommista, pagine Gommista e Gomme e ricambi | orizzontale 3:2 |
| `servizio-carrozzeria.jpg` | Casella Carrozzeria e pagina Carrozzeria | orizzontale 3:2 |
| `servizio-diagnosi.jpg` | Casella Diagnosi e pre-revisione e la sua pagina | orizzontale 3:2 |
| `servizio-soccorso.jpg` | Casella Assistenza a domicilio | orizzontale 3:2 |
| `servizio-ricambi.jpg` | Casella Vendita ricambi e gomme | orizzontale 3:2 |

Poi, dalla radice del progetto:

```sh
python sorgente/foto.py
python sorgente/genera.py
```

Il primo comando ritaglia al centro sul formato giusto e crea in `docs/assets/img/foto/` le versioni WebP senza metadati (posizione GPS compresa). Il secondo rigenera le pagine: ogni foto vera prende il posto di quella stock e la scritta "Foto di esempio" sparisce. L'elenco delle foto ancora di esempio è in `materiali/da-completare.md`.
