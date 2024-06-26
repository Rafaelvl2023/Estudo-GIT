# Estacionamento

class Estacionamento:
    def __init__(self):
        self.beco = []  # Pilha principal do estacionamento
        self.rua = []   # Pilha auxiliar (rua)

    def entrar_estacionamento(self, carro):
        self.beco.append(carro)
        print(f"Carro {carro} entrou no estacionamento.")

    def sair_estacionamento(self, placa):
        carro_removido = None
        for i in range(len(self.beco)):
            if self.beco[i]["placa"] == placa:
                carro_removido = self.beco.pop(i)
                print(f"Carro {carro_removido} saiu do estacionamento.")
                break

        if carro_removido is None:
            print(f"Carro com a placa {placa} não está no estacionamento.")
            return

        # Movendo carros da rua de volta para o estacionamento
        while self.rua:
            veiculo = self.rua.pop()
            self.beco.append(veiculo)
            print(f"Carro {veiculo} voltou para o estacionamento.")

# Função para exibir o menu
def exibir_menu():
    print("\n### MENU DO ESTACIONAMENTO ###")
    print("1. Entrar veículo no estacionamento")
    print("2. Retirar veículo do estacionamento")
    print("3. Sair")
    print("##############################")

# Função principal
def main():
    estacionamento = Estacionamento()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            placa = input("Digite a placa do carro para entrar no estacionamento: ")
            carro = {"placa": placa}
            estacionamento.entrar_estacionamento(carro)
        elif opcao == "2":
            placa = input("Digite a placa do carro para sair do estacionamento: ")
            estacionamento.sair_estacionamento(placa)
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

