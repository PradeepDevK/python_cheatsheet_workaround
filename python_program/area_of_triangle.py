import math

a = float(input("Enter length of the side a: "))
b = float(input("Enter length of the side b: "))
c = float(input("Enter length of the side c: "))

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"Area of a triangle is {area:.2f}")