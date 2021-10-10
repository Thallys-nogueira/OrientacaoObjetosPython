
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo o objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel_saque = (self.__saldo + self.__limite)
        return valor <= valor_disponivel_saque

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassou o limite".format(valor))

    def tranfere(self, valor, conta_destino):
        self.saca(valor)
        conta_destino.deposita(valor)
        print("Transferência de R${} reais  de {} para {} concluída com sucesso!".format(valor, self.__titular,
                                                                                         conta_destino.get_titular()))

    # Funções gets e setters em python podem ser feitas do seguinte modo:
    ## coloca os atributos como privados utilizando __
    ### para funções gets, utiliza-se o mesmo nome do atributo adicionando @property antes da função
    ### para funções sets, utiliza-se o mesmo nome do atributo adicionando @nome_atributo.setter
    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__titular = limite

    # Método estático da classe, não precisa de um objeto criado
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_banco():
        codigos = {"BB":'001', "Caixa":'104', "Bradesco":'237'}
        return codigos