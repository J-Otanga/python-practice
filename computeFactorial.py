#Prompts user to enter number
n = int(input("Enter any number: "))

factorial = 1
#Initialize counter for while loop
i = 1

if n < 0:
    print("Factorial does not exist for negative numbers")

elif n == 0:
    print("Factorial is 1")

else:
    #while 'i' is less than the number input(n), multipy i with the factorial to get new factorial
   while i <= n:
       factorial *= i
       i += 1
   #output factorial
   print("The factorial of", n , "is", factorial )



