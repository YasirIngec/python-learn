# Bu dosyada pandas kütüphanesi ile temel veri analiz işlemleri gösterilmiştir.

import pandas as pd

# -----------------------------
# Örnek veri oluştur (sözlük)
# -----------------------------
veri = {
    "Ad": ["Ali", "Ayşe", "Veli", "Zeynep", "Mert"],
    "Yaş": [25, 30, 22, 28, 35],
    "Şehir": ["Ankara", "İstanbul", "İzmir", "Ankara", "Bursa"]
}

# -----------------------------
# DataFrame oluştur
# -----------------------------
df = pd.DataFrame(veri)
print("Veri Çerçevesi (DataFrame):\n", df)

# -----------------------------
# Belirli sütunu seçme
# -----------------------------
print("\nYalnızca isimler:\n", df["Ad"])

# -----------------------------
# Filtreleme: Ankara'da yaşayanlar
# -----------------------------
ankara_df = df[df["Şehir"] == "Ankara"]
print("\nAnkara'da yaşayanlar:\n", ankara_df)

# -----------------------------
# İstatistiksel özet
# -----------------------------
print("\nYaşlar için özet bilgiler:\n", df["Yaş"].describe())

# -----------------------------
# Sıralama: Yaşa göre artan
# -----------------------------
sirali_df = df.sort_values(by="Yaş")
print("\nYaşa göre sıralı:\n", sirali_df)

# -----------------------------
# Yeni sütun ekleme
# -----------------------------
df["Yetişkin mi?"] = df["Yaş"] >= 18
print("\nYetişkin bilgisi eklenmiş hali:\n", df)

# -----------------------------
# CSV olarak kaydetme
# -----------------------------
df.to_csv("ornek_kisiler.csv", index=False)
print("\nCSV dosyasına yazıldı: ornek_kisiler.csv")
