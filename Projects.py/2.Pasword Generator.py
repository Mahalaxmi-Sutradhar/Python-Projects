#PASSWORD GENERATOR
#LEVEL 1(Unshuffled)
import random
print("Welcome to password generator.")
statement1  = int(input("Enter the no. of numbers."))
statement2 = int(input("Enter the no. of letters."))
statement3 = int(input("Enter the no. of characters."))
alphabets  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G'
,'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
characters = ['!','@','#','$','%','^','&','*','(',')']
password = ""
for i in range(statement1):
    num = random.randint(0,9)
    password = password + str(num)
for j in range(statement2):
    letter = random.choice(alphabets)
    password = password + letter
for k in range(statement3):
    char = random.choice(characters)
    password = password + char
print(f"The password is {password}")


#LEVEL 2(Shuffled)
import random
print("Welcome to password generator.")
statement1  = int(input("Enter the no. of numbers."))
statement2 = int(input("Enter the no. of letters."))
statement3 = int(input("Enter the no. of characters."))
alphabets  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G'
,'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
characters = ['!','@','#','$','%','^','&','*','(',')']
numbers = ['0','2','3','4','5','6','7','8','9']
password = []
for i in range(statement1):
    num = random.choice(numbers)
    password += num
for j in range(statement2):
    letter = random.choice(alphabets)
    password += letter 
for k in range(statement3):
    char = random.choice(characters)
    password += char
random.shuffle(password)
Password = ""
for i in password:
    Password += i
print(f"Password : {Password}")