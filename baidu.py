import bib

##
##nome
##senha
##codigo
##pergunta
##resposta
##

import random


def validar_login(login,lista):

    variavel=1
    for i in range(len(lista)):
        if(login in lista[i][0]):
            variavel=-1
    if variavel == 1:
        return True
    else:
        return False 
            





def validar_nome (nome,lista):    

    variavel=1
    for i in range(len(lista)):
        if(nome in lista[i]):
            variavel=-1
    if variavel == 1:
        return True
    else:
        return False
                  

                  


def validacao_codigo(codigo,lista):
    resposta=0
    for i in range(len(lista)):
        if(codigo in lista[i]):
            resposta = 1
    return resposta

def validacao_codigo_final(lista):
    codigo=random.randint(1000,9999)
    validacao=validacao_codigo(codigo,lista)
    while(validacao == 1):
        codigo=random.randint(1000,9999)
        validacao=validacao_codigo(codigo,lista)

    return codigo


def cadastrar_pergunta():
    opcao=""
    while opcao != 1 and opcao != 2 and opcao != 3:
        dic={1:"Qual o nome do seu cachorro?",2:"Qual o seu apelido?",3:"Qual o nome da sua avó?"}
        print("[1]",dic [1])
        print("[2]",dic [2])
        print("[3]",dic [3])
        mensagem=("Escolha a Opção Correspondende a Pergunta: ")
        opcao = bib.correint(mensagem)
    pergunta = dic[opcao]

    return pergunta
            

def receber_resposta():
    mensagem=("Digite Sua Resposta: ")
    resposta=bib.correstr(mensagem)
    
    
    return resposta

