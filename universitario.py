# Universitária

"""
Para ter uma conta universitária o cliente deve possuir:

- Matrícula  da Universidade
- Data da matrícula
- Previsão de conclusão
- Curso
- Universidade

by Paulo Victor Santos Magalhães

"""

import os

dados = dict()

def linha():
    """Função que retorna uma linha
    """
    print('='*80)


def infoUniversiario(universitarioCliente):
    """
       Informações de uma conta universitaria

    """
    os.system('cls')
    if len(universitarioCliente) >= 1:  # verifica se existe conta salario para leitura das informações
        verificar = int(input('Digite o CPF ou o número identidicador do cliente: '))
        for c in range(0, len(universitarioCliente)):
            if verificar == universitarioCliente[c]['cpfCliente'] or verificar == universitarioCliente[c]['identificadorCliente']:
                linha()
                os.system('cls')
                print(f'{("INFORMARÇÕES CONTA SALARIO"):^80}')  # imprime as informações da conta corrente
                linha()
                print(f'NOME: {universitarioCliente[c]["nomeCliente"]}')
                print(f'CPF: {universitarioCliente[c]["cpfCliente"]}')
                print(f'AGÊNCIA: {universitarioCliente[c]["agenciaUniversitario"]}')
                print(f'CONTA: {universitarioCliente[c]["contaUniversitario"]}')
                print(f'NUMERO DE MATRICULA: {universitarioCliente[c]["matriculaUniversitario"]}')
                print(f'DATA DA MATRICULA: {universitarioCliente[c]["dataMatriUniversitario"]}')
                print(f'CONCLUSÃO DO CURSO: {universitarioCliente[c]["conclusaoUniversitario"]}')
                print(f'CURSO: {universitarioCliente[c]["cursoUniversitario"]}')
                print(f'UNIVERSIDADE: {universitarioCliente[c]["universidadeUniversitario"]}')
                

                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')
    else: # condição se não existir conta salario
        linha()
        print(f'{("NÃO EXISTE CONTA UNIVERSITARIA CADASTRADA"):^80}')
        linha()
        print(' ')
        print('Clique no ENTER para continuar')
        os.system('pause')



def cadastrarUniversiario(cadastroCliente, universitarioCliente):
    os.system('cls')
    linha()
    print(f'{("CADASTRAR CONTA UNIVERSITARIA"):^80}')
    linha()
    cont = 0
    aux2 = 0
    verificar = int(input('Digite o CPF ou o identificador do usuário: '))
    if len(universitarioCliente) > 0:
        for c in range(0,len(universitarioCliente)):
            if universitarioCliente[c]['cpfCliente'] == verificar or universitarioCliente[c]['identificadorCliente'] == verificar:
                os.system('cls')
                print(f'{("CLIENTE JA CADASTRADO NA CONTA UNIVERSITARIA"):^80}')
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
                dados['agenciaUniversitario'] = int(input('Número da agência(SOMENTE NUMEROS): '))
                dados['contaUniversitario'] = int(input('Número da conta(SOMENTE NUMEROS): '))
                dados['matriculaUniversitario'] = int(input('Número de matricula(SOMENTE NUMEROS): '))
                dados['dataMatriUniversitario'] = str(input('Data da matricula: '))
                dados['conclusaoUniversitario'] = str(input('Data de conclusão de curso: '))
                dados['cursoUniversitario'] = str(input('Curso: '))
                dados['universidadeUniversitario'] = str(input('Universidade: '))


                
                print(' ')
                print('Clique no ENTER para continuar')
                os.system('pause')

                universitarioCliente.append(dados.copy())
                aux2 += 1
                break
        if aux2 == 0:  # se o CPF ou o número identificador for inválido
            linha()
            print(f'{("CADASTRO NÃO ENCONTRADO"):^80}')
            linha()
            print(' ')
            print('Clique no ENTER para continuar')
            os.system('pause')


    
def removerUniversiario(universitarioCliente):
    if len(universitarioCliente) >= 1:
        verificar = int(input('Digite o CPF ou número identificador: '))
        for c in range(0,len(universitarioCliente)):
            if verificar == universitarioCliente[c]['cpfCliente'] or verificar == universitarioCliente[c]['identificadorCliente']:
                os.system('cls')
                linha()
                print(f'INFORMAÇÕES DO CLIENTE {universitarioCliente[c]["nomeCliente"]} FORAM DELETADAS')  # mostrar qual cliente está sendo deletado
                linha()
                del universitarioCliente[c]  # função para deletar conta corrente
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


def opcaoUniversitario(cadastroCliente, universitarioCliente):
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
        print(f'{("CONTA UNIVERSITARIA"):^80}')
        linha()
        print('Opção [1]: informações da conta universitaria \nOpção [2]: cadastrar conta universitaria \nOpção [3]: remover conta universitaria ')
        opcao = int(input('Digite a opção: '))
        while True: # loop infinito até o usuário escolher uma opção do menu
            if opcao != 1 and opcao != 2 and opcao != 3:
                opcao = int(input('Digite a opção: '))
            else:
                break
        if opcao == 1:
            infoUniversiario(universitarioCliente)
        elif opcao == 2:
            cadastrarUniversiario(cadastroCliente, universitarioCliente)
        else:
            removerUniversiario(universitarioCliente)