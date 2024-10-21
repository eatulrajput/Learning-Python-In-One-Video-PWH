'''
Calculator App: Build a simple command-line calculator for basic arithmetic (addition, subtraction, multiplication, and division).
'''
print("Welcome to Basic Calculator");

# function for sum
def sum(x,y):
    return x + y

# function for difference
def difference(x,y):
    return x - y

# function for multiply
def product(x,y):
    return x * y

# function for division
def divide (x,y):
    return x/y

print("Please select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while(True):
    # Taking input from the user
    choices =  input("Please enter your choice(1/2/3/4): ")
    
    # if Choices is one out of four operations
    if choices in ('1','2','3','4'):
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second number: "))
        except ValueError:
            print("This option is not available, please enter from 1-4")
            continue

        if choices =='1':
            print(num1,"+", num2, "=", sum(num1, num2))

        elif choices =='2':
            print(num1,"-", num2, "=", difference(num1, num2))

        elif choices =='3':
            print(num1, "*", num2, "=", product(num1, num2))

        elif choices == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Checking if the user wants more calculation otherwise break the while loop

        next_calculation = input("Do you want to calculate more (Yes/ No): ")

        if next_calculation == "No":
            break

        else:
            print("Ok, we will continue the program)")






