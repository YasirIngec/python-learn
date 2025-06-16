# Kümeler (set), sırasız ve tekrarsız elemanlar içeren veri yapılarıdır.
# Süslü parantez { } ile tanımlanır.
# Elemanlar benzersizdir, yinelenen değerler otomatik olarak elenir.

# Temel küme tanımı
renkler = {"kırmızı", "yeşil", "mavi", "kırmızı"}
print("Renkler kümesi:", renkler)  # 'kırmızı' sadece bir kez görünür

# Boş küme oluşturmak için set() kullanılır, çünkü {} boş sözlük olarak kabul edilir.
bos_kume = set()
print("Boş küme tipi:", type(bos_kume))  # <class 'set'>

# Eleman ekleme
renkler.add("sarı")
print("Yeni renk eklendi:", renkler)

# Eleman silme
renkler.remove("yeşil")
print("Yeşil çıkarıldı:", renkler)

# discard() → eleman yoksa hata vermez
renkler.discard("mor")  # hata vermez
print("Mor çıkarılmaya çalışıldı:", renkler)

# clear() → tüm elemanları siler
kume = {1, 2, 3}
kume.clear()
print("Temizlenmiş küme:", kume)

# Küme işlemleri (matematiksel)
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Birleşim (A ∪ B):", A | B)
print("Kesişim (A ∩ B):", A & B)
print("Fark (A - B):", A - B)
print("Sadece birinde olanlar (A Δ B):", A ^ B)

# Hatalı kullanım: İndeksleme yapılamaz (sırasızdır)
try:
    print(A[0])
except TypeError as e:
    print("Hata:", e)

# Gerçek kullanım: Listede tekrar eden elemanları temizleme
liste = ["elma", "armut", "elma", "muz", "armut"]
benzersiz = list(set(liste))
print("Benzersiz liste:", benzersiz)
