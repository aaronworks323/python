#for loops - execute a block of code a fixed number of times
#you can iterate over a range, string, sequence, etc.


for x in range(1, 20, 2):
    print(x)


name = "parker"
for letter in name:
    print(letter)


array = ["aaron", "ruby", "parker"]
for name in array:
    print(name)

new_array = ["hey", "hello", "bonjour"]
for salutation in new_array:
    if salutation == "hello":
        continue
    else:
        print(salutation)





groceries = ["apples", "mangoes", "chocolates", "cereals"]
for item in groceries:
    print(item)

user_input = input("Enter your item: ")
while user_input not in groceries:
    print(f"{user_input} is not available")
    user_input = input("Enter your item: ")

print(f"Your item is {user_input}")



import time

user_input = int(input("Enter the time in seconds: "))
for seconds in reversed(range(0, (user_input + 1))):
    time.sleep(1)
    print(seconds)

print("Happy New Year")



    







