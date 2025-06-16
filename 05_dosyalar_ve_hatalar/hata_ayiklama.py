# Hata yönetimi örneği

try:
    sayi = int(input("Bir sayı girin: "))
    sonuc = 10 / sayi
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")
except ValueError:
    print("Lütfen sayısal bir değer girin.")
else:
    print("Sonuç:", sonuc)
finally:
    print("Bu blok her zaman çalışır.")

# Hata fırlatma örneği
def yas_kontrol(yas):
    if yas < 0:
        raise ValueError("Yaş negatif olamaz!")
    print("Geçerli yaş:", yas)

yas_kontrol(20)
