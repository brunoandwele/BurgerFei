from funcoes.br import br

def menuPedido(cpf): #Função para criar um novo novoPedido que possui como argumento a string do cpf do cliente
    br()#Quebra de linha

    cpf = cpf.strip('\n') #Realiza o strip da string do cpf, tirando o \n que veio após ser tirado do arquivo, para então poder associar ao nome do arquivo que será o carrinho do cliente

    carrinho = open('{}.txt' .format(cpf),'a') #Cria ou edita o arquivo que é o carrinho do cliente

    
    #Fiz uma matriz para representar o cardápio do burgerFei
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
    valores = [0, 10, 10, 7.5, 8, 5.5, 4.5, 6.25] #Lista contendo os valores em reais dos produtos, para que futuramente seja calculado o preço total a se pagar!

    quantidade_total = 0 #Varíavel que será usada para indicar quantos itens novos foram adicionados ao carrinho

    valor_total_adicionado = 0 #Varíavel que será usada para indicar qual o valor total em reais de todos os produtos adicionados no carrinho.
    
    while True:

        #Toda vez que for adicionado um item no carrinho, ele mostrará novamente o cardápio
        #Sistema abaixo feito para imprimir corretamente o cardápio
        print('##########################################################################################') #Para isolar o cardápio
        for i in range(len(cardapio)):
            for k in cardapio[i]:
                print('%20s' %(k), end=' ') #Imprime cada item do cardápio com um espaçamento de 20 caracteres reservados à esqueda
            br()#Quebra de linha
        print('##########################################################################################') #Para isolar o cardápio
        
        br(2) #Quebra de 2 linhas

        pedido = input('Qual item gostaria de adicionar ao seu carrinho? \nDigite o número referente ao código do alimento ou "0" caso não deseje adicionar mais nenhum item ao carrinho: \n ') #Pergunta qual item ele quer adicionar no carrinho e caso não queira adicionar mais nada é informado que precisa digitar "0"

        if pedido in ['1','2','3','4','5','6','7']: #Verifica se a variável "pedido" recebeu um desses valores

            produto = (cardapio[int(pedido)][1])#Cria uma variável chamada "produto" que assume um valor do item que será adicionado diretamente da matriz "cardapio", essa variável será usada para pegar o nome do produto para depois usar no extrarto e deixar no carrinho também

            valor_produto = valores[int(pedido)] #Pegar o valor do produto escolhido a partir da lista contendo os valores dos produtos, sendo que o índice na lista se refere ao código do alimento no cardápio

            quantidade = int(input('Quantidade a ser adicionada no carrinho: \n')) #Pergunta quantos itens do alimento desejado deverá ser adicionado no carrinho

            #Valor total de um único produto adicionado no arrinho
            valor_total_produto = valor_produto * quantidade #Aqui está sendo calculado o valor total que será acrescentado no carrinho, em que pegamos o valor do produto e multiplicamos pela quantidade que será inserida no carrinho

            #Quantidade TOTAL de TODOS produtos ADICIONADOS + valor TOTAL ADICIONADO
            quantidade_total = quantidade_total + quantidade #Soma com a variável quantidade_total o valor da quantidade adicionada, somente para depois poder informar o usuário sobre quantos itens foram inseridos no carrinho

            valor_total_adicionado = valor_total_adicionado + valor_total_produto #Variável para informar quantos reais serão adicionados no carrinho após fechar ele!!! 


            #Usei vários write para que se tenha a formatação correta 
            carrinho.write('%2i' %quantidade)
            carrinho.write('%2s' %('-'))
            carrinho.write('%20s' %produto)
            carrinho.write('%2s' %('-'))
            carrinho.write('%20s' %('Preco unitario:'))
            carrinho.write('%6.2f' %valor_produto)
            carrinho.write('%10s' %('Valor: '))
            carrinho.write('%3s' %('+'))
            carrinho.write('%6.2f\n' %valor_total_produto)

            


        elif pedido == '0': #Se o cliente declarar "0" como resposta do input, significa que ele não quer adicionar mais nada no carrinho

            #Informa que o carrinho foi fechado e informa também quantos produtos foram adicionados e o valor em reais total
            print('Carrinho fechado com sucesso!\nForam adicionados %i produto(s) ao carrinho!' %quantidade_total)
            print('Totalizando um total de R$ %.2f adicionados na conta!' %valor_total_adicionado)

            carrinho.close() #Fecha o arquivo do carrinho

            break #Quebra o loop que adiciona pedidos ao carrinho

        else: #Caso o cliente informe algum valor que não seja válido no input, ele informa que o que foi inserido é invalido e pede novamente para inserir um novo valor!
            print('Insira um valor válido!')