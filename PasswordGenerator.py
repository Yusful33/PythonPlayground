#Password Generator
#Write a programme, which generates a random password for 
#the user. Ask the user how long they want their password to 
#be, and how many letters and numbers they want in their password. 
#Have a mix of upper and lowercase letters, as well as numbers and symbols. 
#The password should be a minimum of 6 characters long.
import random
import string
#below gives you all letters in the alphabet (upper and lower case)
string.ascii_letters 
#Asks the users how many characters the password should be
characters = input("How many total characters would you like your password to be?")
characters = int(characters)
letters = int(input("How many of those characters should be letters?"))
numbers = int(input("Would you like the password to include numbers?"))
special = int(input("Would you like the password to include any special characters?"))
print(special + numbers + letters)
password = letters + numbers + special
if characters == password:
    def randomLetters(stringLength=letters):
    #This new password will include letters, numbers and special characters 
        password_characters = string.ascii_lowercase 
        return ''.join(random.choice(password_characters) 
                   for i in range(stringLength))
    def randomNums(numLength=numbers):
        num_characters = string.digits
        return ''.join(random.choice(num_characters)
                       for i in range(numLength))
    def randomChar(numChar=special):
        num_special = string.punctuation
        return ''.join(random.choice(num_special)
                       for i in range(numChar))
        # the sep='' allows there to not be any spaces between each function when it prints out
    print("Here is your new password is: ", randomLetters(), randomNums(), randomChar(), sep='')
else:
    print("Please ensure that your inputs are in alignment and try again")