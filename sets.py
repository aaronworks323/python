# sets are unordered and immutable 
# immutable means we cant alter them.
# no duplicates,  we can add/remove elements

set = {"red", "blue", "orange", "white"}
print(set) # the output is unordered, each time we run this program, the order changes
print(len(set))
#the values cannot be changed after assignment

# print(dir(set))
# print(help(set))

set.add("black")
print(set)

set.remove("white")
print(set)

set.add("black") # we are adding a duplicate value here
# but after printing the set, black appears only once.





