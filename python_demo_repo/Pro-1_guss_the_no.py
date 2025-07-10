import random
n=random.randint(1,50)
a=-1
gusess=1
while(a!=n):
    a=int(input("Enter the number :"))
    if(a<n):
        print("Higher number Please :")
        gusess+=1
    elif(a>n):
        print("Lower number Please :")
        gusess+=1

print(f"You gussed correct no in {gusess}'\n' NO is {n}")  