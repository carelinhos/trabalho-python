




class cliente:
 def __init__(self, nome, banco,agencia,conta,saldo):
        self.nome = nome
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.saldo= saldo
 def deposita(self,valor):
     self.saldo += valor
     print("Depositando R$" , valor , " na conta de ",self.nome)
     print(self.saldo)


 def saca(self,valor):
        if self.saldo >= valor:
           self.saldo -= valor;
           print("Sacando R$" , valor , " da conta de " ,self.nome)
           return 1
        else:
          print("Saldo insuficiente para saque de R$" , valor , " na conta de ",self.nome)
          return 0


 def transfere ( self,valor, destino):
        if self.saldo >= valor:
           self.saldo -= valor
           print("Imprimindo a conta de destino: " , destino.nome)
           destino.deposita(valor)
           print("Transferindo R$" , valor , " da conta de ",self.nome, " para a conta de " + destino.nome)
           return 1
        else:
            print("Saldo insuficiente para transferência de R$" , valor , " da conta de " , self.nome, " para a conta de " , destino.nome);
            return 0



c1=cliente("Miguel Souza","Santander",7688,"75478-8",13090.47)
c2=cliente("Gabriel Costa","Banco do Brasil",2626,"81239-1",17082.45)

c1.transfere(3000,c2)
print(c1.saldo)

