# Sözlük (dictionary), anahtar-değer (key-value) çiftlerinden oluşan veri yapısıdır.
# Süslü parantez { } ile tanımlanır ve her anahtar eşsiz (benzersiz) olmalıdır.

# Temel sözlük tanımı
kisi = {
    "ad": "Yasir",
    "yas": 22,
    "sehir": "Ankara"
}

print("Ad:", kisi["ad"])
print("Yaş:", kisi["yas"])

# Eleman ekleme
kisi["meslek"] = "Öğrenci"
print("Güncel sözlük:", kisi)

# Eleman güncelleme
kisi["yas"] = 23
print("Yaş güncellendi:", kisi)

# Anahtarın olup olmadığını kontrol etme
if "email" in kisi:
    print("Email var")
else:
    print("Email yok")

# get() → Anahtar yoksa hata vermez, varsayılan değer dönebilir
print("Email (get):", kisi.get("email", "tanımsız"))

# Eleman silme
del kisi["sehir"]
print("Şehir silindi:", kisi)

# Tüm anahtarlar ve değerler
print("Tüm anahtarlar:", list(kisi.keys()))
print("Tüm değerler:", list(kisi.values()))
print("Tüm çiftler:", list(kisi.items()))

# Döngü ile tüm çiftleri yazdırma
for anahtar, deger in kisi.items():
    print(f"{anahtar} → {deger}")

# Hatalı kullanım: Olmayan anahtara direkt erişim
try:
    print(kisi["telefon"])
except KeyError as e:
    print("Hata:", e)

# Gerçek kullanım: Öğrenci notlarını tutan sözlük
notlar = {
    "Ali": 85,
    "Ayşe": 92,
    "Veli": 77
}

for isim, notu in notlar.items():
    durum = "Geçti" if notu >= 60 else "Kaldı"
    print(f"{isim}: {notu} → {durum}")
