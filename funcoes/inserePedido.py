from funcoes.menuPedido import menuPedido

from funcoes.novoPedido import novoPedido

def inserePedido(): #Ele irá tentar fazer o login do cliente, se não tiver o cadastro ele perguntará se quer cadastrar.Além de que recebe como argumento a conta_pagar pois ela irá chamar novamente a funçãp menuPedido(), a qual precisa do valor da conta para que ela seja atualizada

    print('Faça o login! Informe seu CPF e sua senha: \n') #Informa que irá prosseguir para o login

    cadastro = open('cadastro.txt','r') #Abre o arquivo com os cadastros

    data = cadastro.readlines() #Adiciona à "data" todos os valores de cadastros (adiciona em forma de lista - 1 linha = 1 elemento da lista)

    cadastro.close() #Fecha o arquivo dos cadastros

    cpf = input('Digite seu CPF (apenas dígitos):\n') #pergunta o cpf do usuário  e logo depois verifica se tem no arquivo

    if (cpf + '\n') in data: #Verifica se o usuário já está cadastrado ou não, se estiver irá perguntar a senha se não irá cadastrar ele

        index_cpf = data.index(cpf + '\n') #Pega o valor do índice do cpf na lista pois a senha fica 1 indece à frente

        index_senha = index_cpf + 1 #Adiciona 1 ao valor do indice do cpf, pois se refere ao indice da senha

        while True: #Loop até o cliente acertar a senha

            senha = input('Digite sua senha:\n') #OBS: é adicionado o "\n" pois ao usar o readlines() as informações são passadas com o \n

            if (senha + '\n') == data[index_senha]: #Verifica se a senha digitada está associada ao CPF e se está correta
                print('Login realizado com sucesso!') #Avisa que o login foi realizado com sucesso
                menuPedido(cpf)
                break #Para o loop
                
            else:
                print("Senha incorreta! Tente novamente") #Diz que a senha está incorreta e informa que precisará dizer novamente qual que é 

    else: #Caso o CPF não esteja no arquivo de cadastros - irá informar que o cliente precisa realizar cadastro!

        while True: #Loop até ter um input válido - 1 ou 0

            realizar_cadastro = input('CPF não encontrado nos registros! Deseja realizar o cadastro: \n 0 - Não \n 1 - Sim\n') #pergunta se o cliente quer realizar um cadastro já que não tem um
        
            if realizar_cadastro == '0': #Se ele recusar o programa só irá fechar
                print('Ok!')
                break
            elif realizar_cadastro == '1': #Se ele aceitar, a função de cadastro "novoPedido()" será chamada
                novoPedido() #Chama a função novoPedido
                break
            else:
                print('Valor inválido!  \n 0 - Não \n 1 - Sim \n') #Se ele não colcoar nem 0 nem 1, ele continuará perguntando até um desses caracteres serem digitados.


