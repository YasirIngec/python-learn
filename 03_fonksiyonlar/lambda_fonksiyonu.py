# Lambda fonksiyonları, kısa ve isimsiz (anonim) fonksiyonlardır.
# Genellikle tek satırlık fonksiyonlarda tercih edilir.
# Yapısı: lambda parametreler: ifade

# Temel kullanım
karesi = lambda x: x ** 2
print("5'in karesi:", karesi(5))

# Birden fazla parametre ile kullanım
topla = lambda a, b: a + b
print("Toplam:", topla(3, 7))

# Koşullu ifade ile lambda
tek_mi = lambda x: "Tek" if x % 2 != 0 else "Çift"
print("7:", tek_mi(7))
print("8:", tek_mi(8))

# map() ile kullanım: Listedeki her elemanın karesini al
sayilar = [1, 2, 3, 4, 5]
kareler = list(map(lambda x: x**2, sayilar))
print("Kareler:", kareler)

# filter() ile kullanım: Sadece çift sayıları filtrele
ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print("Çiftler:", ciftler)

# sorted() ile kullanım: Listeyi belirli bir kritere göre sırala
ogrenciler = [("Ali", 90), ("Veli", 80), ("Ayşe", 95)]
sirali = sorted(ogrenciler, key=lambda x: x[1], reverse=True)
print("Notlara göre sıralı:", sirali)

# Hatalı kullanım: Çok satırlı işlem yapılamaz
try:
    # Bu yapı geçersizdir
    hata_lambda = lambda x: (x + 1; print(x))  # SyntaxError olurdu
except SyntaxError:
    print("Lambda fonksiyonları sadece tek satır işlem içerebilir.")

# Gerçek kullanım: Menüdeki ürünleri fiyata göre filtreleme
menu = [
    {"isim": "Kahve", "fiyat": 30},
    {"isim": "Çay", "fiyat": 15},
    {"isim": "Pasta", "fiyat": 60},
    {"isim": "Kurabiye", "fiyat": 25}
]

ucuz_urunler = list(filter(lambda urun: urun["fiyat"] < 40, menu))
print("40 TL altı ürünler:")
for urun in ucuz_urunler:
    print(f"- {urun['isim']} ({urun['fiyat']} TL)")

