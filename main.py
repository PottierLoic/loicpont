# DM Algo
# Auteur : Loïc Pottier
# Date de création : 28/11/2022

tab=[]
h_start=5
h_end=2

i_piece=[1, 1, 1, 1]
o_piece=[[1, 1],
         [1, 1]]
t_piece=[[0, 1, 0],
         [1, 1, 1]]
j_piece=[[1, 1, 1],
         [0, 0, 1]]
l_piece=[[1, 1, 1],
         [1, 0, 0]]
z_piece=[[1, 1, 0],
         [0, 1, 1]]
s_piece=[[0, 1, 1],
         [1, 1, 0]]

def menu():
    print("----- LE JEU DU print RATIOOOO -----")
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
        start(tab)

def credits():
    print("-----Credits-----")
    print("Auteur : Loïc Pottier")
    print("Date de creation : 28/11/2022")
    print("RATIOOOOOOOO")
    input("")
    menu()

def options():
    print("-----Options-----")
    h_start=input("Hauteur du départ : ")
    h_end=input("Hauteur d'arrivée : ")
    input("") 
    menu()

def start(tab):
    for i in range(10):
        tab.append([])
        for j in range(10):
            tab[i].append(0)
    tab.append([h_start, h_end])
    return tab

def choix():
    print("Choix   : 0-9 : Placer la piece dans une colonne")
    print("R : Rotation horaire de la piece")
    print("L : Roation trigonométrique de la piece")
    print("S : Stocker la piece")
    ch=input("Veuillez entrer votre choix : ")

def affichage():
    for ligne in range (len(tab)-1):
        if ligne == 5:
            print("Départ-"+str(tab[ligne]))
        elif ligne == 2:
            print("       "+str(tab[ligne])+"-Arrivée ")
        else:
            print("       "+str(tab[ligne]))

menu()
affichage()