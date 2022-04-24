def br(linhas=1): #Funçãp para inserir quebras de linhas!
    for i in range(linhas):
        print()
########################################################################################################################
########################################################################################################################
#Funções que envolvem o cadastro dos usuários!

#Cadastrar novos usuários
def clienteNovo(): #Função para criar um cadastro - será chamada dentro da função "novoPedido_1()"
    nome = input('Digite seu nome completo:\n') #Coletar o nome do usuário
    cpf = input('Digite seu CPF (apenas dígitos):\n') #Coletar o cpf do usuário
    senha = input('Digite sua nova senha:\n') #Coletar a senha do usuário

    cadastro = open('cadastro.txt','a') # Cria ou Abre o arquivo com todos os cadastros e adiciona um novo

    cadastro.write('%s\n%s\n%s\n' %(cpf, senha, nome)) #Escrever no arquivo o CPF, a senha e o nome respectivamente do novo usuário
    cadastro.write('\n') #Para acrescentar uma quebra de linha entre o cadastro de cada usuário

    cadastro.close() #Fechar o arquivo

    return nome,cpf #Retorna o nome e o cpf para o cadastro()

#-----------------------------------------------------------------------------------------------------------------------

#Login de antigos clientes
def clienteAntigo(): #Ele irá tentar fazer o login do cliente, se não tiver o cadastro ele perguntará se quer cadastrar

    print('Faça o login! Informe seu CPF e sua senha: \n') #Informa que irá prosseguir para o login

    cadastro = open('cadastro.txt','r') #Abre o arquivo com os cadastros

    data = cadastro.readlines() #Adiciona à "data" todos os valores de cadastros (adiciona em forma de lista - 1 linha = 1 elemento da lista)

    cadastro.close() #Fecha o arquivo dos cadastros

    cpf = input('Digite seu CPF (apenas dígitos):\n') + '\n' #pergunta o cpf do usuário  e logo depois verifica se tem no arquivo - OBS: é adicionado o "\n" pois ao usar o readlines() as informações são passadas com o \n

    if cpf in data: #Verifica se o usuário já está cadastrado ou não, se estiver irá perguntar a senha se não irá cadastrar ele

        index_cpf = data.index(cpf) #Pega o valor do índice do cpf na lista pois a senha fica 1 indece à frente

        index_senha = index_cpf + 1 #Adiciona 1 ao valor do indice do cpf, pois se refere ao indice da senha

        index_nome = index_cpf + 2 #Adiciona 2 ao valor do índice do cpf, pois se refere ao indice do nome que é dois a frente do cpf

        nome = data[index_nome] #atribui um valor à variável "nome", pois mais para frente irei retornar ela ao main()

        while True: #Loop até o cliente acertar a senha

            senha = input('Digite sua senha:\n') + '\n' #OBS: é adicionado o "\n" pois ao usar o readlines() as informações são passadas com o \n

            if senha == data[index_senha]: #Verifica se a senha digitada está associada ao CPF e se está correta
                print('Login realizado com sucesso!') #Avisa que o login foi realizado com sucesso
                return nome, cpf #Retorna o nome e o cpf para o cadastro()
                break #Para o loop
                
            


            else:
                print("Senha incorreta! Tente novamente") #Diz que a senha está incorreta e informa que precisará dizer novamente qual que é 
    
    else: #Caso o CPF não esteja no arquivo de cadastros - irá informar que o cliente precisa realizar cadastro!

        while True: #Loop até ter um input válido - 1 ou 0

            realizar_cadastro = input('CPF não encontrado nos registros! Deseja realizar o cadastro: \n 0 - Não \n 1 - Sim\n') #pergunta se o cliente quer realizar um cadastro já que não tem um
        
            if realizar_cadastro == '0': #Se ele recusar o programa só irá fechar
                print('Ok!')
                break
            elif realizar_cadastro == '1': #Se ele aceitar, a função de cadastro "clienteNovo()" será chamada
                clienteNovo()
                break
            else:
                print('Valor inválido!  \n 0 - Não \n 1 - Sim \n') #Se ele não colcoar nem 0 nem 1, ele continuará perguntando até um desses caracteres serem digitados.


#-----------------------------------------------------------------------------------------------------------------------

#Função que verifica o cliente
def cadastro(): #Função para criar um novo pedido!

    while True: #Loop para verificar se o cliente já existe!

        verify = input('Já possui cadastro? \n 0 - Não \n 1 - Sim \n') #Pergunta se já possui cadastro ou não

        if verify== '0': #Caso o usuário não tenha cadastro, chamará a função para criar um

            nome, cpf = clienteNovo() #Função para criar cadastro, retornando o nome e o cpf
            return nome, cpf #Retorna o nome e o cpf para o main()

            break #Parar o loop de pergunta se já tem cadastro

        elif verify == '1': #Se ele já for cadastrado, ou achar que tem cadastro, chamará a função "clienteAntigo()" para tentar realizar o login

            nome, cpf = clienteAntigo() #Função que da o login de um cliente antigo, retornando o nome e cpf
            return nome, cpf #Retorna o nome e o cpf para o main()

            break

        else: #Caso o usuário não digite nem 1 nem 0, o programa continuará perguntando se o usuário tem ou não cadastro

            print('Valor inválido \n')
            continue


########################################################################################################################
########################################################################################################################
#Função para pedir novo pedido

def novo_pedido(nome,cpf): #Função para criar um novo novoPedido que possui como argumento a string do cpf do cliente
    br()#Quebra de linha

    cpf = cpf.strip('\n') #Realiza o strip da string do cpf, tirando o \n que veio após ser tirado do arquivo, para então poder associar ao nome do arquivo que será o carrinho do cliente

    carrinho = open('{}.txt' .format(cpf),'a') #Cria ou edita o arquivo que é o carrinho do cliente!


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

            produto = (cardapio[int(pedido)][1])#Cria uma variável chamada "produto" que assume um valor do item que será adicionado diretamente da matriz "cardapio", portanto é necessário juntar os elementos da linha em uma string única

            valor_produto = valores[int(pedido)] #Pegar o valor do produto escolhido a partir da lista contendo os valores dos produtos, sendo que o índice na lista se refere ao código do alimento no cardápio

            print(valor_produto)


            quantidade = int(input('Quantidade a ser adicionada no carrinho: \n')) #Pergunta quantos itens do alimento desejado deverá ser adicionado no carrinho

            quantidade_total = quantidade_total + quantidade #Soma com a variável quantidade_total o valor da quantidade adicionada, somente para depois poder informar o usuário sobre quantos itens foram inseridos no carrinho

            valor_total_produto = valor_produto * quantidade #Aqui está sendo calculado o valor total que será acrescentado no carrinho, em que pegamos o valor do produto e multiplicamos pela quantidade que será inserida no carrinho

            print(valor_total_produto)

            valor_conta = valor_conta + valor_total_produto

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
            print('Carrinho fechado com sucesso!\nForam adicionados %i produto(s) ao carrinho!' %quantidade_total) #Informa que o carrinho foi fechado e informa também quantos produtos foram adicionados
            carrinho.close() #Fecha o arquivo do carrinho
            break #Quebra o loop que adiciona pedidos ao carrinho

        else: #Caso o cliente informe algum valor que não seja válido no input, ele informa que o que foi inserido é invalido e pede novamente para inserir um novo valor!
            print('Insira um valor válido!')

    return valor_conta #Retorna para o main() a quantidade total que o cliente terá que pagar! Para que futuramente saia no extrato






########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
def main():
    nome, cpf = cadastro() #Após a função cadastro finalizar sua atividade, serão retornados os valores do nome e do cpf
    valor_conta = novo_pedido(nome,cpf) #Chama a função para adicionar pedidos no carrinho do cliente

main()