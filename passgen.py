import random
import string

password_length = int(input("Enter the desired length of the password: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(password_length))


print("Generated Password:", password)
 
