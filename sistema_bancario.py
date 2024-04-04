from abc import ABC, abstractclassmethod, abstractproperty

class Transacao (ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar_transacao(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    #TODO: implement
    def registrar_transacao(self, valor):
        pass

class Depositar(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    #TODO: implement
    def registrar_transacao(self, valor):
        pass

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    #TODO: implement
    def realizar_transacao(self, conta, transacao):
        pass

    #TODO: implement
    def adicionar_conta(self, conta):
        pass

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Historico:
    def __init__(self) -> None:
        self._transacoes = []

    #TODO: implement
    @property
    def transacoes(self):
        pass

    #TODO: implement using append method, probably some 
            # information about the transaction may need to be acessed later, so it maybe better to use dictionaries to store this information
    def adicionar_transacoes(self, transacao):
        pass

class Conta:
    def __init__(self, numero_conta, cliente):
        self._saldo = 0
        self._numero_conta = numero_conta
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(self, numero_conta, cliente):
        return Conta(numero_conta, cliente)
    
    #TODO: implement
    def sacar(self, valor):
        pass

    #TODO: implement
    def depositar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite_transacao=1500, limite_saques=5):
        super().__init__(numero_conta, cliente)
        self.limite_transacao = limite_transacao
        self.limite_saques = limite_saques

    #TODO: rewrite sacar() method to adequate the parameters limite_saques and limite_transacoes
    def sacar(self, valor):
        pass

    #TODO: rewrite __str__ method to make it more readable
    def __str__(self) -> str:
        pass
