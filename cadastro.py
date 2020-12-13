# Cadastro

"""
Contém as seguintes funções:

[x] Cadastrar Clientes
[x] Remover Clientes
[x] Informações do cliente

"""
import os
import random

dados = dict()

def linha():
    """Função que imprime uma linha
    """
    print('='*80)

def infoClientes(cadastroCliente):
    """
    Informa os dados de um cliente
    :param cadastroCliente:
    :return: Nome do cliente, sobrenome, endereço, email, tefelefone, CPF e gera um número aleatório único identificador
    """
    cont = 0 # Se não existir o CPF nem o identificador de um cliente
    if len(cadastroCliente) > 0: # Verifica se existe contas cadastradas
        verificar = int(input('Digite o CPF(SOMENTE NÚMEROS) ou o número identificador do cliente: '))
        for c in range(0,len(cadastroCliente)):
            if verificar == cadastroCliente[c]['cpfCliente'] or verificar == cadastroCliente[c]['identificadorCliente']:
                os.system('cls')
                linha()
                print(f'{("INFORMAÇÕES DO CLIENTE"):^80}') # a partir daqui são colocadas as informações do cliente
                linha()
                print(f'NOME: {cadastroCliente[c]["nomeCliente"]}')
                print(f'SOBRENOME: {cadastroCliente[c]["sobrenomeCliente"]}')
                print(f'ENDEREÇO: {cadastroCliente[c]["enderecoCliente"]}')
                print(f'EMAIL: {cadastroCliente[c]["emailCliente"]}')
                print(f'TELEFONE: {cadastroCliente[c]["telefoneCliente"]}')
                print(f'CPF: {cadastroCliente[c]["cpfCliente"]}')
                print(f'IDENTIFICADOR: {cadastroCliente[c]["identificadorCliente"]}')
                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')
                cont += 1
        if cont == 0: # Se não existir o CPF nem o identificador de um cliente
            os.system('cls')
            linha()
            print(f'{("CLIENTE NÃO ENCONTRADO"):^80}')
            linha()
            print(' ')
            print('Clique no ENTER para continuar')
            os.system('pause')


    else: # comadas se não existir contas cadastradas
        os.system('cls')
        linha()
        print(f'{("Não existe contas cadastradas"):^80}')
        linha()
        print(' ')
        print('Clique no ENTER para continuar')
        os.system('pause')


def cadastrarClientes(cadastroCliente):
    """
    Cadastra um cliente
    :param cadastroCliente:
    :return: Nome do cliente, sobrenome, endereço, email, tefelefone, CPF e gera um número aleatório único identificador
    """
    os.system('cls')
    linha()
    print(f'{("CADASTRO DO CLIENTE"):^80}')
    linha()
    dados['nomeCliente'] = str(input('Nome: ')).strip() # inserir o nome do cliente
    dados['sobrenomeCliente'] = str(input('Sobrenome: ')).strip() # inserir o sobrenome do cliente
    dados['enderecoCliente'] = str(input('Endereço: ')).strip() # inserir o endereço do cliente
    dados['emailCliente'] = str(input('Email: ')).strip() # inserir o email do cliente
    dados['telefoneCliente'] = str(input('Telefone: ')).strip() # inserir o telefone do cliente
    dados['cpfCliente'] = int(input('CPF(somente numeros): ')) # inserir o CPF do cliente
    aux = 0
    if len(cadastroCliente) > 0:
        for p in range(0, len(cadastroCliente)):
            if cadastroCliente[p]['cpfCliente'] == dados['cpfCliente']:
                os.system('cls')
                linha()
                print(f'{("CPF JA UTILIZADO"):^80}')
                linha()
                aux += 1
                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')
    if aux == 0:
        aleatorio = random.randint(100000, 999999)  # gera um numero aleatório de nove digitos para o cliente
        for c in range(0, len(cadastroCliente)):  # verifica se o número aleatório não pertece a outro cliente
            while True:
                if aleatorio == cadastroCliente[c]['identificadorCliente']:
                    aleatorio = random.randint(100000, 999999)
                else:
                    break
        dados['identificadorCliente'] = aleatorio  # a biblioteca recebe o identificador aleatório do cliente
        print(' ')
        print(f'Identificador do cliente {dados["nomeCliente"]}: {dados["identificadorCliente"]}')  # Mostra o número aleatório
        print(' ')
        print('Clique no ENTER para continuar')
        os.system('pause')

        cadastroCliente.append(dados.copy())



def removerClientes(cadastroCliente):
    """
    Deleta um cliente
    :param cadastroCliente:
    :return: deleta as informações de um cliente
    """
    if len(cadastroCliente) > 0: # Verifica se existe contas cadastradas
        verificar = int(input('Digite o CPF ou o número identificador do cliente: '))
        for c in range(0,len(cadastroCliente)):
            if verificar == cadastroCliente[c]['cpfCliente'] or verificar == cadastroCliente[c]['identificadorCliente']:
                os.system('cls')
                linha()
                print(f'INFORMAÇÕES DO CLIENTE {cadastroCliente[c]["nomeCliente"]} FORAM DELETADAS') # mostrar qual cliente está sendo deletado
                linha()
                del cadastroCliente[c] # função para deletar cliente
                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')

    else: # comadas se não existir contas cadastradas
        os.system('cls')
        linha()
        print(f'{("Não existe contas cadastradas"):^80}')
        linha()
        print(' ')
        print('Clique no ENTER para continuar')
        os.system('pause')




def opcaoCadastro(cadastroCliente):
    """Função principal do arquivo cadastro, aqui que o usuário ira escolher as opções informações do cliente, cadastrar um cliente ou remover um cliente.

    Args:
        cadastroCliente (lista): lista para verificar as informações do cliente/ inserir cliente/ remover cliente
    """
    os.system('cls')
    linha()
    print(f'{("CONFIGURAÇÕES DO CLIENTE"):^80}')
    linha()
    print('Opção [1]: verificar as informações do cliente \nOpção [2]: cadastrar cliente \nOpção [3]: remover clientes')
    opcao = int(input('Digite a opção: ')) # "opcao" é a variável que ira definir a escolha do usuário
    while True: # Laço infinito até o usuário escolher alguma alternativa do menu...
        if opcao != 1 and opcao != 2 and opcao != 3:
            opcao = int(input('Digite a opção: '))
        else:
            break
    if opcao == 1: # Se o usuário escolher as informações do cliente
        infoClientes(cadastroCliente)
    elif opcao == 2: # Se o usuário escolher cadastrar um cliente
        cadastrarClientes(cadastroCliente)
    else: # Se o usuário escolher remover um cliente
        removerClientes(cadastroCliente)
