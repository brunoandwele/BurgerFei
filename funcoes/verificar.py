from funcoes.br import br
import os

def verificacao():
    clear = lambda: os.system('cls') #Cria a função para limpar o console
    clear()
    # Informa que irá prosseguir para o login
    print('Faça o login! Informe seu CPF e sua senha: \n')

    cadastro = open('cadastro.txt', 'r')  # Abre o arquivo com os cadastros

    # Adiciona à "data" todos os valores de cadastros (adiciona em forma de lista - 1 linha = 1 elemento da lista)
    data = cadastro.readlines()

    cadastro.close()  # Fecha o arquivo dos cadastros

    # pergunta o cpf do usuário  e logo depois verifica se tem no arquivo
    clear()
    cpf = input('Digite seu CPF (apenas dígitos):\n')

    if (cpf + '\n') in data:  # Verifica se o usuário já está cadastrado ou não, se estiver irá perguntar a senha se não irá cadastrar ele

        # Pega o valor do índice do cpf na lista pois a senha fica 1 indece à frente
        index_cpf = data.index(cpf + '\n')

        # Adiciona 1 ao valor do indice do cpf, pois se refere ao indice da senha
        index_senha = index_cpf + 1

        clear()
        while True:  # Loop até o cliente acertar a senha
            # OBS: é adicionado o "\n" pois ao usar o readlines() as informações são passadas com o \n
            senha = input('Digite sua senha:\n')

            # Verifica se a senha digitada está associada ao CPF e se está correta
            if (senha + '\n') == data[index_senha]:
                # Avisa que o login foi realizado com sucesso
                clear()
                print('Login realizado com sucesso!')
                br()
                return cpf, True #Retorna o cpf e True para informar que o login foi realizado com sucesso

            else:
                # Diz que a senha está incorreta e informa que precisará dizer novamente qual que é
                clear()
                print("Senha incorreta! Tente novamente")
                br(1)
                
    else:
        clear()
        print('CPF não encontrado no sistema!')
        br()
        cpf = 'null'
        return cpf, False #retorna o cpf como null e False para informar que o login não foi feito com sucesso!
