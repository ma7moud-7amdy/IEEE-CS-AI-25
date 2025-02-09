import random
password = ""
for _ in range(8):
    x = random.randint(1,3)
    if(x==1): #upper case letter
        num = random.randint(65 , 90)
    elif (x==2): #lower case letter
        num = random.randint(97 , 122)
    else: # number
        num = random.randint(48 , 57)
    ch = f"{num:c}"
    password+=ch
print(password)



