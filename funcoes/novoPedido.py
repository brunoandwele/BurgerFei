from funcoes.menuPedido import menuPedido
from funcoes.br import br

def novoPedido(): #Função para criar um cadastro - será chamada dentro da função "novoPedido_1()"
          br(10)
          cadastro = open('cadastro.txt','r') # Cria ou Abre o arquivo com todos os cadastros e adiciona um novo
          cadastro_linhas = cadastro.readlines()
          cadastro.close()

          while True:
                    cpf = input('Digite seu CPF (apenas dígitos):\n') #Coletar o cpf do usuário
                    br(5)

                    if (cpf + '\n') in cadastro_linhas:
                              print('CPF já cadastrado! Para adicionar novo itens no carrinho use a opção "Inserir produtos"! ')
                              br(5)
                              break

                    else:
                              nome = input('Digite seu nome completo:\n') #Coletar o nome do usuário
                              br(5)
                              senha = input('Digite sua nova senha:\n') #Coletar a senha do usuário
                              br(5)
                              
                              cadastro = open('cadastro.txt','a')
                              cadastro.write('%s\n%s\n%s\n' %(cpf, senha, nome))#Escrever no arquivo o CPF, a senha e o nome respectivamente do novo usuário
                              cadastro.write('\n\n') #Para acrescentar duas quebra de linha entre o cadastro de cada usuário no arquivo
                              cadastro.close()

                              menuPedido(cpf) #Chama a função de adicionar novos produtos!
                              break
          
