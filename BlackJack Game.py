import random
print('\n'*50)
print(r'''
♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣
        █▀▀ █   █▀█ █▀▀ █▄▀    █ █▀█ █▀▀ █▄▀ 
        █▀▄ █▄▄ █▀█ █▄▄ █ █ ▄▄ █ █▀█ █▄▄ █ █ 
♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠               
 __      __         __                                      __             
/  \    /  \  ____ |  |   ____  ____   _____   ____       _/  |_   ____     
\   \/\/   /_/ __ \|  | _/ ___\/  _ \ /     \_/ __ \      \   __\ /  _ \    
 \        / \  ___/|  |_\  \__(  <_> )  Y Y  \  ___/       |  |  (  <_> )   
  \__/\  /   \___  >____/\___  >____/|__|_|  /\___  >      |__|_  \____/    
       \/        \/          \/            \/     \/       /____/       
 __________ __                 __       __                 __        ________  ____ 
 \______   \  | _____    ____ |  |     |__|____    ____   |  | __    \_____  \/_   |
  |    |  _/  | \__  \ _/ ___\|  |  _  |  \__  \ _/ ___\  |  |/ /     /  ____/ |   |
  |    |   \  |__/ __ \\  \___|  |_( ) |  |/ __ \\  \___  |    <     /       \ |   |
  |______  /____(____  /\___  >____/|__|  (____  /\___  > |__|_ \    \_______ \|___|
         \/          \/     \/     \/          \/     \/       \/            \/''')
def blackjack_game():
    
    nos=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    def card_get():
        card=random.choice(nos)
        return card
    computer_cards=[]
    user_cards=[]

    for i in range(2):
        user_cards.append(card_get())
        computer_cards.append(card_get())

    u_score=sum(user_cards)
    comp_score=sum(computer_cards)
    def sum_cards():
        print(f'User Cards {user_cards} | Sum: {u_score}')
        print(f'Computer Cards {random.choice(computer_cards)}')


    sum_cards()
    if  u_score==21 and len(user_cards)==2:
        print('=========================================')
        print('''_____.___.               __      __.__         ._._._.
    \__  |   | ____  __ __  /  \    /  \__| ____   | | | |
    /   |   |/  _ \|  |  \ \   \/\/   /  |/    \  | | | |
    \____   (  <_> )  |  /  \        /|  |   |  \  \|\|\|
    / ______|\____/|____/    \__/\  / |__|___|  /  ______
    \/                            \/          \/   \/\/\/''')
        print('=========================================')
        print("IT'S A BLACKJACK!!")
        return
    a=input('''♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣
 
    Do you want to 'Hit'? 
    [y] Yes, Hit me!
    [n] No, I'll Stand.
 
 ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠
 >''')

    for i in range(1):
        if a =='y':
            user_cards.append(card_get())
            u_score=sum(user_cards)
            if u_score>21 and 11 in user_cards:
                user_cards[user_cards.index(11)] = 1
                u_score=sum(user_cards)
                print(f'''My Cards {user_cards} | My Score: {u_score}''')
        elif a=='n':
            print(f'''My Cards {user_cards} | My Score: {u_score}''')
            print(f'''My Cards {computer_cards} | My Score: {comp_score}''')
        else:
            print(f'''My Cards {user_cards} | My Score: {u_score}''')
            print(f'''My Cards {computer_cards} | My Score: {comp_score}''')
    for i in range(1):
        if  comp_score==21 and len(computer_cards)==2:
            print('=========================================')
            print('''_____.___.               __      __.__         ._._._.
    \__  |   | ____  __ __  /  \    /  \__| ____   | | | |
    /   |   |/  _ \|  |  \ \   \/\/   /  |/    \  | | | |
    \____   (  <_> )  |  /  \        /|  |   |  \  \|\|\|
    / ______|\____/|____/    \__/\  / |__|___|  /  ______
    \/                            \/          \/   \/\/\/''')
            print('=========================================')
            print('DEALER GOT THE BLACKJACK!!')
            return
    if comp_score==u_score and u_score<=21:
        print('''__________ ____ ___  _________ ___ ___  
\______   \    |   \/   _____//   |   \ 
 |     ___/    |   /\_____  \/    ~    \
 |    |   |    |  / /        \    Y    /
 |____|   |______/ /_______  /\___|_  / 
                           \/       \/  
            We Both have an equal score''')
    else:
        while comp_score<17:
            computer_cards.append(random.choice(nos))
            comp_score = sum(computer_cards)
            if comp_score < 17:
                if comp_score>21 and 11 in computer_cards:
                    computer_cards[computer_cards.index(11)] = 1
                    comp_score = sum(computer_cards)
                    print(f"Dealer's Cards {computer_cards} | Dealer's Score: {comp_score}")
                    print(f"Dealer's Cards {user_cards} | Dealer's Score: {u_score}")
                elif 10<comp_score<17:
                    if computer_cards==11:
                        computer_cards[computer_cards.index(11)] = 1
                        comp_score = sum(computer_cards)
                    print(f"Dealer's Cards {computer_cards} | Dealer's Score: {comp_score}")
                    print(f"My Cards {user_cards} | My Score: {u_score}")
        if comp_score==u_score:
            print('''__________ ____ ___  _________ ___ ___  
\______   \    |   \/   _____//   |   \ 
 |     ___/    |   /\_____  \/    ~   '\'
 |    |   |    |  / /        \    Y    /
 |____|   |______/ /_______  /\___|_  / 
                           \/       \/  
                We Both have an equal score''')
            print(f"My Cards {user_cards} | My Score: {u_score}")
            print(f"Dealer's Cards {computer_cards} | Dealer's Score: {comp_score}")
        elif u_score>21:
            print('=========================================')
            print('''_____.___.              .____                         ._.
\__  |   | ____  __ __  |    |    ____  ______ ____   | |
 /   |   |/  _ \|  |  \ |    |   /  _ \/  ___// __ \  | |
 \____   (  <_> )  |  / |    |__(  <_> )___ \\  ___/   \|
 / ______|\____/|____/  |_______ \____/____  >\___  >  __
 \/                             \/         \/     \/   \/''')
            print('=========================================')
            print(f"My Cards {user_cards} | My Score: {u_score}")
            print(f"Dealer's Cards {computer_cards} | Dealer's Score: {comp_score}")
        elif comp_score>21:
            print('=========================================')
            print('''_____.___.               __      __.__         ._._._.
\__  |   | ____  __ __  /  \    /  \__| ____   | | | |
 /   |   |/  _ \|  |  \ \   \/\/   /  |/    \  | | | |
 \____   (  <_> )  |  /  \        /|  |   |  \  \|\|\|
 / ______|\____/|____/    \__/\  / |__|___|  /  ______
 \/                            \/          \/   \/\/\/''')
            print('=========================================')
            print(f"My Cards {user_cards} | My Score: {u_score}")
            print(f"Dealer's Cards {computer_cards} | Dealer's Score: {comp_score}")
        elif u_score>comp_score:
            print('=========================================')
            print('''_____.___.               __      __.__         ._._._.
\__  |   | ____  __ __  /  \    /  \__| ____   | | | |
 /   |   |/  _ \|  |  \ \   \/\/   /  |/    \  | | | |
 \____   (  <_> )  |  /  \        /|  |   |  \  \|\|\|
 / ______|\____/|____/    \__/\  / |__|___|  /  ______
 \/                            \/          \/   \/\/\/''')
            print('=========================================')
            print(f"My Cards {user_cards} | My Score: {u_score}")
            print(f"Dealer's Cards {computer_cards} | Dealer's Score: {comp_score}")
        elif u_score<comp_score:
            print('=========================================')
            print('''_____.___.              .____                         ._.
\__  |   | ____  __ __  |    |    ____  ______ ____   | |
 /   |   |/  _ \|  |  \ |    |   /  _ \/  ___// __ \  | |
 \____   (  <_> )  |  / |    |__(  <_> )___ \\  ___/   \|
 / ______|\____/|____/  |_______ \____/____  >\___  >  __
 \/                             \/         \/     \/   \/''')
            print('=========================================')
            print(f"My Cards {user_cards} | My Score: {u_score}")
            print(f"Dealer's Cards {computer_cards} | Dealer's Score: {comp_score}")
        elif u_score==comp_score and u_score>21:
            print('=========================================')
            print('''_____.___.              .____                         ._.
\__  |   | ____  __ __  |    |    ____  ______ ____   | |
 /   |   |/  _ \|  |  \ |    |   /  _ \/  ___// __ \  | |
 \____   (  <_> )  |  / |    |__(  <_> )___ \\  ___/   \|
 / ______|\____/|____/  |_______ \____/____  >\___  >  __
 \/                             \/         \/     \/   \/''')
            print('=========================================')
            print("We Both have an equal score")
            print(f"My Cards {user_cards} | My Score: {u_score}")
            print(f"Dealer's Cards {computer_cards} | Dealer's Score: {comp_score}")
if comp_score>21 and 11 in (computer_cards):
        computer_cards[computer_cards.index(11)]=1
        comp_score=sum(computer_cards)
        print(f"DEALER'S SCORE: {comp_score}|DEALER'S CARDS: {computer_cards}")
        print(f"MY SCORE: {u_score}|MY CARDS: {user_cards}")
while input('''    ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ ♠ ♥ ♦ ♣ 
    DO YOU WANT TO PLAY A GAME OF BLACKJACK? (y/n): ''') == 'y':
    print("    ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠ ♣ ♦ ♥ ♠")

    blackjack_game()
