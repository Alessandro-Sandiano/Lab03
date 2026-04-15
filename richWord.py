class RichWord:
    def __init__(self, parola):
        self._parola = parola # this is a string
        self._corretta = False # this is a bool

    @property
    def corretta(self):
        # print("getter of parola called")
        return self._corretta

    @corretta.setter
    def corretta(self, bool_value):
        # print("setter of parola called")
        self._corretta = bool_value

    def __str__(self):
        return self._parola