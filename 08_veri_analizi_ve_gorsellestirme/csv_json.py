# Bu dosyada Python'da CSV ve JSON dosyaları ile veri okuma ve yazma işlemleri anlatılmıştır.
# json: JSON formatlı veri ile çalışma
# csv: CSV formatlı tablo verisi ile çalışma

import csv
import json

# --------------------
# CSV yazma işlemi
# --------------------
def csv_yaz(dosya_adi, veriler):
    with open(dosya_adi, mode='w', newline='', encoding='utf-8') as dosya:
        yazar = csv.writer(dosya)
        yazar.writerow(["Ad", "Yaş", "Şehir"])  # Başlık satırı
        for veri in veriler:
            yazar.writerow(veri)

# --------------------
# CSV okuma işlemi
# --------------------
def csv_oku(dosya_adi):
    with open(dosya_adi, mode='r', encoding='utf-8') as dosya:
        okuyucu = csv.reader(dosya)
        for satir in okuyucu:
            print(satir)

# --------------------
# JSON yazma işlemi
# --------------------
def json_yaz(dosya_adi, veri):
    with open(dosya_adi, 'w', encoding='utf-8') as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=4)

# --------------------
# JSON okuma işlemi
# --------------------
def json_oku(dosya_adi):
    with open(dosya_adi, 'r', encoding='utf-8') as dosya:
        veri = json.load(dosya)
        print(json.dumps(veri, indent=4, ensure_ascii=False))


# Örnek veri
kisiler = [
    ["Ali", 25, "Ankara"],
    ["Ayşe", 30, "İstanbul"],
    ["Veli", 22, "İzmir"]
]

kisi_dict = {
    "kisiler": [
        {"ad": "Ali", "yas": 25, "sehir": "Ankara"},
        {"ad": "Ayşe", "yas": 30, "sehir": "İstanbul"},
        {"ad": "Veli", "yas": 22, "sehir": "İzmir"}
    ]
}

# Fonksiyonları çalıştır
csv_yaz("kisiler.csv", kisiler)
print("CSV Okuma:")
csv_oku("kisiler.csv")

json_yaz("kisiler.json", kisi_dict)
print("\nJSON Okuma:")
json_oku("kisiler.json")
