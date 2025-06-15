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
