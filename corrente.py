# CORRENTE

"""
- Agência
- Número da conta

"""
import os


dados = dict()

def linha():
    """
    Função que imprime uma linha

    """
    print("="*80)


def infoCorrente(correnteCliente):
    """
    Informações de uma conta corrente

    """
    if len(correnteCliente) >= 1: # verifica se existe conta corrente para leitura das informações
        verificar = int(input('Digite o CPF ou o número identidicador do cliente: '))
        for c in range(0,len(correnteCliente)):
            if verificar == correnteCliente[c]['cpfCliente'] or verificar == correnteCliente[c]['identificadorCliente']:
                linha()
                print(f'{("INFORMARÇÕES CONTA CORRENTE"):^80}') # imprime as informações da conta corrente
                linha()
                print(f'NOME: {correnteCliente[c]["nomeCliente"]}')
                print(f'CPF: {correnteCliente[c]["cpfCliente"]}')
                print(f'AGÊNCIA: {correnteCliente[c]["agenciaCorrente"]}')
                print(f'CONTA: {correnteCliente[c]["contaCorrente"]}')
                print(f'IDENTIFICADOR: {correnteCliente[c]["identificadorCliente"]}')
                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')


    else: # condição se não existir conta corrente
        linha()
        print(f'{("NÃO EXISTE CONTA CORRENTE CADASTRADA"):^80}')
        linha()
        print(' ')
        print('Clique no ENTER para continuar')
        os.system('pause')


def cadastrarCorrente(cadastroCliente,correnteCliente):
    """
    Cadastrar cliente na conta corrente
    :param cadastroCliente:
    :param correnteCliente:
    :return: cadastro da agencia e conta da conta corrente.
    """
    os.system('cls')
    linha()
    print(f'{("CADASTRAR CONTA CORRENTE"):^80}')
    linha()
    aux1 = 0 #Verificar se existe ja existe um mesmo cadastro
    aux2 = 0 # se o CPF ou o número identificador for inválido
    verificar = int(input('Digite o CPF ou o numero identidicador do cliente: ')) # verifica o CPF ou identificador do cliente para realizar cadastro na conta corrente
    for p in range(0,len(correnteCliente)):
        if correnteCliente[p]['identificadorCliente'] == verificar or correnteCliente[p]['cpfCliente'] == verificar:
            linha()
            print(f'{("CONTA CORRENTE JA CADASTRADA"):^80}')
            linha()
            aux1 += 1
            print(' ')
            print('Clique no ENTER para continuar')
            os.system('pause')
    if aux1 == 0: # Verificar se existe um mesmo cadastro
        for c in range(0, len(cadastroCliente)):
            if cadastroCliente[c]['cpfCliente'] == verificar or cadastroCliente[c]['identificadorCliente'] == verificar:
                dados['agenciaCorrente'] = int(input('Número da agência: '))
                dados['contaCorrente'] = int(input('Número da conta: '))
                dados['nomeCliente'] = cadastroCliente[c]['nomeCliente']
                dados['cpfCliente'] = cadastroCliente[c]['cpfCliente']
                dados['identificadorCliente'] = cadastroCliente[c]['identificadorCliente']
                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')


                correnteCliente.append(dados.copy())
                aux2 += 1
                break
        if aux2 == 0:  # se o CPF ou o número identificador for inválido
            linha()
            print(f'{("CADASTRO NÃO ENCONTRADO"):^80}')
            linha()
            print(' ')
            print('Clique no ENTER para continuar')
            os.system('pause')






def removerCorrente(correnteCliente):
    if len(correnteCliente) >= 1:
        verificar = int(input('Digite o CPF ou número identificador: '))
        for c in range(0,len(correnteCliente)):
            if verificar == correnteCliente[c]['cpfCliente'] or verificar == correnteCliente[c]['identificadorCliente']:
                os.system('cls')
                linha()
                print(f'INFORMAÇÕES DO CLIENTE {correnteCliente[c]["nomeCliente"]} FORAM DELETADAS')  # mostrar qual cliente está sendo deletado
                linha()
                del correnteCliente[c]  # função para deletar conta corrente
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


def opcaoCorrente(cadastroCliente,correnteCliente):
    """
    função principal do arquivo corrente, nela que o usuário irá escolhar as opções

    :param cadastroCliente:
    :param correnteCliente:
    :return: Menu para informação da conta corrente, cadastrar conta corrente, remover conta corrente, tranferir conta.
    """
    os.system('cls')
    if len(cadastroCliente) <= 0: # verificar se existe contas no cadastro
        linha()
        print(f'{("NÃO EXISTEM CADASTROS"):^80}')
        linha()
        print(' ')
        print('Clique no ENTER para continuar')
        os.system('pause')
    else: # condição que o usuário escolhe as opções do menu
        linha()
        print(f'{("CONTA CORRENTE"):^80}')
        linha()
        print('Opção [1]: informações da conta corrente \nOpção [2]: cadastrar conta corrente \nOpção [3]: remover conta corrente ')
        opcao = int(input('Digite a opção: '))
        while True: # loop infinito até o usuário escolher uma opção do menu
            if opcao != 1 and opcao != 2 and opcao != 3:
                opcao = int(input('Digite a opção'))
            else:
                break
        if opcao == 1:
            infoCorrente(correnteCliente)
        elif opcao == 2:
            cadastrarCorrente(cadastroCliente, correnteCliente)
        else:
            removerCorrente(correnteCliente)
       






