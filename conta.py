class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def extrato(self):
        print("saldo {} do titular {}". format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel


    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("passou o valor {} do limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.titular
    #Na linguagem Python, os métodos que dão acesso são nomeados como properties. Desta forma, indicaremos para o Python nossa intenção de ter acesso ao objeto.
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self,limite):
        self.__limite=limite
        return self.__saldo

    @staticmethod
    def codigo_BB():
        return "001"
    @staticmethod
    def codigo_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco":"237"}

    #exemplo de como chamar um objeto.
    #referência é o nome do objeto que você quer chamar
    # o . é referente ao solicitação de acesso
    # descrever a função solicitada
    # exemplo conta_2.extrato()