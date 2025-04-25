#prompts user to enter any number
number = int(input("Enter any number: "))

#checks and outputs if number is even or odd
if number % 2 == 0:
    print(number, "is an even number")

else:
    print(number, "is an odd number")
