import random

print (" --- MASTERMIND --- \n")
print ("Entre code color\n")
print ("Couleurs : .\nRouge(R),Jaune(J), bleu(B),Orange(O), Vert(V) et Noir(N) ")

colors = ["R", "J", "B", "O", "V", "N"]
trompe = 0
play = True
color_cod = random.sample(colors,4)	
print (color_cod)
while play:
    correct = 0 
    correct_not_in_place = 0
    joueur_try = raw_input("Code: ").upper()
    trompe += 1
	
    if len(joueur_try) != len(color_cod):
		print ("\nCouleurs code egale 4")
		continue
    for i in range(4):
		if joueur_try[i] not in colors:
			print ("\nCouleurs code possible 'R', 'J', 'B', 'O', 'V', N' ")
			break

    color_cod_2= "".join(color_cod)
    for j,k in enumerate(color_cod_2):
        if joueur_try[j] == color_cod_2[j]:
            correct +=1
        elif color_cod_2[j] in joueur_try:
            correct_not_in_place +=1
    if trompe == 1:
            print ("|---------------------------------------|\n")

    print ("|"+joueur_try+"| "+str(correct)+" | "+str(correct_not_in_place)+" | "+str(trompe)+"/10|\n")
    
    if trompe == 10:
        play = False
    if correct == len(color_cod_2):
        print("Correct , Bien jouer!")
        play = False
            
            