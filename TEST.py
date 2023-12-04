import time

def afficher_heure(heure, heure_alarme, format_12h=True):
    while True:
        heure[2] += 1
        if heure[2] >= 60:
            heure[1] += 1
            heure[2] = 0
        if heure[1] >= 60:
            heure[0] += 1
            heure[1] = 0
        if heure[0] >= 24:
            heure[0] = 0


        if format_12h:
           heure_str = f"{(heure[0] % 12) or 12}:{heure[1]:02d}:{heure[2]:02d} {'AM' if heure[0] < 12 else 'PM'}"
        else:
             heure_str = f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}"

        print(heure_str)
        
        if heure == heure_alarme:
            print("Alarme!")

        time.sleep(5)

def choisir_format():
    choix = input("Voulez-vous afficher l'heure en format 12H ? (oui/non): ")
    return choix.startswith("oui")

heure_alarme = [16, 30, 1]
heure = [16, 30, 00]

format_24h = choisir_format()

afficher_heure(heure, heure_alarme, format_24h)


