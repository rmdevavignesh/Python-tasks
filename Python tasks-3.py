'''#task 
#1
a=int(input("enter a no:"))
if a%2==0:
    print("no is even")
if a%2==1:
    print("no is odd")

#2
a=int(input("enter a no:"))
if a>0:
    print("no is positive")
elif a<0:
    print("no is negative")
else:
    print("no is zero")

#3
a=int(input("enter a no:"))
b=a%10
if b==0:
    print("no is divisible by both 2 and 5")
else:
    print("no is not divisible by both 2 and 5")

#4
m=int(input("enter marks:"))
if m>=95:
    print("Grade A")
elif m>=85:
     print("Grade B")
elif m>=75:
     print("Grade C")
elif m>=65:
     print("Grade D")
else:
    print("Grade E")

#6
for j in range(1,11):
    print(j)

#8
for i in range(10,0,-1):
    print(i)

#7
for i in range(1,11):
    print("square of",i,"is",i**2)

#9
a=int(input("enter age:"))
if a in range(0,13):
      print("You are a child")
if a in range(13,20):
      print("You are a teen")
if a in range(20,60):
      print("You are an adult")
if a in range(60,120):
      print("You are a senior")

#10
a=int(input("enter a no:"))
if a**3>=100:
    print("the cube of no is greater than 100")
else:
    print("the cube of no is lesser than or equal to 100")

#13
n=int(input("enter a natural no:"))
print("the sum of first",n,"natural numbers is",(n*(n+1)/2))

#12
character=input("enter a character:")
if character in ("a","e","i","o","u"):
    print("the given character is a vowel")
else:
    print("the given character is a constant")

#14
for i in range(65,91):
    print(chr(i),end="")
print()

#16(a)
n=int(input("enter a no:"))
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()

#16(b)
n=int(input("enter a no:"))
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()

#17(a)
n=int(input("enter a no:"))
for i in range(n):
    for j in range(i+1):
        print(i,end="")
    print()

#17(b)
n=int(input("enter a no:"))
for i in range(n):
    for j in range(i,n):
        print(i,end="")
    print()

#17(c)
n=int(input("enter a no:"))
p=0
for i in range(n):
    for j in range(i+1):
        print(p,end="")
        p+=2
    print()

#18(a)
n=int(input("enter a no:"))
p=65
for i in range(n):
    for j in range(i,n):
        print(chr(p),end="")
        p+=1
    print()

#18(b)
    p=65
n=int(input("enter a no:"))
for i in range(n):
    for j in range(i+1):
        print(chr(p),end="")
        p+=1
    print()

#11
n=(input("enter username:"))
if n=="deva":
    m=input("enter password:")
    if m=="deva@123":
        print("Login Successful")
    else:
     print("Login failed due to incorrect password")
else:
     print("Invalid username")

#15(a)
t=7
r=1
for i in range(1,10):
    print("7 x",r,"=",t*r)
    r+=1
    print()

#15(b)
a=12
b=1
for i in range(1,11):
    print("12 x",b,"=",b*a)
    b+=1
    print()

#5
p=int(input("enter year:"))
q=p%4
r=p%100
s=p%400
if q==0:
    if s==0:
        print("it is a leap year")
    elif r==0:
        print("it is not a leap year")
    elif q==0:
        print("it is a leap year")
else:
        print("it is not a leap year")

#19
p=input("enter password:")
while p=="deva123":
    print("correct password,access granted")
    break
else:
    print("incorrect password")

#20
n=1
sum=0
while n<=100:
    sum=sum+n
    n=n+1
print("The final sum is:",sum)'''


    
