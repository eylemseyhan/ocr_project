import pytesseract
import cv2
import os
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from symspell_corrector import final_correction

# path
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"

def preprocess_image(path):
    img = Image.open(path)
    img = np.array(img)
    
    # Resizing + Grayscale
    img = cv2.resize(img, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    # Kontrast artırma ve gürültü azaltma
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    # İnce detayları koruma
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.bilateralFilter(img, 9, 50, 50)

    img = remove_horizontal_lines(img)
    return img

def remove_horizontal_lines(img):
    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (70, 1))
    remove_horizontal = cv2.morphologyEx(img, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    
    cnts = cv2.findContours(remove_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(img, [c], -1, (255, 255, 255), 5)
    return img


def export_output(corrected_text):
    output_path = os.path.join(os.path.dirname(__file__), "../output/output.txt")
    with open(output_path, "w") as file:
        file.write(corrected_text)
    print("Düzeltilmiş çıktı output klasörüne kaydedildi.")

# Düzeltilmiş çıktıyı ayrı bir dosyaya kaydet
def export_corrected_output(corrected_text):
    output_path = os.path.join(os.path.dirname(__file__), "../output/corrected_output.txt")
    with open(output_path, "w") as file:
        file.write(corrected_text)
    print("Düzeltilmiş çıktı corrected_output.txt dosyasına kaydedildi.")


path = "image.png"
img = preprocess_image(path)
text = pytesseract.image_to_string(img)
corrected_text = final_correction(text)

# Çıktıyı yazdır
print("Orijinal çıktı: \n", text)
print("Düzeltilmiş çıktı: \n", corrected_text)

export_output(corrected_text)
export_corrected_output(corrected_text)
