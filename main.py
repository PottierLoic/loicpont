# DM Algo
# Auteur : Loïc Pottier
# Date de création : 28/11/2022

def menu():
    print("Menu")
    print("1 - Nouvelle partie")
    print("2 - Options")
    print("3 - Crédits")
    print("4 - Quitter le jeu")

    choix=input("Choissisez une option : ")
    print("")
    if choix=="4":
        quit()
    elif choix=="3":
        credits()
    elif choix=="2":
        options()
    elif choix=="1":
        start()

def credits():
    print("Credits : ")
    print("Auteur : Loïc Pottier")
    print("Date de creation : 28/11/2022")
    print("RATIOOOOOOOO")
    print("")
    menu()

def options():
    print("")
    menu()

def start():
    tab =[]
    for i in range(10):
        tab.append([])
        for j in range(10):
            tab[i].append(0)
    tab.append([5, 8])

    




menu()