a = float(input("Please enter value a (ax^2 + bc + c): "))
b = float(input("Please enter value b (ax^2 + bc + c): "))
c = float(input("Please enter value c (ax^2 + bc + c): "))
discrim = ( b ** 2 + (-4*a*c) )
if discrim < 0:
    discrim = (discrim / -1) ** 0.5
    print(str(-b / (2*a)) + " +/- " + (str(discrim / (2*a)) + "i"))
else:
    discrim = (discrim) ** 0.5
    print((-b + discrim) / (2*a), (-b - discrim) / (2*a))
