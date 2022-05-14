import os
from funcoes.verificar import verificacao
from funcoes.br import br


def cancelaPedido():
    clear = lambda: os.system('cls')
    clear()
    while True:
        #Pergunta se ele quer mesmo cancelar
        deletar = input(
        'Gostaria de cancelar o seu pedido? \nEstá ação não poderá ser desfeita! \n\nSim - "1"\n\nNão - "0"\n\nDigite sua opção aqui:')

        if deletar == '1':

            cpf, verificacao_bool = verificacao() #Recebe os valores de cpf e se o login foi feito com sucesso

            if verificacao_bool == True:
                try: #Tenta apagar o arquivo usando o os.remove()
                    os.remove("{}.txt" .format(cpf))
                    os.remove("extrato_{}.txt" .format(cpf))
                    print("Pedido cancelado com sucesso! Obrigado!")
                    br()
                    break
                except:#Se não conseguir deletar, significa que não há pedidos com esse cpf, por tanto irá informar isso ao usuário
                    clear()
                    print('Pedido não encontrado! Pedido já deletado ou não iniciado!')
                    br(1)

            else: #Caso não tenha realizado o login corretamente
                clear()
                print('CPF digitado incorretamente ou não cadastrado')
                br(1)
                break
                

        elif deletar == '0': #Caso queira voltar ao menu
            clear()
            break

        else: #Caso tenha digitado algum valor invalido, ou seja, diferente de 0 ou 1
            clear()
            print('Digite um valor válido!')
            br(1)
