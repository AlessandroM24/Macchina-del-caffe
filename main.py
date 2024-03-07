MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}


def verifica_risorse(bevanda):
    ingredienti_bevanda = MENU[bevanda]["ingredients"]

    for ingrediente in ingredienti_bevanda:
        if resources[ingrediente] - ingredienti_bevanda[ingrediente] < 0:
            return False
    return True


def get_risorse_mancanti(bevanda):
    ingredienti_bevanda = MENU[bevanda]["ingredients"]
    lista_ingredienti_mancanti = []

    for ingrediente in ingredienti_bevanda:
        if resources[ingrediente] - ingredienti_bevanda[ingrediente] < 0:
            lista_ingredienti_mancanti.append(ingrediente)

    return lista_ingredienti_mancanti


def scala_risorse(bevanda):
    ingredienti_bevanda = MENU[bevanda]["ingredients"]

    for ingrediente in ingredienti_bevanda:
        resources[ingrediente] -= ingredienti_bevanda[ingrediente]


def refill():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


def calcola_resto(bevanda, denaro_utente):
    prezzo_bevanda = MENU[bevanda]["cost"]
    return denaro_utente - prezzo_bevanda


def get_report():
    stringa = f"""Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${resources["money"]}"""
    return stringa


while True:
    scelta = input("Cosa vuoi ordinare? (espresso/latte/cappuccino): ").lower()

    if scelta == "off":
        break  # Il programma termina la propria esecuzione.
    elif scelta == "report":
        print(get_report())  # Stampa lo stato attuale delle risorse della macchina del caffè.
    elif scelta == "refill":
        refill()  # Imposta il valore delle risorse allo stato iniziale.
    elif scelta == "help":
        print("off, report, refill, espresso, latte, cappuccino")  # Stampa tutti i comandi possibili.

    elif scelta == "espresso" or scelta == "latte" or scelta == "cappuccino":
        if verifica_risorse(scelta):  # Verifica che le risorse siano sufficienti per la bevanda scelta.
            quarters = float(input("Inserire quarters (0.25): "))
            dimes = float(input("Inserire dimes ($0.10): "))
            nickels = float(input("Inserire nickels ($0.05): "))
            pennies = float(input("Inserire pennies ($0.01): "))
            totale = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

            if totale == MENU[scelta]["cost"]:  # Verifica se i soldi inseriti possono comprare la bevanda.
                print("Acquisto effettuato con successo.")
                scala_risorse(scelta)
                resources["money"] += totale
            elif totale > MENU[scelta]["cost"]:  # Verifica se i soldi inseriti sono troppi, consegna il resto.
                print("Acquisto effettuato con successo.")
                print(f"Saldo inserito: ${totale}, resto di ${calcola_resto(scelta, totale)}")
                scala_risorse(scelta)
                resources["money"] += totale - calcola_resto(scelta, totale)
            else:  # Se non ci sono abbastanza soldi per l'acquisto, stampa un errore.
                print("Errore nell'acquisto, fondi insufficienti.")

        else:  # Stampa le risorse che mancano.
            print(f"Ingredienti mancanti: {get_risorse_mancanti(scelta)}")
