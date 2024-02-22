import nltk
from nltk.stem import PorterStemmer

# Download necessary NLTK resources (if not already downloaded)
nltk.download('punkt')

# Initialize Porter Stemmer
porter_stemmer = PorterStemmer()

# List of words to stem
words = ["running", "easily", "friendships", "beautifully", "believe", "happiness", "interesting", "purchased"]

# Stem the words using Porter Stemmer
stemmed_words = [porter_stemmer.stem(word) for word in words]

# Print original words and their stemmed forms
for original, stemmed in zip(words, stemmed_words):
    print(f"{original} -> {stemmed}")
