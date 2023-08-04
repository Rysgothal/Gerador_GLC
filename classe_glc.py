from collections import defaultdict
import random

# Crio a Classe GLC
class GLC(object):
    # 'F' de Field para representar uma variavel acessada por outros lugares
    # Função para Instanciar a Classe e Criar o "Dicionário"
    def __init__(self):
        self.FDicionario = defaultdict(list)
        self.FCaminhoSequencia = ''
        self.FGramatica = ''

    # 'p' antes, para representar Parametros da função
    # Função para adiconar palavras ao dicionário
    def AdicionarDicionario(self, pSigla, pPalavras):     
        # 'v' antes, para representar Variaveis Locais
        vDicionario = pPalavras.split('|')
        self.FGramatica += '\n' + pSigla.ljust(4, ' ')   
        self.FGramatica += ' --> ' + pPalavras

        
        for vItem in vDicionario:
            if vItem.strip() == '':
                continue
            
            self.FDicionario[pSigla].append(tuple(vItem.split()))

    # Gera uma sequencia aleatoria de palavras de acordo com a gramatica
    def GerarSequenciaAleatoria(self, pSimbolo):
        vSentenca = ''

        #seleciona um simbolo aleatoriamente
        vAleatorio = random.choice(self.FDicionario[pSimbolo])
        self.FCaminhoSequencia += ' --> ' + pSimbolo

        for vSimbolo in vAleatorio:
            if vSimbolo in self.FDicionario:
                vSentenca += self.GerarSequenciaAleatoria(vSimbolo)

            else:
                vSentenca += vSimbolo + ' '
                self.FCaminhoSequencia += '(' + vSimbolo + ')'

        return vSentenca
    
    # Função para Limpar o Caminho Antigo
    def LimparCaminhoAnterior(self):
        self.FCaminhoSequencia = ''
    
    # Função para Limpar o Dicionario
    def LimparDicionario(self):
        self.FDicionario.clear()
    
    #Função para Limpar a classe inteira
    def LimparGLC(self):
        self.LimparDicionario()
        self.LimparCaminhoAnterior()
        self.FGramatica = ''
        