#logical operators allow us to evaluate multiple conditions
# or, and, not.

#or = atleast one condition must be True
#and = both conditions must be True
#not = inverts the conditon (not False, not True)


money = 60
car_available = False

if money <= 1000 or car_available:
    print("Event is cancelled")
else:
    print("Event is scheduled")



#and
friends = False
money = 5000

if friends and money >= 5000:
    print("Event is scheduled")
else:
    print("Event is cancelled")



temp = 20
is_snowing = True

if temp <= 20 and not is_snowing:
    print("Event is scheduled")
else:
    print("Event is cancelled")