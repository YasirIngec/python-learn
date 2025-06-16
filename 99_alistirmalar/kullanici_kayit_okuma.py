# Bu program, kullanıcıdan ad, yaş ve şehir bilgilerini alır.
# Bu bilgileri bir sözlük olarak bir dosyaya yazar.
# Daha sonra dosyayı okuyarak bilgileri tekrar ekrana yazdırır.

def kullanici_bilgisi_al():
    try:
        ad = input("Adınızı girin: ")
        yas = int(input("Yaşınızı girin: "))
        sehir = input("Şehrinizi girin: ")
        return {"ad": ad, "yas": yas, "sehir": sehir}
    except ValueError:
        print("Yaş sayısal bir değer olmalı.")
        return None

def bilgileri_dosyaya_yaz(kisi, dosya_adi):
    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        for key, value in kisi.items():
            dosya.write(f"{key}:{value}\n")

def dosyadan_bilgileri_oku(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            print("\nKayıtlı Bilgiler:")
            for satir in dosya:
                print(satir.strip())
    except FileNotFoundError:
        print("Dosya bulunamadı.")

# Ana akış
dosya_adi = "kullanici_bilgisi.txt"
kisi = kullanici_bilgisi_al()

if kisi:
    bilgileri_dosyaya_yaz(kisi, dosya_adi)
    dosyadan_bilgileri_oku(dosya_adi)
