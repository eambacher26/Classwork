age=int(input("How old are you? "))
while age <= 0:
    print("Invalid age. Please enter age: ")
    age=int(input("How old are you? "))
if age >= 55:
    print("You can drive")
    print("You can vote")
    print("You can enjoy a beer")
    print("You get the senior discount")
elif age >= 21:
    print("You can drive")
    print("You can vote")
    print("You can enjoy a beer")
elif age >=18:
    print("You can drive")
    print("You can vote")
elif age >=16:
    print("you can drive a car")
elif age < 16:
    print("You are a student")

    