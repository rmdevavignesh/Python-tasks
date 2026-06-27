'''#task 5
#list
#1
students=["deva","kiran","nateesh","tharun"]
print(students)

#2
students=["deva","kiran","nateesh","tharun"]
print(students.append("kavin"))
print(students)

#3
students=["deva","kiran","nateesh","tharun"]
print(students.remove("tharun"))
print(students)

#4
students=["deva","kiran","nateesh","tharun"]
for i in students:
    print(i)

#5
n=[6,12,18,24,30]
print("largest no is:",max(n))
print("smallest no is:",min(n))

#7
n=[1,3,2,5,4]
print(n.reverse())
print(n)

#8
n=[5,3,4,1,2]
print(n.sort())
print(n)

#9
n=[1,2,3,4,5,6,7,8,9]
S=sum(n)
A=S/len(n)
print("the sum is",S)
print("the average is",A)

#10
n=[5,10,15,20,25]
a=int(input("enter a no:"))
if a in n:
    print("element is present in list")
if a not in n:
    print("element is not present in list")

#tuple
#1
numbers=(2,4,6,8,10)
print(numbers)

#2
n=(2,4,6,8,10)
print(n[0])
print(n[1])
print(n[2])

#3
w=('red','orange','blue','white','pink')
print(len(w))

#4
w=('red','orange','blue','white','pink')
print(w.count('red'))

#5
w=('red','orange','blue','white','pink')
print(w.index("blue"))

#7
t=(1,2,3,4,5)
l=list(t)
print(l)

#8
l=[1,2,3,4,5]
t=tuple(l)
print(t)

#9
n=(20,40,60,80,0)
print("maximum value is:",max(n))
print("minimum value is:",min(n))

#10
fruit=("apple","banana","orange")
for i in fruit:
    print(i)

#6
fruit=("apple","banana","orange","strawberry")
print(fruit[0:2])

#set
#1
n={3,6,9,12,15}
print(n)

#2
n={4,16,32,64,256}
print(n.add(128))
print(n)

#3
n={7,14,21,28}
print(n.remove(7))
print(n)

#4
A={1,2,3,4,5}
B={1,3,5,6}
print(A|B)

#5
A={1,2,3,4,5}
B={1,3,5,6}
print(A&B)

#6
A={1,2,3,4,5}
B={1,3,5,6}
print(A^B)

#8
A={1,2,3,4,5}
B={1,3,5,}
print(A<=B)
print(A>=B)
print(B.issubset(A))
print(B.issuperset(A))

#10
l=['red','blue','green']
s=set(l)
print(s)

#7
l=['red','blue','green','red','blue']
s=set(l)
print(s)

#dictionary
#1
student={"name":"deva","marks":92}
print(student)

#2
student={"name":"deva","marks":92}
student["course"]="python"
print(student)

#3
student={"name":"deva","marks":92}
student["name"]="DEVA"
print(student)

#4
student={"name":"deva","marks":92}
student.pop("name")
print(student)

#5(a)
student={"name":"deva","marks":92,"course":"python"}
print(student.items())

#5(b)
student={"name":"deva","marks":92}
print(student.keys())
print(student.values())'''

