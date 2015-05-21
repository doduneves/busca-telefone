from time import time
from time import sleep
import math 

# Mudar para 1 para testar o tempo de execucao
testeTempo = 0
inicio = time()	

# Tratamento do arquivo texto com telefones
ARQUIVO = "telefones.txt"

arquivo = open(ARQUIVO, "r")
palavras = arquivo.readlines()
arquivo.close()

palavraExcesso = 0
for p in palavras:
        if len(p)-1 < 1 or len(p)-1 > 30:
                palavraExcesso = 1
                palavras.remove(p)

# Crio um dicionario do alfabeto maiusculo
alfabeto = {}

for i in range(65, 91):
	alfabeto[''.join(map(chr, [i]))] =  i-64

numerosTel = {}
numerosTel[2] = "ABC"
numerosTel[3] = "DEF"
numerosTel[4] = "GHI"
numerosTel[5] = "JKL"
numerosTel[6] = "MNO"
numerosTel[7] = "PQRS"
numerosTel[8] = "TUV"
numerosTel[9] = "WXYZ"

# Metodo que percorre todos as linhas do array numerosTel
def buscaDoInicio(letra):
	for n in numerosTel:
		if(buscaPalavra(letra, n)):
			return n
			exit(0)
		if testeTempo: sleep(0.005)
	return letra

# Metodo que chuto um provavel valor onde esta minha letra no array numerosTel
def buscaPaginada(letra):
	if alfabeto.get(letra) == None:
		if testeTempo: sleep(0.005)
		return letra
	else:
		chute = int(math.floor(alfabeto.get(letra)/3)+2)
		if chute == 10 : chute = 9  # offset
		if testeTempo: sleep(0.005)
		return buscaPalavra(letra, chute) if  buscaPalavra(letra, chute)  else buscaPalavra(letra, chute-1) 

# Busco a letra em determinada palavra de numerosTel
def buscaPalavra(letra, n):
	for i in numerosTel[n]:
		if (i == letra):
			return n
			exit(0)

			
			
def mostraResultado(arrPalavras, metodoBusca):
	for palavra in arrPalavras:	
		telefone = ''
		for l in palavra:
			telefone += str(metodoBusca(l))
		print telefone
	
	if testeTempo:
		print("\n----------------------------------")
		print str(metodoBusca)
		print ("Tempo de execucao: %f" % (time() - inicio))
		print("----------------------------------\n")

if palavraExcesso: print("Atencao, ha palavras fora do limite de 1 a 30 caracteres no arquivo!\n")
        
mostraResultado(palavras, buscaPaginada)
#mostraResultado(palavras, buscaDoInicio)

