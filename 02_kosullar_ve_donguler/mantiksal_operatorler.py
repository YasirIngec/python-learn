# Mantıksal operatörler, birden fazla koşulu birlikte değerlendirmek için kullanılır.
# and, or, not operatörleri kullanılır.

# and → Tüm koşullar True ise sonuç True olur
# or → En az bir koşul True ise sonuç True olur
# not → Koşulun tersini alır (True → False)

# and örneği
yas = 25
ehliyet_var = True

if yas >= 18 and ehliyet_var:
    print("Araç kullanabilirsiniz.")
else:
    print("Araç kullanamazsınız.")

# or örneği
hava_yagmurlu = False
semsiye_var = True

if hava_yagmurlu or semsiye_var:
    print("Dışarı çıkabilirsiniz.")
else:
    print("Ya ıslanırsın ya da eve mahkûmsun.")

# not örneği
aktif = False

if not aktif:
    print("Hesap pasif durumda.")
else:
    print("Hesap aktif.")

# Karmaşık bir mantıksal ifade
puan = 85
devamsizlik = 3

if puan >= 70 and devamsizlik <= 5:
    print("Sınıfı geçtiniz.")
else:
    print("Kaldınız.")

# Hatalı kullanım: parantezsiz karışık ifadeler
x = True
y = False
z = True

# Operatör önceliği bazen kafa karıştırabilir
print("Sonuç:", x or y and not z)  # doğru yorumlamak için parantez önerilir
# Daha okunabilir versiyon:
print("Parantezli sonuç:", (x or y) and (not z))

# Gerçek kullanım senaryosu: Basit güvenlik doğrulaması
kullanici_adi = input("Kullanıcı adı: ")
sifre = input("Şifre: ")
giris_basarili = kullanici_adi == "admin" and sifre == "1234"

if giris_basarili:
    print("Sisteme giriş başarılı.")
else:
    print("Giriş başarısız.")

