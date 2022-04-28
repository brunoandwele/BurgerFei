import os

def cancelaPedido():
    while True:
        deletar = input('Gostaria de cancelar o seu pedido? \nEstá ação não poderá ser desfeita! \nNão - "0"\nSim - "1"\n "voltar" - Para voltar\n\nDigite sua opção aqui:')
        
        if deletar == '1':
            
            cadastro = open('cadastro.txt','r') #Abre o arquivo com os cadastros

            data = cadastro.readlines() #Adiciona à "data" todos os valores de cadastros (adiciona em forma de lista - 1 linha = 1 elemento da lista)

            cadastro.close() #Fecha o arquivo dos cadastros
            while True:
                cpf = input('Digite seu CPF (apenas dígitos):\n') + '\n' #pergunta o cpf do usuário  e logo depois verifica se tem no arquivo - OBS: é adicionado o "\n" pois ao usar o readlines() as informações são passadas com o \n
            
                if cpf in data: #Verifica se o usuário já está cadastrado ou não, se estiver irá perguntar a senha se não irá cadastrar ele

                    index_cpf = data.index(cpf) #Pega o valor do índice do cpf na lista pois a senha fica 1 indece à frente

                    index_senha = index_cpf + 1 #Adiciona 1 ao valor do indice do cpf, pois se refere ao indice da senha


                    while True: #Loop até o cliente acertar a senha

                        senha = input('Digite sua senha:\n') + '\n' #OBS: é adicionado o "\n" pois ao usar o readlines() as informações são passadas com o \n

                        if senha == data[index_senha]: #Verifica se a senha digitada está associada ao CPF e se está correta
                            os.remove("{}.txt" .format(cpf.strip('\n')))
                            print("Pedido cancelado com sucesso! Obrigado!")
                            break #Para o loop da senha
                            
                        else:
                            print("Senha incorreta! Tente novamente") #Diz que a senha está incorreta e informa que precisará dizer novamente qual que é 
                    break #Para o loop de fora

                else:
                    print('CPF digitado incorretamente ou não cadastrado \nCaso acredite que ele nã esteja cadastrado, digite "voltar" para voltar ao menu!')

        elif deletar == 'voltar':
            break       

        elif deletar !='1' and deletar != '0' and deletar != 'sair':
            print('Digite um valor válido!')

