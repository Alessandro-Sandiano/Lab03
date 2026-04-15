class Dictionary:
    def __init__(self):
        self._words_list = list()

    def load_dictionary(self, path):
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                self._words_list.append(line.strip())

    def print_all(self):
        for w in self._words_list: print(w)

    @property
    def words_list(self):
        return self._words_list