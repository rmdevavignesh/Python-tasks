'''#task 6
#1
def even_number():
    for n in range(1,51):
        if n%2 ==0:
            print(n)
even_number()

#2
def addition_of_numbers(a,b):
    print(a+b)
addition_of_numbers(7,6)

#5
def student_detail(name,age,roll_no,course):
    print("Name:",name)
    print("Age:",age)
    print("Roll no:",roll_no)
    print("Course:",course)
student_detail("deva",18,7,"python")

#6
def rectangle_area(l,b):
    area=l*b
    print("Area of rectangle is:",area)
rectangle_area(5,7)

#7
def simple_interest(p,t_in_years,r=9):
   interest=p*r*t_in_years
   print("Simple interest is:",interest)
simple_interest(5000,1)

#8
def power_of_number(n,p=2):
    required_value=n**p
    print("The power of number is:",required_value)
power_of_number(5)

#13
s=lambda n:n*n
print(s(int(input("enter a no:"))))

#16
n=[1,2,3,4,5,6]
m=list(map(lambda a:a*a,n))
print(m)

#17
n=[1,4,9,16,25,36,49,64,81,100]
m=list(filter(lambda a:a%2!=1,n))
print(m)

#18
n=[1,8,27,64,125,216,343,512,729,1000]
m=list(filter(lambda a:a>100,n))
print(m)

#20
def fibonacci_series(N):
    if N==0:
        return 0
    if N==1:
        return 1
    else:
        return fibonacci_series(N-2)+fibonacci_series(N-1)
N=int(input("Enter no of terms:"))
for i in range(N):
    print(fibonacci_series(i),end="")

#19
x=int(input("enter base:"))
y=int(input("enter exponent:"))
def power(x,y):
    if y==1:
        return x
    else:
        return x*power(x,y-1)
print(power(x,y))

#14
a=int(input("Enter no:"))
b=int(input("Enter no:"))
L=lambda a,b:a if a>b else b
print(L(a,b))

#15
c=[0,5,10,15,20]
f=list(map(lambda t:t*(9/5)+32,c))
print("Temperature in fahrenheit is:",f)

#4
a=int(input("Enter no:"))
b=int(input("Enter no:"))
c=int(input("Enter no:"))
def max(a,b,c):
    if a>b and a>c:
        return(a)
    elif b>c and b>a:
        return(b)
    else:
        return(c)
p=max(a,b,c)
print(p)'''




