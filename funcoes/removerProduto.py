from funcoes.verificar import verificacao
from funcoes.br import br
import os


def removerProduto():
    clear = lambda: os.system('cls')
    clear()
    print('Para remover um produto é necessário informar novamente o cpf e a senha!')
    br(1)
    confirmar = input(
        'Gostaria mesmo de remover um produto? \n\nSim - "1" \n\nNão - "0" \n\nDigite aqui sua respsota:')

    if confirmar == '1':

        cardapio = [
            ['Código', 'Produto', 'Preço'],
            ['1', 'X-salada', 'R$ 10,00'],
            ['2', 'X-burger', 'R$ 10,00'],
            ['3', 'Cachorro quente', 'R$ 7,50'],
            ['4', 'Misto quente', 'R$ 8,00'],
            ['5', 'Salada de frutas', 'R$ 5,50'],
            ['6', 'Refrigerante', 'R$ 4,50'],
            ['7', 'Suco natural', 'R$ 6,25']
        ]

        # Lista contendo os valores em reais dos produtos, para que futuramente seja calculado o preço total a se pagar!
        valores = ['-', 10, 10, 7.5, 8, 5.5, 4.5, 6.25]
        cpf, verificacao_bool = verificacao()

        if verificacao_bool == True:

            try:
                carrinho = open('{}.txt' .format(cpf), 'r')
                carrinho_linhas = carrinho.readlines()
                conta = float(carrinho_linhas[0].strip('\n'))
                quantidades = (carrinho_linhas[1].strip('\n')).split(' ')
                carrinho.close()
                clear()
                while True:
                    
                    carrinho = open('{}.txt' .format(cpf), 'r')
                    carrinho_linhas = carrinho.readlines()

                    for i in range(2, len(carrinho_linhas)):
                        print(carrinho_linhas[i])

                    carrinho = open('{}.txt' .format(cpf), 'a')

                    produto = input(
                        'Qual o produto que deseja remover?\nDigite o código dele!\nCaso queira voltar, digite "voltar" para voltar ao menu!\n: ')
                    br(1)

                    # Verifica se a variável "produto" recebeu um desses valores
                    if (produto in ['1', '2', '3', '4', '5', '6', '7'] and \
                        int(quantidades[int(produto)]) > 0 ):

                        while True:

                            # Pergunta quantos itens do alimento desejado deverá ser adicionado no carrinho
                            quantidade_escolhida = (input(
                                'Digite a quantidade a ser removida do carrinho:\n(OBS:Caso queira voltar, digite "voltar")\n:'))
                            br(1)

                            if quantidade_escolhida == 'voltar':
                                clear()
                                print('Voltando')
                                br()
                                break

                            else:

                                if (int(quantidades[int(produto)]) - int(quantidade_escolhida)) < 0:
                                    clear()
                                    print(
                                        'Quantidade inválida! Quantidade inserida é maior do que a quantidade dentro do carrinho!')
                                    br(1)
                                    break

                                else:
                                    quantidades[int(produto)] = (
                                        int(quantidades[int(produto)]) - int(quantidade_escolhida))

                                    # Cria uma variável chamada "produto" que assume um valor do item que será adicionado diretamente da matriz "cardapio", essa variável será usada para pegar o nome do produto para depois usar no extrarto e deixar no carrinho também
                                    produto_remover = (cardapio[int(produto)][1])

                                    # Pegar o valor do produto escolhido a partir da lista contendo os valores dos produtos, sendo que o índice na lista se refere ao código do alimento no cardápio
                                    valor_produto = valores[int(produto)]

                                    # Valor total de um único produto adicionado no arrinho
                                    # Aqui está sendo calculado o valor total que será acrescentado no carrinho, em que pegamos o valor do produto e multiplicamos pela quantidade que será inserida no carrinho
                                    valor_total_produto = valor_produto * \
                                        int(quantidade_escolhida)

                                    conta -= valor_total_produto  # Atualiza o valor da conta

                                    # Usei vários write para que se tenha a formatação correta
                                    carrinho.write('%2s' % quantidade_escolhida)
                                    carrinho.write('%2s' % ('-'))
                                    carrinho.write('%20s' % produto_remover)
                                    carrinho.write('%2s' % ('-'))
                                    carrinho.write('%20s' % ('Preco unitario:'))
                                    carrinho.write('%6.2f' % valor_produto)
                                    carrinho.write('%10s' % ('Valor: '))
                                    carrinho.write('%3s' % ('-'))
                                    carrinho.write('%6.2f' % valor_total_produto)
                                    carrinho.write('%10s' %
                                                ('Código: %s' % (produto)))
                                    carrinho.write('%10s\n' % ('- Cancelado'))

                                    carrinho.close()

                                    # --------------------------------------------------------------------------------Atualizadno conta e qunatidades no carrinho!

                                    # Transforma em string novamente a lista qunatidades
                                    quantidades_string = ''
                                    for elemento in quantidades:
                                        quantidades_string += str(elemento) + ' '

                                    carrinho = open('{}.txt' .format(cpf), 'r')
                                    carrinho_linhas = carrinho.readlines()
                                    carrinho.close()

                                    # Volta a conta para o tipo string e com o \n na lista do cadastro
                                    carrinho_linhas[0] = str(conta) + '\n'
                                    # Adiciona com \n na lista do cadastro
                                    carrinho_linhas[1] = quantidades_string + '\n'

                                    carrinho_update = open(
                                        '{}.txt' .format(cpf), 'w')
                                    # Reescreve o arquivo inteiro mas com o valor da conta atualizado
                                    for elemento in carrinho_linhas:
                                        carrinho_update.write(elemento)

                                    carrinho_update.close()

                                    break

                    elif (produto == 'voltar'):
                        clear()
                        break

                    else:
                        clear()
                        print('Código de produto inválido! Digite novamente!')
                        br(1)
            except:
                print('Não há registros de pedido com esse CPF!')

        else:
            clear()
            print('Cadastro não encontrado ou digitado incorretamente!')
            br(1)
