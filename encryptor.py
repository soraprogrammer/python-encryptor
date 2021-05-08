#!/usr/bin/env python3

import bcrypt as b

password = str(input("Enter password: ")).encode('UTF-8')
salt = b.gensalt()
hashed = b.hashpw(password, salt)
print(hashed)

print("-" * 30)
print("Login")
password2 = str(input("Enter password: ")).encode('UTF-8')
hashed2 = b.hashpw(password2, salt)

if hashed == hashed2:
	print("Ok, you passed!")
else:
	print("Nope!")

print("-" * 30)