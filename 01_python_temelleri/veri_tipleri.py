# Veri Tipleri
# Python'da temel veri tipleri: int (tam sayı), float (ondalıklı), str (metin), bool (mantıksal)
# Bunlar değişkenlere değer atarken Python tarafından otomatik olarak belirlenir.

# Temel Örnekler
tam_sayi = 42
ondalikli_sayi = 3.14
metin = "Merhaba Python"
mantiksal = True

print("tam_sayi türü:", type(tam_sayi))        # <class 'int'>
print("ondalikli_sayi türü:", type(ondalikli_sayi))  # <class 'float'>
print("metin türü:", type(metin))              # <class 'str'>
print("mantiksal türü:", type(mantiksal))      # <class 'bool'>

# Orta Seviye Kullanım
# Bir değerin türünü değiştirmek (type casting)
sayi_str = "123"
sayi_int = int(sayi_str)  # string -> int
print("Toplam:", sayi_int + 7)

# str(), float(), bool() ile dönüşümler yapılabilir
print(str(3.5))      # "3.5"
print(float("5"))    # 5.0
print(bool(0))       # False

# Hatalı Kullanım
try:
    print(int("abc"))  # Hatalı dönüşüm -> ValueError
except ValueError as hata:
    print("Hata:", hata)

# Gerçek Hayattan Uygulama
# Kullanıcıdan doğum yılı al, yaşını hesapla
try:
    dogum_yili = int(input("Doğum yılınızı girin: "))
    yas = 2025 - dogum_yili
    print(f"Şu anki yaşınız: {yas}")
except ValueError:
    print("Lütfen geçerli bir yıl giriniz (sayı olmalı).")
