#Prompt user to enter a word
word = input("Enter a word: ")

#empty string to store the reversed word

reversedWord = ""

#Iterate through each letter in the original word

for letter in word:
    #Add each new letter taken, to the front of the reversed word
    reversedWord = letter + reversedWord

#Output the reversed word
print("The reversed word for ", word , "is",reversedWord)