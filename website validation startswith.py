
website=input("give me a website: ")
result = website.startswith("http://")
if result == False:
    print("this is not a valid website.")
elif result == True:
    print("thank you!")

