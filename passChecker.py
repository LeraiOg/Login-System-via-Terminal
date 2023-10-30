

#A Simple Password Validator
import time
import credentials
print("If you have an account already press 1")
if int(input()) == 1:
 print("Enter your username")
if input() == credentials.user():
 print("Enter your password to gain access to Caution Club Administrator Panel")
if input() == credentials.passP():
    time.sleep(2)
    print("Logged in as " + credentials.user())
else:
    print("Password or Username Incorrect!")
