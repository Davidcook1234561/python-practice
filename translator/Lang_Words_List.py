class LangWords:
    def __init__(self):
        
        self.Languages = {
            "English": {
                1: "run",
                2: "jump",
                3: "swim",
                4: "eat",
                5: "sleep"
            },
            "French": {
                1: "courir",
                2: "sauter",
                3: "nager",
                4: "manger",
                5: "dormir"
            }
        }

    def get_language(self, lang_name):
            language = self.Languages.get(lang_name)
            if language is None:
                print("Language not found.")
            return language    

    def get_all_languages(self):
        return list(self.Languages.keys())
    
    
    def translate(self, from_lang, to_lang, word):
        """Translate a word from one language to another"""
        word_id = self.get_id_by_word(from_lang, word)

        if word_id:
            return self.get_word_by_id(to_lang, word_id)
        else:
            return None
        
    def get_id_by_word(self, lang_name, word):
        for word_id, w in self.Languages[lang_name].items():
            if w == word:
                return word_id
        return None       

    def get_word_by_id(self, lang_name, word_id):
        return self.Languages[lang_name].get(word_id) 