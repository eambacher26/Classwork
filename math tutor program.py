import random
questions={}
score = 0                        # need to assign base value to score
for i in range(11):                 # means it will generate ten questions need 11 for 10 questions?
    int_a = random.randint(1,10)                # will be first number
    int_b = random.randint(1,10)                #will be second number
    operators = ['+', '-', '*', '/'] #need to find out how to round for division that results in decimals to get correct answer
    operator_value = random.choice(operators)
    if operator_value == "/":
        int_a = int_a * int_b
    question = str(int_a) + ' ' +str(operator_value) + ' ' + str(int_b) #will print question in string form for user
    answer = eval(question)
    question+= ': '             # adds colon/ string to question formula

    questions.update({question:str(answer)}) #turns random equations into dictionary values, set answer to str to match user input so no int/ string incompatiblity occurs
name=input("What is your name?: ")
print("Hello " + name + " , here are some math questions.")
for q in questions.keys():              # q can be any variable, it is temporary now and is simply the varaible for key strings
    user_answer = input(q)              # q paramater here to populate the input string question automatically
    if questions.get(q) == str(user_answer): #turn to a string to match key value
        print("Correct!")             #the .get function returns key values
        score=score+1       #this will assign one to score variable in case of right answer to be printed out at end
    else:
        print("Incorrect!")
        print(questions.get(q))
print("You got " + str(score) + " correct!") #important to set score as str, otherwise it is an int and has print problems.