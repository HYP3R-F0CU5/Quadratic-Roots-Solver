import math
a = int(input("Please enter value a (ax^2 + bc + c): "))
b = int(input("Please enter value b (ax^2 + bc + c): "))
c = int(input("Please enter value c (ax^2 + bc + c): "))
discrim = ( b ** 2 + (-4*a*c) )
if discrim < 0:
    discrim = math.sqrt((discrim / -1))
    print(str(-b / (2*a)) + " +/- " + (str(discrim / (2*a)) + "i"))
else:
    print((-b + discrim) / (2*a), (-b - discrim) / (2*a))
