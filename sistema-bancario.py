"""A v1 do projeto trabalha apenas com um usuário, e deve ser possível depositar valores POSITIVOS na conta
O sistema deve permitir realizar 3 saques diários com o limite máximo de 500 por saque
Caso o usuário não tenha saldo, o sistema deve exibir uma mensagem informando que n é possível sacar por falta de saldo
Todos os saques e depósitos devem ser armazenados em uma variável, e exibidos na operaçào de extrato
Operação de extrato: Listar todos os depósitos e saques, e no fim deve informar o saldo da conta
Os valores devem ser exibidos utilizando o formato R$ xxx.xx
"""
from datetime import date, datetime, date


opcao = "y"
saldo = 150
saques_feitos_hoje = 0
data_ultimo_saque = ""
data_ultimo_deposito = ""
limite_saques_diarios = 3
limite_por_operacao = 500
extrato_operacao = "" 
menu = """
        Digite [d] para fazer um depósito;
        Digite [s] para fazer um saque;
        Digite [e] para ver o extrato de operações;
        Digite [x] para sair da aplicação;
"""

data_hoje = date.today()

def validar_deposito(valor_deposito):
    # Função para garantir que o depósito é um valor positivo e válido
    while valor_deposito <= 0:
        valor_deposito = int(input("Você não pode fazer um depósito de valor nulo ou negativo. Por favor, digite um valor válido para depósito: "))
        
    return valor_deposito


def validar_saque(valor_saque):
    global saldo
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
    
def validar_limite_trx_diario(data_hoje, data_ultimo_saque, limite_saques_diarios, saques_feitos_hoje):
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
        deposito = validar_deposito(deposito)
        saldo+=deposito
        extrato_operacao += f"Depósito: R${deposito:.2f} - Data: {data_hoje}\n"
        data_ultimo_deposito = date.today()
        print(f"Depósito de R$ {deposito} realizado com sucesso!\n Seu saldo atual é de R$ {saldo:.2f}.\nDeseja fazer outra operação?")
        print(menu)
        opcao = input("Digite a opção desejada: ")[0].lower()
        continue
    elif opcao == "s":
        # Realiza saque
        valor_do_saque = float(input("Digite o valor a ser sacado: "))
        teste_de_valor, valor_a_ser_sacado = validar_saque(valor_do_saque)
        teste_de_limite, saques_feitos_hoje, data_ultimo_saque = validar_limite_trx_diario(data_hoje, data_ultimo_saque, limite_saques_diarios, saques_feitos_hoje)
        if teste_de_valor == True and teste_de_limite == True:
            data_ultimo_saque = data_hoje
            saldo -= valor_a_ser_sacado
            extrato_operacao += f"Saque: R${valor_a_ser_sacado:.2f} - Data: {data_hoje}\n"
            print(f"Saque de R$ {valor_a_ser_sacado} realizado com sucesso!\nSeu saldo atual é de R$ {saldo:.2f}.\n Retire seu dinheiro no local indicado.")
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


