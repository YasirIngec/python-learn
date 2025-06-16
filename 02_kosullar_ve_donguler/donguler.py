# Döngüler tekrarlı işlemleri kolaylaştırmak için kullanılır.
# Python'da iki temel döngü yapısı vardır: for ve while

# FOR DÖNGÜSÜ
# Bir koleksiyon (liste, dizi, string vs.) üzerinde gezinmek için kullanılır
meyveler = ["elma", "armut", "çilek"]
for meyve in meyveler:
    print("Meyve:", meyve)

# range() fonksiyonu ile sayısal döngü
for i in range(5):  # 0'dan 4'e kadar
    print("Sayı:", i)

# WHILE DÖNGÜSÜ
# Belirli bir koşul doğru olduğu sürece döner
sayi = 0
while sayi < 3:
    print("while döngüsü içindeyiz:", sayi)
    sayi += 1

# break ve continue kullanımı
for i in range(1, 6):
    if i == 3:
        continue  # 3'ü atlar
    if i == 5:
        break     # 5'e gelince döngüyü sonlandırır
    print("i:", i)

# Sonsuz döngü örneği (kullanılmamalı ama bilinmeli)
# while True:
#     print("Bu döngü sonsuza kadar devam eder")

# Hatalı kullanım örneği
# Mantıksız artış/değişim olmazsa sonsuz döngü oluşur
try:
    a = 0
    while a < 5:
        print("a =", a)
        # a += 1  # Eğer bu satır yoksa, sonsuz döngü olur
except KeyboardInterrupt:
    print("Elle durduruldu.")

# Gerçek senaryo: Kullanıcı doğru şifre girene kadar deneme hakkı
dogru_sifre = "1234"
hak = 3
while hak > 0:
    girilen = input("Şifreyi girin: ")
    if girilen == dogru_sifre:
        print("Giriş başarılı.")
        break
    else:
        hak -= 1
        print("Yanlış şifre. Kalan deneme:", hak)
if hak == 0:
    print("Hesap kilitlendi.")
