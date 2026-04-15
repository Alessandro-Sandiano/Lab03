class RichWord:
    def __init__(self, word):
        self._word = word #this is a string
        self._correct = None #this is a bool

    @property
    def word(self):
        return self._word

    @property
    def correct(self):
        #print("getter of word called")
        return self._correct

    @correct.setter
    def correct(self, bool_value):
        #print("setter of word called")
        self._correct = bool_value

    def __str__(self):
        return self._word