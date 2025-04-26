#prompts user to enter any number
number = int(input("Enter any number: "))

def fact(number):
    if(number == 0):
        return 1
    return number * fact(number - 1)
result = fact(number)

print("The factorial of", number , "is", result )
