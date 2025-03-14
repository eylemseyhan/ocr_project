# OCR ile Fatura Tanıma ve Metin Düzeltme Projesi

Bu proje, fatura gibi belgeler üzerinden optik karakter tanıma (OCR) yaparak metin çıkarma, düzeltme ve anlamlı verileri temizleme üzerine yoğunlaşmaktadır.

# Kullanılan Teknolojiler

Python

OpenCV: Görüntüler üzerinde önişlem yapma

Tesseract OCR: Metin tanıma

SymSpell: Yazım hatalarını düzeltme


PIL (Pillow): Görüntü işleme

# Kurulum

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

Gerekli paketleri yükleyin:

pip install -r requirements.txt

Tesseract OCR'yi indirin ve kurun.

Linux/Mac: /opt/homebrew/bin/tesseract gibi bir dizinde bulunmalı.

Windows: tesseract.exe yolunu belirleyin.

Projeyi çalıştırmak için:

python main.py image.png

# Projenin Yapısı

project-folder/
│── main.py                  # Ana çalışma dosyası
│── symspell_corrector.py    # Metin düzeltme ve temizleme fonksiyonları
│── requirements.txt         # Gerekli paketler
│── output/                  # OCR çıktıları
              

# Çıktı Formatı

OCR tarafından çıkarılan metinler output/output.txt olarak kaydedilir. Düzeltilmiş ve temizlenmiş hali output/corrected_output.txt dosyasına yazılır.



