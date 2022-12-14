# DM Algo
# Author : Loïc Pottier
# date : 28/11/2022

# IMPORTS
import random as rd
import os
import copy

# start en end position
h_start=5
h_end=2

length=10
width=10

# List of all the different pieces
# 1st index = piece list
# 2nd index = name, lines
# 3rd index = col
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

# main menu
def menu():
    print("----- LE JEU DU RATIOOOO -----")
    print("1 - Nouvelle partie")
    print("2 - Options")
    print("3 - Crédits")
    print("4 - Quitter le jeu")

    choix=input("Choissisez une option : ")
    print("")
    return(choix)

# credit menu
def credits():
    print("-----Credits-----")
    print("Auteur : Loïc Pottier")
    print("Date de creation : 28/11/2022")
    input("")

# options menu
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

# creation of game board
# 10x10 list of 0
def start(tab):
    for i in range(length):
        tab.append([])
        for j in range(width):
            tab[i].append(0)
    tab.append([h_start, h_end])
    return tab

# asks the user choice for the actual turn
# return the input value
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

# asks the usr validation for the previsualisation displayed previously
def validationPrevisu():
    print("Ce placement vous convient ?")

    return(input("O / N"))

# print the game board in parameter
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

# return a random piece from "pieces"
def aleaPiece():
    global pieces
    return(rd.choice(pieces))

# rotate a piece to the left
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

# rotate a piece to the right
def rotateR(piece):
    for i in range(3):
        piece=rotateL(piece)
    return piece

# add piece to the bottom of the main board
def addPiece(tab, piece, position):
    valide=True
    posValide=0
    for ligne in range(0, length-len(piece[1])+1):
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

# add piece to the top of the board, used for previsualisation
def previsu(tab, piece, position):
    for i in range(len(piece[1])):
        for j in range(len(piece[1][i])):
            if piece[1][i][j]==1:
                tab[i][int(position)+j-1]=piece[1][i][j]
    return(tab)

# check if the bridge is valid
def checkWin(tab):
    h_actu=h_start
    v=True
    for col in range(width):
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

# main game loop
def game():
    stock=[]
    next_pieces=[]
    tab=[]
    tab1=[]
    demarrage=False

    for i in range(3):
        next_pieces.append(aleaPiece())
    
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

        for i in range(length):
            for j in range (width):
                tab1[i][j]=tab[i][j]

        if ch=="S":
            if stock==[]:
                stock=next_pieces[0]
                next_pieces.pop(0)
                next_pieces.append(aleaPiece())
            else:
                temp=copy.deepcopy(stock)
                stock=next_pieces[0]
                next_pieces.pop(0)
                next_pieces.insert(0, temp)
        elif ch=="R":
            p=rotateR(next_pieces[0])
            next_pieces.pop(0)
            next_pieces.insert(0, p)
        elif ch=="L":
            p=rotateL(next_pieces[0])
            next_pieces.pop(0)
            next_pieces.insert(0, p)
        elif ch=="1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10": 
            if int(ch)+len(next_pieces[0][1][0])-2<width:
                affichage(previsu(tab1, next_pieces[0], ch))

                if validationPrevisu()=="O":
                    addPiece(tab1, next_pieces[0], ch)
                    addPiece(tab, next_pieces[0], ch)
                    next_pieces.pop(0)
                    next_pieces.append(aleaPiece())
                    print("validé")
            else:
                print("raté")
        else:
            print("Choix invalide !")
            
        if checkWin(tab):
            break
    os.system('cls')
    if checkWin(tab):
        affichage(tab)
    
        
# game launch

os.system('cls')

while True:
    game()
    print("")
    print("")
    print("Bravo, vous avez gagné !")
    if input("Recommencer une partie ? O/N")!="O":
        print("Bye bye !")
        quit()
