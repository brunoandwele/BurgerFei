from funcoes.br import br
from funcoes.verificar import verificacao
from datetime import datetime
import os


def extrato():
    def clear(): return os.system('cls') #Cria a função para limpar o console
    clear()

    cpf, verificar_bool = verificacao() #Recebe os valores de cpf e se o login foi realizado com sucesso

    if verificar_bool:
        clear()
        try :
            # Pegando valor do nome
            #Abre o arquivo do cadastro para pegar o nome do usuário, usando como referencia o cpf dele
            cadastro = open('cadastro.txt', 'r')
            cadastro_linhas = cadastro.readlines()
            cadastro.close()
            cpf_index = cadastro_linhas.index(cpf + '\n')
            nome = cadastro_linhas[cpf_index + 2].strip('\n')

            # Pegando valor da conta
            #Pega o valor da conta do arquivo do pedido, o qual é o valor que aparece na primeira linha do arquivo
            pedido = open('{}.txt' .format(cpf), 'r')
            pedido_linhas = pedido.readlines()
            pedido.close()
            conta = pedido_linhas[0].strip('\n')

            # Pegando o histórico dos pedidos
            #Pega o que foi adicionado e retirado do arquivo do pedido, começando da segunda linha do arquivo
            historico = []
            for i in range(2, len(pedido_linhas)):
                historico.append(pedido_linhas[i].strip('\n'))

            # Pegando a data
            #Usa a função now do datetime para pegar a data e a hora do computador
            data = datetime.now() 
            data_formatada = data.strftime("%Y/%m/%d %H:%M")

            # Imprimindo extrato:
            #Como o extrato é algo que normalmente é impresso, decidi fazer um novo arquivo, escrevendo nele tudo o que estava no exemplo com a formatação correta.
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
            #Após escrever o arquivo, ele o imprime com o metodo read()
            clear()
            print(extratoFile_ler)
            br(1)
            back = input('Aperte enter para voltar!') #Input vazio apenas para travar o programa e soh permitir que ele volte a rodar depois que o usuário siga
            clear()
            
        except:#Caso não encontre o arquivo do pedido com o respectivo cpf
            clear()
            print('Não há registro de pedidos com esse CPF!')
            br(1)

    else:#Caso não tenha realizado o login com sucesso
        clear()
        print('CPF não encontrado no sistemaou digitado incorretamente!')
        br(1)
