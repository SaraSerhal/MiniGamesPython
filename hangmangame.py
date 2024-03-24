# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 23:01:32 2022

@author: saras
"""
#Jeu du pendu
#Sara Serhal

print("Welcome to Hangman game!")

player1 = input("Enter the name of the first player: ") #le joueur 1 entre le mot à deviner
player2 = input("Enter the name of the second player: ") #le joueur 2 doit deviner le mot
print("Hello", player2, "! Good luck guessing the word of", player1)

word= input("Please select a random word: ") #le joueur 1 entre le mot à deviner
word=word.replace(' ',"") #les espaces sont supprimés

solution=[] #liste vide qui va permettre plus tard de récupérer la solution c'est à dire le mot à deviner sous forme de liste
affichage=[] #liste vide qui va permettre plus tard de récupérer le nombre de lettres à deviner

#La boucle for va permettre de mettre sous forme de liste les caractères du mot à deviner
for i in word.lower() or word.upper():
    solution.append(i) #affiche le mot à deviner sous forme d'une liste de caratère
    affichage.append("_") #affiche le nombre de lettres à deviner sous forme d'une liste
    
print(affichage) #le nombre de lettres à deviner est imprimé au joueur

amount_of_attemps = 8 #le nombre de tentatives est limité à 8
letter_found = "" #permet de stocker les lettres trouvées par le joueur 2

#La boucle while permet de compter les tentatives restantes au joueur
while amount_of_attemps > 0:
    letter= input("Please enter the letter or word to guess: ")
    #La boucle if permet de tester le cas où le joueur veut deviner le mot complet
    if len(letter)>1: #Si la longueur de la lettre entrée est supérieure à 1, le joueur veut deviner directement le mot 
        if letter.lower()==word or letter.upper()==word:#si le mot entré est égal au mot à deviner 
            print("You find the word!")#le joueur a deviné le mot
            break #permet de sortir de la boucle while si le joueur 2 trouve le mot et gagne
        
#La lettre proposée par le joueur 2 est dans la solution , c'est à dire qu'elle est dans le mot choisi par le joueur 1
    if letter.lower or letter.upper() in solution: #lettre minuscule ou majuscule
        for (index,element) in enumerate(solution): #on ajoute un compteur à la liste pour permettre de renvoyer l'élément et sa position
           
            #Si un élément de la liste de caractère du mot à deviner est égal à la lettre proposée par le joueur
            if element==letter.lower() or element==letter.upper(): #les lettres minuscules et majuscules sont acceptés
                affichage[index]=element #on affichage l'élément à sa position dans le mot à deviner
        letter_found=affichage #on affiche la lettre trouvée dans la liste 
        print("Yes! That letter is inside the word!",letter_found)
        
    #Le joueur 2 a trouvé toutes les lettres du mot choisi par le joueur 1
        if solution==affichage:#toutes les lettres à trouver sont dans la liste
            print(word)
            print("You won!")
            break #on sort de la boucle while car le joueur 2 a gagné et la partie est terminée
            
    #La lettre proposée par le joueur 2 n'est pas dans la solution   
    else:
        amount_of_attemps = amount_of_attemps-1 #le joueur perd un essai s'il se trompe
        print("Amount of attemps:", amount_of_attemps) #affiche le nombre d'essais restants
        
#Le nombre d'essais atteint 0
if amount_of_attemps==0:
    print("You lost!") #Le joueur n'a plus de tentatives donc il a perdu
