import random
flag=0
print("You have 3 rounds")
p=0
while(p<3):
    choice=int(input("Enter a number from 1 to 5: "))
    n=random.randint(1,5)
    if(choice==n):
        print("Right guess")
        flag=1
        break
    else:
        print("Incorrect. It was ",n)
        
    p+=1
if flag==1:
    print("Good job")
else:
    print("Tough luck")
    