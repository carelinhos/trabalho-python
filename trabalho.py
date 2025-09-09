import csv

class Cliente:
    def __init__(self, nome, banco, agencia, conta, saldo):
        self.nome = nome
        self.banco = banco
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.extrato = []  # agora inicializado

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

    @staticmethod
    def processar_lote(arquivo, clientes):
        with open(arquivo, newline="", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                operacao = linha["operacao"]
                nome = linha["nome"]
                valor = float(linha["valor"])
                destino = linha.get("destino", "")

                cliente = clientes.get(nome)

                if not cliente:
                    print(f"Cliente {nome} não encontrado no sistema.")
                    continue

                if operacao == "deposito":
                    cliente.deposita(valor)
                elif operacao == "saque":
                    cliente.saca(valor)
                elif operacao == "transferencia" and destino in clientes:
                    cliente.transfere(valor, clientes[destino])
                else:
                    print(f"Operação inválida ou cliente de destino não encontrado: {linha}")


# --- Teste manual ---
c1 = Cliente("Miguel Souza", "Santander", 7688, "75478-8", 13090.47)
c2 = Cliente("Gabriel Costa", "Banco do Brasil", 2626, "81239-1", 17082.45)

c1.transfere(3000, c2)
c1.mostrar_extrato()
c2.mostrar_extrato()

# Exemplo de como rodar um lote:
# Cliente.processar_lote("lote.csv", {"Miguel Souza": c1, "Gabriel Costa": c2})
