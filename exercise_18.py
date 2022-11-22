"""
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s^2.
You can use the formula vf =(vi^2 + 2ad)^1/2 to compute the final speed, vf
when the initial speed, vi, acceleration, a, and distance, d, are known.
"""

d = int(input("Lütfen nesnenizi düşürdüğünüz yüksekliği metre cinsinden giriniz: "))

a = 9.8
vi = 0

vf = ((vi ** 2 ) + (2 * a * d)) ** (1/2)

print("Nesnenizin hızı : {} m/s".format(vf))