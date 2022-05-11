import os
from funcoes.verificar import verificacao
from funcoes.br import br


def cancelaPedido():
    clear = lambda: os.system('cls')
    clear()
    while True:
    
        deletar = input(
        'Gostaria de cancelar o seu pedido? \nEstá ação não poderá ser desfeita! \n\nSim - "1"\n\nNão - "0"\n\nDigite sua opção aqui:')

        if deletar == '1':

            cpf, verificacao_bool = verificacao()

            if verificacao_bool == True:
                try:
                    os.remove("{}.txt" .format(cpf))
                    os.remove("extrato_{}.txt" .format(cpf))
                    print("Pedido cancelado com sucesso! Obrigado!")
                    br()
                    break
                except:
                    clear()
                    print('Pedido não encontrado! Pedido já deletado ou não iniciado!')
                    br(1)

            else:
                clear()
                print('CPF digitado incorretamente ou não cadastrado')
                br(1)
                break
                

        elif deletar == '0':
            clear()
            break

        else:
            clear()
            print('Digite um valor válido!')
            br(1)
