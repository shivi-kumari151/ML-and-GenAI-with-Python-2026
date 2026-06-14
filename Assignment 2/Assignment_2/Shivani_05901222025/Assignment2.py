# Q1. Find Sum of First 10 Natural Numbers

sum_numbers = 0

for i in range(1, 11):
    sum_numbers += i

print("Sum of first 10 natural numbers =", sum_numbers)


# Q2. Find Factorial of a Number

num = int(input("\nEnter a number to find factorial: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial of", num, "=", factorial)


# Q3. Print Fibonacci Series

n = int(input("\nEnter the number of terms for Fibonacci Series: "))

first = 0
second = 1

print("Fibonacci Series:")

for i in range(n):
    print(first, end=" ")
    next_term = first + second
    first = second
    second = next_term

print()


# Q4. Find Largest Among 3 Numbers

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest number is =", largest)


# Q5. Student Result System

# Input Student Details
print("\n STUDENT RESULT SYSTEM ")

student_name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Input Number of Subjects
num_subjects = int(input("Enter number of subjects: "))

total_marks = 0

# Loop to Input Marks
for i in range(1, num_subjects + 1):
    marks = float(input(f"Enter marks for Subject {i}: "))
    total_marks += marks

# Calculate Percentage
percentage = total_marks / num_subjects

# Determine Grade using if-elif-else
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

# Display Result
print("\n RESULT ")
print("Student Name :", student_name)
print("Roll Number  :", roll_no)
print("Total Marks  :", total_marks)
print("Percentage   :", round(percentage, 2), "%")
print("Grade        :", grade)

if grade == "F":
    print("Result       : Fail")
else:
    print("Result       : Pass")