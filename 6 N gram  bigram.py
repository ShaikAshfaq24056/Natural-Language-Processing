import random

class BigramModel:
    def __init__(self):
        self.bigrams = {}
        self.start_tokens = []

    def train(self, text):
        # Tokenize the text into words
        words = text.split()

        # Store the start tokens
        self.start_tokens.append(words[0])

        # Generate bigrams
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            if current_word in self.bigrams:
                self.bigrams[current_word].append(next_word)
            else:
                self.bigrams[current_word] = [next_word]

    def generate_text(self, length=10):
        # Start the text generation with a random start token
        current_word = random.choice(self.start_tokens)
        generated_text = [current_word]

        # Generate text based on bigrams
        for _ in range(length - 1):
            next_word = random.choice(self.bigrams.get(current_word, ['']))
            if next_word:
                generated_text.append(next_word)
                current_word = next_word
            else:
                break

        return ' '.join(generated_text)


# Example usage:
if __name__ == "__main__":
    # Example text for training
    text = "The cat sat on the mat. The cat ate the fish. The dog barked at the cat."

    # Initialize the bigram model
    bigram_model = BigramModel()

    # Train the model
    bigram_model.train(text)

    # Generate text using the bigram model
    generated_text = bigram_model.generate_text(length=10)
    print("Generated text:", generated_text)
