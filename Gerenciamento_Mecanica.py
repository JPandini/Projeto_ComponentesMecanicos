pecas = [
    {"nome": "Parafuso", "material": "Aço", "quantidade": 50, "preco": 0.5},
    {"nome": "Porca", "material": "Alumínio", "quantidade": 30, "preco": 0.8},
]

def calcular_tensao():
    F = float(input("Digite a força aplicada (N): "))
    A = float(input("Digite a área (m²): "))
    tensao = F / A
    print(f"A tensão mecânica é {tensao:.2f} Pa")

def cadastrar_peca():
    pass

def consultar_peca():
    pass

def atualizar_estoque():
    pass

def gerar_relatorios():
    pass

while True:
    print("\nMenu:")
    print("1. Cadastrar peça")
    print("2. Consultar peça")
    print("3. Atualizar estoque")
    print("4. Realizar cálculos")
    print("5. Gerar relatórios")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastrar_peca()
    elif escolha == "2":
        consultar_peca()
    elif escolha == "3":
        atualizar_estoque()
    elif escolha == "4":
        calcular_tensao()
    elif escolha == "5":
        gerar_relatorios()
    elif escolha == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")


