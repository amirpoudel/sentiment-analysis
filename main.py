from normalization import TextNormalizer
from text_cleaner import TextCleaner

textNormalizer = TextNormalizer()
textCleaner = TextCleaner(); 
text = "Yeha  ko Khana ekdam ramro xa .....  but buff momo teti mitho chahi xaina hai.... "

cleaned_text = textCleaner.text_cleaning(text)
normalized_text = textNormalizer.normalize_text(cleaned_text)
print(normalized_text)