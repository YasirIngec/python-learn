# Python'da hata ayıklama (exception handling), programın beklenmeyen durumlarda çökmesini engeller.
# try-except bloklarıyla hataları yakalayabilir ve programın kontrollü çalışmasını sağlayabiliriz.

# Temel try-except örneği
try:
    sayi = int(input("Bir sayı girin: "))
    print("Girdiğiniz sayı:", sayi)
except ValueError:
    print("Geçersiz giriş! Lütfen sadece sayı girin.")

# Birden fazla except bloğu
try:
    a = int(input("Pay: "))
    b = int(input("Payda: "))
    sonuc = a / b
    print("Sonuç:", sonuc)
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")
except ValueError:
    print("Sayı girişi hatalı!")

# try-except-else-finally yapısı
try:
    f = open("veri.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Dosya bulunamadı.")
else:
    print("Dosya başarıyla açıldı.")
    f.close()
finally:
    print("Dosya işlemi tamamlandı (başarılı ya da hatalı).")

# raise ile hata fırlatma
def pozitif_kontrol(sayi):
    if sayi < 0:
        raise ValueError("Negatif sayı kabul edilemez.")
    return sayi

try:
    pozitif_kontrol(-10)
except ValueError as e:
    print("Hata:", e)

# Gerçek senaryo: Kullanıcıdan yaş al ve emekliliğe kalan yılı hesapla
try:
    yas = int(input("Yaşınızı girin: "))
    if yas < 0 or yas > 120:
        raise ValueError("Geçersiz yaş.")
    kalan = 65 - yas
    if kalan > 0:
        print(f"Emekliliğe {kalan} yıl kaldı.")
    else:
        print("Zaten emeklisiniz.")
except ValueError as e:
    print("Hata:", e)
