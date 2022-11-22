"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum =(n)(n + 1) / 2
"""
sayı = int(input("Lütfen sayı giriniz:"))
toplam = ((sayı)*(sayı + 1)) / 2
toplam = int(toplam)

print("Sayınız: {}, 1'den sayınıza kadar olan sayıların toplamı: {}".format(sayı,toplam))