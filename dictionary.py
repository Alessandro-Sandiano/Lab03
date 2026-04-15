class Dictionary:
    def __init__(self, language):
        self._words_list = list()
        self._language = language

    def load_dictionary(self,path):
        with open(path,'r', encoding="utf-8") as file:
            for line in file:
                self._words_list.append(line.strip())
        file.close()

    def print_all(self):
        print (self._words_list.__str__())


    @property
    def words_list(self):
        return self._words_list

    @property
    def language(self):
        return self._language