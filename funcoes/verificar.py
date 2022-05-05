def verificacao():
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
                return cpf,True
                break #Para o loop
                
            else:
                print("Senha incorreta! Tente novamente") #Diz que a senha está incorreta e informa que precisará dizer novamente qual que é 
    else:
        print('CPF não encontrado no sistema!')
        return False