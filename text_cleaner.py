import string

class TextCleaner:
    def __init__(self):
        # Define punctuation characters to be removed
        self.punctuation_table = str.maketrans('', '', string.punctuation)

    def text_cleaning(self, text):
        """
        Cleans the text by removing punctuation, extra spaces, and converting to lowercase.
        :param text: The input text to clean.
        :return: The cleaned text.
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = text.translate(self.punctuation_table)
        
        # Remove extra spaces
        return ' '.join(text.split())
