# pip, Python paketlerini yüklemek ve yönetmek için kullanılan resmi paket yöneticisidir.
# pip sayesinde PyPI'daki (Python Package Index) binlerce paketi kolayca projeye dahil edebiliriz.

# Terminal/komut satırı üzerinden kullanılır.
# Aşağıda en yaygın pip komutları ve açıklamaları yer alır:

# Paket yüklemek:
# pip install paket_adi
# Örnek:
# pip install requests

# Belirli bir sürümü yüklemek:
# pip install paket_adi==1.2.3

# Yüklü paketleri listelemek:
# pip list

# Paket bilgilerini görmek:
# pip show paket_adi

# Paket güncellemek:
# pip install --upgrade paket_adi

# Paket kaldırmak:
# pip uninstall paket_adi

# Tüm bağımlılıkları requirements.txt dosyasından yüklemek:
# pip install -r requirements.txt

# requirements.txt örneği:
# pandas==2.2.2
# matplotlib>=3.5

# Yeni bir requirements.txt oluşturmak (projede yüklü olan paketleri listele):
# pip freeze > requirements.txt

# pip ile yüklenen paketi Python içinde kullanmak:
import requests

cevap = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status code:", cevap.status_code)
print("JSON verisi:", cevap.json())

# Hatalı kullanım: pip ile yüklenmemiş paketi import etmek
try:
    import bilinmeyen_paket
except ModuleNotFoundError as e:
    print("pip ile yüklenmemiş paket:", e)
