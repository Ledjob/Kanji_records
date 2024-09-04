import random
from file_handler import FileHandler
class KanjiBook:
    def __init__(self):

        """
        Initializes an empty KanjiBook.

        Attributes:
            __kanjis (dict): A dictionary where the keys are kanji and the values are lists of translations.
        """

        self.__kanjis = {}
        
    def add_kanji(self, kanji: str, translation: str):
        if not kanji in self.__kanjis:
            self.__kanjis[kanji] = []
        
        self.__kanjis[kanji].append(translation)
        
    def get_kanjis(self, kanji: str):
        if not kanji in self.__kanjis:
            return None

        return self.__kanjis[kanji]
    
    def get_translation(self, translation: str):
        translation_lower = translation.lower()  # Handle case-insensitive search
        for kanji, translations in self.__kanjis.items():
            for full_translation in translations:
                # Split by commas, then by spaces
                phrases = full_translation.split(',')
                for phrase in phrases:
                    words = phrase.strip().split()  # Split by spaces and strip extra spaces
                    if translation_lower in " ".join(words).lower():
                        return kanji
        return None
    
    def all_kanjis(self):
        return self.__kanjis
    
    

    def __str__(self):
        return f' this book has the following kanjis: {self.__kanjis}'

class JapRecordApplication:
    def __init__(self, storage_service):

        """
        Initializes a new JapRecordApplication with the given storage service, and initializes its kanjibook.
        
        Args:
            storage_service (FileHandler): The storage service to use for storing and loading the kanjibook.
        """

        self.__kanjibook = KanjiBook()
        self.__storage_service = storage_service
        
        
       
        for kanji, translations in self.__storage_service.load_file().items():
            for translation in translations:
                self.__kanjibook.add_kanji(kanji, translation)
                
        for kanji, translations in self.__storage_service.load_learning_file().items():
            for translation in translations:
                self.__kanjibook.add_kanji(kanji, translation)

    def help(self):
        print("commands:")
        print("'help' - print this menu")
        print("0 - exit")
        print("1 - add entry")
        print("2 - search by kanji")
        print("3 - search by translation")
        print("4 - learn a new kanji")
        print("5 - list all entries")
        
    def exit_app(self):
        self.__storage_service.save_file(self.__kanjibook.all_kanjis())
        print("Bye!")
        exit()
        
    def add_entry(self):
        kanji = input("Kanji: ")
        translation = input("Translation: ")
        self.__kanjibook.add_kanji(kanji, translation)

    def search(self):
        word = input("Search kanji: ")
        kanjis = self.__kanjibook.get_kanjis(word)
        if kanjis == None:
            print("Kanji not found")
        else:
            for kanji in kanjis:
                print(kanji)
                
    def search_by_translation(self):
        word = input("Search translation: ")
        translation = self.__kanjibook.get_translation(word)
        if translation == None:
            print("Translation not found")
        else:
            print(translation)
            
    def learn_kanji(self):
        kanji = random.choice(list(self.__kanjibook.all_kanjis()))  # Use list() to convert dict_keys to list
        print(kanji)
                
    def get_all_kanjis(self):
        print(self.__kanjibook)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("Command: ")
            if command == "help":
                self.help()
            elif command == "0":
                self.exit_app()
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.search_by_translation()
            elif command == "4":
                self.learn_kanji()
            elif command == "5":
                self.get_all_kanjis()
                # print(self.__kanjibook)
            else:
                print("Invalid command")
                self.help()


                
if __name__ == "__main__": 
    storage_service = FileHandler("kanjibook.txt", "50_kanji.txt")      
    kanjibook = JapRecordApplication(storage_service)
    kanjibook.execute()
