# Bu dosyada matplotlib kullanarak çeşitli grafik örnekleri oluşturulmuştur.

import matplotlib.pyplot as plt

# -------------------------------
# Çizgi Grafiği
# -------------------------------
# Yıllara göre nüfus artışı örneği
yillar = [2015, 2016, 2017, 2018, 2019, 2020]
nufuslar = [72, 75, 78, 80, 82, 84]

plt.plot(yillar, nufuslar, marker='o')
plt.title("Yıllara Göre Nüfus Artışı")
plt.xlabel("Yıl")
plt.ylabel("Nüfus (milyon)")
plt.grid(True)
plt.savefig("nufus_cizgi.png")
plt.show()

# -------------------------------
# Sütun Grafiği
# -------------------------------
# Şehirlere göre öğrenci sayısı
sehirler = ["Ankara", "İstanbul", "İzmir", "Bursa"]
ogrenci_sayilari = [120, 250, 180, 100]

plt.bar(sehirler, ogrenci_sayilari, color="green")
plt.title("Şehirlere Göre Öğrenci Sayısı")
plt.xlabel("Şehir")
plt.ylabel("Öğrenci Sayısı")
plt.savefig("ogrenci_sutun.png")
plt.show()

# -------------------------------
# Pasta Grafiği
# -------------------------------
# Anket sonucu: Tercih edilen diller
diller = ["Python", "Java", "C++", "JavaScript"]
oranlar = [45, 25, 15, 15]

plt.pie(oranlar, labels=diller, autopct="%1.1f%%")
plt.title("Tercih Edilen Programlama Dilleri")
plt.savefig("dil_pasta.png")
plt.show()
