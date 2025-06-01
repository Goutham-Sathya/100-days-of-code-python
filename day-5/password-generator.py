# Import the random module for generating random choices
import random

# Define character sets for password generation
letters = ['a','b','c','d','e','f','g','h','j','i','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z',
           'A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P','Z','X','C','V','B','N','M']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','_','-','+','=','?']

# Get user input for password composition
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Initialize an empty list to build the password
prototype = []

# Add random letters to the password prototype
for char in range(0, num_letters):
    prototype.append(random.choice(letters))

# Add random symbols to the password prototype
for char in range(0, num_symbols):
    prototype.append(random.choice(symbols))

# Add random numbers to the password prototype
for char in range(0, num_numbers):
    prototype.append(random.choice(numbers))

# Shuffle the characters to randomize the order
random.shuffle(prototype)

# Convert the list of characters into a single string
password = ""
for char in prototype:
    password += char

# Display the generated password
print(f"Your password is: {password}")