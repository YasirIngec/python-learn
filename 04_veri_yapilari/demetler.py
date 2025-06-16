# Demet (tuple), listelere benzer ancak değiştirilemez (immutable) yapılardır.
# Parantez () ile tanımlanır. İçeriği sonradan değiştirilemez.

# Temel tuple tanımı
renkler = ("kırmızı", "yeşil", "mavi")
sayilar = (1, 2, 3, 4, 5)

print("Renkler:", renkler)
print("İlk renk:", renkler[0])
print("Son sayı:", sayilar[-1])

# Tuple içinde farklı veri tipleri bulunabilir
karisik = (1, "iki", 3.0, True)
print("Karışık tuple:", karisik)

# Tek elemanlı tuple oluşturmak için sonuna virgül koymak gerekir
tek = ("elma",)
print("Tek elemanlı tuple tipi:", type(tek))  # <class 'tuple'>

# Değiştirilemezlik örneği
try:
    renkler[0] = "turuncu"
except TypeError as e:
    print("Hata:", e)

# Tuple üzerinde döngü
for renk in renkler:
    print("Renk:", renk)

# Tuple parçalama (unpacking)
kisi = ("Yasir", 22, "Ankara")
ad, yas, sehir = kisi
print("Ad:", ad)
print("Yaş:", yas)
print("Şehir:", sehir)

# Tuple metodları (sınırlı sayıdadır çünkü değiştirilemez)
rakamlar = (1, 2, 2, 3, 2, 4)

print("2 kaç kez geçiyor:", rakamlar.count(2))
print("3 hangi indexte:", rakamlar.index(3))

# Gerçek kullanım: Fonksiyonlardan birden fazla değer döndürme
def islemler(a, b):
    toplam = a + b
    carpim = a * b
    return toplam, carpim  # Tuple olarak döner

t, c = islemler(3, 4)
print("Toplam:", t)
print("Çarpım:", c)
