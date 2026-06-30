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
print(s(int(input("enter a no:"))))'''



