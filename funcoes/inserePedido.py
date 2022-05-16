from funcoes.menuPedido import menuPedido
from funcoes.br import br
from funcoes.verificar import verificacao
from funcoes.novoPedido import novoPedido
import os

def inserePedido():  # Ele irá tentar fazer o login do cliente, se não tiver o cadastro ele perguntará se quer cadastrar.Além de que recebe como argumento a conta_pagar pois ela irá chamar novamente a funçãp menuPedido(), a qual precisa do valor da conta para que ela seja atualizada
    clear = lambda: os.system('cls')
    clear()

    cpf, verificacao_bool = verificacao()

    if verificacao_bool == True:
        try: #Tenta ver se já tem um pedido criado ou não, caso já tenha, irá para a função menu pedido
            arquivo = open('{}.txt' .format(cpf),'r')
            arquivo.close()
            pedido = True #Variável para saber se tem ou não um pedido já iniciado
            
        except:#Caso não tenha um pedido iniciado, informa que precisará ir para a função "novoPedido"
            pedido = False

        if pedido:
            menuPedido(cpf)
        
        else:
            clear()
            print('Pedido não iniciado ainda, para criar um novo pedido use a opção "Novo Pedido"')
            br(1)

    else:  # Caso o CPF não esteja no arquivo de cadastros - irá informar que o cliente precisa realizar cadastro!
        clear()
        print('Cadastro não encontrado!\nPara criar um novo pedido, use a opção "1- Novo pedido"')
        br()
                
