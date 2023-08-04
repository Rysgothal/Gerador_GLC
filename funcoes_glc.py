import classe_glc
from tkinter import *

# Função para deixar SOMENTE a primeira letra da frase
def DeixarLetraMaiusculaComecoFrase(pFrase):
    vFrase = ''
    for vLetra in pFrase:
        if vFrase.__len__() < 1:
            vFrase = vLetra.capitalize()
        else:
            vFrase += vLetra

    return vFrase

'''
    Símbolos e seus significados 

    S: Símbolo de entrada

    N: Nome
    P: Pronome
    V: Verbo

    DetM: Determinante Masculino
    DetF: Determinante Feminino

    SM: Subtantivo Masculino
    SF: Subtantivo Feminino
'''

# Criação dos dicionarios

def CriarDicionarioBase(pGLC: classe_glc.GLC()):
    # S
    pGLC.AdicionarDicionario('S', 'NP VP')

    # NP
    pGLC.AdicionarDicionario('NP', 'DetM SM | DetF SF')
    pGLC.AdicionarDicionario('NP', 'DetF SF | DetM SM')

    #VP
    pGLC.AdicionarDicionario('VP', 'V NP')

def CriarDicionarioPadrao(pGLC: classe_glc.GLC()):
    CriarDicionarioBase(pGLC)
    
    pGLC.AdicionarDicionario('NP', 'ele | ela | você | Jose |' + 
        ' Maria | Hemerson | Cláudia | Marcos')

    #DetF e DetM
    pGLC.AdicionarDicionario('DetF', 'uma | a | minha')
    pGLC.AdicionarDicionario('DetM', 'um | o | meu')

    #SM e SF
    pGLC.AdicionarDicionario('SM', 'carro | rato | casaco | sofa')
    pGLC.AdicionarDicionario('SF', 'girafa | mesa | calça | carne')

    #V
    pGLC.AdicionarDicionario('V', 'pegou | jogou | pulou | comeu')

def CriarDicionarioPersonalizadoNP(pGLC: classe_glc.GLC(), pNP: str):
    pGLC.AdicionarDicionario('NP', pNP)
    
def CriarDicionarioPersonalizadoDetF(pGLC: classe_glc.GLC(), pDetF: str):
    pGLC.AdicionarDicionario('DetF', pDetF)
    
def CriarDicionarioPersonalizadoDetM(pGLC: classe_glc.GLC(), pDetM: str):
    pGLC.AdicionarDicionario('DetM', pDetM)
    
def CriarDicionarioPersonalizadoSM(pGLC: classe_glc.GLC(), pSM: str):
    pGLC.AdicionarDicionario('SM', pSM)    

def CriarDicionarioPersonalizadoSF(pGLC: classe_glc.GLC(), pSF: str):
    pGLC.AdicionarDicionario('SF', pSF)   

def CriarDicionarioPersonalizadoV(pGLC: classe_glc.GLC(), pV: str):
    pGLC.AdicionarDicionario('V', pV)   

def GerarUmaFrase(pGLC: classe_glc.GLC()):
    #simbolo de entrada S // nesse laço voce escolhe quantas frases quer
    pGLC.LimparCaminhoAnterior()
    vFrase = pGLC.GerarSequenciaAleatoria('S') 

    vResultado = DeixarLetraMaiusculaComecoFrase(vFrase)
    vResultado += '\n\n Caminho Feito:\n' + pGLC.FCaminhoSequencia  
    
    return vResultado
