#Input the Any Number to check palindrome or not !
n=int(input("Enter Any Number:"))
temp=n
r=0     #r is remainder
re=0    #re is revase number
while n>0:
    r=n%10
    re=re*10+(r)
    n=n//10
if re==temp:
    print("{} is Palindrom Number".format(re))
else:
    print("{} is Not Palindrom Number".format(temp))
