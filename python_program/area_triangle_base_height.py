#Find area of triangle with base and height

base = float(input("Enter the base "))
height = float(input("Enter the height "))

if base > 0 and height > 0:
    area = (1/2) * base * height
    print(f"Area is {area:.2f}")
else:
    print("enter postive numbers")