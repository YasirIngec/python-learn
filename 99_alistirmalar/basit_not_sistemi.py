# Bu program öğrenci adı ve 3 sınav notu alır.
# - Ortalama hesaplar
# - "Geçti" ya da "Kaldı" bilgisini gösterir
# - Bilgileri dosyaya kaydeder
# - Dosyayı okuyarak bilgileri tekrar ekrana yazdırır

def not_ortalama_hesapla(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def not_durumu(ortalama):
    return "Geçti" if ortalama >= 50 else "Kaldı"

def bilgileri_dosyaya_yaz(ad, notlar, ort, durum, dosya_adi):
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        dosya.write(f"Ad: {ad}\n")
        dosya.write(f"Notlar: {notlar}\n")
        dosya.write(f"Ortalama: {ortalama:.2f}\n")
        dosya.write(f"Durum: {durum}\n")

def dosyayi_oku(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            print("\nKayıtlı Bilgiler:")
            for satir in dosya:
                print(satir.strip())
    except FileNotFoundError:
        print("Dosya bulunamadı.")

# Ana akış
try:
    ad = input("Öğrenci adı: ")
    n1 = float(input("1. Not: "))
    n2 = float(input("2. Not: "))
    n3 = float(input("3. Not: "))

    ortalama = not_ortalama_hesapla(n1, n2, n3)
    durum = not_durumu(ortalama)

    print(f"{ad} adlı öğrencinin ortalaması: {ortalama:.2f} → {durum}")

    dosya = "not_kaydi.txt"
    notlar = [n1, n2, n3]
    bilgileri_dosyaya_yaz(ad, notlar, ortalama, durum, dosya)
    dosyayi_oku(dosya)

except ValueError:
    print("Lütfen geçerli bir not değeri girin.")
