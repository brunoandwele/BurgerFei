from funcoes.br import br
from funcoes.verificar import verificacao
import os

def valorPagar():
    clear = lambda: os.system('cls') #Cria a função para limpar o console
    clear()
    

        

    cpf, verificar_bool = verificacao() #Chama a função verificar e receber os valores de cpf e se deu login com sucesso ou não

    if verificar_bool == True: #Caso tenha dado com sucesso, irá mostrar o valor

        clear()

        try: #Tenta abrir o arquivo com o cpf do cliente já cadastrado
            pedido = open('{}.txt' .format(cpf), 'r')
            pedido_linhas = pedido.readlines()
            pedido.close()

            conta = pedido_linhas[0].strip('\n') #Pega dentro da lista com as linhas do arquivo o valor da conta

            print('###############################')
            print('Valor a se pagar: R$%s' %conta)
            print('###############################')
            br(2)
            back = input('Aperte enter para voltar!') #Input apenas para parar o programa para mostrar ao usuario
            clear()
        except:#Se não encontrar o arquivo do usuário, significa que ele está cadastrado mas não tem um pedido ativo
            clear()
            print('Não há pedidos registros com esse cpf!')
            br(1)

    else: #Caso ele queira ver a conta, mas não tem login, aparaece essa mensagem!
        clear()
        print('CPF não encontrado no sistema ou digitado incorretamente!')
        br(1)

            


