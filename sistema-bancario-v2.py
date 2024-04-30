saldo = 0
extrato = []
usuarios = []
contas = []
numero_conta = 1

def sacar(*, valor):

    global saldo
    global extrato
    quantidade_saque = 0
    LIMITE_SAQUE = 3

    if quantidade_saque == 3:

        print('Já atingiu o limite de saque diario!')

    elif valor > 500:

        print('Limite maximo de saque é de R$ 500.00')
        
    elif valor > saldo:

        print('Saldo insuficente!')
        
    elif valor <= saldo:
        print('Aguarde a contagem do dinheiro!')
        saldo -= valor
        quantidade_saque += 1
        descricao_saque = f'Saque no valor R$ {valor:.2f}'
        extrato.append(descricao_saque)
        print(f'Sacado: R$ {valor:.2f}')

    else:
        print('Por favor, digite um valor válido para o saque.')
    
def depositar(valor, /):

    global saldo
    global extrato

    if valor > 0:

        saldo += valor
        descricao_deposito = f'Deposito no valor R$ {valor:.2f}'
        extrato.append(descricao_deposito)
        print(f'Deposito no valor de R$ {valor:.2f} efetuado com sucesso!')

    else:
        print('Por favor, digite um valor válido para o deposito.')

def imprime_extrato():
    
    print(f'Seu saldo atual é de R$ {saldo:.2f}\n')
            
    if len(extrato) == 0:
        print(f'##### Seu extrato bancario: #####\n')
        print('Nenhuma transação efetuada no momento!!')
        
    else:
        print(f'##### Seu extrato bancario: #####\n')
        for ext in extrato:
            print(ext)

def cadastrar_usuario(*, nome, data_nascimento, cpf, endereco):
    
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF já cadastrado!")
    else:
        usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
        print("Usuário cadastrado com sucesso!")

def criar_conta(cpf_usuario):

    global numero_conta

    if any(usuario['cpf'] == cpf_usuario for usuario in usuarios):
        conta = {'agencia': "0001", 'numero_conta': numero_conta, 'usuario': cpf_usuario}
        contas.append(conta)
        numero_conta += 1
        print(f"Conta cadastrada com sucesso! Número da conta: {conta['numero_conta']}")
    
    else:
        print("Usuário não encontrado!")


menu_principal = """
    Menu!!!

    [1] cadastrar usuário
    [2] criar conta
    [3] entrar
    [0] sair
"""

while True:

    opcao = int(input(menu_principal))
    print(opcao)

    if opcao == 1:

        print("Informe seus dados!!\n")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        cpf = input("CPF: ")
        endereco = input("Endereço (logradouro, nro - bairro - cidade/estado): ")

        cadastrar_usuario(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    if opcao == 2:

        print("Informe o cpf para criar sua conta!!\n")
        cpf = input("CPF: ")

        criar_conta(cpf_usuario=cpf)

    if opcao == 3:
        
        cpf_usuario = input("Informe o cpf para entrar na sua conta!!\n")
        if any(usuario['cpf'] == cpf_usuario for usuario in usuarios):
        
            menu = """
                Menu!!!

                [1] sacar
                [2] depositar
                [3] Extrato
                [0] Sair

            """

            while True:
                
                opcao = int(input(menu))
                print(opcao)

                if opcao == 1:

                    saque = float(input('Valor do saque: '))
                    sacar(valor=saque)
                    
                
                elif opcao == 2:

                    deposito = float(input('Valor do deposito:'))
                    depositar(deposito)
                
                elif opcao == 3:
                    imprime_extrato()

                elif opcao == 0:
                    break

                else:
                    print('Por favor, digite uma opção válida!!.')
            
        else:
            print("Conta não encontrado!")
    
    elif opcao == 0:
        break

    else:
        print('Por favor, digite uma opção válida!!.')