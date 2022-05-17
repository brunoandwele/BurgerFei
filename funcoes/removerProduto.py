from funcoes.verificar import verificacao
from funcoes.br import br
import os


def removerProduto():
    clear = lambda: os.system('cls') #Cria a função para limpar o console
    clear()

    #Para remover usei um método muito parecido com o de inserir produto e do novo pedido, por tanto para adicionar no carrinho que um pedido foi cancelado eu precisei do cardápio e da lista dos precos para poder adicionar no arquivo, já que eu me baseei totalemente nessas duas listas com seus elementos para fazer isso!


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

    cpf, verificacao_bool = verificacao() #Verifica o login e retorna se foi relaizado com sucesso ou não e o valor do cpf do usuário

    if verificacao_bool == True:

        try: #Tenta abrir o pedido do usuário
            carrinho = open('{}.txt' .format(cpf), 'r')
            carrinho_linhas = carrinho.readlines()
            conta = float(carrinho_linhas[0].strip('\n')) #Pega o valor da conta e transforma e float novamente tirando o \n
            quantidades = (carrinho_linhas[1].strip('\n')).split(' ') #Pega o valor das quantidades e tira o \n e depois transforma em lista novamente
            carrinho.close()

            clear()
            while True:
                
                carrinho = open('{}.txt' .format(cpf), 'r')
                carrinho_linhas = carrinho.readlines()

                #Imprime o carrinho do usuario sem mostrar as duas primeiras linhas, já que elas são os valores da conta e das quantidades
                for i in range(2, len(carrinho_linhas)):
                    print(carrinho_linhas[i])

                    
                carrinho = open('{}.txt' .format(cpf), 'a')

                #Pergunta qual produto quer remover a partir do codigo, e caso a pessoa desista ela pode esrever "v" para voltar
                produto = input(
                    'Qual o produto que deseja remover?\nDigite o código dele!\nCaso queira voltar, digite "v" para voltar ao menu!\n\nDigite aqui sua resposta: ')
                br(1)

                # Verifica se a variável "produto" recebeu um desses valores
                if (produto in ['1', '2', '3', '4', '5', '6', '7'] and \
                    int(quantidades[int(produto)]) > 0 ):

                    while True:

                        # Pergunta quantos itens do alimento desejado deverá ser remover do carrinho
                        quantidade_escolhida = (input(
                            'Digite a quantidade a ser removida do carrinho:\n(OBS:Caso queira voltar, digite "v")\n\nDigite aqui sua resposta: '))
                        br(1)

                        if quantidade_escolhida == 'v': #Se digitou V, ele voltará
                            clear()
                            print('Voltando')
                            br()
                            break

                        else:#Caso contrário, irá atualizar o carrinho
                            
                            #Se o valor digitado é maior do que o valor dentro do carrinho, irá informar que a quantidade digitada é maior do que a dentro do carrinho
                            if (int(quantidades[int(produto)]) - int(quantidade_escolhida)) < 0:
                                clear()
                                print(
                                    'Quantidade inválida! Quantidade inserida é maior do que a quantidade dentro do carrinho!')
                                br(1)
                                break

                            else:
                                while True:
                                    try:
                                        clear()
                                        quantidades[int(produto)] = (
                                            int(quantidades[int(produto)]) - int(quantidade_escolhida))

                                        # Cria uma variável chamada "produto" que assume um valor do item que será removido diretamente da matriz "cardapio", essa variável será usada para pegar o nome do produto para depois usar no extrarto e deixar no carrinho também
                                        produto_remover = (cardapio[int(produto)][1])

                                        # Pegar o valor do produto escolhido a partir da lista contendo os valores dos produtos, sendo que o índice na lista se refere ao código do alimento no cardápio
                                        valor_produto = valores[int(produto)]

                                        
                                        # Aqui está sendo calculado o valor total que será removido do carrinho, em que pegamos o valor do produto e multiplicamos pela quantidade que será inserida no carrinho
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
                                        carrinho.write('%10s\n' % ('- Cancelado')) #Acrescenta que foi cancelado!

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
                                    except:
                                        clear()
                                        print('Digite uma quantidade válida para ser removida!')
                                break

                elif (produto == 'v'): #Caso queira voltar
                    clear()
                    break

                else: #Caso digite algum valor diferente dos aceitos
                    clear()
                    print('Código de produto inválido! Digite novamente!')
                    br(1)
        except: #Caso não consiga abrir o arquivo
            clear()
            print('Não há registros de pedido com esse CPF!')
            br(1)

    else:#Caso o login não seja feito com sucesso
        clear()
        print('Cadastro não encontrado ou digitado incorretamente!')
        br(1)
