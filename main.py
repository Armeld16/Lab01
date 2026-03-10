import random
class Domanda:
    domanda:str
    difficolta: int
    opzione_giusta: str
    opzioni: [str]
    def __init__(self, domanda, difficolta, opzione_giusta, opzioni):
        self.domanda = domanda
        self.difficolta = difficolta
        self.opzione_giusta = opzione_giusta
        self.opzioni = opzioni


def leggi_domande():
        domande = [] # creiamo una lista delle domande, perchè sono più domande
        with open("domande.txt", "r", encoding="utf-8") as f:
            righe  = f.readlines() # Ora righe è una lista dove ogni elemento è una riga del file
            righe = [riga.strip() for riga in righe]
            for i in range(0, len(righe),7):
                riga_domanda = righe[i]
                riga_difficolta = righe[i+1]
                riga_giusta = righe[i + 2]
                riga_sbagliate = righe[i+3], righe[i+4], righe[i+5]
                d = Domanda(riga_domanda, int(riga_difficolta), riga_giusta, riga_sbagliate)
                domande.append(d)
        return domande
def leggi_punti():
    punteggi = []
    with open("punti.txt", "r", encoding="utf-8") as f:
        righe = f.readlines()
    for riga in righe:
        if riga.strip() != "":  # ignora righe vuote
            parti = riga.strip().split()
            punteggi.append([parti[0], int(parti[1])])
    return punteggi
def salva_punti(punteggi):
    with open("punti.txt", "w", encoding="utf-8") as f:
        for p in punteggi:
            f.write(f"{p[0]} {p[1]}\n")
def gioca(domande):
    punti = 0
    livello_corrente = 0
    nickname = ""
    while True:
        # filtra domande del livello corrente
        domande_livello = []
        for d in domande:
            if d.difficolta == livello_corrente:
                domande_livello.append(d)

        if len(domande_livello) == 0:
            print("Hai completato tutti i livelli!")
            break

        # pesca una casuale
        domanda_scelta = random.choice(domande_livello)

        # stampa la domanda
        print(domanda_scelta.domanda)
        risposte = list(domanda_scelta.opzioni) + [domanda_scelta.opzione_giusta]
        random.shuffle(risposte)
        for i, risposta in enumerate(risposte):
            print(i + 1, risposta)
        risposta_giocatore = int(input("Inserisci la risposta: "))
        if risposte[risposta_giocatore - 1] == domanda_scelta.opzione_giusta:
            print("Risposta corretta!")
            livello_corrente += 1
            punti += 1
        else:
            print(f"Risposta sbagliata!, la risposta giusta è: {domanda_scelta.opzione_giusta}")
            break

    nickname = input("Partita finita inserire il tuo nickname: ")
    print(f"Hai totalizzato {punti} punti!")
    punteggi = leggi_punti()
    punteggi.append([nickname, punti])
    punteggi.sort(key=lambda x: x[1], reverse=True)
    salva_punti(punteggi)




domande = leggi_domande()
gioca(domande)






