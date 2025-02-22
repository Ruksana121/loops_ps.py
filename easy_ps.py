# Conditional statements essay level
# 1)check whether number is positive and negative and zero 
num=int(input("enter a number:"))
if num>0:
    print(num, "is positive")
elif num<0:
    print(num, "is negative number")
else:
    print(num, "is equal to zero")
# 2)even or add
num1=int(input("Enter a number:"))
if num1%2==0:
    print({num1}, "is even")
else:
    print({num1}, "is odd")
# 3)eligible to vote (age >= 18)
age=int(input("enter age:"))
if(age>=18):
    print("eligible to vote")
else:
    print("not eligible to vote")
marks=int(input("enter a number:"))
if marks>90:
    print("Grade A")
elif marks>=80 and marks<=89:
    print("Grade B")
elif marks>=70 and marks<=79:
    print("Grade C")
else:
    print("Fail")
# 3)find the greatest of two numbers
first_num=int(input('Enter first number :'))
secod_num=int(input('Enter second number :'))
if first_num>secod_num:
    print(first_num, "is greater")
else:
    print(secod_num, "is greater")
# 4)"Pass" if a student scores more than 40 marks; otherwise, print "Fail."
std_marks=int(input("Enter marks:"))
if std_marks>40:
    print("Pass")
else:
    print("Fail")
# 4)Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).
day=int(input("enter a day:"))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thrusday")
elif day==5:
    print("Firday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Enter valid day")
# 5)Implement a simple calculator to perform addition, subtraction, multiplication, and division.
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
operator=input("enter opertaor:")
if operator=='+':
    print(num1+num2)
elif operator=='-':
    print(num1-num2)
elif operator=='*':
    print(num1*num2)
elif operator=='/':
    print(num1/num2)
else:
    print("valid operator")
# Loops easy level
# i. Print all numbers from 1 to 100 using a for loop.
for i in range(1,101):
    print(i, end=" ")
# ii. Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
n=int(input("Enter number : "))
sum=0
for i in range(1, n+1):
    sum=sum+i
print(sum)
# (or)
n=int(input("Enter number : "))
sum=0
sum=int(n*(n+1)/2)
print(sum)
# iii. Print all even numbers between 1 and 50 using a while loop.
i=1
while(i<=50):
    if(i%2==0):
        print(i)
    i=i+1
# Write a program to calculate the factorial of a number using a while loop.
n=int(input("Enter number: "))
i=1
res=1
while(i<=n):
    res=res*i
    i=i+1
print(res)
# 4)iv. Write a program to display the multiplication table of a given number. First 20
num=int(input("Enter table number you want:" ))
for i in range(1,21):
    res=num*i
    print(num,"*",i,"=",res)

