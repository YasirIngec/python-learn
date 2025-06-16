# Bu program 10 adet rastgele sayı üretir (1-100 arası)
# - Sayıları listeye ekler
# - Çift ve tek olanları ayırır
# - Küme ile tekrar edenleri kaldırır
# - Ortalama, maksimum, minimum gibi istatistikleri gösterir

import random

def rastgele_sayilar_uret(adet=10, alt=1, ust=100):
    return [random.randint(alt, ust) for _ in range(adet)]

def sayilari_ayir(liste):
    tekler = [s for s in liste if s % 2 != 0]
    ciftler = [s for s in liste if s % 2 == 0]
    return tekler, ciftler

def istatistik_hesapla(liste):
    return {
        "Ortalama": sum(liste) / len(liste),
        "Minimum": min(liste),
        "Maksimum": max(liste),
        "Tekrarsiz Sayilar": list(set(liste))
    }

sayilar = rastgele_sayilar_uret()
print("Üretilen sayılar:", sayilar)

tekler, ciftler = sayilari_ayir(sayilar)
print("Tek sayılar:", tekler)
print("Çift sayılar:", ciftler)

istatistik = istatistik_hesapla(sayilar)
for k, v in istatistik.items():
    print(f"{k}: {v}")
