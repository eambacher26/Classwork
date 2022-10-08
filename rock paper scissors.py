from tkinter.messagebox import YES



player_score=0
computer_score=0
games_left=7

game_over = False

choice_list=["rock","paper","scissors"] # must be at top for user input verification


while game_over == True:
    exit()

while game_over == False:
            
        player_choice=input("Rock, Paper, or Scissors?: ").lower()
        while player_choice not in choice_list: #how to link user input to prepopulated list for verification
                input("This is not a valid selection, please choose rock, paper, or scissors: ")
                break
                                            
        import random
        import time
        
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
                games_left=games_left-0
                player_score=player_score+0
                computer_score=computer_score+0
        if player_choice.lower() == "rock":
                if opp_choice == "scissors":
                    print("Rock beats scissors, you win!")
                    games_left=games_left-1
                    player_score=player_score+1
                    computer_score=computer_score+0
        if player_choice.lower() == "rock":
                if opp_choice == "paper":
                    print("Paper beats rock, you lose!")
                    games_left=games_left-1
                    player_score=player_score+0
                    computer_score=computer_score+1            
        if player_choice.lower() == "scissors":
                if opp_choice == "paper":
                    print("Scissors beat paper, you win!")
                    games_left=games_left-1
                    player_score=player_score+1
                    computer_score=computer_score+0           
        if player_choice.lower() == "scissors":
                if opp_choice == "rock":
                    print("Rock beats scissors, you lose!")
                    games_left=games_left-1
                    player_score=player_score+0
                    computer_score=computer_score+1
        if player_choice.lower() == "paper":
                if opp_choice == "rock":
                    print("paper beats rock, you win!")
                    games_left=games_left-1
                    player_score=player_score+0
                    computer_score=computer_score+0
        if player_choice.lower() == "paper":
                if opp_choice == "scissors":
                    print("Scissors beats paper, you lose!")
                    games_left=games_left-1
                    player_score=player_score+0
                    computer_score=computer_score+1
        print("Your score so far: "+ str(player_score))                        
        print("Computer score so far is: " +str(computer_score))

        #GAME OVER ENDING DISPLAY AND REPLAY OPTION

        if games_left <=0:
            print("Game over!")
            if player_score < computer_score:
                print("You lost! " + str(player_score) + " to " + str(computer_score) + ".")
            elif player_score > computer_score:   
                print("You won! " + str(player_score) + " to " + str(computer_score) + ".")
            
            restart_game=input("Play another game?: " ).lower()
            if restart_game == "yes":
                player_score=0
                computer_score=0
                games_left=7
                game_over=False
            elif restart_game == "no":
                game_over = True
                print("Thanks for playing!")
                exit()
            else:
                while restart_game != "yes" or "no":
                    print("I do not understand")
                    restart_game=input("play again? yes/no: ").lower()
                    if restart_game == "yes":
                        game_over=False
                        player_score=0
                        computer_score=0
                        games_left=7
                        break
                    if restart_game == "no":
                        print("Thanks for playing!")
                        game_over = True
                        break
 #KEEP PLAYING PROMPT    
        while games_left > 0 and games_left <7:
                keep_playing=input("Keep playing?: " ).lower()
                if keep_playing == "yes":
                    game_over=False
                    break
                elif keep_playing == "no":
                    game_over = True
                    print("Thanks for playing!")
                    exit()
                else:                       #else statement needed before while for repeating loop
                    while keep_playing != 'yes' or 'no': #COULD ALSO USE LIST OF CHOICES
                        print("I do not understand")
                        keep_playing=input("keep playing? yes/no: ").lower()
                        if keep_playing == "yes":
                            game_over=False
                            break
                        if keep_playing == "no":
                            print("Thanks for playing!")
                            game_over = True
                            break
                    


                

    
        


#elif statements did not work here. would not return print statement on victor. Switched to if statements and worked.
            
                
