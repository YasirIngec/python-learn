# Bu program, 'kisiler.txt' dosyasından verileri okur.
# Kullanıcıdan şehir bilgisi alır.
# O şehirde yaşayan kişileri listeler.

def kisileri_dosyadan_oku(dosya_adi):
    try:
        with open(dosya_adi, "r", encoding="utf-8") as dosya:
            kisiler = []
            for satir in dosya:
                ad, sehir = satir.strip().split(",")
                kisiler.append({"ad": ad.strip(), "sehir": sehir.strip().lower()})
            return kisiler
    except FileNotFoundError:
        print("Dosya bulunamadı.")
        return []

def sehire_gore_ara(kisiler, aranan_sehir):
    sonuc = [k["ad"] for k in kisiler if k["sehir"] == aranan_sehir.lower()]
    return sonuc

# Ana akış
dosya = "kisiler.txt"
veriler = kisileri_dosyadan_oku(dosya)

if veriler:
    sehir = input("Hangi şehirde yaşayanları arıyorsunuz? ")
    bulunan = sehire_gore_ara(veriler, sehir)
    
    if bulunan:
        print(f"\n{sehir.title()} şehrinde yaşayan kişiler:")
        for kisi in bulunan:
            print("-", kisi)
    else:
        print(f"{sehir.title()} şehrinde kişi bulunamadı.")
