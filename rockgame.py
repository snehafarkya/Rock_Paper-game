import random 

print("Hey",input("Your Good name? "),"!\nWelcome to ROCK, PAPER, SCISSOR game ✌" )
print("Deep dive in a game and rock it🤙")
lis = ("🥌" ,"📜" ,"✂" )

comp = random.choice(lis) 
user = input('Choose any one:- \n "R for 🥌" or "P for 📜" or " S for ✂" : ' ) 

if (comp == "🥌" and user == "S") or (comp == "📜" and user == "R") or (comp == "✂" and user == "P"):
    print("  Computer's choice: ", comp , "\n  Your choice: ",user, "\n  Computer won 🥳! Better luck next time")  

elif (comp == "🥌" and user == "P") or (comp == "📜" and user == "S") or (comp == "✂" and user == "R"):
    print("  Computer's choice ", comp, "\n  Your choice: ",user, "\n  Yayyyy🥳! Congratulations, You won!!")
else: 
    print("OOPS!! You both have similiar taste😉")
