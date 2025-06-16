# Dictionary (sözlük), anahtar-değer ikilileriyle veri tutar.

ogrenci = {
    "isim": "Yasir",
    "yas": 21,
    "bolum": "Siber Güvenlik"
}

print("Ad:", ogrenci["isim"])         # Yasir
print("Bölüm:", ogrenci.get("bolum")) # Siber Güvenlik
print("Tüm sözlük:", ogrenci)

# Yeni anahtar-değer ekleme
ogrenci["okul"] = "Üniversite"
print("Yeni sözlük:", ogrenci)

# Değer güncelleme
ogrenci["yas"] = 22

# Anahtar silme
del ogrenci["bolum"]
print("Güncel sözlük:", ogrenci)

# Döngü ile sözlüğü gezmek
for anahtar, deger in ogrenci.items():
    print(f"{anahtar} → {deger}")

# 1'den 5'e kadar sayıların karelerini sözlük olarak üret
kare_dict = {x: x**2 for x in range(1, 6)}
print(kare_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Liste içinde sözlük örneği:
ogrenciler = [
    {"isim": "Ali", "not": 85},
    {"isim": "Ayşe", "not": 92}
]
for ogr in ogrenciler:
    print(f"{ogr['isim']} → {ogr['not']}")
