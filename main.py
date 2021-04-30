numero = 123
titular = "Nico"
saldo = 55.0
limite = 1000.0
conta = {"numero": 123, "titular": "Nico", "saldo": 55.0, "limite": 1000.0}
def cria_conta(numero, titular, saldo, limite):
    conta= {"numero":numero, "titular": titular, "saldo": saldo, "limite":limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo {} do titular {}".format(self.saldo, self.titular))
