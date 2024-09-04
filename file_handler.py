class FileHandler():
    def __init__(self, filename, filename2):

        """
        Initializes a new FileHandler with the given filenames, and sets the corresponding
        filenames as instance variables.
        
        Args:
            filename (str): The filename to load the kanjibook from.
            filename2 (str): The filename to load the learning kanjibook from.
        """

        self.__filename = filename
        self.__filename2 = filename2
        
    def load_file(self):
        kanjis = {}
        with open(self.__filename,  encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                kanji, *translation = parts
                kanjis[kanji] = translation
                
        return kanjis
    
    def load_learning_file(self):
        kanjis = {}
        with open(self.__filename2,  encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                kanji, *translation = parts
                kanjis[kanji] = translation
        return kanjis
    
    def save_file(self, kanjibook: dict):
        with open(self.__filename, "w", encoding="utf-8") as f:
            for kanji, translations in kanjibook.items():
                line = [kanji] + translations
                f.write(";".join(line) + "\n")