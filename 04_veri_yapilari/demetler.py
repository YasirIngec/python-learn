# Tuple (demet), sıralı ama değiştirilemez veri yapısıdır.

renkler = ("kırmızı", "yeşil", "mavi")

print("Tüm demet:", renkler)
print("İlk eleman:", renkler[0])       # çıktı: kırmızı
print("Son eleman:", renkler[-1])      # çıktı: mavi
print("Uzunluk:", len(renkler))        # çıktı: 3

# Tek elemanlı tuple için sonunda virgül olmalı
tek = ("siyah",)
print(type(tek))                       # <class 'tuple'>

# Tuple’lar değiştirilemez:
# renkler[0] = "sarı"  → HATA verir!
