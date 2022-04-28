from menuPedido import menuPedido

def novoPedido(): #Função para criar um cadastro - será chamada dentro da função "novoPedido_1()"
    nome = input('Digite seu nome completo:\n') #Coletar o nome do usuário
    cpf = input('Digite seu CPF (apenas dígitos):\n') #Coletar o cpf do usuário
    senha = input('Digite sua nova senha:\n') #Coletar a senha do usuário

    cadastro = open('cadastro.txt','a') # Cria ou Abre o arquivo com todos os cadastros e adiciona um novo

    cadastro.write('%s\n%s\n%s\n' %(cpf, senha, nome)) #Escrever no arquivo o CPF, a senha e o nome respectivamente do novo usuário
    cadastro.write('\n') #Para acrescentar uma quebra de linha entre o cadastro de cada usuário

    cadastro.close()

    menuPedido(cpf)

    return nome,cpf #Retorna para o main os valores do nome, do cpf e da conta.
