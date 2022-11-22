"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.
"""
feet = float(input("Feet cinsinden uzunluk ölçüsü: "))

inch = feet / 12
yard = feet * 3
mile = 5280 * feet

print("Girdiğiniz feet ölçüsüne göe yapılan inç, yarda ve mil değişimleri aşağıda bulunmaktadır.")
print("Feet: {} , İnç: {} , Yard: {} , Mil: {}".format(feet,inch,yard,mile))
