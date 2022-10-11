grocery_list=[]


item=input("enter a grocery item, or type none to exit: \n").lower()
grocery_list.append(item)

while item != "none":
    item=input().lower()
    grocery_list.append(item)

if item =="none":
    grocery_list.remove("none")
    print("your shopping list: \n")
    for x in grocery_list:
        print(x)
receipt=[]        
while len(grocery_list) > 0:
    item=input("Enter items as you pick them up: ").lower()
    price= input("how much did it cost?: ")
    quantity= input("how many did you get?")
    receipt.append((item, float(price), int(quantity)))
    if item in grocery_list: 
        grocery_list.remove(item)  
    else:
        print("item not found")
    for x in grocery_list:
        print(x)
    if len(grocery_list) == 0:
        print("all done!")
    for lineitem in receipt:
        (item,price, quantity)= lineitem
        total = (price*quantity)
        print("Item " + str(item) + " " + " QTY: " + str(quantity) + " $" + str(price))
        print("your total is: " + "$" + str(total))

    
