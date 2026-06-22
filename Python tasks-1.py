'''#task 1
#7
Radius=int(input("enter a no:"))
Height=int(input("enter a no:"))
Volume_of_cylinder=3.14*Height*Radius*Radius
print(Volume_of_cylinder)

#8
length=int(input("enter a no:"))
height=int(input("enter a no:"))
breadth=int(input("enter a no:"))
volume_of_cuboid=length*breadth*height
print(volume_of_cuboid)

#9
a=int(input("enter a no:"))
Number=a/100
print(Number)

#10
distance=int(input("enter a no:"))
time=int(input("enter a no:"))
speed=distance/time
print(speed)

#1
a=12345
lastdigit=a%10
print(lastdigit)

#2
b=54321
removelastdigit=b//10
print(removelastdigit)

#3
c=15625
lastdigits=c%100
print(lastdigits)

#5
weight=int(input("enter a no:"))
heightincm=float(input("enter a no:"))
BMI=weight/(heightincm/100)**2
print(BMI)

#6
a=int(input("enter a no:"))
p=a%10
q=a%100
q//=10
q*=10
r=a%1000
r//=100
r*=100
s=a
s//=1000
s*=1000
print(s,"+",r,"+",q,"+",p)

#4
no=int(input("enter a 5digit no:"))
x=no//100
number=x%10
print(number**2)'''
