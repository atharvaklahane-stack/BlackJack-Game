import random
def blackjack():
    nos = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    c1=[]
    c2=[]
    for i in range(2):
        c1.append(random.choice(nos))
        c2.append(random.choice(nos))
    s1=sum(c1)
    s2=(sum(c2))
    print(f"MY CARDS: {c1}| MY SCORE: {s1}")
    print(f"DEALER'S 1ST CARD: {c2[0]}")
    if s1==21 and len(c1)==2:
        print("YOU WIN!!\nIT'S A BLACKJACK!!")
        return
    if s2==21 and len(c2)==2:
        print('YOU LOSE!!\nTHE DEALER GOT THE BLACKJACK ')
        return
    
    a=input("DO YOU WANT TO DRAW A CARD!!(Y/N)").upper()
    for i in range(1):
        if a =='Y':
            c1.append(random.choice(nos))
            s1=sum(c1)
            
            if s1>21:
                if 11 in c1:
                    c1[c1.index(11)]=1
                    s1=sum(c1)
                    if s1>s2:
                        print("YOU WIN!!")
                        print(f"MY CARDS: {c1}| MY SCORE: {s1}")
                        print(f"DEALER'S CARDS: {c2}| DEALER'S SCORE: {s2}")
                else:
                    print("YOU LOSE!!\nYOUR SCORE IS OVER 21!")
                    print(f"MY CARDS: {c1}| MY SCORE: {s1}")
                    print(f"DEALER'S CARDS: {c2}| DEALER'S SCORE: {s2}")
            elif s1>s2:
                    print("YOU WIN!!")
                    print(f"MY CARDS: {c1}| MY SCORE: {s1}")
                    print(f"DEALER'S CARDS: {c2}| DEALER'S SCORE: {s2}")
            elif s2>s1:
                    print("YOU LOSE!!")
                    print(f"MY CARDS: {c1}| MY SCORE: {s1}")
                    print(f"DEALER'S CARDS: {c2}| DEALER'S SCORE: {s2}")
        else:
            while s2<17:
                c2.append(random.choice(nos))
                s2=sum(c2)
                if s2>21 and 11 in c2:
                    c2[c2.index(11)]=1
                    s2=sum(c2)
            if s2>21 and 11 in c2:
                    c2[c2.index(11)]=1
                    s2=sum(c2)
                    print(f"MY CARDS: {c1}| MY SCORE: {s1}")
                    print(f"DEALER'S CARDS: {c2}| DEALER'S SCORE: {s2}")
            elif s2>21:
                print("YOU WIN!!\n THE DEALER'S SCORE IS OVER 21!")
                print(f"MY CARDS: {c1}| MY SCORE: {s1}")
                print(f"DEALER'S CARDS: {c2}| DEALER'S SCORE: {s2}")
            elif s2<22:
                if s2>s1:
                    print("YOU LOSE!!")
                    print(f"MY CARDS: {c1}| MY SCORE: {s1}")
                    print(f"DEALER'S CARDS: {c2}| DEALER'S SCORE: {s2}")
                elif s2<s1:
                    print("YOU WIN!!")
                    print(f"MY CARDS: {c1}| MY SCORE: {s1}")
                    print(f"DEALER'S CARDS: {c2}| DEALER'S SCORE: {s2}")
                elif s1==s2:
                    print("PUSH!!")
                    print(f"MY CARDS: {c1}| MY SCORE: {s1}")
                    print(f"DEALER'S CARDS: {c2}| DEALER'S SCORE: {s2}")
while True:
    play = input('''    ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ 
    DO YOU WANT TO PLAY A GAME OF BLACKJACK? (y/n): ''').upper()
    
    if play == 'Y':
        print("    ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠")
        blackjack()
    else:
        print("Thanks for playing! Goodbye ♠ ♥ ♦ ♣")
        break
