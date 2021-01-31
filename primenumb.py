a=int(input("enter a number"))
count=0
i=2
while(i<=a//2):
    if(a%i==0):
        count=count+1
        break
    i=i+1
if(count==0 and a!=1):
    print("prime number")
else:
    print("not a prime number")