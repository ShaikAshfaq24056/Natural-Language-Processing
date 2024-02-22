import re

# Example text
text = "The cat sat on the mat. The cat ate the fish. The dog barked at the cat."

# Define a regular expression pattern to search for the word "cat"
pattern = r'\bcat\b'

# Use re.findall() to find all occurrences of the pattern in the text
matches = re.findall(pattern, text)

# Print the matches
print("Matches found:", matches)

# Use re.search() to search for the pattern in the text
search_result = re.search(pattern, text)

if search_result:
    print("Pattern found at index:", search_result.start())
else:
    print("Pattern not found.")

# Use re.sub() to substitute the pattern with another string
new_text = re.sub(pattern, "dog", text)
print("New text after substitution:", new_text)
