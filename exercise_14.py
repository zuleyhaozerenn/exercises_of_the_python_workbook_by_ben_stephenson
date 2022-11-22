"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters.
"""

feet = float(input("Feet cinsinden uzunluk giriniz: "))
inch  = float(input("İnç cinsinden uzunluk giriniz: "))

cm = inch * 2.54
cm2 = feet * 30.48

print("Girdiğiniz feet değerinin cm cinsinden uzunluk ölçüsü: ",cm2)
print("Girdiğiniz inç değerinin cm cinsinden uzunluk ölçüsü: ",cm)
