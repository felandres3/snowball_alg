import re 
import unidecode



def normalize_text(text):
    text = text.lower()
    text = unidecode.unidecode(text)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    
    return text;

