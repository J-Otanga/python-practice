#Prompts user to enter a number
n = int(input("Enter any number: "))

#Stores the original number for printing at the end
original = n

sum = 0

while n > 0:
    #fetch the last digit and store it in dig
    dig = n % 10
    #the last digit is added to the sum and stored in the "new sum"
    sum += dig
    #the last digit is removed from 'n'
    n = n // 10

#output
print("The sum of the digits of", original ,"is",sum)




