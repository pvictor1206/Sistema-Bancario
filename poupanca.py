# Poupança

"""
Para o cliente realizar o cadastro da conta poupança devem ser armazenadas as informações:

- Agência
- Número da conta
- Quando o cliente depositou o dinheiro
- Quanto recebeu no último mês

by Paulo Victor Santos

"""
import os

dados = dict()

def linha():
    print('='*80)


def infoPoupanca(poupancaCliente):
    """
       Informações de uma conta poupança

    """
    os.system('cls')
    if len(poupancaCliente) >= 1:  # verifica se existe conta poupanca para leitura das informações
        verificar = int(input('Digite o CPF ou o número identidicador do cliente: '))
        for c in range(0, len(poupancaCliente)):
            if verificar == poupancaCliente[c]['cpfCliente'] or verificar == poupancaCliente[c]['identificadorCliente']:
                linha()
                os.system('cls')
                print(f'{("INFORMARÇÕES CONTA POUPANÇA"):^80}')  # imprime as informações da conta poupanca
                linha()
                print(f'NOME: {poupancaCliente[c]["nomeCliente"]}')
                print(f'CPF: {poupancaCliente[c]["cpfCliente"]}')
                print(f'AGÊNCIA: {poupancaCliente[c]["agenciaPoupanca"]}')
                print(f'CONTA: {poupancaCliente[c]["contaPoupanca"]}')
                print(f'DEPOSITO: {poupancaCliente[c]["depositoPoupanca"]}')
                print(f'ULTIMO DEPOSITO: {poupancaCliente[c]["recebeuPoupanca"]}')
                print(f'IDENTIFICADOR: {poupancaCliente[c]["identificadorCliente"]}')

                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')
    else: # condição se não existir conta poupança
        linha()
        print(f'{("NÃO EXISTE CONTA POUPANÇA CADASTRADA"):^80}')
        linha()
        print(' ')
        print('Clique no ENTER para continuar')
        os.system('pause')

def cadastrarPoupanca(cadastroCliente, poupancaCliente):
    os.system('cls')
    linha()
    print(f'{("CADASTRAR CONTA POUPANÇA"):^80}')
    linha()
    cont = 0
    aux2 = 0
    verificar = int(input('Digite o CPF ou o identificador do usuário: '))
    if len(poupancaCliente) > 0:
        for c in range(0,len(poupancaCliente)):
            if poupancaCliente[c]['cpfCliente'] == verificar or poupancaCliente[c]['identificadorCliente'] == verificar:
                print(f'{("CLIENTE JA CADASTRADO EM CONTA POUPANÇA"):^80}')
                cont += 1
                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')
                break
    if cont == 0: # Verificar se existe ja existe um mesmo cadastro
        for c in range(0,len(cadastroCliente)):
            if cadastroCliente[c]['cpfCliente'] == verificar or cadastroCliente[c]['identificadorCliente']== verificar:
                dados['nomeCliente'] = cadastroCliente[c]['nomeCliente']
                dados['cpfCliente'] = cadastroCliente[c]['cpfCliente']
                dados['identificadorCliente'] = cadastroCliente[c]['identificadorCliente']
                dados['agenciaPoupanca'] = int(input('Número da agência(SOMENTE NUMEROS): '))
                dados['contaPoupanca'] = int(input('Número da conta(SOMENTE NUMEROS): '))
                dados['depositoPoupanca'] = str(input('Data do ultimo deposito: ')).strip()
                dados['recebeuPoupanca'] = str(input('Quantidade recebida no ultimo mês: ')).strip()
                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')

                poupancaCliente.append(dados.copy())
                aux2 += 1
                break
        if aux2 == 0:  # se o CPF ou o número identificador for inválido
            linha()
            print(f'{("CADASTRO NÃO ENCONTRADO"):^80}')
            linha()
            print(' ')
            print('Clique no ENTER para continuar')
            os.system('pause')


def removerPoupanca(poupancaCliente):
    if len(poupancaCliente) >= 1:
        verificar = int(input('Digite o CPF ou número identificador: '))
        for c in range(0,len(poupancaCliente)):
            if verificar == poupancaCliente[c]['cpfCliente'] or verificar == poupancaCliente[c]['identificadorCliente']:
                os.system('cls')
                linha()
                print(f'INFORMAÇÕES DO CLIENTE {poupancaCliente[c]["nomeCliente"]} FORAM DELETADAS')  # mostrar qual cliente está sendo deletado
                linha()
                del poupancaCliente[c]  # função para deletar conta corrente
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

def opcaoPoupanca(cadastroCliente, poupancaCliente):
    """
    função principal do arquivo corrente, nela que o usuário irá escolhar as opções
    :param cadastroCliente:
    :param poupancaCliente:
    :return:
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
        print(f'{("CONTA POUPANÇA"):^80}')
        linha()
        print('Opção [1]: informações da conta poupança \nOpção [2]: cadastrar conta poupança \nOpção [3]: remover conta poupança ')
        opcao = int(input('Digite a opção: '))
        while True: # loop infinito até o usuário escolher uma opção do menu
            if opcao != 1 and opcao != 2 and opcao != 3:
                opcao = int(input('Digite a opção: '))
            else:
                break
        if opcao == 1:
            infoPoupanca(poupancaCliente)
        elif opcao == 2:
            cadastrarPoupanca(cadastroCliente, poupancaCliente)
        else:
            removerPoupanca(poupancaCliente)





