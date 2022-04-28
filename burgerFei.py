###############################################
###############################################
#Função para um novo pedido
from funcoes.novoPedido import novoPedido

#----------------------------------------------
#Função para remover pedido
from funcoes.cancelaPedido import cancelaPedido

#----------------------------------------------
#Função para inserir pedidos
from funcoes.inserePedido import inserePedido

#----------------------------------------------
#Função principal
def main():
    while True:
        opcao = input('1 - Novo Pedido \n2 - Cancela Pedido \n3 - Insere produto \n4 - Cancela Produto \n5 - Valor do pedido \n6 - Extrato \n\n0 - Sair \nDigite sua opção:')

        if  opcao == '1':
            novoPedido() #Chama a função novo pedido e retorna o valor do nome,cpf e conta atualizada
        elif opcao == '2':
            cancelaPedido()
        elif opcao == '3':
            inserePedido()#Chama a função inserePedido e retorna os valores do nome, cpf e conta atualiada
        elif opcao == '0':
            break
        else:
            print('Insira uma opção válida')

if __name__ == "__main__":
    main() #Ele veifica se o arquivo é o que está sendo executado, então se for ele será rodado, caso alguém importe sem querer essa biblioteca, ele não será executado a não ser que seja chamada de forma proposital!