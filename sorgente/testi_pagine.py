"""Testi delle pagine nuove (servizi, officina, home). Ogni testo è una coppia (italiano, inglese).
Fonti dei fatti: contenuti.py, biglietto da visita, versione semplice approvata. Niente prezzi né dati da confermare."""

# Note per chi impagina:
# - "title" finisce sempre con " | L.M. Autoservizi" e resta entro 65 caratteri; "description" entro 155.
# - "risposta" è il paragrafo che apre la pagina: è pensato per essere citato così com'è da Google e dagli assistenti AI.
# - Le FAQ sono adatte anche al dato strutturato FAQPage (testo semplice, senza HTML).
# - L'indirizzo dell'officina non è ancora confermato: nei testi c'è solo "a Frassineto Po".

SERVIZI_PAGINE = {
    # ------------------------------------------------------------------ MECCANICA
    "meccanica": {
        "nome": ("Meccanica", "Mechanics"),
        "title": ("Meccanico a Frassineto Po, vicino a Casale | L.M. Autoservizi",
                  "Car mechanic in Frassineto Po, near Casale | L.M. Autoservizi"),
        "description": ("Tagliandi, manutenzione e riparazioni meccaniche sul ponte, su tutte le marche. Officina a Frassineto Po, vicino a Casale. Chiedi un preventivo gratuito.",
                        "Servicing, maintenance and mechanical repairs on the lift, all makes. Workshop in Frassineto Po, near Casale Monferrato. Ask for a free quote."),
        "h1": ("Meccanico a Frassineto Po", "Car mechanic in Frassineto Po"),
        "risposta": ("Sono Luca Miglietta, di L.M. Autoservizi. Lavoro da solo nella mia officina a Frassineto Po, vicino a Casale Monferrato. "
                     "Faccio tagliandi, manutenzione ordinaria e straordinaria e riparazioni meccaniche, anche sul ponte, su tutte le marche. "
                     "Sono aperto dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato. "
                     "Scrivimi su WhatsApp o chiamami: il preventivo è gratuito e arriva prima di iniziare.",
                     "I'm Luca Miglietta, of L.M. Autoservizi. I work alone in my workshop in Frassineto Po, near Casale Monferrato. "
                     "I handle servicing, routine and major maintenance, and mechanical repairs on all makes, including jobs on the lift. "
                     "I'm open Monday to Friday, 7:30 to 19:30, with no lunch break. "
                     "Message me on WhatsApp or call me: the quote is free and comes before any work starts."),
        "comprende": [
            (("Tagliandi", "Servicing"),
             ("Tagliando secondo il piano di manutenzione della casa, su auto, fuoristrada, furgoni e camper.",
              "Servicing to the manufacturer's maintenance schedule, on cars, 4x4s, vans and campervans.")),
            (("Manutenzione ordinaria e straordinaria", "Routine and major maintenance"),
             ("Dai controlli periodici ai lavori più impegnativi. Prima ti dico cosa serve e quanto costa.",
              "From regular checks to bigger jobs. First I tell you what's needed and what it costs.")),
            (("Riparazioni sul ponte", "Repairs on the lift"),
             ("Con il ponte lavoro sotto il mezzo e vedo bene cosa c'è da fare.",
              "With the lift I can work under the vehicle and see clearly what needs doing.")),
            (("Freni, rumori e vibrazioni", "Brakes, noises and vibrations"),
             ("Un rumore in frenata o una vibrazione nuova vanno controllati. Cerco la causa e ti spiego cosa ho trovato.",
              "A noise when braking or a new vibration should be checked. I find the cause and explain what I've found.")),
            (("Ricambi", "Spare parts"),
             ("Vendo ricambi per tutte le marche. Se vuoi, il pezzo lo monto io in officina.",
              "I sell parts for all makes. If you like, I fit the part myself in the workshop.")),
        ],
        "perche": [
            (("Preventivo prima di iniziare", "A quote before I start"),
             ("Prima ascolto il problema, poi ti dico cosa serve e quanto costa. Inizio solo quando ti va bene.",
              "First I listen to the problem, then I tell you what's needed and what it costs. I start only when you're happy with it.")),
            (("Un solo riferimento", "One point of contact"),
             ("Lavoro da solo: la tua auto la segue la stessa persona, dalla prima telefonata alla riconsegna.",
              "I work alone: the same person looks after your car, from the first call to the hand-back.")),
            (("Vettura di cortesia gratuita", "Free courtesy car"),
             ("Per tutta la riparazione hai un'auto con il pieno, pulita e igienizzata.",
              "For the whole repair you have a car that's fuelled, clean and sanitised.")),
        ],
        "faq": [
            (("Fai il tagliando su auto di tutte le marche?", "Do you service all makes of car?"),
             ("Sì, lavoro su auto, fuoristrada, furgoni e camper di tutte le marche. Scrivimi marca, modello e chilometri e ti preparo il preventivo.",
              "Yes, I work on cars, 4x4s, vans and campervans of all makes. Send me the make, model and mileage and I'll prepare a quote.")),
            (("Posso fare il tagliando da te se l'auto è in garanzia?", "Can you service my car while it's still under warranty?"),
             ("In generale sì: per le regole europee la garanzia resta valida se segui il piano di manutenzione della casa. "
              "Riparazioni in garanzia e richiami restano invece alla rete ufficiale. Se hai dubbi, portami il libretto e lo guardiamo insieme.",
              "Yes: in general, under EU rules, the manufacturer's warranty stays valid as long as you follow its maintenance schedule. "
              "Warranty repairs and recalls, however, stay with the official dealer network. If in doubt, bring me the service book and we'll look at it together.")),
            (("Sento un rumore quando freno: è grave?", "I hear a noise when I brake: is it serious?"),
             ("Un rumore in frenata va controllato presto, senza aspettare. Portami l'auto: la guardo sul ponte e ti dico cosa serve e quanto costa.",
              "A noise when braking should be checked soon, rather than left. Bring it in: I'll look at it on the lift and tell you what's needed and what it costs.")),
            (("E se durante il lavoro trovi altro da sistemare?", "What if you find something else during the job?"),
             ("Ti chiamo e ti spiego cosa ho trovato. I lavori in più li faccio solo dopo il tuo ok.",
              "I call you and explain what I've found. I only do extra work once you've given me the OK.")),
            (("Quanto tempo resta in officina l'auto per il tagliando?", "How long does the car stay in for a service?"),
             ("Dipende dal mezzo e da cosa prevede il tagliando. Quando ci accordiamo ti dico quando portarla e quando riprenderla. "
              "Con l'orario continuato puoi lasciarla prima del lavoro e passare a prenderla dopo.",
              "It depends on the vehicle and what the service includes. When we arrange it, I tell you when to bring it in and when to collect it. "
              "As I'm open all day, you can drop it off before work and pick it up afterwards.")),
        ],
        "nota_mezzo": ("Es. tagliando in scadenza, rumore in frenata, perdita d'olio. Scrivi anche i chilometri.",
                       "E.g. service due, noise when braking, oil leak. Add the mileage too."),
        "correlati": ["elettrauto", "diagnosi"],
    },

    # ------------------------------------------------------------------ ELETTRAUTO (con climatizzatore)
    "elettrauto": {
        "nome": ("Elettrauto", "Auto electrics"),
        "title": ("Elettrauto a Frassineto Po, vicino a Casale | L.M. Autoservizi",
                  "Auto electrician in Frassineto Po, near Casale | L.M. Autoservizi"),
        "description": ("Avviamento, batteria, luci, cablaggi e climatizzatore: trovo e riparo i difetti elettrici. Officina a Frassineto Po, vicino a Casale. Scrivimi su WhatsApp.",
                        "Starting, battery, lights, wiring and air conditioning: I find and fix electrical faults. Workshop in Frassineto Po, near Casale. Message me on WhatsApp."),
        "h1": ("Elettrauto a Frassineto Po", "Auto electrician in Frassineto Po"),
        "risposta": ("Sono Luca Miglietta e lavoro da solo nella mia officina, L.M. Autoservizi, a Frassineto Po, vicino a Casale Monferrato. "
                     "Mi occupo di avviamento, batteria e ricarica, impianto luci, accessori e cablaggi. "
                     "Controllo e ricarico anche il climatizzatore. "
                     "Sono aperto dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato. "
                     "Scrivimi su WhatsApp o chiamami: il preventivo è gratuito e arriva prima di iniziare.",
                     "I'm Luca Miglietta and I work alone in my workshop, L.M. Autoservizi, in Frassineto Po, near Casale Monferrato. "
                     "I deal with starting, battery and charging, lights, accessories and wiring. "
                     "I also check and recharge air conditioning. "
                     "I'm open Monday to Friday, 7:30 to 19:30, with no lunch break. "
                     "Message me on WhatsApp or call me: the quote is free and comes before any work starts."),
        "comprende": [
            (("Avviamento", "Starting problems"),
             ("Se l'auto fatica a partire, controllo avviamento, batteria e ricarica e trovo dov'è il problema.",
              "If the car struggles to start, I check the starter, battery and charging and find where the problem is.")),
            (("Batteria e ricarica", "Battery and charging"),
             ("Verifico lo stato della batteria e dell'impianto di ricarica. La sostituisco solo se serve.",
              "I check the battery and the charging system. I replace the battery only if it's needed.")),
            (("Impianto luci", "Lights"),
             ("Fari, frecce, luci di stop e luci interne: trovo il guasto e lo riparo.",
              "Headlights, indicators, brake lights and interior lights: I find the fault and fix it.")),
            (("Accessori e cablaggi", "Accessories and wiring"),
             ("Monto accessori e sistemo cablaggi, anche su furgoni e camper.",
              "I fit accessories and sort out wiring, on vans and campervans too.")),
            (("Difetti elettrici", "Electrical faults"),
             ("Ogni genere di difetto elettrico, anche quelli che vanno e vengono. Prima cerco la causa, poi ti dico cosa serve.",
              "Every kind of electrical fault, including the ones that come and go. First I find the cause, then I tell you what's needed.")),
            (("Climatizzatore", "Air conditioning"),
             ("Controllo dell'impianto e ricarica del gas. Ho la formazione per il recupero dei gas fluorurati (Reg. CE 307/2008).",
              "System check and gas recharge. I'm trained in F-gas recovery (Reg. EC 307/2008).")),
        ],
        "perche": [
            (("Qualifica in elettromeccanica", "Trained in vehicle electromechanics"),
             ("Ho la qualifica di operatore di riparazioni elettromeccaniche per l'autoveicolo. Lavoro su tutte le marche da più di dieci anni.",
              "I'm qualified in electromechanical vehicle repairs. I've worked on all makes for over ten years.")),
            (("Formazione sui gas fluorurati", "F-gas training"),
             ("Per il climatizzatore ho la formazione sul recupero dei gas fluorurati nei veicoli, secondo il Reg. CE 307/2008.",
              "For air conditioning I'm trained in F-gas recovery from vehicles, under Reg. EC 307/2008.")),
            (("Prima il preventivo", "The quote comes first"),
             ("Ti dico cosa ho trovato e quanto costa la riparazione. Se trovo altro, ti chiamo prima di procedere.",
              "I tell you what I've found and what the repair costs. If I find anything else, I call you before going ahead.")),
        ],
        "faq": [
            (("L'auto fatica a partire la mattina: è la batteria?", "The car struggles to start in the morning: is it the battery?"),
             ("Può essere la batteria, ma anche la ricarica o l'avviamento. Con un controllo capisco da dove viene il problema e ti dico cosa serve prima di cambiare qualcosa.",
              "It may be the battery, but it could also be the charging system or the starter. A check shows me where the problem is, and I tell you what's needed before replacing anything.")),
            (("La batteria si scarica anche con l'auto ferma: perché?", "The battery goes flat even when the car is parked: why?"),
             ("Può esserci qualcosa che consuma corrente a motore spento, oppure un difetto nella ricarica. Lo cerco controllando l'impianto elettrico, poi ti dico cosa serve e quanto costa.",
              "Something may be drawing power with the engine off, or there may be a charging fault. I track it down by checking the electrical system, then tell you what's needed and what it costs.")),
            (("Il climatizzatore raffredda poco: basta ricaricarlo?", "The air conditioning is cooling less: is a recharge enough?"),
             ("A volte sì, ma prima controllo l'impianto. Se il gas è calato, conviene capire anche perché. Ti dico cosa serve prima di ricaricare.",
              "Sometimes, yes, but first I check the system. If the gas level has dropped, it's worth finding out why. I tell you what's needed before recharging.")),
            (("Monti anche accessori sull'auto?", "Do you fit accessories too?"),
             ("Sì, monto accessori e sistemo cablaggi e luci. Dimmi cosa vuoi installare e su che mezzo, e ti preparo il preventivo.",
              "Yes, I fit accessories and sort out wiring and lights. Tell me what you'd like fitted and on which vehicle, and I'll prepare a quote.")),
            (("Lavori anche su furgoni e camper?", "Do you work on vans and campervans?"),
             ("Sì: auto, fuoristrada, furgoni e camper, di tutte le marche. Per i mezzi più grandi scrivimi prima, così ti dico quando portarli.",
              "Yes: cars, 4x4s, vans and campervans, all makes. For larger vehicles message me first, so I can tell you when to bring them in.")),
        ],
        "nota_mezzo": ("Es. fatica a partire, la batteria si scarica, il clima raffredda poco. Scrivi anche quando succede.",
                       "E.g. it struggles to start, the battery goes flat, the A/C is cooling less. Say when it happens too."),
        "correlati": ["diagnosi", "meccanica"],
    },

    # ------------------------------------------------------------------ GOMMISTA
    "gommista": {
        "nome": ("Gommista", "Tyres"),
        "title": ("Gommista a Frassineto Po, vicino a Casale | L.M. Autoservizi",
                  "Tyre fitting in Frassineto Po, near Casale | L.M. Autoservizi"),
        "description": ("Cambio gomme, equilibratura, convergenza e forature a Frassineto Po, vicino a Casale. Gomme estive, invernali e quattro stagioni: scrivimi la misura.",
                        "Tyre changes, balancing, alignment and punctures in Frassineto Po, near Casale. Summer, winter and all-season tyres for sale: send me the size."),
        "h1": ("Gommista a Frassineto Po", "Tyre fitting in Frassineto Po"),
        "risposta": ("Sono Luca Miglietta e faccio il gommista nella mia officina a Frassineto Po, vicino a Casale Monferrato. "
                     "Lavoro da solo, con le attrezzature per montaggio, equilibratura e convergenza. "
                     "Riparo forature, faccio il cambio stagionale e vendo gomme estive, invernali e quattro stagioni. "
                     "Sono aperto dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato. "
                     "Scrivimi su WhatsApp o chiamami: il preventivo è gratuito e arriva prima di iniziare.",
                     "I'm Luca Miglietta and I fit tyres in my workshop in Frassineto Po, near Casale Monferrato. "
                     "I work alone, with the equipment for fitting, balancing and alignment. "
                     "I repair punctures, do seasonal changes and sell summer, winter and all-season tyres. "
                     "I'm open Monday to Friday, 7:30 to 19:30, with no lunch break. "
                     "Message me on WhatsApp or call me: the quote is free and comes before any work starts."),
        "comprende": [
            (("Sostituzione pneumatici", "Tyre fitting"),
             ("Smonto e monto le gomme sul cerchio, in officina.",
              "I remove and fit tyres on the rim, in the workshop.")),
            (("Equilibratura", "Wheel balancing"),
             ("Equilibro le ruote quando monto le gomme, o se il volante vibra in velocità.",
              "I balance the wheels when fitting tyres, or if the steering wheel shakes at speed.")),
            (("Convergenza e campanatura", "Alignment and camber"),
             ("Controllo e regolo l'assetto delle ruote. È utile se l'auto tira da un lato.",
              "I check and adjust wheel alignment and camber. It helps if the car pulls to one side.")),
            (("Riparazione forature", "Puncture repair"),
             ("Se il foro si può riparare in sicurezza, lo riparo. Altrimenti ti dico quale gomma conviene montare.",
              "If the puncture can be safely repaired, I repair it. If not, I tell you which tyre is worth fitting.")),
            (("Cambio stagionale", "Seasonal change"),
             ("Monto le invernali in autunno e le estive in primavera, nei periodi previsti.",
              "I fit winter tyres in autumn and summer tyres in spring, within the set dates.")),
            (("Vendita pneumatici", "Tyre sales"),
             ("Estive, invernali e quattro stagioni. Dimmi la misura o la targa e ti rispondo con disponibilità e prezzo.",
              "Summer, winter and all-season. Tell me the size or the number plate and I'll reply with availability and price.")),
        ],
        "perche": [
            (("Tutto nella stessa officina", "Everything in one workshop"),
             ("Montaggio, equilibratura e convergenza li faccio qui, con le attrezzature giuste.",
              "Fitting, balancing and alignment are all done here, with the right equipment.")),
            (("La gomma adatta al tuo uso", "The right tyre for how you drive"),
             ("Estive, invernali o quattro stagioni: ti aiuto a scegliere in base a come usi il mezzo.",
              "Summer, winter or all-season: I help you choose based on how you use your vehicle.")),
            (("Aperto dalle 7:30 alle 19:30", "Open 7:30 to 19:30"),
             ("Dal lunedì al venerdì, orario continuato: lasci l'auto prima del lavoro e la riprendi dopo.",
              "Monday to Friday, straight through: drop the car off before work and pick it up afterwards.")),
        ],
        "faq": [
            (("Quando si montano le gomme invernali?", "When should winter tyres go on?"),
             ("Dove previsto dalle ordinanze, servono gomme invernali o catene a bordo, di solito dal 15 novembre al 15 aprile. "
              "Le invernali si possono montare dal 15 ottobre. Le estive si rimontano entro il 15 maggio.",
              "Where ordinances require it, you need winter tyres or chains on board, usually from 15 November to 15 April. "
              "Winter tyres can go on from 15 October. Summer tyres go back on by 15 May.")),
            (("Ogni quanto si fa la convergenza?", "How often should wheel alignment be done?"),
             ("Dipende dall'auto e da come la usi. Conviene controllarla quando monti gomme nuove o dopo un colpo forte contro una buca o un marciapiede. "
              "Anche se l'auto tira da un lato o le gomme si consumano in modo irregolare.",
              "It depends on the car and how you use it. It's worth checking when you fit new tyres or after a hard knock against a pothole or kerb. "
              "Also if the car pulls to one side or the tyres wear unevenly.")),
            (("Si può riparare una foratura o devo cambiare la gomma?", "Can a puncture be repaired, or do I need a new tyre?"),
             ("Dipende da dove si trova il foro e da quanto è grande. La guardo e ti dico se si ripara in sicurezza o se conviene cambiarla.",
              "It depends on where the hole is and how big it is. I'll look at it and tell you if it can be safely repaired or needs replacing.")),
            (("Vendi anche le gomme?", "Do you sell tyres too?"),
             ("Sì, estive, invernali e quattro stagioni. Scrivimi la misura che trovi sul fianco della gomma, per esempio 205/55 R16, oppure la targa. "
              "Ti rispondo con disponibilità e prezzo.",
              "Yes, summer, winter and all-season. Send me the size printed on the tyre sidewall, for example 205/55 R16, or the number plate. "
              "I'll reply with availability and price.")),
            (("Fai anche equilibratura e convergenza?", "Do you do balancing and alignment too?"),
             ("Sì, in officina ho le attrezzature per montaggio, equilibratura e convergenza. Se la convergenza serve, te lo dico prima di farla.",
              "Yes, the workshop has the equipment for fitting, balancing and alignment. If the alignment needs doing, I tell you before I do it.")),
        ],
        "nota_mezzo": ("Es. cambio stagionale, foratura, gomme nuove. Scrivi la misura: la trovi sul fianco della gomma.",
                       "E.g. seasonal change, puncture, new tyres. Add the size: you'll find it on the tyre sidewall."),
        "correlati": ["meccanica", "diagnosi"],
    },

    # ------------------------------------------------------------------ CARROZZERIA
    "carrozzeria": {
        "nome": ("Carrozzeria", "Bodywork"),
        "title": ("Carrozzeria a Frassineto Po, vicino a Casale | L.M. Autoservizi",
                  "Car bodywork in Frassineto Po, near Casale | L.M. Autoservizi"),
        "description": ("Carrozzeria, verniciatura, saldatura e sistemazioni varie a Frassineto Po, vicino a Casale. Mandami le foto del danno su WhatsApp per una prima idea.",
                        "Bodywork, painting, welding and general repairs in Frassineto Po, near Casale. Send me photos of the damage on WhatsApp for a first idea."),
        "h1": ("Carrozzeria a Frassineto Po", "Bodywork in Frassineto Po"),
        "risposta": ("Sono Luca Miglietta e lavoro da solo nella mia officina a Frassineto Po, vicino a Casale Monferrato. "
                     "Faccio carrozzeria, verniciatura, saldatura e sistemazioni varie, su mezzi di tutte le marche. "
                     "Per una prima idea mandami le foto del danno su WhatsApp, oppure chiamami. "
                     "Il preventivo è gratuito e arriva prima di iniziare. "
                     "Sono aperto dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato.",
                     "I'm Luca Miglietta and I work alone in my workshop in Frassineto Po, near Casale Monferrato. "
                     "I do bodywork, painting, welding and general repairs on vehicles of all makes. "
                     "For a first idea, send me photos of the damage on WhatsApp, or call me. "
                     "The quote is free and comes before any work starts. "
                     "I'm open Monday to Friday, 7:30 to 19:30, with no lunch break."),
        "comprende": [
            (("Carrozzeria", "Body repairs"),
             ("Ammaccature e urti su paraurti, portiere e fiancate.",
              "Dents and knocks on bumpers, doors and side panels.")),
            (("Verniciatura", "Painting"),
             ("Vernicio le parti riparate o rovinate, come una portiera graffiata.",
              "I paint repaired or damaged parts, such as a scratched door.")),
            (("Saldatura", "Welding"),
             ("Saldature sulla carrozzeria, anche su furgoni e camper.",
              "Welding on bodywork, on vans and campervans too.")),
            (("Sistemazioni varie", "General repairs"),
             ("Anche i lavori piccoli. Mandami una foto e ti dico come la vedo.",
              "Small jobs too. Send me a photo and I'll tell you what I think.")),
            (("Prima idea dalle foto", "A first idea from photos"),
             ("Mandami le foto del danno su WhatsApp. Il preventivo preciso te lo faccio quando vedo il mezzo.",
              "Send me photos of the damage on WhatsApp. I give you the exact quote once I've seen the vehicle.")),
        ],
        "perche": [
            (("Preventivo gratuito", "Free quote"),
             ("Sai quanto costa prima che inizi. Così puoi confrontare i prezzi con calma.",
              "You know the cost before I start, so you can compare prices calmly.")),
            (("Un solo riferimento", "One point of contact"),
             ("Parli sempre con me, dalla prima foto alla riconsegna. Ti aggiorno io su come va il lavoro.",
              "You always deal with me, from the first photo to the hand-back. I keep you updated on progress.")),
            (("Vettura di cortesia gratuita", "Free courtesy car"),
             ("Se il lavoro richiede più giorni, hai un'auto con il pieno, pulita e igienizzata.",
              "If the job takes several days, you have a car that's fuelled, clean and sanitised.")),
        ],
        "faq": [
            (("Posso mandarti le foto del danno?", "Can I send you photos of the damage?"),
             ("Sì, mandale su WhatsApp e ti do una prima idea. Il preventivo preciso te lo faccio quando vedo il mezzo.",
              "Yes, send them on WhatsApp and I'll give you a first idea. I give you the exact quote once I've seen the vehicle.")),
            (("Sistemi anche un graffio o una piccola ammaccatura?", "Do you fix a scratch or a small dent?"),
             ("Sì, faccio anche i lavori piccoli. Mandami una foto e ti dico come la vedo.",
              "Yes, I do small jobs too. Send me a photo and I'll tell you what I think.")),
            (("Ripari anche ruggine e parti da saldare?", "Do you repair rust and parts that need welding?"),
             ("Faccio saldature e sistemazioni varie, anche su furgoni e camper. Mandami una foto della zona e ti dico se conviene intervenire.",
              "I do welding and general repairs, on vans and campervans too. Send me a photo of the area and I'll tell you whether it's worth doing.")),
            (("Quanto resta in officina il mezzo?", "How long will the vehicle stay in?"),
             ("Dipende dal lavoro: ne parliamo quando ti do il preventivo. Intanto hai la vettura di cortesia gratuita, per tutta la riparazione.",
              "It depends on the job: we'll talk about it when I give you the quote. Meanwhile you have the free courtesy car for the whole repair.")),
            (("Quando e come pago?", "When and how do I pay?"),
             ("Paghi alla riconsegna, in contanti, con carta o con bancomat.",
              "You pay when you collect the vehicle, in cash or by credit or debit card.")),
        ],
        "nota_mezzo": ("Es. urto sul paraurti, graffio sulla portiera. Mandami anche le foto del danno su WhatsApp.",
                       "E.g. dented bumper, scratched door. Send me photos of the damage on WhatsApp too."),
        "correlati": ["meccanica", "diagnosi"],
    },

    # ------------------------------------------------------------------ DIAGNOSI E PRE-REVISIONE
    "diagnosi": {
        "nome": ("Diagnosi e pre-revisione", "Diagnostics and pre-inspection"),
        "title": ("Diagnosi auto e pre-revisione a Frassineto Po | L.M. Autoservizi",
                  "Diagnostics and pre-inspection, Frassineto Po | L.M. Autoservizi"),
        "description": ("Spie, errori e programmazione centraline con software aggiornato ogni giorno, a Frassineto Po. Controllo gratuito prima della revisione: scrivimi.",
                        "Warning lights, fault codes and ECU programming with daily-updated software, in Frassineto Po. Free check before your roadworthiness test: message me."),
        "h1": ("Diagnosi e pre-revisione a Frassineto Po", "Diagnostics and pre-inspection in Frassineto Po"),
        "risposta": ("Sono Luca Miglietta e lavoro da solo nella mia officina a Frassineto Po, vicino a Casale Monferrato. "
                     "Leggo errori e spie e programmo centraline con software aggiornato ogni giorno. "
                     "Prima della revisione controllo gratis il mezzo e te la prenoto. "
                     "La fanno solo la Motorizzazione o i centri autorizzati. "
                     "Sono aperto dal lunedì al venerdì, 7:30–19:30, orario continuato. "
                     "Scrivimi su WhatsApp o chiamami: il preventivo gratuito arriva prima di iniziare.",
                     "I'm Luca Miglietta. I run my workshop alone in Frassineto Po, near Casale Monferrato. "
                     "I read fault codes and warning lights and program ECUs, using daily-updated software. "
                     "Before your roadworthiness test, I check the vehicle for free and book it. "
                     "Only the Motorizzazione or authorised centres carry out the test. "
                     "I'm open Monday to Friday, 7:30–19:30, no lunch break. "
                     "Message me on WhatsApp or call: the free quote comes first."),
        "comprende": [
            (("Lettura di errori e spie", "Fault codes and warning lights"),
             ("Collego la diagnosi e leggo cosa segnala la centralina, prima di decidere cosa fare.",
              "I connect the diagnostic tool and read what the ECU reports, before deciding what to do.")),
            (("Programmazione centraline", "ECU programming"),
             ("Programmo le centraline quando serve. Dimmi marca, modello e anno e ti dico se posso farlo.",
              "I program ECUs when needed. Tell me the make, model and year and I'll tell you whether I can do it.")),
            (("Controllo pre-revisione gratuito", "Free pre-inspection check"),
             ("Prima della revisione periodica controllo il mezzo gratis. Se trovo qualcosa, ti dico cosa serve e quanto costa.",
              "Before the periodic test I check the vehicle for free. If I find anything, I tell you what's needed and what it costs.")),
            (("Prenotazione della revisione", "Booking the test"),
             ("Ti prenoto io la revisione presso la Motorizzazione o un centro autorizzato.",
              "I book the roadworthiness test for you with the Motorizzazione or an authorised centre.")),
            (("Riparazioni dopo la diagnosi", "Repairs after the diagnosis"),
             ("Se la diagnosi trova un guasto, ti spiego cosa serve. Riparo solo dopo il tuo ok.",
              "If the diagnosis finds a fault, I explain what's needed. I repair it only once you've given the OK.")),
        ],
        "perche": [
            (("Software aggiornato ogni giorno", "Software updated every day"),
             ("Leggo errori e spie con un software di diagnosi aggiornato ogni giorno.",
              "I read fault codes and warning lights with diagnostic software that's updated every day.")),
            (("Responsabile tecnico delle revisioni", "Qualified inspection technical manager"),
             ("Ho l'abilitazione di responsabile tecnico delle revisioni periodiche. Conosco i controlli che aspettano il tuo mezzo.",
              "I'm qualified as a technical manager for periodic vehicle inspections. I know the checks your vehicle will face.")),
            (("Controllo gratuito e prenotazione", "Free check and booking"),
             ("Ti controllo il mezzo gratis prima della revisione e ti prenoto io l'appuntamento.",
              "I check your vehicle for free before the test and book the appointment for you.")),
        ],
        "faq": [
            (("La spia del motore è accesa: posso continuare a guidare?", "The engine warning light is on: can I keep driving?"),
             ("Dipende dalla spia e da come si comporta l'auto. Se la spia è rossa o lampeggia, o l'auto cambia comportamento, fermati appena puoi in sicurezza e chiamami. "
              "Negli altri casi fai leggere l'errore presto.",
              "It depends on the light and how the car behaves. If it's red or flashing, or the car behaves differently, stop when it's safe and call me. "
              "Otherwise, have the fault code read soon.")),
            (("La revisione la fai tu?", "Do you carry out the roadworthiness test (revisione)?"),
             ("La revisione la fanno solo la Motorizzazione o i centri autorizzati. Io controllo il mezzo gratis prima, ti dico se c'è qualcosa da sistemare e ti prenoto la revisione.",
              "The test is carried out only by the Motorizzazione or authorised centres. I check the vehicle for free beforehand, tell you if anything needs fixing and book the test for you.")),
            (("Ogni quanto va fatta la revisione?", "How often is the roadworthiness test due?"),
             ("La prima revisione va fatta entro quattro anni dalla prima immatricolazione, poi ogni due anni. Scrivimi la scadenza e ti organizzo il controllo gratuito prima.",
              "The first test is due within four years of first registration, then every two years. Tell me when yours is due and I'll arrange the free check beforehand.")),
            (("Cosa controlli nella pre-revisione?", "What do you check in the pre-inspection?"),
             ("Guardo i punti che si verificano in revisione, come luci, freni, gomme e spie. Se trovo qualcosa ti dico cosa serve e quanto costa, e decidi tu.",
              "I look at the points checked during the test, such as lights, brakes, tyres and warning lights. If I find anything, I tell you what's needed and what it costs, and you decide.")),
            (("Mi hanno detto che va programmata la centralina: lo fai?", "I've been told my ECU needs programming: can you do it?"),
             ("Programmo le centraline con software aggiornato ogni giorno. Scrivimi marca, modello e anno del mezzo e ti dico se posso farlo e quanto costa.",
              "I program ECUs with software updated every day. Send me the make, model and year: I'll tell you if I can do it and what it costs.")),
            (("La diagnosi si può fare anche fuori dall'officina?", "Can the diagnosis be done away from the workshop?"),
             ("Di solito la faccio in officina. Nei casi semplici leggo le spie anche sul posto, con l'officina mobile, a Casale Monferrato e nei paesi vicini.",
              "I usually do it in the workshop. In simple cases, the mobile workshop lets me read warning lights on site, in Casale Monferrato and nearby villages.")),
        ],
        "nota_mezzo": ("Es. spia del motore accesa, revisione in scadenza a marzo. Se puoi, fai una foto della spia.",
                       "E.g. engine warning light on, test due in March. If you can, take a photo of the light."),
        "correlati": ["elettrauto", "meccanica"],
    },
}

SERVIZI_HUB = {
    "title": ("Servizi auto a Frassineto Po, vicino a Casale | L.M. Autoservizi",
              "Car services in Frassineto Po, near Casale | L.M. Autoservizi"),
    "description": ("Meccanica, elettrauto e clima, gommista, carrozzeria, diagnosi e pre-revisione su tutte le marche, a Frassineto Po. Chiedi un preventivo gratuito.",
                    "Mechanics, auto electrics and A/C, tyres, bodywork, diagnostics and pre-inspection on all makes in Frassineto Po. Ask for a free quote."),
    "h1": ("Servizi auto a Frassineto Po", "Car services in Frassineto Po"),
    "intro": ("Nella mia officina a Frassineto Po, vicino a Casale Monferrato, seguo auto, fuoristrada, furgoni e camper. "
              "Lavoro su tutte le marche, da solo, dalla prima telefonata alla riconsegna. "
              "Scegli il servizio: per ognuno trovi cosa comprende e le domande più frequenti. "
              "Il preventivo è gratuito e arriva prima di iniziare.",
              "In my workshop in Frassineto Po, near Casale Monferrato, I look after cars, 4x4s, vans and campervans. "
              "I work on all makes, on my own, from the first call to the hand-back. "
              "Choose a service: for each one you'll find what it includes and the most common questions. "
              "The quote is free and comes before any work starts."),
}

OFFICINA_PAGINA = {
    "title": ("Officina a Frassineto Po, orario continuato | L.M. Autoservizi",
              "Workshop in Frassineto Po, open 7:30–19:30 | L.M. Autoservizi"),
    "description": ("Officina multimarca a Frassineto Po, vicino a Casale. Aperta lun–ven 7:30–19:30, orario continuato. Vettura di cortesia gratuita. Chiamami o scrivimi.",
                    "All-makes workshop in Frassineto Po, near Casale. Open Mon–Fri 7:30–19:30, no lunch break. Free courtesy car. Call or message me."),
    "h1": ("L'officina a Frassineto Po", "The workshop in Frassineto Po"),
    "intro": ("La mia officina è a Frassineto Po, a pochi chilometri da Casale Monferrato. "
              "Qui trovi me, il ponte e le attrezzature per lavorare bene sul tuo mezzo. "
              "Sono aperto dal lunedì al venerdì, dalle 7:30 alle 19:30, senza pausa pranzo.",
              "My workshop is in Frassineto Po, a few kilometres from Casale Monferrato. "
              "Here you'll find me, the lift and the equipment to work properly on your vehicle. "
              "I'm open Monday to Friday, 7:30 to 19:30, with no lunch break."),
    "sezioni": [
        (("Cosa trovi in officina", "What's in the workshop"),
         ("Il ponte, per lavorare sotto il mezzo. La diagnosi, con software aggiornato ogni giorno. "
          "Le attrezzature per le gomme: montaggio, equilibratura e convergenza. "
          "E ci sono io, che seguo il tuo mezzo dall'inizio alla fine.",
          "The lift, for working under the vehicle. Diagnostics, with software updated every day. "
          "Tyre equipment for fitting, balancing and alignment. "
          "And me: I look after your vehicle from start to finish.")),
        (("Orario continuato, dal lunedì al venerdì", "Open all day, Monday to Friday"),
         ("Sono aperto dalle 7:30 alle 19:30, senza pausa pranzo. "
          "Puoi lasciare l'auto prima di andare al lavoro e riprenderla quando esci. "
          "Sabato e domenica sono chiuso.",
          "I'm open from 7:30 to 19:30, with no lunch break. "
          "You can drop the car off on your way to work and pick it up on your way home. "
          "I'm closed on Saturdays and Sundays.")),
        (("Vettura di cortesia gratuita", "Free courtesy car"),
         ("Mentre riparo il tuo mezzo, ti lascio una vettura di cortesia gratuita, per tutta la riparazione. "
          "Te la consegno con il pieno, pulita e igienizzata. Le condizioni te le spiego alla consegna.",
          "While I repair your vehicle, I give you a free courtesy car for the whole repair. "
          "It comes fuelled, clean and sanitised. I explain the conditions when I hand it over.")),
        (("Pagamenti", "Payment"),
         ("Paghi alla riconsegna, in contanti, con carta o con bancomat. "
          "Il preventivo è gratuito e i lavori in più li faccio solo dopo il tuo ok.",
          "You pay when you collect the vehicle, in cash or by credit or debit card. "
          "The quote is free, and I only do extra work once you've given me the OK.")),
    ],
    "cortesia_passi": [
        (("Me lo dici quando prenoti", "Tell me when you book"),
         ("Quando mi chiami o mi scrivi, dimmi che ti serve la vettura di cortesia.",
          "When you call or message me, let me know you need the courtesy car.")),
        (("La trovi pronta", "It's ready for you"),
         ("Quando porti il tuo mezzo, la trovi con il pieno, pulita e igienizzata. Ti spiego le condizioni alla consegna.",
          "When you bring your vehicle in, it's waiting for you, fuelled, clean and sanitised. I explain the conditions when I hand it over.")),
        (("La usi per tutta la riparazione", "Use it for the whole repair"),
         ("Resta a te finché il tuo mezzo è pronto. Ti aggiorno io su come va il lavoro.",
          "It stays with you until your vehicle is ready. I keep you updated on progress.")),
        (("Fai cambio alla riconsegna", "Swap back on collection"),
         ("Mi riporti la vettura di cortesia e riprendi il tuo mezzo. Paghi la riparazione alla riconsegna.",
          "You bring the courtesy car back and collect your vehicle. You pay for the repair on collection.")),
    ],
    "faq": [
        (("Quali sono gli orari dell'officina?", "What are the workshop's opening hours?"),
         ("Dal lunedì al venerdì, dalle 7:30 alle 19:30, orario continuato. Sabato e domenica sono chiuso.",
          "Monday to Friday, 7:30 to 19:30, with no lunch break. I'm closed on Saturdays and Sundays.")),
        (("Serve l'appuntamento?", "Do I need an appointment?"),
         ("Meglio chiamare o scrivere prima, così ti dico quando portarla. Se ti serve la vettura di cortesia, dimmelo subito.",
          "It's better to call or message first, so I can tell you when to bring it in. If you need the courtesy car, let me know straight away.")),
        (("Come funziona la vettura di cortesia?", "How does the courtesy car work?"),
         ("È gratuita e la tieni per tutta la riparazione. Te la consegno con il pieno, pulita e igienizzata, e ti spiego le condizioni alla consegna.",
          "It's free and you keep it for the whole repair. It comes fuelled, clean and sanitised, and I explain the conditions when I hand it over.")),
        (("Come posso pagare?", "How can I pay?"),
         ("Paghi alla riconsegna, in contanti, con carta o con bancomat.",
          "You pay when you collect the vehicle, in cash or by credit or debit card.")),
        (("Se faccio il tagliando da te, perdo la garanzia della casa?", "If you service my car, do I lose the manufacturer's warranty?"),
         ("In generale, secondo le regole europee, il tagliando in un'officina indipendente non fa decadere la garanzia del costruttore. "
          "Conta seguire il piano di manutenzione previsto dalla casa. Riparazioni in garanzia e richiami restano alla rete ufficiale.",
          "In general, under EU rules, servicing at an independent workshop does not void the manufacturer's warranty. "
          "What matters is following the manufacturer's maintenance schedule. Warranty repairs and recalls stay with the official dealer network.")),
    ],
}

HOME = {
    # Sezione subito dopo la griglia dei servizi: l'officina al centro.
    "officina_titolo": ("Ti aspetto in officina, a Frassineto Po.", "See you at the workshop in Frassineto Po."),
    "officina_testo": ("La mia officina è a pochi chilometri da Casale Monferrato. "
                       "Sono aperto dal lunedì al venerdì con orario continuato: lasci l'auto prima del lavoro e la riprendi dopo. "
                       "Per tutta la riparazione hai una vettura di cortesia gratuita.",
                       "My workshop is a few kilometres from Casale Monferrato. "
                       "I'm open Monday to Friday with no lunch break: drop the car off before work, collect it after. "
                       "For the whole repair you have a free courtesy car."),
    "officina_punti": [
        (("Orario continuato 7:30–19:30", "Open 7:30–19:30, straight through"),
         ("Dal lunedì al venerdì, senza pausa pranzo. Sabato e domenica chiuso.",
          "Monday to Friday, with no lunch break. Closed on Saturdays and Sundays.")),
        (("Vettura di cortesia gratuita", "Free courtesy car"),
         ("Con il pieno, pulita e igienizzata, per tutta la riparazione.",
          "Fuelled, clean and sanitised, for the whole repair.")),
        (("Preventivo gratuito prima di iniziare", "Free quote before I start"),
         ("Ti dico cosa serve e quanto costa. Si parte solo quando ti va bene.",
          "I tell you what's needed and what it costs. Work starts only when you're happy.")),
    ],
    # Sezione più leggera: comodità in più, mai la promessa principale.
    "extra_titolo": ("Qualche comodità in più.", "A few extras."),
    "extra_testo": ("Il lavoro lo faccio in officina. A Casale Monferrato e nei paesi vicini posso anche ritirare il mezzo o intervenire sul posto, nei casi semplici.",
                    "I do the work in the workshop. In Casale Monferrato and nearby villages I can also collect your vehicle or fix simple problems on the spot."),
    "extra_voci": [
        (("Ritiro e consegna", "Pick-up and delivery"),
         ("Passo a prendere il mezzo a casa o al lavoro e te lo riporto riparato.",
          "I collect the vehicle from your home or workplace and bring it back repaired.")),
        (("Officina mobile", "Mobile workshop"),
         ("Forature, cambio delle ruote già montate, diagnosi e avviamento nei casi semplici: arrivo io.",
          "Punctures, swapping wheels already on rims, diagnostics and simple starting problems: I come to you.")),
        (("Consulenza alle imprese", "Business consulting"),
         ("Per chi lavora nel settore automobilistico. Ne parliamo e capiamo insieme di cosa hai bisogno.",
          "For businesses in the automotive sector. Let's talk and work out together what you need.")),
    ],
}
