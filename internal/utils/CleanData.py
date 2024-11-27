import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def clean_text(text: str) -> str:
    # Convert text to lowercase
    # text = text.lower()
    
    # Remove special characters, numbers, and extra spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Remove html tags
    text = re.sub(r'<.*?>', '', text)

    return text
    
    # # Tokenize the text
    # tokens = word_tokenize(text)
    
    # # Remove stopwords
    # stop_words = set(stopwords.words('english'))
    # tokens = [word for word in tokens if word not in stop_words]
    
    # # Lemmatization
    # lemmatizer = WordNetLemmatizer()
    # tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # # Join tokens back into text
    # cleaned_text = ' '.join(tokens)
    
    # return cleaned_text