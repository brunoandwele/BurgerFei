from funcoes.menuPedido import menuPedido

from funcoes.verificar import verificacao

from funcoes.novoPedido import novoPedido

def inserePedido(): #Ele irá tentar fazer o login do cliente, se não tiver o cadastro ele perguntará se quer cadastrar.Além de que recebe como argumento a conta_pagar pois ela irá chamar novamente a funçãp menuPedido(), a qual precisa do valor da conta para que ela seja atualizada

    cpf,verificacao_bool = verificacao()

    if verificacao_bool == True:  
        menuPedido(cpf)

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


