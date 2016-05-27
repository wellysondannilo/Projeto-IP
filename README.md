# Projeto-IP
Sistema De Controle Academico
import bib
def validar_login_e_senha(nome,senha,lista): ## função que recebe o login e senha
    validação = -1
    for i in range(len(lista)):              ## e retorna true se ouver os dois na lista
        if nome in lista[i][0] and senha in lista[i][1]: ## e false se não.
            validação = i
    return validação

def validar_login(nome,lista):  ## função que recebe o login e 
    indice = -1
    for i in range(len(lista)):   ## retorna o indice, se ouver o login na
        if nome in lista[i][0]:    ## lista e retorna -1 se não ouver.
            indice = i          
    return indice  


def receber_pergunta(lista):
    continua = True
    while continua == True:
        dic = {1: "Qual o nome do seu cachorro?",2: "Qual o seu apelido?", 3: "Qual o nome da sua avó?"}
        print("Selecione a sua pergunta secreta.")
        print("[1]", dic[1])
        print("[2]", dic[2])
        print("[3]", dic[3])
        mensagem = "> "
        opc = bib.correint(mensagem)
        if opc == 1 or opc == 2 or opc == 3:
            pergunta = dic[opc]
            continua = False
            return pergunta            
        else:
            print("""Pergunta invalida!
verifique a pergunta e tente novamente.""")
            mensagem = "Deseja continuar? "
            sair = bib.correstr(mensagem)
            if sair == "s":
                continua = False
            else:
                print("Opção invalida")

def validar_pergunta(pergunta,indice,lista):
    if pergunta in lista[indice]:
        return True
    else:
        return False
    
def validar_resposta(indice,lista):
    mensagem = "Digite a resposta: "
    resposta = bib.correstr(mensagem)
    if resposta in lista[indice]:
        return True
    else:
        return False

def validar_senha(senha,lista):  ## função que recebe o senha e 
    indice = -1
    for i in range(len(lista)):   ## retorna o indice se ouver a senha na
        if senha in lista[i][1]:    ## lista e retorna -1 se não ouver.
            indice = i          
    return indice  

def validar_codigo(codigo,lista):  ## função que recebe o codigo e 
    indice = -1
    for i in range(len(lista)):   ## retorna o indice, se ouver o codigo na
        if codigo in lista[i][2]:    ## lista e retorna -1 se não ouver.
            indice = i          
    return indice
