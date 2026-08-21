#tuples = ()
#tuples are faster than lists, tuples are ordered and unchangeable. DUPLICATES are OK. FASTER.

tuple = ("lamborghini", "ferrari", "tesla", "bmw")
print(tuple)
print(len(tuple))
print("hello" in tuple)
# print(help(tuple))
# print(dir(tuple))

for car in tuple:
    print(car)

user_input = input("Enter your car: ")
while user_input not in tuple:
    print("Car not available.")
    user_input = input("Enter your car: ")

print(f"{user_input} is a nice choice.")

