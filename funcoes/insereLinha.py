def insereLinha(arquivo,elemento,linha): #Função para inserir arquivos em uma linha especifica,precisa fechar o arquivo antes se ele já estiver aberto antes e abri-lo de novo depois!
    #----------------
    abrindoArquivo = open('{}.txt' .format(arquivo.strip('\n')), 'r')
    arquivoLinhas = abrindoArquivo.readlines()
    abrindoArquivo.close()
    #----------------
    arquivoLinhas.insert(linha, (str(elemento) + "\n"))
    abrindoArquivo = open('{}.txt' .format(arquivo.strip('\n')), 'w')
    abrindoArquivo.writelines(arquivoLinhas)
    abrindoArquivo.close()