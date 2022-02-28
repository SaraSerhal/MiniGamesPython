# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:15:34 2022

@author: saras
"""
#Jeu du morpion
#BENARBIA Siham, SERHAL Sara

print("Welcome to Tic Tac Toe Game!")

player1 = "X"
player2="O"
#création plateau
l1=["_"]*3#création ligne 1 du plateau avec 3 colones
l2=["_"]*3#création ligne 2 du plateau avec 3 colones
l3=["_"]*3#création ligne 3 du plateau avec 3 colones
win_o="false"#création d'un flag pour arreter le jeu lorsque le joueur "o" gagne
win_x="false"#création d'un flag pour arreter le jeu lorsque le joueur "x" gagne
while win_o!="true" and win_x!="true":#la boucle du jeu qui continue jusqu'à ce qu'un des joueurs gagne
    #vérifie qu'il y a encore des cases vide et donc si le jeu peut continuer
    if l1[0]!="_" and l1[1]!="_" and l1[2]!="_" and l2[0]!="_"and l2[1]!="_" and l2[2]!="_"and l3[0]!="_"and l3[1]!="_"and l3[2]!="_":
        break
    print("Player x turn")#affiche le tour du joueur x
    #affiche le plateau
    print(l1)
    print(l2)
    print(l3)
    ligne=int(input("Entrez la ligne:"))#demande la ligne souhaité par le joueur x
    colonne=int(input("Entrez la colonne:"))#demande la colonne souhaité par le joueur x
    #modification du plateau en fonction de ce qu'a choisi le joueur x
    if ligne==1:
        l1[colonne-1]="x"
    if ligne==2:
        l2[colonne-1]="x"
    if ligne==3:
        l3[colonne-1]="x"
    #vérifie les conditions de victoire
    if l1[0]==l2[1]==l3[2]=="x" or l1[0]==l1[1]==l1[2]=="x" or l2[0]==l2[1]==l2[2]=="x" or l3[0]==l3[1]==l3[2]=="x" or l1[2]==l2[1]==l3[0]=="x":
        win_x="true"#change le flag pour avertir que le joueur a gagné
        break#termine la boucle pour ne pas lancé le tour du joueur o
    print("Player o turn")#affiche le tour de joueur o
    #affiche le plateau (avec les modification )
    print(l1)
    print(l2)
    print(l3)
    ligne=int(input("Entrez la ligne:"))#demande la ligne souhaité par le joueur o
    colonne=int(input("Entrez la colonne:"))#demande la colonne souhaité par le joueur o
    #modification du plateau en fonction de ce qu'a choisi le joueur o
    if ligne==1:
        l1[colonne-1]="o"
    if ligne==2:
        l2[colonne-1]="o"
    if ligne==3:
        l3[colonne-1]="o"
    #vérifie les conditions de victoire
    if l1[0]==l2[1]==l3[2]=="o" or l1[0]==l1[1]==l1[2]=="o" or l2[0]==l2[1]==l2[2]=="o" or l3[0]==l3[1]==l3[2]=="o" or l1[2]==l2[1]==l3[0]=="o":
        win_o="true"#change le flag pour avertir que le joueur a gagner
       
print(l1)
print(l2)
print(l3)
if win_o=="true":
    print("Le joueur O a gagné la partie")
elif win_x=="true":
    print("le joueur x a gagné")
else:
    print("Game over")