import random 

print("Hey",input("Your Good name? "),"!\nWelcome to ROCK, PAPER, SCISSOR game β" )
print("Deep dive in a game and rock itπ€")
lis = ("π₯" ,"π" ,"β" )

comp = random.choice(lis) 
user = input('Choose any one:- \n "R for π₯" or "P for π" or " S for β" : ' ) 

if (comp == "π₯" and user == "S") or (comp == "π" and user == "R") or (comp == "β" and user == "P"):
    print("  Computer's choice: ", comp , "\n  Your choice: ",user, "\n  Computer won π₯³! Better luck next time")  

elif (comp == "π₯" and user == "P") or (comp == "π" and user == "S") or (comp == "β" and user == "R"):
    print("  Computer's choice ", comp, "\n  Your choice: ",user, "\n  Yayyyyπ₯³! Congratulations, You won!!")
else: 
    print("OOPS!! You both have similiar tasteπ")
