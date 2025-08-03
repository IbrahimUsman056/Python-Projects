import random

player_score=0
balls=0

def score(num):
    global player_score,balls,game

    list=[1,2,3,4,5,6]

    computer=random.choice(list)

    if(num==computer):
        print("OUT")
        game=False
    else:
        player_score+=num

    balls+=1
    print("YOU CHOSE:",num)
    print("COMPUTER CHOSE:",computer)
    print("SCORE:",player_score)
    print("BALLS PLAYED:",balls)


print("=== HEADS & TAILS GAME ===\n")
game=True
while game:
    print("\nCHOICES:")
    print("1. 1 RUN\n2. 2 RUNS\n3. 3 RUNS\n4. FOUR\n5. 5 RUNS\n6. SIX")
    try:
        num=int(input("PRESS ANY NUMBER FROM 1-6 TO SCORE: "))
        if num<1 or num>6:
            print("Please enter a number between 1 and 6.")
            continue
    except ValueError:
        print("Invalid input.")
        continue

    score(num)

print("\n*** GAME ENDED ***")
print("=== MATCH SUMMARY ===")
print("YOUR TOTAL SCORE:", player_score)
print("TOTAL BALLS FACED:", balls)