

#A Simple Password Validator
import time
import credentials
print("Enter your Username")
if input() == credentials.user():
 print("Enter your password to gain access to Caution Club Administrator Panel")
if input() == credentials.passP():
    time.sleep(2)
    print("Logged in as " + credentials.user())
else:
    print("Password or Username Incorrect!")