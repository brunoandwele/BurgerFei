from funcoes.verificar import verificacao

from funcoes.br import br

def removerProduto():
    br()
    print('Para remover um produto é necessário informar novamente o cpf e a senha!')
    confirmar = input('Gostaria mesmo de remover um produto? \nSim - "1" \nNão - "0" \n: ')
    br()

    if confirmar == '1':

        cardapio = [
                ['Código','Produto', 'Preço'],
                ['1', 'X-salada', 'R$ 10,00'],
                ['2', 'X-burger', 'R$ 10,00'],
                ['3', 'Cachorro quente', 'R$ 7,50'],
                ['4', 'Misto quente', 'R$ 8,00'],
                ['5', 'Salada de frutas', 'R$ 5,50'],
                ['6', 'Refrigerante', 'R$ 4,50'],
                ['7', 'Suco natural', 'R$ 6,25']
            ]
        valores = ['-', 10, 10, 7.5, 8, 5.5, 4.5, 6.25] #Lista contendo os valores em reais dos produtos, para que futuramente seja calculado o preço total a se pagar!
        
        cpf,verificacao_bool = verificacao()

        if verificacao_bool == True:

            cadastro = open('cadastro.txt','r')
            cadastro_linhas = cadastro.readlines()
            index_conta = cadastro_linhas.index(cpf + '\n') + 3
            index_quantidades = cadastro_linhas.index(cpf + '\n') + 4
            conta = cadastro_linhas[index_conta]
            quantidades = cadastro_linhas[index_quantidades]

            conta = float(cadastro_linhas[index_conta].strip("\n")) #tira o \n e transforma a conta em float
            quantidades = (cadastro_linhas[index_quantidades].strip('\n')).split(' ') #Transforma

            cadastro.close()

            carrinho = open('{}.txt' .format(cpf),'r')
            carrinho_texto = carrinho.read()
            print(carrinho_texto)
            carrinho.close()

            carrinho = open('{}.txt' .format(cpf),'a')

            while True:
                br()
                produto = input('Qual o produto que deseja remover?\nDigite o código dele!\nCaso tenha entrado sem querer, digite "voltar" para voltar ao menu!\n: ')
                br()

                if produto in ['1','2','3','4','5','6','7']: #Verifica se a variável "produto" recebeu um desses valores

                    while True:
                        br()
                        quantidade_escolhida = (input('Digite a quantidade a ser removida do carrinho:\n(OBS:Caso queira voltar, digite "voltar")\n:')) #Pergunta quantos itens do alimento desejado deverá ser adicionado no carrinho
                        br()

                        if quantidade_escolhida == 'voltar':
                            br()
                            print('Voltando')
                            br()
                            break
                        
                        else:

                            quantidades[int(produto)] = int(quantidades[int(produto)]) - int(quantidade_escolhida) #Atualiza a quantidade do produto adicionado na lista quantidade!

                            if quantidades[int(produto)] < 0 :

                                quantidades[int(produto)] = 0
                                br()
                                print('Quantidade inválida! Quantidade inserida é maior do que a quantidade dentro do carrinho!')
                                (br)

                            else:

                                produto_remover = (cardapio[int(produto)][1])#Cria uma variável chamada "produto" que assume um valor do item que será adicionado diretamente da matriz "cardapio", essa variável será usada para pegar o nome do produto para depois usar no extrarto e deixar no carrinho também

                                valor_produto = valores[int(produto)] #Pegar o valor do produto escolhido a partir da lista contendo os valores dos produtos, sendo que o índice na lista se refere ao código do alimento no cardápio

                                #Valor total de um único produto adicionado no arrinho
                                valor_total_produto = valor_produto * int(quantidade_escolhida) #Aqui está sendo calculado o valor total que será acrescentado no carrinho, em que pegamos o valor do produto e multiplicamos pela quantidade que será inserida no carrinho

                                conta -= valor_total_produto #Atualiza o valor da conta

                                #Usei vários write para que se tenha a formatação correta 
                                carrinho.write('%2s' %quantidade_escolhida)
                                carrinho.write('%2s' %('-'))
                                carrinho.write('%20s' %produto_remover)
                                carrinho.write('%2s' %('-'))
                                carrinho.write('%20s' %('Preco unitario:'))
                                carrinho.write('%6.2f' %valor_produto)
                                carrinho.write('%10s' %('Valor: '))
                                carrinho.write('%3s' %('-'))
                                carrinho.write('%6.2f' %valor_total_produto)
                                carrinho.write('%10s' %('Código: %s' %(produto)))
                                carrinho.write('%10s' %('- Cancelado'))

                                carrinho.close()

                                #Transforma em string novamente a lista qunatidades
                                quantidades_string = ''
                                for elemento in quantidades:
                                    quantidades_string += str(elemento) + ' '
                                    

                                cadastro_linhas[index_conta] = str(conta) + '\n' #Volta a conta para o tipo string e com o \n na lista do cadastro
                                cadastro_linhas[index_quantidades] = quantidades_string + '\n' #Adiciona com \n na lista do cadastro


                                cadastro_update = open('cadastro.txt','w') 
                                #Reescreve o arquivo inteiro mas com o valor da conta atualizado
                                for elemento in cadastro_linhas:
                                    cadastro_update.write(elemento)

                                cadastro_update.close()

                                break
                    break
                
                elif produto == 'voltar' or quantidade == 'voltar':
                    break
                    
                else:
                    br()
                    print('Código de produto inválido! Digite novamente!')
                    br()

        else:
            br()
            print('Cadastro não encontrado ou digitado incorretamente!')
            br()


            







