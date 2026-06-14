# Q1. Function to Print First 10 Natural Numbers

def print_natural_numbers():
    print("First 10 Natural Numbers:")
    for i in range(1, 11):
        print(i, end=" ")
    print()


print_natural_numbers()

# Q2. Function to Calculate Sum of First N Natural Numbers

def sum_natural_numbers(n):
    return n * (n + 1) // 2


n = int(input("\nEnter N: "))
print("Sum of first", n, "natural numbers =", sum_natural_numbers(n))

# Q3. Function to Reverse a Number

def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse


num = int(input("\nEnter a number to reverse: "))
print("Reversed Number =", reverse_number(num))

# Q4. Function to Count Digits in a Number

def count_digits(num):
    count = 0

    if num == 0:
        return 1

    while num > 0:
        count += 1
        num = num // 10

    return count


num = int(input("\nEnter a number: "))
print("Number of digits =", count_digits(num))


# Q5. Function to Check Palindrome Number

def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return original == reverse


num = int(input("\nEnter a number to check palindrome: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# Q6. Function to Generate Fibonacci Series

def fibonacci_series(n):
    a = 0
    b = 1

    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

    print()


terms = int(input("\nEnter number of Fibonacci terms: "))
fibonacci_series(terms)


# Q7. Calculator Using Functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


print("\n===== CALCULATOR =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Select operation (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))

elif choice == 2:
    print("Result =", subtract(num1, num2))

elif choice == 3:
    print("Result =", multiply(num1, num2))

elif choice == 4:
    if num2 != 0:
        print("Result =", divide(num1, num2))
    else:
        print("Cannot divide by zero")

else:
    print("Invalid Choice")

# Q8. Create a Text File and Store Student Details

file = open("student.txt", "w")

name = input("\nEnter Student Name: ")
roll = input("Enter Roll Number: ")
marks = input("Enter Marks: ")

file.write("Name: " + name + "\n")
file.write("Roll No: " + roll + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("Student details stored in student.txt")


# Q9. Read Data from a File

print("\nReading data from file:")

file = open("student.txt", "r")

content = file.read()
print(content)

file.close()


# Q10. Handle Division by Zero Using Exception Handling

try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))

    result = a / b

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# Q11. Create a Student Class with Name and Marks

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Name :", self.name)
        print("Marks:", self.marks)


student_name = input("\nEnter Student Name for Class: ")
student_marks = float(input("Enter Marks: "))

student1 = Student(student_name, student_marks)

student1.display()