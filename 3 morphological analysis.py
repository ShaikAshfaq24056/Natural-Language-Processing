import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Sample text
text = "The cats are chasing mice and playing in the garden."

# Tokenize the text into words
tokens = word_tokenize(text)

# Perform Part-of-Speech (POS) tagging
pos_tags = nltk.pos_tag(tokens)

# Lemmatization using WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

lemmatized_words = []
for token, pos_tag in pos_tags:
    # Convert POS tags to WordNet POS tags
    wn_pos_tag = nltk.map_tag('en-ptb', 'universal', pos_tag)
    # Lemmatize the word based on its POS tag
    lemmatized_word = lemmatizer.lemmatize(token, pos=wn_pos_tag.lower()[0])
    lemmatized_words.append((token, lemmatized_word))

# Print the original words and their lemmatized forms
print("Original Word\tLemmatized Word")
print("-----------------------------")
for original, lemmatized in lemmatized_words:
    print(original + "\t\t" + lemmatized)
