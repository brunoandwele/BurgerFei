from funcoes.menuPedido import menuPedido

def novoPedido(): #Função para criar um cadastro - será chamada dentro da função "novoPedido_1()"
    nome = input('Digite seu nome completo:\n') #Coletar o nome do usuário
    cpf = input('Digite seu CPF (apenas dígitos):\n') #Coletar o cpf do usuário
    senha = input('Digite sua nova senha:\n') #Coletar a senha do usuário

    conta = 0 #Cria a variável conta que será usada para registrar os precos!

    cadastro = open('cadastro.txt','a') # Cria ou Abre o arquivo com todos os cadastros e adiciona um novo

    quantidades = '- 0 0 0 0 0 0 0' #string que será transformada em lista depois para atualizar os valores das quantidades 

    cadastro.write('%s\n%s\n%s\n%.2f\n%s\n' %(cpf, senha, nome, conta, quantidades))#Escrever no arquivo o CPF, a senha e o nome, a conta e a quantidade de produtos respectivamente do novo usuário

    cadastro.write('\n\n') #Para acrescentar duas quebra de linha entre o cadastro de cada usuário no arquivo

    cadastro.close()

    menuPedido(cpf)

    
