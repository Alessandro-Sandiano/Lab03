import dictionary as d
import richWord as rW

class MultiDictionary:

    def __init__(self):
        self._italian = d.Dictionary()
        self._italian.load_dictionary("resources/Italian.txt")
        self._english = d.Dictionary()
        self._english.load_dictionary("resources/English.txt")
        self._spanish = d.Dictionary()
        self._spanish.load_dictionary("resources/Spanish.txt")

    def print_dic(self, language):
        # match language:
        #     case "italian": self._italian.print_all()
        #     case "english": self._english.print_all()
        #     case "spanish": self._spanish.print_all()
        getattr(self, f"_{language}").print_all()

    def search_word(self, words, language):
        rich_words = list()
        for w in words: rich_words.append(rW.RichWord(w))
        for r_w in rich_words:
            if getattr(self, f"_{language}").words_list.__contains__(r_w.word): r_w.correct = True
            else: r_w.correct = False
        return rich_words

    def search_word_linear(self, words, language):
        rich_words = list()
        for w in words: rich_words.append(rW.RichWord(w))
        for r_w in rich_words:
            r_w.correct = False
            for word in getattr(self, f"_{language}").words_list:
                if r_w.word == word:
                    r_w.correct = True
                    break
        return rich_words

    def search_word_dichotomic(self, words, language):
        rich_words = list()
        for w in words: rich_words.append(rW.RichWord(w))
        for r_w in rich_words:
            r_w.correct = False
            minimum = 0
            maximum = getattr(self, f"_{language}").words_list.__len__()
            half = int((maximum - minimum) / 2)
            # (maximum-minimum != 1) instead of (maximum-minimum > 1 or maximum == 1)
            # is enough if getattr(self, f"_{language}").words_list.__len__() > 1
            # because getattr(self, f"_{language}").words_list.__len__() == 1
            # is the only case in which maximum == 1 at the beginning and
            # maximum-minimum can be zero (i.e. if r_w.word < getattr(self, f"_{language}").words_list[half])
            while maximum-minimum > 1 or maximum == 1:
                if r_w.word == getattr(self, f"_{language}").words_list[half]:
                    r_w.correct = True
                    break
                if r_w.word < getattr(self, f"_{language}").words_list[half]:
                    maximum = half
                    half -= int((maximum - minimum) / 2)
                if r_w.word > getattr(self, f"_{language}").words_list[half]:
                    minimum = half
                    half += int((maximum - minimum) / 2)
                if maximum == 1:
                    if r_w.word == getattr(self, f"_{language}").words_list[0]: r_w.correct = True
                    break
        return rich_words
                    




