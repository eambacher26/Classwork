factors=[]

def countalpha(text):
    alpha = 0
    for c in text:
        if c.isalpha():
            alpha = alpha+1
    return alpha

def num_sum(text):
    for x in text:
        if x.isnumeric():
            factors.append(int(x)) #has to be indented to update list

            
        

text = input('please enter a phrase: ') 
answer=num_sum(text)
total=sum(factors)#sum function has to be down here OR a seperate function
print(total)
