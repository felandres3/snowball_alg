def stem(word: str) -> str:
    suffixes = [
        "amiento", "imientos", "amiento", "imiento",
        "aciones", "uciones", "adores", "ancias", "encias",
        "mente", "idad", "iva", "ivo", "ivas", "ivos",
        "ando", "iendo", "aron", "aban", "ían", "ías", "ado", "ido",
        "ar", "er", "ir", "os", "as", "es", "s", "cion"
    ]
    
    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 2:
            return word[:-len(suffix)]
    return word