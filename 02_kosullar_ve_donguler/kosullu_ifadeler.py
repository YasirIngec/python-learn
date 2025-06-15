# Kullanıcının girdiği sayıya göre pozitif, negatif veya sıfır olduğunu kontrol ederiz.

sayi = int(input("Bir sayı girin: "))

if sayi > 0:
    print("Pozitif sayı")
elif sayi < 0:
    print("Negatif sayı")
else:
    print("Sıfır")
