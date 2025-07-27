import random

def game(ch):
    list=["R","P","S"]
    computer= random.choice(list)
    if(ch==computer):
        print("You:",ch," Computer:",computer)
        print("DRAW")
    elif((ch=="R" and computer=="S") or (ch=="P" and computer=="R") or (ch=="S" and computer=="P")):
        print("You:",ch," Computer:",computer)
        print("YOU WON. COMPUTER LOST")
    else:
        print("You:",ch," Computer:",computer)
        print("COMPUTER WON. YOU LOST")



print("Play rock,paper,scissor with computer!")
ch=input("Enter R for rock, P for paper, S for scissor:")

game(ch)