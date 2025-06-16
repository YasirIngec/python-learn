# Koşullu ifadeler, bir duruma göre farklı işlemler yapmak için kullanılır.
# if, elif ve else blokları ile kurulur.

# Temel kullanım
sayi = 10
if sayi > 0:
    print("Sayı pozitiftir.")
elif sayi < 0:
    print("Sayı negatiftir.")
else:
    print("Sayı sıfırdır.")

# Birden fazla koşul kontrolü
not_ort = 75
if not_ort >= 90:
    print("Harf Notu: AA")
elif not_ort >= 80:
    print("Harf Notu: BA")
elif not_ort >= 70:
    print("Harf Notu: BB")
else:
    print("Kaldınız.")

# Nested (iç içe) if yapısı
yas = 20
if yas >= 18:
    ehliyet_var = True
    if ehliyet_var:
        print("Araç kullanabilirsiniz.")
    else:
        print("Ehliyetiniz yok.")
else:
    print("Yaşınız yetmiyor.")

# Hatalı kullanım örneği
try:
    deger = input("Bir sayı girin: ")
    if int(deger) > 100:
        print("100'den büyük.")
    else:
        print("100 veya daha küçük.")
except ValueError:
    print("Geçersiz giriş! Sayı girilmelidir.")

# Gerçek senaryo: Kullanıcının sisteme giriş yapabilmesi
kullanici = input("Kullanıcı adı: ")
sifre = input("Şifre: ")
if kullanici == "admin" and sifre == "1234":
    print("Giriş başarılı.")
else:
    print("Kullanıcı adı veya şifre hatalı.")
