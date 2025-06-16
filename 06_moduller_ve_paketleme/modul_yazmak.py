# Python'da kendi modülümüzü oluşturarak, fonksiyonlarımızı ve verilerimizi farklı dosyalarda tekrar kullanabiliriz.
# Modül: Bir Python dosyasıdır (.py uzantılı), içinde fonksiyonlar, değişkenler, sınıflar olabilir.

# 1. Örnek modül dosyası: hesap.py
# Bu dosyada şunlar olabilir:
# def topla(a, b):
#     return a + b

# def carp(a, b):
#     return a * b

# 2. Bu dosyada modülü kullanıyoruz:
import hesap  # aynı klasörde olmalı

print("Toplam:", hesap.topla(3, 5))
print("Çarpım:", hesap.carp(2, 4))

# 3. Belirli fonksiyonları import etmek
from hesap import topla

print("Sadece toplama:", topla(10, 20))

# 4. Takma adla kullanmak
import hesap as hsp

print("Alias ile çarpım:", hsp.carp(6, 7))

# Hatalı kullanım: Modül yoksa
try:
    import olmayan_modul
except ModuleNotFoundError as e:
    print("Modül bulunamadı:", e)

# Gerçek kullanım: hesap.py içinde 4 işlem fonksiyonu tanımlayıp burada kullanmak
# hesap.py içeriği:
# def bol(a, b):
#     if b == 0:
#         return "Tanımsız"
#     return a / b
#
# def fark(a, b):
#     return a - b

print("Fark:", hesap.fark(10, 3))
print("Bölme:", hesap.bol(8, 2))
