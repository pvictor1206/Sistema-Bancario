"""
Cadastro de clientes de um banco, cada cliente tem um nome,
sobrenome, um endereço, um email, telefone, CPF e um identificador.
Um cliente pode ter um dos quatro tipos de conta permitidos pelo Banco:

- Corrente
- Salário
- Poupança
- universitária

Todas as contas contém uma agência e um número.

Sistema Bancário Paulo Magalhães V1.0

by Paulo Victor Santos Magalhães

"""

import os
import cadastro
import corrente
import poupanca
import salario
import universitario

cadastroCliente = list()
correnteCliente = list()
poupancaCliente = list()
salarioCliente = list()
universitarioCliente = list()


def linha():
    """Função que imprime uma linha
    """
    print('=' * 80)


try:
    while True:
        os.system('cls')
        linha()
        print(f'{("BANCO PAULO MAGALHAES V1.0"):^80}')
        linha()
        print('Opcao [1]: Conta Cliente \nOpção [2]: Conta Salário \nOpção [3]: Conta Poupança \nOpção [4]: Conta Universitária \nOpção [5]: Conta Corrente \nOpção [6]: Sair do Programa')
        linha()

        opcao = int(input('Digite a opção: '))  # a variável "opcao" ira definir as próximas funções do programa

        if opcao == 1:  # informações do cliente/ cadastrar cliente/ remover cliente
            cadastro.opcaoCadastro(cadastroCliente)
        elif opcao == 2:  # conta salário
            salario.opcaoSalario(cadastroCliente, salarioCliente)
        elif opcao == 3:  # conta poupança
            poupanca.opcaoPoupanca(cadastroCliente, poupancaCliente)
        elif opcao == 4:  # conta universitaria
            universitario.opcaoUniversitario(cadastroCliente, universitarioCliente)
        elif opcao == 5:  # conta corrente
            corrente.opcaoCorrente(cadastroCliente,correnteCliente)
        elif opcao == 6:  # Sair do programa
            print('SAINDO DO PROGRAMA... VOLTE SEMPRE')
            os.system('pause')
            break



except Exception as erro:
    print(f'HOUVE UM ERRO: {erro.__class__}')
    linha()
    print(' ')
    print('Clique no ENTER para continuar')
    os.system('pause')
