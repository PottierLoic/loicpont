# DM Algo
# Auteur : Loïc Pottier
# Date de création : 28/11/2022

# IMPORTS
import random as rd

# Tableau de jeu vide
tab=[]

# Positions de base du départ et de l'arrivée
h_start=5
h_end=2

# Liste des différentes pièces en rotation normale
# premier index = piece
# deuxieme index = nom ou forme
# troisieme index = ligne de la piece
pieces=[["i_piece", [[0, 0, 0, 0],
                     [1, 1, 1, 1]]],
        ["o_piece", [[1, 1], 
                     [1, 1]]],
        ["t_piece", [[0, 1, 0],
                     [1, 1, 1]]],
        ["j_piece", [[1, 1, 1],
                     [0, 0, 1]]],
        ["l_piece", [[1, 1, 1],
                     [1, 0, 0]]],
        ["z_piece", [[1, 1, 0],
                     [0, 1, 1]]],
        ["s_piece", [[0, 1, 1],
                     [1, 1, 0]]]]

# Lancement du menu principal
def menu():
    print("----- LE JEU DU RATIOOOO -----")
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

# Lancement du menu "crédits"
def credits():
    print("-----Credits-----")
    print("Auteur : Loïc Pottier")
    print("Date de creation : 28/11/2022")
    print("RATIOOOOOOOO")
    input("")
    menu()

# Lancement du menu "options"
def options():
    print("-----Options-----")
    print("1 - Changer la hauteur de départ")
    print("2 - Changer la hauteur de d'arrivée")
    print("3 - Retour")
    choix=input("Choissisez une option : ")
    print("")
    if choix=="3":
        menu()
    elif choix=="2":
        h_start=input("Hauteur du départ : ")
        print("")
        options()
    elif choix=="1":
        h_end=input("Hauteur d'arrivée : ")
        print("")
        options()
    input("") 
    menu()

# Création du plateau de jeu
def start(tab):
    for i in range(10):
        tab.append([])
        for j in range(10):
            tab[i].append(0)
    tab.append([h_start, h_end])
    game()

# Demande du choix du joueur pour le tour actuel
def choix(next_pieces, stock):

    print("Choix   : 0-9 : Placer la piece dans une colonne")
    print("R : Rotation horaire de la piece")
    print("L : Roation trigonométrique de la piece")
    print("S : Stocker la piece")
    print("")

    print("Prochaines pièces : ")
    for i in range (3):
        print(i+1, ":", [next_pieces[i][0]])
        for j in range(len(next_pieces[i][1])):
            print(next_pieces[i][1][j])
        print("")

    if stock!=[]:
        print("Pièce stockée :",stock[0])
        for i in range(len(stock[1])):
            print(stock[1][i])
    else:
        print("Stock Vide")
    print("")

    return(input("Veuillez entrer votre choix : "))

# Affichage du plateau de jeu
def affichage():
    for ligne in range (len(tab)-1):
        if ligne == 5:
            print("Départ-"+str(tab[ligne]))
        elif ligne == 2:
            print("       "+str(tab[ligne])+"-Arrivée")
        else:
            print("       "+str(tab[ligne]))
    print("")

# Retourne un pièce aléatoire parmi la liste "pieces"
def aleaPiece(pieces):
    return(rd.choice(pieces))

# Retourne la piece donnée en paramètre tournée dans le sens voulu
def rotate(piece, sens):
    print("rotate")
    return piece    

# Ajoute la piece au plateau
def addPiece(piece, position):
    valide=True
    posValide=0
    for ligne in range(0,9):
        for i in range(len(piece[1])-1):
            for j in range(len(piece[1][i])-1):
                if piece[1][i][j]==1 and tab[ligne+i][int(position)-1+j]!=0:
                    valide=False
        if valide:
            posValide=ligne

    for i in range(len(piece[1])):
        for j in range(len(piece[1][i])):
            if piece[1][i][j]==1:
                tab[posValide+i][int(position)+j-1]=piece[1][i][j]
                
    return(tab)


# Ajoute la piece actuelle au stock
def stockPiece(piece, stock):
    return piece

def checkWin():
    return False

# Boucle du jeu
def game():
    stock=[]
    next_pieces=[]
    for i in range(3):
        next_pieces.append(aleaPiece(pieces))

    print("DEBUT DU JEU")
    

    while True:
        affichage()

        ch=choix(next_pieces, stock)

        if ch=="S":
            stock=stockPiece(next_pieces[0], stock)
            next_pieces.pop(0)
            next_pieces.append(aleaPiece(pieces))
        elif ch=="R":
            rotate(next_pieces[0], "R")
        elif ch=="S":
            rotate(next_pieces[0], "L")
        elif ch=="1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10":
            tab=addPiece(next_pieces[0], ch)
            next_pieces.pop(0)
            next_pieces.append(aleaPiece(pieces))
        else:
            print("Choix invalide !")
        
        if checkWin():
            print("Vous avez gagné !")
            print("")
            break
        



# Lancement du jeu
menu()