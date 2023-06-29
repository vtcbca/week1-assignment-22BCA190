#input a any number for armstrong
a=int(input('Enter Any Number:'))
b=a
s=len(str(a))
sum=0
while(a!=0):
    r=a%10
    sum=sum+(r**s)
    a=a//10
if(b==sum):
    print("{} is Armstrong Number.".format(b))
else:
    print("{} is Not Armstrong Number.".format(b))
