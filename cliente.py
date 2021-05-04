class Cliente:
    def __init__(self, none):
        self.__none = none

    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__none.title()
    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome= nome


