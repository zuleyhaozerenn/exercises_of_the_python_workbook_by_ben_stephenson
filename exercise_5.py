"""
In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and always displays exactly two decimal places.
"""

az = 0.10
çok = 0.25

kap_sayısı1 = int(input("Lütfen 1 litre veya daha az miktarda olan içecek kabı sayısını giriniz:"))
kap_sayısı2 = int(input("Lütfen 1 litreden fazla miktarda olan içecek kabı sayısını giriniz:"))

sonuç = (az * kap_sayısı1) + (çok * kap_sayısı2)

print("Geri Ödemeniz: $%.2f" % sonuç)