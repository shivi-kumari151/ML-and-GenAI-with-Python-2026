# Q1. Find Area of Rectangle

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = length * width

print("Area of Rectangle =", area)


# Q2. Find Simple Interest
# Formula: SI = (P * R * T) / 100

principal = float(input("\nEnter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)


# Q3. Convert Celsius to Fahrenheit
# Formula: F = (C * 9/5) + 32

celsius = float(input("\nEnter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


# Q4. Calculate Average of 3 Numbers

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)


# Q5. Find Square and Cube of a Number

number = float(input("\nEnter a number: "))

square = number ** 2
cube = number ** 3

print("Square =", square)
print("Cube =", cube)

# Q6. Swap Two Numbers Without Third Variable

a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))

print("Before Swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("After Swapping:")
print("a =", a)
print("b =", b)

# Q7. Student Report Program

# Taking student details as input
student_name = input("\nEnter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Taking marks of three subjects
mark1 = float(input("Enter marks in Subject 1: "))
mark2 = float(input("Enter marks in Subject 2: "))
mark3 = float(input("Enter marks in Subject 3: "))

# Calculating total marks
total = mark1 + mark2 + mark3

# Calculating percentage
percentage = total / 3

# Displaying student report
print("\n STUDENT REPORT ")
print("Student Name :", student_name)
print("Roll Number  :", roll_no)
print("Subject 1 Marks :", mark1)
print("Subject 2 Marks :", mark2)
print("Subject 3 Marks :", mark3)
print("Total Marks :", total)
print("Percentage  :", percentage, "%")