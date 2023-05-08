class ContaBancaria:

    def __init__(self, numero_conta, numero_agencia, saldo):
        self.numero_conta = numero_conta
        self.numero_agencia = numero_agencia
        self.saldo = saldo
        
    def deposito(self, valor):
        if(valor > 0):
            self.saldo += valor
        else:
            print("Valor para depósito inválido para depósito")
            
    def saque(self, valor):
        if(valor <= 0):
            print("Valor inválido para saque")
        if(valor > self.saldo):
            print("Saldo insuficiente na conta")
        if(valor > 0 and valor <= self.saldo):
            self.saldo -= valor       
            
    def __str__(self):
        return f'Ag: {self.numero_agencia}, conta: {self.numero_conta}, saldo: {self.saldo}'
    
    def mesma_agencia(self, outro):
        if(self.numero_agencia == outro.numero_agencia):
            print(f'Contas {self.numero_conta} e {outro.numero_conta} são da mesma agência')
        else:
            print(f'Contas {self.numero_conta} e {outro.numero_conta} não são da mesma agência')
        

def main():
    c1 = ContaBancaria(100, 2, 1000.0)
    c2 = ContaBancaria(200, 8, 500.0)
    c3 = ContaBancaria(300, 2, 2000.0)

    c1.deposito(-5) # valor inválido para depósito
    c1.saque(-5) # valor inválido para saque
    print(c1)

    c1.deposito(100)
    c1.saque(1200) # saldo insuficiente
    c1.saque(600)
    print(c1)

    c1.mesma_agencia(c2) # não têm mesma agência
    c1.mesma_agencia(c3) # têm mesma agência

if __name__ == '__main__':
    main()