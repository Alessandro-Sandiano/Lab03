import time
import multiDictionary as mD

class SpellChecker:

    def __init__(self):
        self._multiDict = mD.MultiDictionary()

    def handle_sentence(self, txt_in, language):
        txt_in = replace_chars(txt_in).lower().split()

        # Contains
        toc = time.time()
        rich_word_list = self._multiDict.search_word(txt_in, language)
        tic = time.time()
        wrong_words = [w for w in rich_word_list if w.corretta == False]
        string = "--------------------------\nUsing contains\n"
        for w in wrong_words:
            string += w.__str__() + "\n"
        string += f"\nTime elapsed: {tic-toc}\n"

        # Linear search
        string += "--------------------------\nUsing Linear search\n"
        toc = time.time()
        rich_word_list = self._multiDict.search_word_linear(txt_in, language)
        tic = time.time()
        wrong_words = [w for w in rich_word_list if w.corretta == False]
        for w in wrong_words:
            string += w.__str__() + "\n"
        string += f"\nTime elapsed: {tic - toc}\n"

        # Dichotomic Search
        string += "--------------------------\nUsing Dichotomic search\n"
        toc = time.time()
        rich_word_list = self._multiDict.search_word_dichotomic(txt_in, language)
        tic = time.time()
        wrong_words = [w for w in rich_word_list if w.corretta == False]
        for w in wrong_words:
            string += w.__str__() + "\n"
        string += f"\nTime elapsed: {tic - toc}\n"
        return string

    @staticmethod
    def print_menu():
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replace_chars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~\""
    for c in chars:
        text = text.replace(c, "")
    return text