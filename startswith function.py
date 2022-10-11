
def startswith():
    word=input("Give me a word that starts with 'C': ").lower()
    if word.startswith("c"):
        print("the 'c' word you chose was " + str(word))
    else:
        while word.startswith("c") == False:
            print("Your word does not start with 'C' ")
            word=input("Give me a word that starts with 'C' ").lower()
            print("Thank you, the 'c' word you chose was " + str(word))

startswith()        