
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
elif age <= 0:
    print("You havent been born yet")
else:
    print("You must be 18 to sign up")




#python script to create new users in linux


import subprocess

user_name = input("Enter user name: ").strip()
if user_name == "":
    print("Username cannot be blank")
else:
    subprocess.run(["sudo", "useradd", user_name])
    subprocess.run(["sudo", "passwd", user_name])
    print(f"User {user_name} created successfully")

del_user_input = input(f"Would you like to delete user {user_name} (Y/N): ").strip()
if del_user_input == "Y":
    subprocess.run(["sudo", "deluser", user_name])
elif del_user_input == "y":
    subprocess.run(["sudo", "deluser", user_name])
else:
    print("User deletion discontinued")



print("Mango")
print("Strawberry")
print("Orange")

fruits = input("Enter any fruits that you want to eat: ")
if fruits == "Mango":
    print("Mango is a great choice. Its perfect.")
elif fruits == "mango":
    print("Mango is a great choice. Its perfect.")
elif fruits == "Strawberry":
    print("Strawberry is a great choice.")
elif fruits == "strawberry":
    print("Strawberry is a great choice.")
elif fruits == "Orange":
    print("Orange is a great choice.")
elif fruits == "orange":
    print("Orange is a great choice.")
else:
    print("Well, thats ok")

"""

operator = input("Enter an operator (+ - * /): ")
number1 = float(int(input("Enter the first number: ")))
number2 =  float(int(input("Enter the second number: ")))

if operator == "+":
    number3 = number1 + number2
    print(number3)
elif operator == "-":
    number3 = number1 - number2
    print(number3)
elif operator == "*":
    number3 = number1 * number2
    print(number3)
elif operator == "/":
    number3 = number1 / number2
    print(number3)
else:
    print("Your entered operator doesnt exist. Try again.")

