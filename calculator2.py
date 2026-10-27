def menu():
    print("Welcome to my first calculator!")
    print("Please enter two numbers to perform calculations.")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    sign = input("Enter the operation (+, -, *, /): ")
    return num1, num2, sign

def calculate(num1,num2,sign):
    if sign == "+":
        print(num1 + num2)
    elif sign == "-":
        print(num1 - num2)
    elif sign == "*":
        print(num1 * num2)
    elif sign == "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Zero cannot be divided")

def restart():
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again in ["yes", "Yes", "YES", "yEs", "yeS", "YEs", "YeS", "yES"]:
        num1,num2,sign = menu()
        calculate(num1, num2, sign)
        restart()
    elif again in ["no", "No", "NO", "nO"]:
        print("Tky for using my calculator, see ya! :) ")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        restart()

num1, num2, sign = menu()
calculate(num1, num2, sign)
restart()