from funcoes.menuPedido import menuPedido
from funcoes.br import br
import os



def novoPedido():  # Função para criar um cadastro - será chamada dentro da função "novoPedido_1()"
    clear = lambda: os.system('cls')
    clear()
    # Cria ou Abre o arquivo com todos os cadastros e adiciona um novo
    cadastro = open('cadastro.txt', 'r')
    cadastro_linhas = cadastro.readlines()
    cadastro.close()

    while True:
        # Coletar o cpf do usuário
        cpf = input('Digite seu CPF (apenas dígitos):\n')

        if (cpf + '\n') in cadastro_linhas:
            clear()
            print(
                'CPF já cadastrado! Para adicionar novo itens no carrinho use a opção "Inserir produtos"! ')
            break

        else:
            clear()
            # Coletar o nome do usuário
            nome = input('Digite seu nome completo:\n')
            clear()
            # Coletar a senha do usuário
            senha = input('Digite sua nova senha:\n')
            
            cadastro = open('cadastro.txt', 'a')
            # Escrever no arquivo o CPF, a senha e o nome respectivamente do novo usuário
            cadastro.write('%s\n%s\n%s\n' % (cpf, senha, nome))
            # Para acrescentar duas quebra de linha entre o cadastro de cada usuário no arquivo
            cadastro.write('\n\n')
            cadastro.close()

            menuPedido(cpf)  # Chama a função de adicionar novos produtos!
            break
