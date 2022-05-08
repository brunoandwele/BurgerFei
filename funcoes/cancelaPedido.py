import os

from funcoes.verificar import verificacao
from funcoes.br import br


def cancelaPedido():
          br(10)
          deletar = input('Gostaria de cancelar o seu pedido? \nEstá ação não poderá ser desfeita! \nNão - "0"\nSim - "1"\n "voltar" - Para voltar\n\nDigite sua opção aqui:')
          br(5)

          while True:    
                    if deletar == '1':

                              cpf,verificacao_bool = verificacao()

                              if verificacao_bool == True:
                                        os.remove("{}.txt" .format(cpf.strip('\n')))
                                        print("Pedido cancelado com sucesso! Obrigado!")
                                        br(5)
                                        break
                
                              else:
                                        print('CPF digitado incorretamente ou não cadastrado \nCaso acredite que ele não esteja cadastrado, digite "voltar" para voltar ao menu!')
                                        br(5)

                    elif deletar == 'voltar':
                              break       

                    elif deletar !='1' and deletar != '0' and deletar != 'voltar':
                              print('Digite um valor válido!')
                              br(5)

