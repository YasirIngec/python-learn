# Fonksiyonlar, belirli işlemleri tekrar kullanmak için tanımlanır.
# def anahtar kelimesi ile tanımlanır.

# Temel fonksiyon tanımı
def selamla():
    print("Merhaba, hoş geldiniz!")

# Fonksiyonu çağırma
selamla()

# Parametre alan fonksiyon
def topla(a, b):
    return a + b

print("Toplam:", topla(5, 3))  # 8

# Varsayılan parametreli fonksiyon
def selam_ver(isim="Ziyaretçi"):
    print(f"Merhaba {isim}")

selam_ver("Yasir")
selam_ver()

# Geriye değer döndürmeyen fonksiyon (void benzeri)
def yazdir_ortalama(s1, s2, s3):
    ort = (s1 + s2 + s3) / 3
    print("Ortalama:", ort)

yazdir_ortalama(70, 80, 90)

# Geriye değer döndüren fonksiyon
def ortalama(s1, s2, s3):
    return (s1 + s2 + s3) / 3

print("Dönen ortalama:", ortalama(60, 70, 80))

# Hatalı kullanım: Parametre eksikliği
try:
    print(topla(5))  # 2 parametre bekliyor, sadece 1 verildi
except TypeError as e:
    print("Hata:", e)

# Gerçek hayat senaryosu: Yaş hesaplama fonksiyonu
def yas_hesapla(dogum_yili, mevcut_yil=2025):
    return mevcut_yil - dogum_yili

kisi_adi = input("Adınız: ")
try:
    dogum = int(input("Doğum yılınız: "))
    print(f"{kisi_adi}, yaşınız: {yas_hesapla(dogum)}")
except ValueError:
    print("Lütfen geçerli bir yıl girin.")

