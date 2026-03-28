from Lang_Words_List import LangWords
from translator import Translator

def main():
    # Create the LangWords object
    lang_words = LangWords()
    
    # Get available languages
    languages = lang_words.get_all_languages()
    print("Available languages:", languages)
    
    # Show menu
    print("\nChoose languages:")
    for i, lang in enumerate(languages, 1):
        print(f"{i}. {lang}")
    
    # Ask user which language to translate FROM
    source_choice = int(input("\nTranslate FROM (enter number): ")) - 1
    source_language = languages[source_choice]
    
    # Ask user which language to translate TO
    target_choice = int(input("Translate TO (enter number): ")) - 1
    target_language = languages[target_choice]
    
    # Create the Translator object
    translator = Translator(source_language, target_language, lang_words)
    
    # Run it!
    translator.run()

if __name__ == "__main__":
    main()