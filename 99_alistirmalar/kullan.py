# Bu program hesap_modulu.py içindeki fonksiyonları kullanarak hesaplama yapar

import hesap_modulu

try:
    sayi1 = float(input("1. sayıyı girin: "))
    islem = input("İşlem türü (+ - * /): ")
    sayi2 = float(input("2. sayıyı girin: "))

    if islem == "+":
        sonuc = hesap_modulu.topla(sayi1, sayi2)
    elif islem == "-":
        sonuc = hesap_modulu.cikar(sayi1, sayi2)
    elif islem == "*":
        sonuc = hesap_modulu.carp(sayi1, sayi2)
    elif islem == "/":
        sonuc = hesap_modulu.bol(sayi1, sayi2)
    else:
        sonuc = "Geçersiz işlem."

    print("Sonuç:", sonuc)

except ValueError:
    print("Lütfen sayıları doğru girin.")
