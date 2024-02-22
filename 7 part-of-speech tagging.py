import nltk
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources (if not already downloaded)
nltk.download('punkt')

# Sample text
text = "The cat sat on the mat. The dog barked at the cat."

# Tokenize the text into words
words = word_tokenize(text)

# Perform Part-of-Speech (POS) tagging
pos_tags = nltk.pos_tag(words)

# Print the tagged words
print("Word\t\tPOS Tag")
print("------------------------")
for word, pos_tag in pos_tags:
    print(f"{word}\t\t{pos_tag}")
