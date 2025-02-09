import random
num = random.randint(1,100)
answer = False
for _ in range(5):
    enteredNum = int(input())
    if(num > enteredNum):
        print("the number is higher")
    elif(num < enteredNum):
        print("the number is lower")
    else:
        answer = True
        break
if(answer):
    print("win")
else:
    print("lose")
