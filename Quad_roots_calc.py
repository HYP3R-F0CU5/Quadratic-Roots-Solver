import math

a = int(input("Please enter value a (ax^2 + bc + c): "))
b = int(input("Please enter value b (ax^2 + bc + c): "))
c = int(input("Please enter value c (ax^2 + bc + c): "))

discrim = math.sqrt(( b ** 2 + (-4*a*c) ))
print(discrim)
ans1 = (-b + discrim) / (2*a)
ans2 = (-b - discrim) / (2*a)
print(ans1, ans2)
