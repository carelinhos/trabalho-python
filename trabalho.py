import csv

with open("cadastro.csv", "r", encoding="utf-8") as arquivo:
    conteudo = csv.reader(arquivo)






class Cliente:
    def __init__(self, nome, banco, agencia, conta, saldo):
        self.nome = nome
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.extrato = []

    def registrar_extrato(self, descricao):
        self.extrato.append(descricao)

    def deposita(self, valor):
        self.saldo += valor
        descricao = f"Depósito de R$ {valor:.2f}"
        self.registrar_extrato(descricao)
        print(descricao, "na conta de", self.nome)

    def saca(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            descricao = f"Saque de R$ {valor:.2f}"
            self.registrar_extrato(descricao)
            print(descricao, "na conta de", self.nome)
            return 1
        else:
            print("Saldo insuficiente para saque de R$", valor, "na conta de", self.nome)
            return 0

    def transfere(self, valor, destino):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.deposita(valor)
            descricao = f"Transferência de R$ {valor:.2f} para {destino.nome}"
            self.registrar_extrato(descricao)
            destino.registrar_extrato(f"Transferência recebida de R$ {valor:.2f} de {self.nome}")
            print(descricao, "da conta de", self.nome)
            return 1
        else:
            print("Saldo insuficiente para transferência de R$", valor, "da conta de", self.nome, "para a conta de", destino.nome)
            return 0

    def mostrar_saldo(self):
        print(f"Saldo atual de {self.nome}: R$ {self.saldo:.2f}")

    def mostrar_extrato(self):
        print(f"\nExtrato de {self.nome}:")
        for item in self.extrato:
            print(" -", item)
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")


    while True:
     print("extrato 0")
     print("tranferencia 1")
     print("saque 2")
     print("deposito 3")
     print("saldo 4")
     print("sair 5")

     ação = int(input("escolha uma opçao:"))

     if (ação == 0):
      nome=input("nome do cliente: ")
      agencia=int(input("agencia do cliente: "))
      banco=input("banco do cliente: ")
      extrato=nome.mostrar_extrato()
      print(extrato)

      if(ação == 1):
          nome = input("nome do cliente: ")
          agencia = int(input("agencia do cliente: "))
          banco = input("banco do cliente: ")
          nome2 = input("nome do cliente: ")
          agencia2 = int(input("agencia do cliente: "))
          banco2 = input("banco do cliente: ")
          transfere(nome, agencia)

      if (ação ==2):
          nome = input("nome do cliente: ")
          agencia = int(input("agencia do cliente: "))
          banco = input("banco do cliente: ")
          saca()

     if (ação == 3):
         nome = input("nome do cliente: ")
         agencia = int(input("agencia do cliente: "))
         banco = input("banco do cliente: ")
         deposita()

     if ação == 4:
         nome = input("nome do cliente: ")
         agencia = int(input("agencia do cliente: "))
         banco = input("banco do cliente: ")
         mostrar_saldo()


     if(banco == 5):
         break



c1 = Cliente("Miguel Souza", "Santander", 7688, "75478-8", 13090.47)
c2 = Cliente("Gabriel Costa", "Banco do Brasil", 2626, "81239-1", 17082.45)

c1.transfere(3000, c2)
c1.mostrar_extrato()
c2.mostrar_extrato()

