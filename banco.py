
dados_cliente = []
numero_conta = 1
numero_agencia = 1

print("Seja bem-vindo ao nosso banco, para começar a usar precisamos de algumas informações.")

def solicitacao_dados_clientes():
 global numero_conta
 nome = (input("Digite seu nome para gente\n-> "))
 cpf = input("Digite seu cpf para gente: (Apenas números.))\n-> ")
 data_nascimento = input("Digite sua data de nascimento: (Apenas números.)\n-> ")
 endereco = (input("Digite seu endereço pra gente: UF/CIDADE\n-> "))

 cliente = {
    "nome": nome,
    "cpf": cpf,
    "data_nascimento": data_nascimento,
    "endereço": endereco,
    "conta": numero_conta,
    "saldo": 0,
    "extrato": "",
    "numeros_saques": 0

  }
 
 dados_cliente.append(cliente)
 numero_conta += 1


 print(f"Sua conta foi criada com sucesso. \n Sua agencia é: {numero_agencia}\n Numero da conta: {numero_conta} ")
 return cliente

cliente_atual = solicitacao_dados_clientes()

menu = f"""
   Olá {cliente_atual['nome']}

   [1] Depositar
   [2] Sacar
   [3] Extrato
   [4] Nova conta
   [0] Sair
   
=> """

LIMITE_SAQUE = 1
LIMITE_SAQUE_VALOR = 500

def depositar(cliente):
    valor = int(input("Digite o valor que deseja depositar: "))
    if valor > 0:
      cliente["saldo"] += valor
      cliente["extrato"] += f"Depósito: R$ {valor:.2f}\n"
    else:
     print("Valor inválido para depósito.")

def sacar(cliente):
    if cliente["numero_saques"] >= LIMITE_SAQUE_VALOR:
        print("Limite de saques diarios atingido.!")
    else:
        saque = int(input("Digite o valor que deseja sacar: "))
        if saque > 0:
            if saque > cliente["saldo"]:
                print("Você não tem saldo suficiente")
            elif saque > LIMITE_SAQUE:
                print("O limite de saque é de: 500 R$")
            else:
                cliente["saldo"] -= saque
                cliente["extrato"] += f"Saque: R$ {saque:.2f}\n"
                cliente["numero_saques"] += 1
        else:
          print("Digite um valor válido para o saque")
def exibir_extrato(cliente):
   mensagem_extrato = f""" =========================

                                {cliente["extrato"]}
                                
                          ========================= 
                          Saldo: R$ {cliente["saldo"]:.2f}
                          """
   print(mensagem_extrato)

def criarconta():
  global cliente_atual
  cliente_atual = solicitacao_dados_clientes()


while True:
    opcao = int(input(menu))

    if opcao == 1:
     depositar(cliente_atual)

    elif opcao == 2:
       sacar(cliente_atual)

    elif opcao == 3:
      exibir_extrato(cliente_atual)

    elif opcao == 4:
       criarconta()

    elif opcao == 0:
        print("Operação finalizada.")
        break

    else:
        print("Opção inválida. Tente novamente.")