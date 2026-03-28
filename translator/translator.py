class Translator:
    def __init__(self, source_lang, target_lang, lang_words_obj):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.lang_words = lang_words_obj
    
    def translate(self, word):
        """Translate a word from source to target language"""
        return self.lang_words.translate(self.source_lang, self.target_lang, word)
    
    def run(self):
        print(f"\nWelcome! Translating {self.source_lang} to {self.target_lang}")

        while True:
            word = input(f"Enter a {self.source_lang} word (or 'quit' to stop): ").lower().strip()
            if word == "quit":
                print("Goodbye!")
                break

            if not word:  # Skip if empty
                print("Please enter a word!\n")
                continue
            
            translation = self.translate(word)

            if translation:
                print(f"'{word}' in {self.target_lang}: {translation}\n")
            else:
                print(f"Sorry, '{word}' not found in {self.source_lang}.\n")
