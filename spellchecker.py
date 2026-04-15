import time
import multiDictionary as mD

class SpellChecker:

    def __init__(self):
        self._multi_dictionary = mD.MultiDictionary()

    def handle_sentence(self, txt_in, language):
        words = list()
        for w in txt_in.split(): words.append(replace_chars(w.lower()))

        t1 = time.time()
        rich_words = self._multi_dictionary.search_word(words, language)
        t2 = time.time()
        s = "------------------------------\nUsing contains\n"
        for r_w in rich_words:
            if r_w.correct is False: s += r_w.word + "\n"
        s += "Time elapsed: " + str(t2 - t1) + "\n------------------------------\n"

        t1 = time.time()
        rich_words = self._multi_dictionary.search_word_linear(words, language)
        t2 = time.time()
        s += "Using Linear search\n"
        for r_w in rich_words:
            if r_w.correct is False: s += r_w.word + "\n"
        s += "Time elapsed: " + str(t2 - t1) + "\n------------------------------\n"

        t1 = time.time()
        rich_words = self._multi_dictionary.search_word_dichotomic(words, language)
        t2 = time.time()
        s += "Using Dichotomic search\n"
        for r_w in rich_words:
            if r_w.correct is False: s += r_w.word + "\n"
        s += "Time elapsed: " + str(t2 - t1) + "\n\n\n"
        return s



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

    @property
    def multi_dictionary(self):
        return self._multi_dictionary

def replace_chars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text