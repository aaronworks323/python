# in linx user-names can't start with a digit (123user), letters + digits are fine, all digits are not allowed.
# while loop programs
import subprocess

user_name = input("Enter your username: ")
while user_name == "" or user_name.isdigit():
    print("Incorrect user-name format. Try again !!")
    user_name = input("Enter your username: ")

subprocess.run(["sudo", "useradd", user_name])
subprocess.run(["sudo", "passwd", user_name ])
print(f"User {user_name} created succesfully")



number = int(input("Enter a numner between 1 to 10: "))
while number > 10 or number < 1:
    print("Invalid range")
    number = int(input("Enter a number between 1 to 10: "))

print(f"Your number is {number}")