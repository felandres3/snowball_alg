import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from stemmer.stemmer import stem
from stemmer.normalizer import normalize_text

words = [
    "comprando", "compramos", "educación", "felicidad",
    "corriendo", "cantaban", "jugador", "inversiones",
    "felices", "felicidades", "felicidad", "felicidad",
]

for word in words:
    normalized_word = normalize_text(word)
    # print(f"{word} → {stem(word)}")
    print(f"{normalized_word} → {stem(normalized_word)}")
