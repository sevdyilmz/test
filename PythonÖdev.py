PythonÖdev
1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

boy = float(input("Lütfen boyunuzu giriniz: \n"))
agirlik = float(input("LÜtfen kilonuzu giriniz: \n"))
vki = float(agirlik / (boy * boy))
print("Vücut kitle indeksiniz:", vki)


2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

maas = float(input("Maaşınızı giriniz: \n"))
zamOrani = float(input("Zam oranı giriniz: \n"))
zamliMaas = float(maas * zamOrani / 100 + maas)
print(zamliMaas)


3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

birinciSayi = int(input("Lütfen birinci sayıyı girin: \n"))
ikinciSayi = int(input("Lütfen birinci sayıyı girin: \n"))
ucuncuSayi = int(input("Lütfen birinci sayıyı girin: \n"))
Maxnum=max(birinciSayi, ikinciSayi, ucuncuSayi)
print("En büyük değer:", Maxnum)


4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

pi = 3.14
daireYaricapi = float(input("Lütfen değer giriniz: \n"))

daireAlan = pi * (daireYaricapi * daireYaricapi)
daireCevre = 2 * (pi * daireYaricapi)

print(daireAlan)
print(daireCevre)

5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
sayi = input("Lütfen bir sayi girin: ")
ters_sayi = sayi[::-1]
if sayi == ters_sayi:
    print("Girdiğiniz sayi bir palindromdur.")
else:
    print("Girdiğiniz sayi bir palindrom değildir.")