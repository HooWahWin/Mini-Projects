def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")


def sub(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}")


def multi(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}")


def divi(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer}")


print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")

choice = input("Enter your operation: ")
while True:
    if choice.lower() == 'a':
        print("addition")
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        add(a, b)
        break

    elif choice.lower() == 'b':
        print("subtraction")
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        sub(a, b)
        break

    elif choice.lower() == 'c':
        print("multiplication")
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        multi(a, b)
        break

    elif choice.lower() == 'd':
        print("division")
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        divi(a, b)
        break

    else:
        print("this is not a valid operation")
        choice = input("Enter your operation: ")
