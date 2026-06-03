# blackjack
import random

dealer_hand = []
Player_hand = []
deck_l1 = ['A', 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 'K' , 'Q' , 'J' ]

def start_game():
   
    while len(dealer_hand)<2:   #distribute cards to dealer
            dealer_hand.append(random.choice(deck_l1))
    print(f"the cards in dealer hand are:{dealer_hand}")

    while len(Player_hand) < 2: #distribute cards to player
          Player_hand.append(random.choice(deck_l1))
    print(f'the cards in player hand are:{Player_hand}')



    def card_value(card): #converts face value to number
          if card in ['K','J','Q']:
                      return 10
          elif card in ['A']:
                 return 11
          else:
                 return card

    def game_move():
                # player's move
                player_total = sum(card_value(card) for card in Player_hand) 
                if player_total<18:
                        print('player has decided to hit')
                        Player_hand.append(random.choice(deck_l1))
                        print(f"the player cards after hit are{Player_hand}")
                else:
                        print('player has opted to stand and no card has been drawn')


                #calculate player's total after new cards
                player_total = sum(card_value(card) for card in Player_hand) 
                if player_total>21:
                                print("game is busted player loses")
                elif player_total==21:
                                print("player wins with total equal to 21")


                if player_total<21:
                        #delaer's game
                        dealer_total = sum(card_value(card) for card in dealer_hand) 
                        print(f"the sum of dealer's hand is{dealer_total}")
                        if dealer_total<17:
                                dealer_hand.append(random.choice(deck_l1))
                                print(f"the new dealer's hand is {dealer_hand}")
                        dealer_total = sum(card_value(card) for card in dealer_hand)
                        print(f"the sum of dealer's new hand is{dealer_total}")
                        if dealer_total>21:
                                print("game busted dealer loses")
                        elif dealer_total>=17 and dealer_total>player_total:
                                print("dealers wins with score greater then player")
                        if player_total>dealer_total:
                                print("player wins because dealer total is less than player total")
                        if dealer_total==21:
                                print("dealer wins with score 21")


               
                


                

    game_move()


          
          




           
        


start_game()


