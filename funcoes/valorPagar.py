from funcoes.br import br
from funcoes.verificar import verificacao

def valorPagar():
          br(10)
          while True:
                    pergunta = input('Gostaria de verificar o valor da conta? \nSim -"1" \nNão-"0"\n:')
                    br(5)

                    if pergunta == '1':

                              while True:
                                        cpf, verificar_bool = verificacao()

                                        if verificar_bool == True:
                                                  cadastro = open('cadastro.txt', 'r')
                                                  cadastro_linhas = cadastro.readlines()
                                                  cpf_index = cadastro_linhas.index(cpf + '\n')
                                                  conta_index = cpf_index + 3

                                                  
                                                  print('Valor a se pagar: R$%.2f' %float(cadastro_linhas[conta_index].strip('\n')))
                                                  br(5)

                                                  break

                                        else:
                                                  print('CPF não encontrado no sistema!')
                                                  br(5)
                              break
                                        
                    elif pergunta == '0':
                              
                              print('Voltando...')
                              br(5)
                              break
                    else:                  
                              print('Insira um valor válido!')
                              br(5)