# collection = single "variable" used to store multiple values
# lists = [] ordered and changeable, DUPLICATES ARE OK
# SET = {} unordered and immutable, but add/remove OK. No Duplicates
# tuple = () ordered and unchangeable. Duplicates OK. Faster

cars = ["lambo", "ferrari", "rolls-royce", "tesla"]
print(cars)

#dir(cars) #print this - print(dir(cars))
#help(cars) #print(help(cars))

#print(len(cars))
#print("honda" in cars) - we can use the "in" operator to check if an element is present within a list

print(cars[1])
print(cars[3])
print(cars[0])

print(cars[::2])#prints every second element
print(cars[::-1]) #reverse the list
print(cars[:3]) #:3 is exclusive, so it prints elements till the 2nd one.

for car in cars:
    print(car)


cars[0] = "honda"
print(cars)

cars.append("hyundai")
print(cars)

cars.append("honda") #adds elements at the end of the list
print(cars)

cars.remove("honda")
print(cars) #removes "honda" indexed at [0]

cars.insert(0, "honda")
print(cars)


print(cars.index("tesla"))

print(cars.count("honda"))

 