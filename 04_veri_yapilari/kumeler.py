# Set (küme), sırasız ve benzersiz (tekrarsız) elemanlardan oluşur.

sayilar = {1, 2, 3, 3, 4, 5, 5}
print("Küme:", sayilar)  # çıktı: {1, 2, 3, 4, 5}

# Eleman ekleme
sayilar.add(6)
print("Ekleme sonrası:", sayilar)

# Eleman silme
sayilar.remove(3)
print("3 silindi:", sayilar)

# Küme işlemleri
A = {1, 2, 3}
B = {3, 4, 5}

print("Kesişim:", A & B)          # {3}
print("Birleşim:", A | B)         # {1, 2, 3, 4, 5}
print("Fark:", A - B)             # {1, 2}

# Çift sayıları kümeye ekleyelim
ciftler = {x for x in range(10) if x % 2 == 0}
print(ciftler)  # {0, 2, 4, 6, 8}