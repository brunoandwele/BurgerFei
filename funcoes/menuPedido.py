from funcoes.br import br
import os
#OBS: aqui eu usei duas ferramentas para controlar o valor da conta e a quantidade - Assim que é criado o pedido ele adiciona nas duas primeiras linhas um "0\n" e uma string "- 0 0 0 0 0 0 0\n", essas duas strings representam respectivamente o valor da conta e a lista sobre a quantidade de itens no carrinho: a conta é um valor que toda vez que algo é adicionado ou removido do carrinho é necessário pegar esse valor, tirar o \n e então transformar em float e depois reescrever o arquivo; e o segundo é uma string que toda vez que algo é adicionado ou removido eu mudo os valores de cada 0 a partir do código do produto no menu, já que como comeca no indice 1 ele segue o mesmo do menu, então eu tiro o \n e uso o metodo split() dando split no ' ' (espaço), transformando em lista e após mudar eu reescrevo no arquivo, transformando em uma string primeiramente.

def menuPedido(cpf):  # Função para criar um novo novoPedido que possui como argumento a string do cpf do cliente
    clear = lambda: os.system('cls')
    clear()
    try: #Ele tenta abrir o pedido do usuário, caso já exista ele irá pegar os valores 
        carrinho = open('{}.txt' .format(cpf), 'r')
        carrinho_linhas = carrinho.readlines()
        # tira o \n e transforma a conta em float
        conta = float(carrinho_linhas[0].strip("\n")) #Transforma a string da conta em float novamente sem o \n
        quantidades = (carrinho_linhas[1].strip('\n')).split(
            ' ')  # Transforma em lista a string das quantidades, tirando o \n
        carrinho.close()

    except: #Caso não exista ainda um pedido, ele cria um arquivo, além de criar os valores da conta e das quantidades
        carrinho = open('{}.txt' .format(cpf), 'a')
        conta = 0
        quantidades = '- 0 0 0 0 0 0 0'
        carrinho.write('%.2f\n%s\n' % (conta, quantidades))
        quantidades = quantidades.split(' ')
        carrinho.close()

    carrinho = open('{}.txt' .format(cpf), 'a')

    # Fiz uma matriz para representar o cardápio do burgerFei
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

    while True:
        # Toda vez que for adicionado um item no carrinho, ele mostrará novamente o cardápio
        # Sistema abaixo feito para imprimir corretamente o cardápio
        # Para isolar o cardápio
        print('##########################################################################################')
        for i in range(len(cardapio)):
            for k in cardapio[i]:
                # Imprime cada item do cardápio com um espaçamento de 20 caracteres reservados à esqueda
                print('%20s' % (k), end=' ')
            br()  # Quebra de linha
        # Para isolar o cardápio
        print('##########################################################################################')

        br(1)  # Quebra de 2 linhas

        # Pergunta qual item ele quer adicionar no carrinho e caso não queira adicionar mais nada é informado que precisa digitar "0"
        pedido = input('Qual item gostaria de adicionar ao seu carrinho? \nDigite o número referente ao código do alimento ou "0" caso não deseje adicionar mais nenhum item ao carrinho\n\nDigite sua resposta aqui: ')
        br(1)

        # Verifica se a variável "pedido" recebeu um desses valores
        if pedido in ['1', '2', '3', '4', '5', '6', '7']:

            # Cria uma variável chamada "produto" que assume um valor do item que será adicionado diretamente da matriz "cardapio", essa variável será usada para pegar o nome do produto para depois usar no extrarto e deixar no carrinho também
            produto = (cardapio[int(pedido)][1])

            # Pegar o valor do produto escolhido a partir da lista contendo os valores dos produtos, sendo que o índice na lista se refere ao código do alimento no cardápio
            valor_produto = valores[int(pedido)]

            # Pergunta quantos itens do alimento desejado deverá ser adicionado no carrinho
            quantidade_escolhida = int(
                input('Quantidade a ser adicionada no carrinho: \n'))
            br(1)
            clear()

            # Atualiza a quantidade do produto adicionado na lista quantidade!
            quantidades[int(pedido)] = int(
                quantidades[int(pedido)]) + quantidade_escolhida

            # Valor total de um único produto adicionado no arrinho
            # Aqui está sendo calculado o valor total que será acrescentado no carrinho, em que pegamos o valor do produto e multiplicamos pela quantidade que será inserida no carrinho
            valor_total_produto = valor_produto * quantidade_escolhida

            conta += valor_total_produto  # Atualiza o valor da conta

            # Usei vários write para que se tenha a formatação correta
            carrinho.write('%2i' % quantidade_escolhida)
            carrinho.write('%2s' % ('-'))
            carrinho.write('%20s' % produto)
            carrinho.write('%2s' % ('-'))
            carrinho.write('%20s' % ('Preco unitario:'))
            carrinho.write('%6.2f' % valor_produto)
            carrinho.write('%10s' % ('Valor: '))
            carrinho.write('%3s' % ('+'))
            carrinho.write('%6.2f' % valor_total_produto)
            carrinho.write('%10s\n' % ('Código: %s' % (pedido)))

        elif pedido == '0':  # Se o cliente declarar "0" como resposta do input, significa que ele não quer adicionar mais nada no carrinho

            carrinho.close()  # Fecha o arquivo do carrinho

            break  # Quebra o loop que adiciona pedidos ao carrinho

        else:  # Caso o cliente informe algum valor que não seja válido no input, ele informa que o que foi inserido é invalido e pede novamente para inserir um novo valor!
            clear()
            print('Insira um valor válido!')
            br(1)


    #Atualizadno conta e qunatidades no carrinho!

    # Transforma em string novamente a lista qunatidades
    quantidades_string = ''
    for elemento in quantidades:
        quantidades_string += str(elemento) + ' '

    carrinho = open('{}.txt' .format(cpf), 'r')
    carrinho_linhas = carrinho.readlines()
    carrinho.close()

    # Volta a conta para o tipo string e com o \n na lista do cadastro
    carrinho_linhas[0] = str(conta) + '\n'
    carrinho_linhas[1] = quantidades_string + \
        '\n'  # Adiciona com \n na lista do cadastro

    carrinho_update = open('{}.txt' .format(cpf), 'w')
    # Reescreve o arquivo inteiro mas com o valor da conta atualizado
    for elemento in carrinho_linhas:
        carrinho_update.write(elemento)

    carrinho_update.close()

    #--------------------------------------------------------
    #Caso o usuário não tenha adicionado nada no carrinho, o carrinho ficará vazio mas o pedido ainda existirá, então para não ter esse problema,ele irá verificar se ele está vazio e se estiver ele irá apagar o pedido
    verifica = carrinho = open('{}.txt' .format(cpf), 'r')
    verifica_linhas = verifica.readlines()
    verifica.close()
    if len(verifica_linhas) < 3:
            os.remove("{}.txt" .format(cpf))
    #--------------------------------------------------------

    clear()

    