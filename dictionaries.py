# dictionary =  a collection of {key: value} pairs
# ordered and changeable, no duplicates allowed


car_origins = {"Honda": "Japan",
               "Lamborghini": "Italy",
               "Ferrari": "Italy",
               "Ford": "USA"}

# print(dir(car_origins))
# print(help(car_origins))

print(car_origins.get("Honda"))

if car_origins.get("Lamborghini"):
    print("That car is from Italy")
else:
    print("That car doesnt not exist")



car_origins.update({"BMW": "Germany"}) # update the dictionary
print(car_origins.get("BMW"))

car_origins.update({"Honda": "Tokyo"}) # update the dictionary
print(car_origins.get("Honda"))

car_origins.pop("Ford") # delete a key-value pair
print(car_origins)

car_origins.popitem() # delete the latest key-value pair in the dictionary.
print(car_origins)

#car_origins.clear()
#print(car_origins) # clears the dictionary

keys = car_origins.keys() # to get all the key values of the dictionary
print(keys)

for key in keys:
    print(key)


values = car_origins.values() # to get all the values in the dictionary
print(values)

for value in values:
    print(value ,end=" ")


items =  car_origins.items()
print(items)

for item in items:
    for x in item:
        print(x ,end=" ")





