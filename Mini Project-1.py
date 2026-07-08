#-----------------------------------QUIZ_MANIA----------------------------------#
import math
import random

#Math quiz
def math_quiz():
    print("\n---MATH QUIZ---\n")
    print("1.Easy mode")
    print("2.Moderate mode")
    print("3.Difficult mode")
    print()

    mode=int(input("Enter your choice:"))

    if mode==1:
        print("Easy mode")
        print()

        n1=random.randint(2,5)
        n2=random.randint(1,3)

        correct=math.pow(n1,n2)
        print("What is",n1,"to the power of",n2,"?")

        answer=int(input("Enter your answer:"))

        if answer==correct:
            print("\nYou are correct!")
            print("You have scored a point")
        else:
            print("\nWrong!Correct answer is",correct)
            print("No points scored")
       

    elif mode==2:
        print("Moderate mode")
        print()

        print("What is the square root of 1296?")
        opt1=["44","36","34","46"]

        i=0
        while i<len(opt1):
            print(str(i+1)+"."+opt1[i])
            i=i+1

        choice=int(input("Enter your option:"))
        answer=int(math.sqrt(1296))

        if choice==2:
            print("\nYou are correct!")
            print("You have scored a point")
        else:
            print("\nWrong!Correct answer is",answer)
            print("No points scored")
    

    elif mode==3:
        print("Difficult mode")
        print()

        n=random.randint(5,9)
        
        correct=math.factorial(n)
        print("What is the factorial of",n,"?")

        answer=int(input("Enter your answer:"))

        if answer==correct:
            print("\nYou are correct!")
            print("You have scored a point")
        else:
            print("\nWrong!Correct answer is",correct)
            print("No points scored")

    else:
        print("Invalid choice")

#Python quiz
def python_quiz():
    print("\n---PYTHON QUIZ---\n")
    print("1.Easy mode")
    print("2.Moderate mode")
    print("3.Difficult mode")
    print()

    mode=int(input("Enter your choice:"))

    if mode==1:
        print("Easy mode")
        print()

        print("Which symbol is used for comments in python?")
        opt1=["!","#","&","%"]

        i=0
        while i<len(opt1):
            print(str(i+1)+"."+opt1[i])
            i=i+1

        choice=int(input("Enter your option:"))
        answer="#"

        if choice==2:
            print("\nYou are correct!")
            print("You have scored a point")
            
        else:
            print("\nWrong!Correct answer is",answer)
            print("No points scored")

    elif mode==2:
        print("Moderate mode")
        print()

        print("Which function is used to find length of a string?")
        opt2=["size()","count()","length()","len()"]

        i=0
        while i<len(opt2):
            print(str(i+1)+"."+opt2[i])
            i=i+1

        choice=int(input("Enter your option:"))
        answer="len()"

        if choice==4:
            print("\nYou are correct!")
            print("You have scored a point")
        else:
            print("\nWrong!Correct answer is",answer)
            print("No points scored")

    elif mode==3:
        print("Difficult mode")
        print()

        print("Which loop is used when number of iterations is not known?")
        opt3=["while","for","do while","exit"]

        i=0
        while i<len(opt3):
            print(str(i+1)+"."+opt3[i])
            i=i+1

        choice=int(input("Enter your option:"))
        answer="while"

        if choice==1:
            print("\nYou are correct!")
            print("You have scored a point")
        else:
            print("\nWrong!Correct answer is",answer)
            print("No points scored")

    else:
        print("Invalid choice")

#Science quiz
def science_quiz():
    print("\n---SCIENCE QUIZ---\n")
    print("1.Easy mode")
    print("2.Moderate mode")
    print("3.Difficult mode")
    print()

    mode=int(input("Enter your choice:"))

    if mode==1:
        print("Easy mode")
        print()

        print("Which gas do humans inhale during respiration?")
        print("1.Carbon dioxide")
        print("2.Carbon monoxide")
        print("3.Oxygen")
        print("4.Nitrogen")
        print()

        choice=int(input("Enter your option:"))
        answer="Oxygen"

        if choice==3:
            print("\nYou are correct!")
            print("You have scored a point")
        else:
            print("\nWrong!Correct answer is",answer)
            print("No points scored")

    elif mode==2:
        print("Moderate mode")
        print()

        print("What is the chemical symbol for platinum?")
        print("1.Pa")
        print("2.Pt")
        print("3.Pd")
        print("4.Pu")
        print()

        choice=int(input("Enter your option:"))
        answer="Pt"

        if choice==2:
            print("\nYou are correct!")
            print("You have scored a point")
        else:
            print("\nWrong!Correct answer is",answer)
            print("No points scored")

    elif mode==3:
        print("Difficult mode")
        print()

        print("Who is known as Father of Modern Physics?")
        print("1.Isaac Newton")
        print("2.Albert Einstein")
        print("3.Nikola Tesla")
        print("4.Galileo Galilei")
        print()

        choice=int(input("Enter your option:"))
        answer="Albert Einstein"

        if choice==2:
            print("\nYou are correct!")
            print("You have scored a point")
        else:
            print("\nWrong!Correct answer is",answer)
            print("No points scored")

    else:
       print("Invalid choice")

#Main menu
def main_menu():
    while True:
        print("\n-----QUIZ GAME MAIN MENU----\n")
        print("1.MATH QUIZ")
        print("2.PYTHON QUIZ")
        print("3.SCIENCE QUIZ")
        print("4.EXIT GAME")
        print()

        choice=int(input("Enter your choice:"))

        if choice==1:
            math_quiz()
        elif choice==2:
            python_quiz()
        elif choice==3:
             science_quiz()
        elif choice==4:
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice")

#Calling the function
main_menu()

    


        

    
        

    

        
        
    
