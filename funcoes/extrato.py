from funcoes.br import br
from funcoes.verificar import verificacao
from datetime import datetime
import os


def extrato():
    def clear(): return os.system('cls')
    clear()
    while True:
        pergunta = input(
            'Gostaria de verificar o extrato? \n\nSim - "1" \n\nNão - "0"\n\nDigite aqui sua resposta: ')

        if pergunta == '1':

            cpf, verificar_bool = verificacao()

            if verificar_bool:
                clear()

                # Pegando valor do nome
                cadastro = open('cadastro.txt', 'r')
                cadastro_linhas = cadastro.readlines()
                cadastro.close()
                cpf_index = cadastro_linhas.index(cpf + '\n')
                nome = cadastro_linhas[cpf_index + 2].strip('\n')

                # Pegando valor da conta
                pedido = open('{}.txt' .format(cpf), 'r')
                pedido_linhas = pedido.readlines()
                pedido.close()
                conta = pedido_linhas[0].strip('\n')

                # Pegando o histórico dos pedidos
                historico = []
                for i in range(2, len(pedido_linhas)):
                    historico.append(pedido_linhas[i].strip('\n'))

                # Pegando a data
                data = datetime.now()
                data_formatada = data.strftime("%Y/%m/%d %H:%M")

                # Imprimindo extrato:
                extratoFile = open('extrato_{}.txt' .format(cpf), 'w')

                extratoFile.write('Nome: %s\n' % nome)
                extratoFile.write('CPF: %s\n' % cpf)
                extratoFile.write('Total: R$ %s\n' % conta)
                extratoFile.write('Data: %s\n' % data_formatada)
                extratoFile.write('Itens do pedido:\n')
                for elemento in historico:
                    extratoFile.write(elemento + '\n')
                extratoFile.close()

                extratoFile = open('extrato_{}.txt' .format(cpf), 'r')
                extratoFile_ler = extratoFile.read()

                clear()
                print(extratoFile_ler)
                br(1)
                back = input('Aperte enter para voltar!')
                clear()
                break

            else:
                clear()
                print('CPF não encontrado no sistemaou digitado incorretamente!')
                br(1)
                break

        elif pergunta == '0':
            clear()
            break

        else:
            clear()
            print('Insira um valor válido!')
            br(1)
