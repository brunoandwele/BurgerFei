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

    # Coletar o cpf do usuário
    cpf = input('Digite seu CPF (apenas dígitos):\n')

    if (cpf + '\n') in cadastro_linhas:
        index_senha = cadastro_linhas.index(cpf + '\n') + 1
        clear()
        while True:
            senha = input('CPF já cadastrado\nInforme a sua senha: ')
            if (senha + '\n') == cadastro_linhas[index_senha]:
                try: 
                    clear()
                    while True:
                        carrinho = open('{}.txt' .format(cpf), 'r')
                        carrinho_linhas = carrinho.readlines()
                        carrinho.close()
                        print('Um pedido com o seu CPF já está ativo!\n')
                        for i in range(2, len(carrinho_linhas)):
                            print(carrinho_linhas[i])
                        br(2)
                        novo = input('Gostaria de criar um novo pedido ou manter o original?\n\nNovo pedido - "novo"\n\nManter pedido atual - "manter"\n\nDigite sua opção aqui: ')

                        if novo.lower() == 'novo':
                            os.remove("{}.txt" .format(cpf))
                            os.remove("extrato_{}.txt" .format(cpf))
                            menuPedido(cpf)
                            break
                        elif novo.lower() == 'manter':
                            clear()
                            print('Pedido mantido! Para adicionar novo itens no carrinho use a opção "Inserir produto" no menu de opções!')
                            br(2)
                            break
                        else:
                            clear()
                            print('Insira uma opção válida!')
                    

                except:
                    menuPedido(cpf)
                break
            else:
                clear()
                print('Senha incorreta!Tente novamente!')

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
