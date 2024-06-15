"""
Restrições:

* A segunda versão do projeto trabalha com duas novas funções: criar usuário (cliente) e criar conta corrente (vincular com o usuário);
	* Criar usuário: O programa deve armazenar os usuários em uma lista, e cada usuário é composto por:
		* Nome, data de nascimento, cpf e endereço, sendo que endereço é uma string com formato: logradouro, numero - bairro - cidade/uf.
		* Deve ser armazenado apenas os números do CPF, sem caracteres especiais, e não podem ter usuários com o mesmo cpf.
	* Criar conta: O programa deve armazenar as contas em uma lista.
		* Conta é composta por: agencia, numero da conta, e usuário. O numero da conta é sequencial, iniciando em 1. O número da agencia é fixo = "0001".
		* Cada usuário pode ter mais de uma conta, mas cada conta só pode ter um usuário;
* Todas as operações do sistema devem ser realizadas através de funções;
* Para efeito de estudo, cada função vai ter que receber os argumentos com uma regra de passagem diferente, o retorno pode ser feito da maneira como preferir;
	* A função de saque vai ser keyword only;
	* A função de depósito vai ser positional only;
	* A função de extrato deve receber uma parte positional (saldo), e uma parte por keyword (extrato).
* O sistema deve permitir apenas depósitos de valores positivos;
* Existe uma limitação de 3 saques por dia, excedido o limite, o sistema não deve permitir outro saque;
* Existe uma limitação de R$500,00 por saque, mais do que isso o sistema não deve permitir sacar;
* Não existe cheque especial nesta versão, assim que, sem saldo não é possível realizar saques;
* O sistema deve armazenar as transações efetuadas, e possibilitar que o usuário veja o histórico de transações realizadas (saques + depósitos);
* Os valores devem ser exibidos utilizando o formato R$ 000.00.
"""
from datetime import date, datetime, date

usuarios = []
contas = []
opcao = "y"
saldo = 150
saques_feitos_hoje = 0
data_ultimo_saque = ""
data_ultimo_deposito = ""
limite_saques_diarios = 3
limite_por_operacao = 500
extrato_operacao = "" 
# Menu principal
menu = """
        Digite [d] para fazer um depósito;
        Digite [s] para fazer um saque;
        Digite [e] para ver o extrato de operações;
        Digite [u] para cadastrar um novo usuário;
        Digite [c] para cadastrar uma nova conta corrente para um usuário existente;
        Digite [v] para acessar a lista de usuários cadastrados;
        Digite [b] para acessar a lista de contas por CPF;
        Digite [x] para sair da aplicação;
"""

data_hoje = date.today()

def validar_deposito(valor_deposito,/, saldo):
    # Função para garantir que o depósito é um valor positivo e válido
    while valor_deposito <= 0:
        valor_deposito = int(input("Você não pode fazer um depósito de valor nulo ou negativo. Por favor, digite um valor válido para depósito: "))
        
    return valor_deposito

def coletar_nome():
    # Garante que o nome passado no cadastro não está vazio
    nome = input("Digite o nome do completo do usuário a ser cadastrado:\n")
    while nome == "":
        nome = input("Você não pode cadastrar uma conta sem nome. Por favor, digite um nome válido: \n")
    return nome

def coletar_logradouro():
    # Garante que o logradouro passado no cadastro não está vazio
    logradouro = input("Digite o logradouro: \n")
    while logradouro == "":
        logradouro = input("Você não pode cadastrar um endereço vazio. Por favor, digite um logradouro válido: \n")
    return logradouro

def coletar_cidade():
    # Garante que o nome da cidade passado no cadastro não está vazio
    cidade = input("Digite o nome da cidade: \n")
    while cidade == "":
        cidade = input("Você não pode cadastrar uma cidade vazia. Por favor, digite um nome de cidade válido: \n")
    return cidade

def coletar_bairro():
    # Garante que o nome do bairro passado no cadastro não está vazio
    bairro = input("Digite o nome do  bairro: \n")
    while bairro == "":
        bairro = input("Você não pode cadastrar um bairro vazio. Por favor, digite um nome de bairro válido: \n")
    return bairro

def coletar_numero():
    # Garante que o número passado no cadastro não está vazio
    numero = input("Digite o número da residência/estabelecimento: \n")
    while numero == "":
        numero = input("Você não pode cadastrar um endereço com número vazio. Se não houver numeração, digite 'S/N': \n")
    return numero

def coletar_UF():
    # Garante que a UF passada no cadastro não está vazia, e tem apenas duas letras
    uf = input("Digite a UF:(SP) \n")
    while uf == "" or len(uf)>2 or uf.isalpha == False:
        uf = input("A UF precisa conter apenas duas letras. Digite uma UF válida: \n")
    return uf


def validar_cpf():
    # Garante que o CPF passado tem 11 dígitos numericos
    cpf =input(("Digite um CPF válido (apenas números):\n"))
    while len(cpf) <11 or not cpf.isdigit():
        cpf = input("O CPF precisa conter somente números, sem caracteres especiais. Por favor, digite um CPF válido:\n")    
    return cpf

def verificar_cpf_existe(cpf):
    # Busca CPF na base de usuários
    for usuario in usuarios:
        if cpf == usuario[0]:
            return True
    return False

def coletar_dados_usuario():
    # Coleta dos dados do usuário para cadastro inicial
    print("Para começar, precisamos do CPF do usuário.")
    cpf = validar_cpf()
    nome = coletar_nome()
    data_nascimento = input("Digite a data de nascimento do usuário: \n")
    logradouro = coletar_logradouro()
    numero = coletar_numero()
    bairro = coletar_bairro()
    cidade = coletar_cidade()
    uf = coletar_UF()     
    endereco = logradouro + ", " + numero + " - " + bairro + " - " + cidade + " / " + uf

    return cpf, nome, data_nascimento, endereco


def cadastrar_conta(contas):
    # pede e valida o cpf para cadastro da conta  
    cpf_nova_conta = validar_cpf()
    # Se existe o cpf, faz o cadastro
    if verificar_cpf_existe(cpf_nova_conta) == True:
        num_conta = len(contas)+1
        agencia = "0001"
        nova_conta = [cpf_nova_conta, agencia, num_conta]
        contas.append(nova_conta)
        print("Conta cadastrada com sucesso!")
    # Se não existe, avisa 
    else:
        print("O CPF digitado não existe em nossa base de dados. Não é possível abrir uma conta para um CPF não cadastrado. Favor, verificar.")


def validar_saque(valor_saque,*, saldo):

    # Valida se o valor do saque é positivo e menor do que 500
    while valor_saque <= 0 or valor_saque > limite_por_operacao:
        valor_saque = float(input(f"Você não pode sacar um valor nulo ou negativo, e também não pode sacar mais de R${limite_por_operacao} por operação. Por favor digite um valor válido para saque: "))
    # Valida se tem saldo suficiente para fazer o saque
    if valor_do_saque > saldo:
        #caso negativo, informa o usário e devolve o teste como falso
        print(f"Você não pode sacar R${valor_saque:.2f}, pois seu saldo é insuficiente. Você possui apenas R${saldo:.2f} de saldo")
        return False, valor_saque
    # Se passou em todos os testes, retorna true com o valor validado
    return True, valor_saque
    
def validar_limite_trx_diario(data_hoje, data_ultimo_saque, /,limite_saques_diarios, *,saques_feitos_hoje):
    # Valida se o usuário n excedeu o limite diário de trx
    if data_ultimo_saque == data_hoje:
        # Se a data de hoje for igual a do ultimo saque, significa que não é a primeira vez que sacam, por isso valida se a quantidade está dentro
        if (saques_feitos_hoje + 1)> limite_saques_diarios:
            print(f"Você não pode fazer esta operação por ter excedido a quantidade de {limite_saques_diarios} saques diários. Mais informações, procure o gerente da sua conta.")
            return False, saques_feitos_hoje, data_ultimo_saque
    # Se a data for diferente, é o primeiro saque do dia, não pode barrar
    saques_feitos_hoje += 1
    
    return True, saques_feitos_hoje, data_ultimo_saque
    


# Inicia a operação com o usuário

print(menu)
opcao = input("Digite a opção desejada: ")[0].lower()
while opcao != "00000":

    if opcao == "d":
        #Realiza depósito
        deposito = float(input("Digite o valor do depósito: "))
        deposito = validar_deposito(deposito, saldo)
        saldo+=deposito
        extrato_operacao += f"Depósito: R${deposito:.2f} - Data: {data_hoje}\n"
        data_ultimo_deposito = date.today()
        print(f"Depósito de R$ {deposito} realizado com sucesso!\n Seu saldo atual é de R$ {saldo:.2f}.\nDeseja fazer outra operação?")
        # Retorna ao menu principal
        print(menu)
        opcao = input("Digite a opção desejada: ")[0].lower()
        continue
    elif opcao == "s":
        # Realiza saque
        valor_do_saque = float(input("Digite o valor a ser sacado: "))
        teste_de_valor, valor_a_ser_sacado = validar_saque(valor_do_saque, saldo)
        teste_de_limite, saques_feitos_hoje, data_ultimo_saque = validar_limite_trx_diario(data_hoje, data_ultimo_saque, limite_saques_diarios, saques_feitos_hoje)
        if teste_de_valor == True and teste_de_limite == True:
            data_ultimo_saque = data_hoje
            saldo -= valor_a_ser_sacado
            extrato_operacao += f"Saque: R${valor_a_ser_sacado:.2f} - Data: {data_hoje}\n"
            print(f"Saque de R$ {valor_a_ser_sacado} realizado com sucesso!\nSeu saldo atual é de R$ {saldo:.2f}.\n Retire seu dinheiro no local indicado.")
        # Retorna ao menu principal
        print("Deseja fazer outra operação?")
        print(menu)
        opcao = input("Digite a opção desejada: ")[0].lower()
        continue


    elif opcao == "e":
        #Mostra o extrato bancário

        print(" EXTRATO BANCÁRIO ".center(100,"*"))
        print(f"DATA: {data_hoje}")
        print(f"SALDO ATUAL: R${saldo:.2f}")
        print(" DETALHE DE MOVIMENTAÇÕES ".center(100,"*"))
        

        # Verifica se o extrato está vazio ou não antes de exibir os resultados
        if extrato_operacao == "":
            print("Você não possui operações realizadas nesta conta.")

            print(f"SALDO ATUAL: R${saldo:.2f}")
        else:
            print(extrato_operacao)

        print(" OBRIGADO ".center(100,"*"))
        # Retorna ao menu principal
        print("Deseja fazer outra operação?")
        print(menu)
        opcao = input("Digite a opção desejada: ")[0].lower()
        continue
    
    elif opcao == "u":
        #Cadastra novos usuários
        print("Iniciando cadastro de USUÁRIOS...")
        cpf, nome, data_nascimento, endereco = coletar_dados_usuario()

        #Verifica se o CPF já existe na base pra n permitir duplicação
        if verificar_cpf_existe(cpf) == False:
            usuarios.append([cpf, nome, data_nascimento, endereco])
            print("Usuário cadastrado com sucesso! Voltando ao menu principal...")
            print(menu)
            opcao = input("Digite a opção desejada: ")[0].lower()
            continue
        # Se existir, informa o erro
        else:
            print("ERRO! Já existe um usuário com este cpf em nossa base de dados. Voltando ao menu principal.")
            # Retorna ao menu principal
            print(menu)
            opcao = input("Digite a opção desejada: ")[0].lower()
            continue

    elif opcao == "v":
        # Exibe lista de usuários cadastrados
        print(" USUÁRIOS CADASTRADOS ".center(100,"*"))
        for usuario in usuarios:
            
            print(f'CPF:{usuario[0]} - Nome: {usuario[1]} - Data de Nascimento: {usuario[2]} - Endereço: {usuario[3]} \n')
            print("-"*100)
        print(" FIM DA LISTA ".center(100,"*"))
        # Retorna ao menu principal
        print("Deseja fazer outra operação?")
        print(menu)
        opcao = input("Digite a opção desejada: ")[0].lower()
        continue
    
    elif opcao == "c":
        # Cadastra contas correntes para usuários já cadastrados
        print("Iniciando cadastro de contas para usuários...")
        cadastrar_conta(contas)
        # Retorna ao menu principal
        print("Deseja fazer outra operação?")
        print(menu)
        opcao = input("Digite a opção desejada: ")[0].lower()
        continue

    elif opcao == "b":
        # Pesquisa as contas criadas para cada CPF
        print("Para buscar as contas de um usário, precisamos do CPF do mesmo.")
        cpf_para_busca = validar_cpf()

        if verificar_cpf_existe(cpf_para_busca) == True:
            # Traz os dados do usuário
            for usuario in usuarios:
                if usuario[0] == cpf_para_busca:
                    print("*"*100)
                    print(f"Usuário: {usuario[1]} - CPF: {usuario[0]}".center(100,"*"))
                    print("*"*100)
            for conta in contas:
                # Traz as contas do usuário
                if conta[0] == cpf_para_busca:
                    print(f"Conta corrente: {conta[2]} - Agência: {conta[1]}")

            print(" FIM DA LISTA ".center(100,"*"))
        else:
            print(" Usuário não encontrado na base de dados. FAvor verificar.")
        # Retorna ao menu principal
        print("Deseja fazer outra operação?")
        print(menu)
        opcao = input("Digite a opção desejada: ")[0].lower()
        continue
    elif opcao == "x":
        # Fecha a aplicação
        print("Agradecemos a preferência. Saindo da aplicação...")
        break
    else:
        print("Opção inválida.")
        print(menu)
        opcao = input("Digite a opção desejada: ")[0].lower()


