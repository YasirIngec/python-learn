# Liste, birden fazla değeri tek bir değişkende saklamak için kullanılır.
# Köşeli parantez [ ] ile tanımlanır ve farklı türde veriler içerebilir.

# Temel liste tanımı
meyveler = ["elma", "armut", "çilek"]
sayilar = [1, 2, 3, 4, 5]
karisik = [1, "iki", 3.0, True]

print("Meyveler:", meyveler)
print("Sayilar:", sayilar)

# Elemanlara erişim (index ile)
print("İlk meyve:", meyveler[0])     # elma
print("Son meyve:", meyveler[-1])    # çilek

# Eleman değiştirme
meyveler[1] = "muz"
print("Yeni meyveler:", meyveler)

# Eleman ekleme
meyveler.append("kiraz")
print("Append sonrası:", meyveler)

meyveler.insert(1, "portakal")  # Belirli index'e ekleme
print("Insert sonrası:", meyveler)

# Eleman silme
meyveler.remove("elma")
print("Elma silindi:", meyveler)

son = meyveler.pop()  # Son elemanı siler
print("Pop edilen:", son)
print("Kalanlar:", meyveler)

# Listeyi ters çevirme ve sıralama
sayilar = [5, 1, 3, 2, 4]
sayilar.sort()     # Küçükten büyüğe
print("Sıralı:", sayilar)

sayilar.reverse()  # Ters çevirme
print("Ters:", sayilar)

# Liste içinde liste (nested list)
ogrenciler = [["Ali", 90], ["Ayşe", 85], ["Veli", 75]]
print("İlk öğrenci adı:", ogrenciler[0][0])
print("İlk öğrenci notu:", ogrenciler[0][1])

# Hatalı kullanım: Index dışı erişim
try:
    print(meyveler[100])
except IndexError as e:
    print("Hata:", e)

# Gerçek kullanım: Listeyi gezerek işlem yapmak
notlar = [65, 70, 90, 45, 80]
gecenler = []

for n in notlar:
    if n >= 60:
        gecenler.append(n)

print("Geçen notlar:", gecenler)
