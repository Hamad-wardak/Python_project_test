'''Mathematical quadruple operations  whit if elif and else function and for prime and non prime numbers we use the
modula method '''
print("Hallo, that is a calculator:")
print("Please choose one of the following operations:")
print("Addition (A), Subtraction(S), Multiplication(M), Division (D)")
operation: str = input()

is_valid: bool = True
print(is_valid)
if operation == "A":
    print("You have chosen Add")
    print("Please enter two numbers to Addition:")
    number1 = int(input())
    number2 = int(input())
    print(number1 + number2)

elif operation == "S":
    print("You have chosen Subtraction ")
    print("Please enter two numbers to subtraction:")
    number1 = int(input())
    number2 = int(input())
    print(number1 - number2)

elif operation == "M":
    print("You have chosen Multiplication ")
    print("Please enter two numbers to Multiplication:")
    number1 = int(input())
    number2 = int(input())
    print(number1 * number2)
elif operation == "D":
    print("You have chosen Division. ")
    print("Please enter two number to Division:")
    number1 = float(input())
    number2 = float(input())
    print(number1 / number2)
else:
    print("your tasks is finished!")
    is_valid = False
print(is_valid)
if is_valid:

    operation: float = float(input("Enter the result:"))
    if operation < 10:
        print("You don't win because the result is less than 10.")
    else:
        print("You won because the result is more than 10.")
    # I only want to show even or odd numbers here, but I don't know.
    print("Please enter the result again:")
    number_even = int(input())
    if 10 % 2 == 0:  # modulo
        print("Even yuhju")  # Even
    else:
        print("add oh oh")  # Odd
    print("this program is finished!")
else:
    print("The program will now close. Bye")

''' by def function we build calculator for mathematical quadruple operation and we use also Global . But in general 
that methode means  recursion '''

# we are making a calculator today, but this is beginner.
# first we do addition:
def addtion(a, b):
    Resualt = a + b
    return Resualt
Resualt = addtion(3, 7)
print(Resualt)
# in second step we make multiflaction together.
def multaflaction(a, b):
    Result = a - b
    return Result
Result = multaflaction(4, 3)
print(Result)
# In third step we make division together:
def deviesion(a, b):
    Resulat = a / b
    return Resulat
Resulat = deviesion(9, 3)
print(Resulat)
# we builden new python function
# def add(x, y):
#    return x + y

input_number = 6
def add_two():
    """ this function is always adding 2 to the input number"""
    global input_number
    input_number = input_number + 2
    return input_number
print(input_number)
print(add_two())
print(input_number)
print(add_two())
print(input_number)






