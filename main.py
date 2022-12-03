# DM Algo
# Auteur : Loïc Pottier
# Date de création : 28/11/2022

# IMPORTS
import random as rd
import os

# Positions de base du départ et de l'arrivée
h_start=5
h_end=2

longueur=10
largeur=10

# Liste des différentes pièces en rotation normale
# premier index = piece
# deuxieme index = nom ou forme
# troisieme index = ligne de la piece
pieces=[["i_piece", [[1, 1, 1, 1]]],
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
    return(choix)

# Lancement du menu "crédits"
def credits():
    print("-----Credits-----")
    print("Auteur : Loïc Pottier")
    print("Date de creation : 28/11/2022")
    print("RATIOOOOOOOO")
    input("")

# Lancement du menu "options"
def options():
    print("-----Options-----")
    print("1 - Changer la hauteur de départ")
    print("2 - Changer la hauteur de d'arrivée")
    print("3 - Retour")
    choix=input("Choissisez une option : ")
    print("")
    if choix=="2":
        h_start=input("Hauteur du départ : ")
        print("")
        options()
    elif choix=="1":
        h_end=input("Hauteur d'arrivée : ")
        print("")
        options()
    input("") 

# Création du plateau de jeu
def start(tab):
    for i in range(longueur):
        tab.append([])
        for j in range(largeur):
            tab[i].append(0)
    tab.append([h_start, h_end])
    return tab

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

# Demande au joueur de valider la prévisualisation
def validationPrevisu():
    print("Ce placement vous convient ?")

    return(input("O / N"))

# Affichage du plateau de jeu
def affichage(tab):
    symbol=""
    for ligne in range (len(tab)-1):
        if ligne == 5:
            print("Départ-", end="")
        else:
            print("       ", end="")
        for col in range (len(tab[0])):
            if col!=9:
                if tab[ligne][col]==0:
                    print("□ ", end="")
                else:
                    print("■ ", end="")
            elif col==9 and ligne==2:
                if tab[ligne][col]==0:
                    print("□-Arrivée")
                else:
                    print("■-Arrivée")
            else:
                if tab[ligne][col]==0:
                    print("□ ")
                else:
                    print("■ ")
            
    print("")

# Retourne un pièce aléatoire parmi la liste "pieces"
def aleaPiece(pieces):
    return(rd.choice(pieces))

# Retourne la piece donnée en paramètre tournée dans le sens voulu
def rotateL(piece):
    piece2=[]
    piece2.append(piece[0])
    piece2.append([])

    for i in range (len(piece[1][0])):
        piece2[1].append([])
    for i in range (len(piece[1])):
        for j in range (len(piece[1][i])):
            piece2[1][len(piece[1][0])-j-1].append(piece[1][i][j])

    return piece2

# Retourne la piece donnée en paramètre tournée dans le sens voulu
def rotateR(piece):
    for i in range(3):
        piece=rotateL(piece)
    return piece

# Ajoute la piece au plateau
def addPiece(tab, piece, position):
    valide=True
    posValide=0
    for ligne in range(0, longueur-len(piece[1])+1):
        for i in range(len(piece[1])):
            for j in range(len(piece[1][i])):
                if piece[1][i][j]==1 and tab[ligne+i][int(position)+j-1]!=0:
                    valide=False
        if valide:
            posValide=ligne

    for i in range(len(piece[1])):
        for j in range(len(piece[1][i])):
            if piece[1][i][j]==1:
                tab[posValide+i][int(position)+j-1]=piece[1][i][j]
    return(tab)

# Ajoute la piece actuelle eu haut du tableau
def previsu(tab, piece, position):
    for i in range(len(piece[1])):
        for j in range(len(piece[1][i])):
            if piece[1][i][j]==1:
                tab[i][int(position)+j-1]=piece[1][i][j]
    return(tab)

# Verifie si le joueur a gagné
def checkWin(tab):
    h_actu=h_start
    v=True
    for col in range(largeur):
        if tab[h_actu-1][col]:
            h_actu-=1
        elif tab[h_actu][col]:
            pass
        elif tab[h_actu+1][col]:
            h_actu+=1
        else:
            v=False

    if not (h_actu>=h_end-1 and h_actu<=h_end+1):
        v=False
    
    return v
        
    
# Boucle du jeu
def game():
    stock=[]
    next_pieces=[]
    tab=[]
    tab1=[]
    demarrage=False

    for i in range(3):
        next_pieces.append(aleaPiece(pieces))
    
    while not demarrage:
        m=menu()
        if m=="4":
            quit()
        elif m=="3":
            credits()
        elif m=="2":
            options()
        elif m=="1":
            tab=start(tab)
            tab1=start(tab1)
            demarrage=True

    os.system('cls')  
    print("DEBUT DU JEU")
    while True:
        affichage(tab)
        ch=choix(next_pieces, stock)

        for i in range(longueur):
            for j in range (largeur):
                tab1[i][j]=tab[i][j]

        if ch=="S":
            stock=next_pieces[0]
            next_pieces.pop(0)
            next_pieces.append(aleaPiece(pieces))
        elif ch=="R":
            p=rotateR(next_pieces[0])
            next_pieces.pop(0)
            next_pieces.insert(0, p)
        elif ch=="L":
            p=rotateL(next_pieces[0])
            next_pieces.pop(0)
            next_pieces.insert(0, p)
        elif ch=="1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10": 
            affichage(previsu(tab1, next_pieces[0], ch))

            if validationPrevisu()=="O":
                addPiece(tab1, next_pieces[0], ch)
                addPiece(tab, next_pieces[0], ch)
                next_pieces.pop(0)
                next_pieces.append(aleaPiece(pieces))
                print("validé")
        else:
            print("Choix invalide !")

        if checkWin(tab):
            break
    os.system('cls')
    if checkWin(tab):
        affichage(tab)
    
        
# Lancement du jeu
os.system('cls')

while True:
    game()
    print("")
    print("")
    print("Bravo, vous avez gagné !")
    if input("Recommencer une partie ? O/N")!="O":
        print("Bye bye !")
        quit()
