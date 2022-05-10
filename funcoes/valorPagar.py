from funcoes.br import br
from funcoes.verificar import verificacao
import os

def valorPagar():
    clear = lambda: os.system('cls')
    clear()
    while True:
        pergunta = input(
            'Gostaria de verificar o valor da conta? \nSim -"1" \nNão-"0"\n:')

        if pergunta == '1':

            cpf, verificar_bool = verificacao()

            if verificar_bool == True:
                clear()

                pedido = open('{}.txt' .format(cpf), 'r')
                pedido_linhas = pedido.readlines()
                pedido.close()

                conta = pedido_linhas[0].strip('\n')

                print('###############################')
                print('Valor a se pagar: R$%s' %conta)
                print('###############################')
                br(2)
                back = input('Aperte enter para voltar!')
                clear()
        
            else:
                clear()
                print('CPF não encontrado no sistema ou digitado incorretamente!')
                br(1)

            break

        elif pergunta == '0':
            clear()
            print('Voltando...')
            br(1)
            break

        else:
            clear()
            print('Insira um valor válido!')
            br(1)
