# -------------------------------------------------------------------------------------------------------------------------------------------------
# program 1-Even or Odd Checker
# -------------------------------------------------------------------------------------------------------------------------------------------------
Number =int(input("enter the number:"))
if Number % 2 == 0 :
    print(Number,"is an even number")
else:
    print(Number,"is an odd number")
# ______________________________________________________________________________________________________________________________________________
# Program 2- Positive, Negativi or zero
# ------------------------------------------------------------------------------------------------------------------------------------------------
number = int(input("enter the number:"))
if number >0:
    print(number,"is positive")
elif number <0:
    print(number,"is negative")
else:
    print("number is Zero")
#------------------------------------------------------------------------------------------------------------------------------------------------
# program 3- Largest of two numbers
#------------------------------------------------------------------------------------------------------------------------------------------------
number1 = int(input("enter the first number:"))
number2 = int(input("enter the second number:"))
if number1 > number2:
    print(number1,"is largest number")
elif number1<number2:
    print(number2,"is the largest number")
else:
    print("number1 is equal to number2")
# ------------------------------------------------------------------------------------------------------------------------------------------------
# program 4- largest of three numbers
# ------------------------------------------------------------------------------------------------------------------------------------------------
n1= int(input("enter 1st number:"))
n2= int(input("enter 2nd number:"))
n3= int(input("enter 3rd number:"))
if n1>n2 and n1>n3:
    print(n1,"is the largest")
elif n1<n2 and n2>n3:
    print(n2,"is the largest")
elif n3>n1 and n3>n2:
    print(n3,"is the largest")
elif n1==n2 and n1>n3:
    print(n1,"and",n2,"are equal and largest")
elif n1<n2 and n2==n3:
    print(n2,"and",n3,"are equal and largest")
elif n1==n3 and n1>n2:
    print(n1,"and",n3,"are equal and largest")
else:
    print("All numbers are equal")

# ------------------------------------------------------------------------------------------------------------------------------------------------
# program 5-grade calculator
# ------------------------------------------------------------------------------------------------------------------------------------------------
marks= int(input("Enter the marks:"))
if 90<= marks<=100:
    print("grade A")
elif 75<= marks <=89:
    print("Grade B")
elif 50<= marks <=74:
    print("Grade C")
elif 35<= marks <= 49:
    print("Grade D")
elif 0> marks or 100<marks:
    print("invalid marks")
else:
    print("fail")
#--------------------------------------------------------------------------------------------------------------------------------------------------
# program 6- Leap Year Checker
# -------------------------------------------------------------------------------------------------------------------------------------------------
year = int(input("Enter the year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("leap year")
else:
    print("not a leap year")
# -------------------------------------------------------------------------------------------------------------------------------------------------
# program 7- simple calculator
# ------------------------------------------------------------------------------------------------------------------------------------------------
n1 = int(input("Enter 1st number:"))
n2 = int(input("Enter 2nd number:"))
ao = input("Enter Arithmatic Operator:")
if ao =="*":
    print(n1*n2)
elif ao =="/" and n2!=0:
    print(n1/n2)
elif ao=="/" and n2==0:
    print("cannot divided by zero")
elif ao=="+":
    print(n1+n2)
elif ao=="-":
    print(n1-n2)
else:
    print("Invalid Operator")

# --------------------------------------------------------------------------------------------------------------------------------------------------
# program 8- Vowel or consonent Checker
# -------------------------------------------------------------------------------------------------------------------------------------------------
alp = input("Enter a letter:")
if len(alp)!=1:
    print("Invalid input")
elif alp.isdigit():
    print("input is digit")
elif not alp.islower():
    print(" Enter lowercase letter")
elif alp.isalpha() and (alp == "a" or alp== "e" or alp== "i" or alp== "o" or alp== "u"):
    print("letter is Vowel")
elif alp.isalpha() and alp != "a" and alp != "e" and alp != "i" and alp != "o" and alp !="u":
    print("letter is consonent")
else:
    print("Invalid input")
# -------------------------------------------------------------------------------------------------------------------------------------------------
#  program-9 Even or Odd (user input version)
# -------------------------------------------------------------------------------------------------------------------------------------------------
number = input(" Enter the number:")
if number.isdigit():
    n1=int(number)
    if n1 %2 ==0:
        print(n1,"is even")
    else:
        print(n1,"is Odd number")
else:
    print("Invalid Input")
# 
# -------------------------------------------------------------------------------------------------------------------------------------------------
# program-10 Password Strength checker
# -------------------------------------------------------------------------------------------------------------------------------------------------
password = input("Enter the password:")
if len(password)==0:
    print("invalid input")
elif len(password)>=8:
    print("Strong password")
else:
    print("Weak password")