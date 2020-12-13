# Salário

"""
Para o cliente realizar o cadastro da conta salário deve conter as seguintes informações:

- Salário
- órgão em que trabalha
- Cargo
- Data da contratação

by Paulo Victor Santos Magalhães

"""
import os

dados = dict()

def linha():
    """Função que retorna uma linha
    """
    print('='*80)


def infoSalario(salarioCliente):
    """
       Informações de uma conta salario

    """
    os.system('cls')
    if len(salarioCliente) >= 1:  # verifica se existe conta salario para leitura das informações
        verificar = int(input('Digite o CPF ou o número identidicador do cliente: '))
        for c in range(0, len(salarioCliente)):
            if verificar == salarioCliente[c]['cpfCliente'] or verificar == salarioCliente[c]['identificadorCliente']:
                linha()
                os.system('cls')
                print(f'{("INFORMARÇÕES CONTA SALARIO"):^80}')  # imprime as informações da conta corrente
                linha()
                print(f'NOME: {salarioCliente[c]["nomeCliente"]}')
                print(f'CPF: {salarioCliente[c]["cpfCliente"]}')
                print(f'AGÊNCIA: {salarioCliente[c]["agenciaSalario"]}')
                print(f'CONTA: {salarioCliente[c]["contaSalario"]}')
                print(f'SALARIO: {salarioCliente[c]["salario"]}')
                print(f'ORGAO EM QUE TRABALHA: {salarioCliente[c]["orgaoSalario"]}')
                print(f'CARGO: {salarioCliente[c]["cargoSalario"]}')
                print(f'DATA DA CONTRATACAO: {salarioCliente[c]["contratacaoSalario"]}')
                print(f'IDENTIFICADOR: {salarioCliente[c]["identificadorCliente"]}')

                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')
    else: # condição se não existir conta salario
        linha()
        print(f'{("NÃO EXISTE CONTA SALARIO CADASTRADA"):^80}')
        linha()
        print(' ')
        print('Clique no ENTER para continuar')
        os.system('pause')



def cadastrarSalario(cadastroCliente, salarioCliente):
    os.system('cls')
    linha()
    print(f'{("CADASTRAR CONTA SALARIO"):^80}')
    linha()
    cont = 0
    aux2 = 0
    verificar = int(input('Digite o CPF ou o identificador do usuário: '))
    if len(salarioCliente) > 0:
        for c in range(0,len(salarioCliente)):
            if salarioCliente[c]['cpfCliente'] == verificar or salarioCliente[c]['identificadorCliente'] == verificar:
                os.system('cls')
                print(f'{("CLIENTE JA CADASTRADO NA CONTA SALARIO"):^80}')
                cont += 1
                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')
                break
    if cont == 0: # Verificar se existe ja existe um mesmo cadastro
        for c in range(0,len(cadastroCliente)):
            if cadastroCliente[c]['cpfCliente'] == verificar or cadastroCliente[c]['identificadorCliente'] == verificar:
                os.system('cls')
                dados['nomeCliente'] = cadastroCliente[c]['nomeCliente']
                dados['cpfCliente'] = cadastroCliente[c]['cpfCliente']
                dados['identificadorCliente'] = cadastroCliente[c]['identificadorCliente']
                dados['agenciaSalario'] = int(input('Número da agência(SOMENTE NUMEROS): '))
                dados['contaSalario'] = int(input('Número da conta(SOMENTE NUMEROS): '))
                dados['salario'] = int(input('Salario (SOMENTE NUMEROS): '))
                dados['orgaoSalario'] = str(input('Orgão em que trabalha: ')).strip()
                dados['cargoSalario'] = str(input('Cargo: ')).strip()
                dados['contratacaoSalario'] = str(input('Data da contratação: ')).strip()

                
                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')

                salarioCliente.append(dados.copy())
                aux2 += 1
                break
        if aux2 == 0:  # se o CPF ou o número identificador for inválido
            linha()
            print(f'{("CADASTRO NÃO ENCONTRADO"):^80}')
            linha()
            print(' ')
            print('Clique no ENTER para continuar')
            os.system('pause')


    
def removerSalario(salarioCliente):
    if len(salarioCliente) >= 1:
        verificar = int(input('Digite o CPF ou número identificador: '))
        for c in range(0,len(salarioCliente)):
            if verificar == salarioCliente[c]['cpfCliente'] or verificar == salarioCliente[c]['identificadorCliente']:
                os.system('cls')
                linha()
                print(f'INFORMAÇÕES DO CLIENTE {salarioCliente[c]["nomeCliente"]} FORAM DELETADAS')  # mostrar qual cliente está sendo deletado
                linha()
                del salarioCliente[c]  # função para deletar conta corrente
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


def opcaoSalario(cadastroCliente, salarioCliente):
    os.system('cls')
    if len(cadastroCliente) <= 0: # verificar se existe contas no cadastro
        linha()
        print(f'{("NÃO EXISTEM CADASTROS"):^80}')
        linha()
        print(' ')
        print('Clique no ENTER para continuar')
        os.system('pause')
    else:  # condição que o usuário escolhe as opções do menu
        linha()
        print(f'{("CONTA SALÁRIO"):^80}')
        linha()
        print('Opção [1]: informações da conta salario \nOpção [2]: cadastrar conta salario \nOpção [3]: remover conta salario ')
        opcao = int(input('Digite a opção: '))
        while True: # loop infinito até o usuário escolher uma opção do menu
            if opcao != 1 and opcao != 2 and opcao != 3:
                opcao = int(input('Digite a opção: '))
            else:
                break
        if opcao == 1:
            infoSalario(salarioCliente)
        elif opcao == 2:
            cadastrarSalario(cadastroCliente, salarioCliente)
        else:
            removerSalario(salarioCliente)