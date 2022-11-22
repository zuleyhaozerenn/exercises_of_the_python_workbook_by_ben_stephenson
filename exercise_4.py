"""
Create a program that reads the length and width of a farmer’s field from the user in
feet. Display the area of the field in acres.
Hint: There are 43,560 square feet in an acre.
"""

genişlik = float(input("Tarla genişliği(fit):"))
uzunluk = float(input("Tarla uzunluğu(fit):"))

dönüm = (genişlik * uzunluk) / 43560

print("Tarlanın dönümü: ",dönüm)
