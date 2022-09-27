joists=int(input("How many joists in the deck? "))
length=int(input("How long are the joists in inches? "))
board_width=int(input("How wide are your deck boards in nearest whole inches? "))
total_screws=(((length/board_width)*2)*joists)
print(total_screws)
#when performing math with user input make sure it is in int input