# Liste (list), sıralı ve değiştirilebilir bir veri yapısıdır.

meyveler = ["elma", "armut", "muz"]

print("Liste:", meyveler)
print("İlk eleman:", meyveler[0])         # elma
print("Son eleman:", meyveler[-1])        # muz
print("Uzunluk:", len(meyveler))          # 3

# Eleman ekleme
meyveler.append("çilek")
print("Ekleme sonrası:", meyveler)

# Eleman silme
meyveler.remove("armut")
print("Silme sonrası:", meyveler)

# Sıralama
meyveler.sort()
print("Sıralı:", meyveler)

# Döngü ile liste elemanlarını gezmek
for meyve in meyveler:
    print(f"- {meyve}")

# Liste üreteçleri (list comprehension)
kareler = [x**2 for x in range(5)]
print(kareler)  # [0, 1, 4, 9, 16]

# Eleman var mı kontrolü
liste = ["elma", "armut"]
print("elma" in liste)      # True
print("muz" not in liste)   # True
