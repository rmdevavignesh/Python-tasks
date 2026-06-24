'''#task 2
#1
a=int(input("enter a value:"))
b=int(input("enter a value:"))
print(a&b)

#2
wa=int(input("enter a value:"))
b=int(input("enter a value:"))
print(a|b)

#3
a=int(input("enter a value:"))
b=int(input("enter a value:"))
print(a^b)

#4
x=int(input("enter a value:"))
print(~x)

#6
a=int(input("weight of 1:"))
b=int(input("weight of 2:"))
c=int(input("weight of 3:"))
d=int(input("weight of 4:"))
e=int(input("weight of 5:"))
print("average:",(a+b+c+d+e)/5)

#8
a=int(input("enter a value:"))
print("the square of a is:",a**2)

#9
a=int(input("enter a number:"))
print("the cube of a is:",a**3)

#11
x=int(input("enter a no:"))
y=int(input("enter a no:"))
if x==y:
    print("they are equal")
if x!=y:
    print("they are not equal")

#12
p=int(input("enter first no:"))
q=int(input("enter second no:"))
if p>q:
    print("first no is greater")
if p<q:
    print("second no is greater")

#13
a=int(input("enter a no:"))
if a<50:
    print("number is lesser than fifty")
if a>50:
    print("number is greater than fifty")

#14
a=int(input("enter first no:"))
b=int(input("enter second no:"))
if a>=b:
    print("first no is greater than or equal to second no")
else:
    print("second no is greater than first no")

#15
a=int(input("enter a no:"))
b=int(input("enter a no:"))
if b!=a:
    print("not equal")
else:
    print("equal")

#16
y=int(input("enter a no:"))
x=(2,4,6,8,10)
if y in x:
    print("no exists in tuple")
if y not in x:
    print("no does not exist in tuple")

#18
a=[2,3,4,5,6,7]
b=int(input("enter a no:"))
if b in a:
    print("element exists in list")
else:
    print("element does not exist in list")


#19
x=int(input("enter a no:"))
y=int(input("enter a no:"))
print(x is y)

#20
a=2
x=a
y=a
print(x is not y)

#17
p=int(input("principal amount:"))
r=float(input("annual interest rate:"))
n=int(input("no of times interest is compounded per year:"))
t=int(input("time the money is invested or borrowed for(in years):"))
A=p*(1+(r/n))**(n*t)
print("compound interest",A-p)

#7
a=int(input("enter a no:"))
b=a&1
if b==1:
    print("it is not even")
if b==0:
    print("it is even")

#10
x=int(input("enter a no:"))
y=int(input("enter a no:"))
x=x^y
y=x^y
x=x^y
print("first swapped value",x)
print("second swapped value",y)

#5
a=int(input("bill amount:"))
b=int(input("gst percentage:"))
c=(a*b)/100
print("Total amount with gst",a+c)'''
