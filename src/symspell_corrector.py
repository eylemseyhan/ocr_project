from symspellpy import SymSpell
import os
import re

def initialize_symspell():
    sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
    dictionary_path = os.path.join(os.path.dirname(__file__), "frequency_dictionary_en_82_765.txt")

    if not sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1):
        print("Sözlük yüklenemedi!")

    return sym_spell

sym_spell = initialize_symspell()

# Regex ile belirli formatları koruma
def is_protected_word(word):
    patterns = [
        r'^\d{2,}$',  # Sayılar (fatura numarası vb.)
        r'^[A-Z]{2,}$',  # Büyük harfli kelimeler
        r'^\d+\.\d{2}$',  # Para formatı
        r'^[A-Z][a-z]+$'  # Ürün isimleri
    ]
    for pattern in patterns:
        if re.match(pattern, word):
            return True
    return False

def correct_text(text):
    corrected_text = []
    for word in text.split():
        best_match = sym_spell.lookup(word, verbosity=0) # liste döndürüyor [Suggestion(term="memory", distance=1, count=140479833)]
        if best_match:
            corrected_text.append(best_match[0].term)
        else:
            corrected_text.append(word)
    
    # Düzeltilmiş metni döndür
    return " ".join(corrected_text)

def remove_meaningless_words(text):
    meaningless_patterns = [
        r"\b(?:of|a|the|and|for|in|on|to|with|as|by|an|or|at)\b",  # Anlamsız bağlaçlar
        r"\b(?:epee|online)\b",                                      # Gereksiz kelimeler
        r"[^\w\s]",                                                 # Noktalama ve semboller                                              # Yüksek rakamlar
        r"\b(?:sss|oo|aa)\b"                                        # Tekrarlayan karakterler
    ]
    for pattern in meaningless_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return text.strip()


def remove_duplicates(text):
    words = text.split()
    seen = set() # set sadece benzersiz değer tutar
    cleaned_text = []
    for word in words:
        if word not in seen:
            seen.add(word)
            cleaned_text.append(word)
    return " ".join(cleaned_text)




def final_correction(text):
    # OCR sonrası önce metni küçültürsek symspell ile daha iyi sonuç alırız
    text = text.lower()
    text = correct_text(text)
    text = remove_meaningless_words(text)
    text = remove_duplicates(text)
    
    return text
