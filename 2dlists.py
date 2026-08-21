# a 2-D list is a list made up of multiple lists

cars = ["lambo", "ferrari", "maserati"]
colors = ["green", "orange", "blue"]
names = ["bob", "parker", "jack"]

list = [cars, colors, names]
print(list)

print(list[0][0]) #[row][column]

for collection in list:
    for item in collection:
        print(item, end=" ")



num_pad = ((1, 2, 3), 
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))


for row in num_pad: # for every in row in num_pad -- which means every tuple in our 2d tuple
    for num in row: # for every num in row -- which means for every element in our tuple or 'row'
        print(num, end=" ")


