import re
import Levenshtein

# Define a class to normalize Romanized Nepali text using phonetic rules and Levenshtein distance

class TextNormalizer:
    def __init__(self):
        """
        Initializes the TextNormalizer with a list of standard forms.
        :param standard_forms: A list of standard words/phrases to normalize against.
        """
        standard_forms = ['huncha', 'pani', 'thik', 'ramro', 'piro', 'thyo']
        self.standard_forms = standard_forms

    def phonetic_normalization(self, text):
        """
        Applies basic phonetic rules to normalize Romanized Nepali spelling variations.
        :param text: The input text to normalize.
        :return: The text after phonetic normalization.
        """
        # Rule 1: Replace 'x' with 'ch' (e.g., 'hunxa' -> 'huncha')
        text = re.sub(r'\bx', 'ch', text)

        # Rule 2: Normalize 'hha' endings to 'cha' (e.g., 'hunchha' -> 'huncha')
        text = re.sub(r'hha\b', 'cha', text)

        # Rule 3: Handle cases like 'huchha' -> 'huncha'
        text = re.sub(r'\bhuchha\b', 'huncha', text)

        return text

    def closest_word(self, word):
        """
        Finds the closest match for a word from the list of standard forms using Levenshtein distance.
        :param word: The word to match.
        :return: The closest matching word from the standard forms.
        """
        # Find the closest word from the standard forms list based on edit distance
        closest_match = min(self.standard_forms, key=lambda x: Levenshtein.distance(word, x))

        # Set a threshold to avoid replacing words that are too different (distance <= 2)
        if Levenshtein.distance(word, closest_match) <= 2:
            return closest_match
        return word  # Return the original word if no close match is found

    def text_cleaning(self,text):
        """
        Cleans the text by removing extra spaces and converting to lowercase.
        :param text: The input text to clean.
        :return: The cleaned text.
        """
        return ' '.join(text.lower().split())

    def normalize_text(self, text):
        """
        Applies both phonetic normalization and Levenshtein distance-based matching.
        :param text: The input text to normalize.
        :return: The normalized text.
        """
        # Step 1: Apply phonetic normalization
        normalized_text = self.phonetic_normalization(text)

        # Step 2: Apply Levenshtein-based fuzzy matching for remaining variations
        words = normalized_text.split()
        normalized_words = [self.closest_word(word) for word in words]

        return ' '.join(normalized_words)

# Example usage:
if __name__ == "__main__":
    

    # Initialize the TextNormalizer class
    normalizer = TextNormalizer()

    text = "hunxa hunchha huchha piro thik ramro thyo"
