"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added
to the balance of the savings account. Write a program that begins by reading the
amount of money deposited into the account from the user. Then your program should
compute and display the amount in the savings account after 1, 2, and 3 years. Display
each amount so that it is rounded to 2 decimal places.

Yılda yüzde 4 faiz getiren yeni bir tasarruf hesabı açtığınızı farz edin.
Kazandığınız faiz yıl sonunda ödenir ve birikim hesabı bakiyesine eklenir.
Kullanıcıdan hesaba yatırılan para miktarını okuyarak başlayan bir program yazınız.
Ardından programınız 1, 2 ve 3 yıl sonra tasarruf hesabındaki tutarı hesaplamalı ve göstermelidir.
Her tutarı 2 ondalık basamağa yuvarlanacak şekilde görüntüleyin.
"""

hesaba_yatırılan = int(input("Hesabınıza yatırdığınız para miktarını giriniz: "))

faiz = hesaba_yatırılan * (4/100)

yıl_sonu_bakiyesi1 = hesaba_yatırılan + faiz
yıl_sonu_bakiyesi2 = (yıl_sonu_bakiyesi1 * (4/100)) + yıl_sonu_bakiyesi1
yıl_sonu_bakiyesi3 = (yıl_sonu_bakiyesi2 * (4/100)) + yıl_sonu_bakiyesi2

print("1. yıl sonunda hesaptaki bakiye: %.2f" % yıl_sonu_bakiyesi1)
print("2. yıl sonunda hesaptaki bakiye: %.2f" % yıl_sonu_bakiyesi2)
print("3. yıl sonunda hesaptaki bakiye: %.2f" % yıl_sonu_bakiyesi3)