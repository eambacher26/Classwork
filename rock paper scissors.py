def main():      
    game_over = False
    while game_over == True:
        exit()
    while game_over == False:   
            play=input("Do you want to play a game? *creepy Jigsaw voice* ").lower()
            if play == "yes":
                player_choice=input("Rock, Paper, or Scissors?: ").lower()
            elif play == "no":
                print("Goodbye.")
                break
            else:
                while play != "yes" or "no":
                    print("I do not understand")
                    play=input("Do you want to play a game? yes/ no: ").lower()
                    if play == "yes":
                        player_choice = input("Rock, Paper, or Scissors?: ").lower()
                        break #needed to insert break otherwise never proceeds to game
                    if play == "no": 
                        print("Goodbye.")
                        exit()                                      
            import random
            import time
            choice_list=["rock","paper","scissors"] 
            print("Rock...")
            time.sleep(1)
            print("Paper...")
            time.sleep(1)
            print("Scissors...")
            time.sleep(1)       
            opp_choice =(random.choice(choice_list)) 
            print("Player: "+ player_choice)
            print("Computer: " + opp_choice)
            if player_choice.lower() == opp_choice:
                    print("it's a draw!")
            if player_choice.lower() == "rock":
                    if opp_choice == "scissors":
                        print("Rock beats scissors, you win!")
            if player_choice.lower() == "rock":
                    if opp_choice == "paper":
                        print("Paper beats rock, you lose!")            
            if player_choice.lower() == "scissors":
                    if opp_choice == "paper":
                        print("Scissors beat paper, you win!")            
            if player_choice.lower() == "scissors":
                    if opp_choice == "rock":
                        print("Rock beats scissors, you lose!")
            if player_choice.lower() == "paper":
                    if opp_choice == "rock":
                        print("paper beats rock, you win!")
            if player_choice.lower() == "paper":
                    if opp_choice == "scissors":
                        print("Scissors beats paper, you lose!") 

            replay=input("play again? yes/no: ").lower()
            if replay == "yes":
                main()
            elif replay == "no":
                game_over = True
                print("Thanks for playing!")
                
                    
main()

        
            


    #elif statements did not work here. would not return print statement on victor. Switched to if statements and worked.
             
                  
