
# Desafio de projeto: Criando um sistema bancário com Python (v2)


## Restrições:

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
* Os valores devem ser exibidos utilizando o formato R$ XXX.XX.

## Funcionalidades:

* O sistema deve ter um menu interativo com o usuário, onde ele decide se quer:
	* [d] fazer um depósito;
	* [s] fazer um saque;
	* [e] ver o extrato de operações;
	* [u] cadastrar um novo usuário;
	* [c] cadastrar uma nova conta corrente para um usuário existente;
	* [v] acessar a lista de usuários cadastrados;
	* [b] acessar a lista de contas por CPF;
	* [x] sair da aplicação;
* Qualquer operação diferente disso deve retornar um erro, avisando que a operação é inválida.

* Todos os erros gerados a partir de falha nas operações financeiras, devem gerar uma notificação ao usuário, para que ele entenda o motivo de a operação não ter sido bem sucedida.
