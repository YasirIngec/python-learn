# pip: Python modül yöneticisidir. Modül yükleme, kaldırma, güncelleme gibi işlemleri yapar.

# ============================================
# 1. Yeni bir modül yüklemek
# ============================================

# pip install <modul_adi>
# Örnek:
# pip install requests

# Bu komut 'requests' adlı modülü PyPI'den indirip kurar.


# ============================================
# 2. Modülü kaldırmak (uninstall)
# ============================================

# pip uninstall <modul_adi>
# Örnek:
# pip uninstall requests

# Bu komut requests modülünü sistemden kaldırır.


# ============================================
# 3. Yüklü modülleri listelemek
# ============================================

# pip list

# Sistemde yüklü olan tüm modülleri ve sürümlerini listeler.


# ============================================
# 4. Modülün detaylarını görmek (sürüm, yol vs.)
# ============================================

# pip show <modul_adi>
# Örnek:
# pip show pandas

# pandas modülünün versiyonu, yükleme yolu ve bağımlılık bilgilerini verir.


# ============================================
# 5. Tüm bağımlılıkları requirements.txt dosyasına aktarmak
# ============================================

# pip freeze > requirements.txt

# Aktif ortamda yüklü tüm modülleri ve sürümlerini dosyaya yazar.
# Bu dosya, bir projeyi başka ortamda yeniden kurmak için kullanılır.


# ============================================
# 6. requirements.txt dosyasından kurulum yapmak
# ============================================

# pip install -r requirements.txt

# requirements.txt içindeki listedeki tüm modülleri yükler.
# Genellikle projeyi baştan kurarken kullanılır.

