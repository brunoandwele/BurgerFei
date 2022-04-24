nome = input('Digite seu nome completo:\n')
cpf = int(input('Digite seu CPF (apenas dígitos):\n'))
senha = input('Digite sua nova senha:\n')

cadastro = open('{}.txt' .format(cpf),'w')

cadastro.write('%i\n%s\n%s' %(cpf, senha, nome))

cadastro.close()

cadastro = open('{}.txt' .format(cpf), 'r')

data = cadastro.readlines()

cadastro.close()

print(data[0])
print(data[1])
print(data[2])
