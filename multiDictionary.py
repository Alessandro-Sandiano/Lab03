import dictionary as d
import richWord as rW


class MultiDictionary:

    def __init__(self):
        self._dict = [d.Dictionary("Italian"), d.Dictionary("English"), d.Dictionary("Spanish")]
        for i in range(len(self._dict)):
            self._dict[i].load_dictionary(f"resources/{self._dict[i].language}.txt")

    def print_dic(self, language):
        for i in range(len(self._dict)):
            if self._dict[i].language == language:
                self._dict[i].print_all()

    def search_word(self, words, language):
        i=0
        for i in range(len(self._dict)):
            if self._dict[i].language == language: break
        rich_word_list = list()
        for w in words:
            rich_word = rW.RichWord(w)
            if self._dict[i].words_list.__contains__(w): rich_word.corretta = True
            rich_word_list.append(rich_word)
        return rich_word_list

    def search_word_linear(self, words, language):
        i = 0
        for i in range(len(self._dict)):
            if self._dict[i].language == language: break
        rich_word_list = list()
        for w in words:
            rich_word = rW.RichWord(w)
            counter = 0
            while counter < len(self._dict[i].words_list):
                if w == self._dict[i].words_list[counter]:
                    rich_word.corretta = True
                    break
                counter += 1
            rich_word_list.append(rich_word)
        return rich_word_list

    def search_word_dichotomic(self, words, language):
        i = 0
        for i in range(len(self._dict)):
            if self._dict[i].language == language: break
        rich_word_list = list()
        for w in words:
            rich_word = rW.RichWord(w)
            # se len(self._dict[i].words_list) è dispari, si dimezza un numero pari e si prende esattamente l'elemento mediano;
            # se len(self._dict[i].words_list) è pari, si dimezza un numero dispari e l'arrotondamento avviene alternatamente per difetto o per eccesso
            mean = round((len(self._dict[i].words_list)-1) / 2)
            index = mean
            already_checked = set()
            while True:
                already_checked.add(index)
                if w < self._dict[i].words_list[index]:
                    # il valore minimo di mean con cui si può uscire da questo ciclo è 1
                    while index - round(mean/2) < 0:
                        mean = round(mean/2)
                    # index-round(mean/2)>=0 è garantito dal ciclo precedente. Tuttavia, non ho trovato casi in cui tale ciclo sia necessario.
                    # La condizione seguente è equivalente a if mean > 1:
                    if not already_checked.__contains__(index - round(mean / 2)):
                        mean = round(mean/2)
                        index -= mean
                    elif index - 1 >= 0 and not already_checked.__contains__(index - 1):
                        index -= 1
                    else: break
                elif w > self._dict[i].words_list[index]:
                    # il valore minimo di mean con cui si può uscire da questo ciclo è 1
                    while index + round(mean/2) > len(self._dict[i].words_list) - 1:
                        mean = round(mean/2)
                    # index+round(mean/2)<=len(self._dict[i].words_list)-1 è garantito dal ciclo precedente.
                    # Necessario, ad esempio, per len(self._dict[i].words_list)==12, len(self._dict[i].words_list)==23 e len(self._dict[i].words_list)==24.
                    # La condizione seguente è equivalente a if mean > 1:
                    if not already_checked.__contains__(index + round(mean / 2)):
                        mean = round(mean/2)
                        index += mean
                    elif index + 1 <= len(self._dict[i].words_list) - 1 and not already_checked.__contains__(index + 1):
                        index += 1
                    else:
                        break
                # elif w == self._dict[i].words_list[index]:
                else:
                    rich_word.corretta = True
                    break
            rich_word_list.append(rich_word)
        return rich_word_list