# Python'da modüller, fonksiyonları ve sınıfları bir dosyada toplayarak tekrar kullanılabilir hale getirmeye yarar.
# Dahili (gömülü) modüller ve harici (kurulabilir) modüller vardır.

# import modül_adı → tüm modülü içeri alır
# from modül_adı import öğe → sadece gerekli olanı alır
# as → takma ad (alias) verir

# math modülü ile matematiksel işlemler
import math

print("Pi sayısı:", math.pi)
print("Karekök:", math.sqrt(16))
print("Sinüs(0):", math.sin(0))

# random modülü ile rastgele değer üretme
import random

print("1-10 arası rastgele sayı:", random.randint(1, 10))
liste = ["elma", "muz", "kiraz"]
print("Rastgele meyve:", random.choice(liste))

# datetime modülü ile tarih-saat işlemleri
import datetime

simdi = datetime.datetime.now()
print("Şu an:", simdi)
print("Yıl:", simdi.year, "Ay:", simdi.month, "Gün:", simdi.day)

# from ile sadece bir kısmını alma
from math import pow, ceil

print("3^2:", pow(3, 2))
print("3.4 yukarı yuvarla:", ceil(3.4))

# as ile takma ad verme
import statistics as ist

veriler = [60, 70, 80, 90]
print("Ortalama:", ist.mean(veriler))

# Hatalı kullanım: Olmayan modülü import etmek
try:
    import bilinmeyen_modul
except ModuleNotFoundError as e:
    print("Modül hatası:", e)

# Gerçek senaryo: Günün rastgele bir saatini oluşturmak
saat = random.randint(0, 23)
dakika = random.randint(0, 59)
print(f"Rastgele saat: {saat:02}:{dakika:02}")
