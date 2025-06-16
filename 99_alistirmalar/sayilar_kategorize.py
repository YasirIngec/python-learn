# sayi_analiz.py

# "sayilar.txt" adlı dosyayı oku.
# Her satırda bir sayı olacak.
# Sayıları pozitif, negatif ve sıfır olarak kategorize et.

pozitif = []
negatif = []
sifir = []

try:
    with open("sayilar.txt", "r", encoding="utf-8") as dosya:
        for satir in dosya:
            try:
                sayi = int(satir.strip())
                if sayi > 0:
                    pozitif.append(sayi)
                elif sayi < 0:
                    negatif.append(sayi)
                else:
                    sifir.append(sayi)
            except ValueError:
                continue

    print("Pozitif:", pozitif)
    print("Negatif:", negatif)
    print("Sıfır:", sifir)

except FileNotFoundError:
    print("sayilar.txt dosyası bulunamadı.")
