"""
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place.
"""
import math

r = int(input("Silindirinizin yarıçapı: "))
h = int(input("Silindirinizin yüksekliği: "))

volume = math.pi * h * (r ** 2)

print("Silindirinizin hacmi: %.2f" % volume)