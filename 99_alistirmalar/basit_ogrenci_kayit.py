# ogrenci_kayit.py

# Bir öğrencinin adı, yaşı ve notları girilir.
# Her kayıt bir sözlük olarak listeye eklenir.
# Program sonunda dosyaya yazılır.

ogrenciler = []

while True:
    try:
        isim = input("Öğrenci adı (çıkmak için q): ")
        if isim == "q":
            break
        yas = int(input("Yaş: "))
        not1 = float(input("1. Not: "))
        not2 = float(input("2. Not: "))
        ort = (not1 + not2) / 2

        ogrenci = {
            "isim": isim,
            "yas": yas,
            "ortalama": ort
        }
        ogrenciler.append(ogrenci)

    except ValueError:
        print("Hatalı giriş! Sayısal değer giriniz.")

with open("ogrenciler.txt", "w", encoding="utf-8") as dosya:
    for ogr in ogrenciler:
        satir = f"{ogr['isim']}, {ogr['yas']} yaşında, ortalama: {ogr['ortalama']}\n"
        dosya.write(satir)

print("Tüm kayıtlar 'ogrenciler.txt' dosyasına kaydedildi.")
