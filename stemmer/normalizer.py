import re 
import unidecode



def normalize_text(text):
    text = text.lower()
    print(f"Original text: {text}")
    text = unidecode.unidecode(text)
    print(f"After unidecode: {text}")
    text = re.sub(r'[^a-z0-9\s]', '', text)
    print(f"After removing special characters: {text}")
    text = re.sub(r'\s+', ' ', text)
    print(f"After removing extra spaces: {text}")
    
    return text;

