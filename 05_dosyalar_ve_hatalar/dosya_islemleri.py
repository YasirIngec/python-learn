# Python'da dosya işlemleri için `open()` fonksiyonu kullanılır.
# Dosya açma modları:
# "r": okuma (read) – Dosya yoksa hata verir
# "w": yazma (write) – Dosya yoksa oluşturur, varsa içeriği siler
# "a": ekleme (append) – Dosya yoksa oluşturur, sonuna ekleme yapar
# "x": oluşturma (create) – Dosya varsa hata verir
# "b": ikili dosya (binary) modu
# "t": metin dosyası (varsayılan)

# Örnek 1: Dosya yazma ("w" modu – eski içerik silinir)
with open("ornek.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Python dosya işlemleri\n")
    dosya.write("İkinci satır\n")

# Örnek 2: Dosyaya ekleme ("a" modu – var olan içeriği silmeden ekler)
with open("ornek.txt", "a", encoding="utf-8") as dosya:
    dosya.write("Yeni satır eklendi\n")

# Örnek 3: Dosya okuma ("r" modu)
with open("ornek.txt", "r", encoding="utf-8") as dosya:
    icerik = dosya.read()
    print("Dosya içeriği:\n", icerik)

# Örnek 4: Satır satır okuma
with open("ornek.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        print("Satır:", satir.strip())

# Hatalı kullanım: Var olmayan dosyayı okumaya çalışmak
try:
    with open("yok_dosya.txt", "r") as d:
        print(d.read())
except FileNotFoundError as e:
    print("Hata:", e)

# Gerçek senaryo: Öğrenci notlarını dosyadan okuma ve ortalama hesaplama
with open("notlar.txt", "w", encoding="utf-8") as dosya:
    dosya.write("Ali,90\nAyşe,85\nVeli,75")

toplam = 0
adet = 0

with open("notlar.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        isim, notu = satir.strip().split(",")
        toplam += int(notu)
        adet += 1

print("Ortalama not:", toplam / adet)
