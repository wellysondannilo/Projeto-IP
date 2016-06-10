import bib
import pickle
import baidu
def validar_login_e_senha(nome,senha,lista): 
    validação = -1
    for i in range(len(lista)):              
        if nome in lista[i][0] and senha in lista[i][1]: 
            validação = i
    return validação

def validar_login(nome,lista):  
    indice = -1
    for i in range(len(lista)):   
        if nome in lista[i][0]: 
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

# Recebe o codigo de recuperação, verifica se ja existe um igual
# na lista e retorna -1 se não ouver e o indice se ouver.
def validar_codigo(codigo,lista):
    indice = -1
    for i in range(len(lista)):   
        if codigo in lista[i][2]:    
            indice = i          
    return indice

# Salva os dados da lista no arquivo.
def salvararquivo(lista):
    arquivo = open('banco.py','wb')
    pickle.dump(lista,arquivo)
    arquivo.close()
    
# Carrega os dados do arquivo e retorna uma lista com ele.
def carregararquivo():
    arquivo = open('banco.py', 'rb')
    lista = pickle.load(arquivo)
    arquivo.close()
    return lista

# Print com as opções de cadastro.
def opc_cadastro():
    opc = ''
    while opc != 1 and opc != 2:
        print('''
---------------------------
|[1] Cadastro de professor|
|[2] Cadastro de aluno    |
---------------------------''')
        mensagem = 'Digite a opção desajada: '
        opc = bib.correint(mensagem)
    return opc
# Recebe o valor da turma e não permite a entrada de outro valor
# até receber um valor valido.
def receber_turma():
    mensagem = 'Digite a turma: '
    turma = bib.correstr(mensagem)
    while turma != 'a' and turma != 'b' and turma != 'c':
        turma = bib.correstr(mensagem)
    return turma

# Recebe os dados do cadastro, verifica se já existe um login, e salva os
# dados no arquivo.
def receber_dados(lista):
    dic={1:"Introdução A Programação",2:"Matemática Elementar",3:"Introdução Ao Computador",4:"Administração",5:"Sociologia",6:"Metodologia Do Trabalho Cientifico"}
    confirma_login = False
    opc = opc_cadastro()
    while confirma_login == False:
        mensagem = 'Digite o login: '
        nome = bib.correstr(mensagem)
        confirma_login = baidu.validar_login(nome,lista)
        while confirma_login == False:
            print('Já existe alguem com este login')
            mensagem = 'Digite um login valido: '
            nome = bib.correstr(mensagem)
            confirma_login = baidu.validar_login(nome,lista)
    login = nome
    mensagem = 'Digite a senha: '
    senha = bib.correstr(mensagem)
    codigo = baidu.validacao_codigo_final(lista)
    mensagem = 'Digite o seu nome completo: '
    nomecomp = bib.correstr(mensagem)
    pergunta = baidu.cadastrar_pergunta()
    resposta = baidu.receber_resposta()
    if opc == 1:
        classe = 0
        lista.append([login,senha,nomecomp,codigo,pergunta,resposta,classe])
    elif opc == 2:
        turma = receber_turma()
        classe = 1
        lista.append([login,senha,nomecomp,codigo,pergunta,resposta,classe,[[dic[1]],[dic[2]],[dic[3]],[dic[4]],[dic[5]],[dic[6]]],turma])
    salvararquivo(lista)

# Print da tela inicial do programa  
def opc_inicial():
    print('''
--------------
|[1] Login    |
|[2] Cadastrar|
|[x] Sair     |
---------------''')

# Valida apenas o login e retorna o indice, e retorn -1 se não
# estiver na lista
def receber_e_validar_login(lista):
    indice = -1
    while indice == -1:
        mensagem = 'Digite o login: '
        login = bib.correstr(mensagem)
        mensagem = 'Digite a senha: '
        senha = bib.correstr(mensagem)
        indice = validar_login_e_senha(login,senha,lista)
        if indice == -1:
            print('Login ou senha invalida!')
        else:
            print('Login valido!')
    return indice

# Tela mostrada apos o login ser devidamente validado
# mostra as opções disponiveis, recebe a opção do usuario
# e retorna a opção selecionada.
def opc_pos_login():
    print('''
------------------------------------
|[1] Cadastrar notas                |
|[2] Vizualizar notas por cadeira   |
|[3] Buscar aluno                   |
|[4] Buscar por turma               |
||5] Editar notas                   |
|[6] Remover Aluno                  |
|[x] Sair                           |
------------------------------------''')
    mensagem = 'Digite a opção desejada: '
    opc = bib.correstr(mensagem)
    return opc

# verifica se existe um aluno com este nome e retorna o indice e o nome do aluno.
def validar_aluno(lista):
    alunos = []
    mensagem = 'Digite o nome do aluno: '
    aluno = bib.correstr(mensagem)
    verifica = -1
    for i in range(len(lista)):
        if aluno in lista[i][0]:
            verifica = i
    alunos.append([aluno,verifica])
    return alunos

# printa as materia, recebe a materia desejada e retorna o indice, nome do aluno
# e opção escolhida.
def print_receber_materias(lista,indice_do_usuario):
    opc = ''
    retorno = []
    dic={0:"Introdução A Programação",1:"Matemática Elementar",2:"Introdução Ao Computador",3:"Administração",4:"Sociologia",5:"Metodologia Do Trabalho Cientifico"}
    if lista[indice_do_usuario][6] == 0:
        indice = validar_aluno(lista)
        if indice[0][1] > -1:
            while opc != 0 and opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5:
                print('Escolha a cadeira que deseja por a nota: ')
                for i in range(0,6):
                    print('[',i,'] ',dic[i],': ')
                mensagem = 'Digite a materia desejada: '
                opc = bib.correint(mensagem)
        else:
            print('Não existe aluno cadastrado com este nome')
    retorno.append([opc,indice[0][0],indice[0][1]])
    return retorno

# Altera a mensagem dependendo do tamanho da sublista correspondente
# as notas da materia selecionada.
def mostra_n_nota(indice,materia,lista):
    if len(lista[indice][7][materia]) == 1:
        mensagem = 'Digite a primeira nota: '
    elif len(lista[indice][7][materia]) == 2:
        mensagem = 'Digte a segunda nota: '
    elif len(lista[indice][7][materia]) == 3:
        mensagem = 'Digite a terceira nota: '
    elif len(lista[indice][7][materia]) > 3:
        mensagem = '''Já foram cadastrados as 3 notas nesta materia, caso queira
alterar alguma selecione a opção "Editar notas".'''
    return mensagem

# pega o indice da materia, e do aluno, e da append na sublista
# correspondente a materia celecionada.
def receber_aluno_e_salvar(lista,indice_do_usuario):
    if lista[indice_do_usuario][6] == 0:
        protocolo = print_receber_materias(lista,indice_do_usuario)
        indice = protocolo[0][2]
        if indice > -1 and indice < 3:
            materia = protocolo[0][0]
            mensagem = mostra_n_nota(indice,materia,lista)
            nota = bib.correfloat10(mensagem)
            lista[indice][7][materia].append(nota)
        elif indice >= 3:
            mensagem = mostra_n_nota(indice,materia,lista)
            print(mensagem)
    else:
        print('''Somente professores podem editar a nota dos alunos.
Seu nivel de acesso não lhe permite efetuar esta operação.''')
    salvararquivo(lista)

# Recebe a cadeira que será posta a nota e retorna uma lista com a opção 
def receber_cadeira():
    dic = {0:"Introdução A Programação",1:"Matemática Elementar",2:"Introdução Ao Computador",3:"Administração",4:"Sociologia",5:"Metodologia Do Trabalho Cientifico"}
    opc = ''
    lista = []
    while opc != 0 and opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5:
        print('Escolha a cadeira que deseja por a nota: ')
        for i in range(0,6):
            print('[',i,'] ',dic[i],': ')
        mensagem = 'Digite a materia desejada: '
        opc = bib.correint(mensagem)
        if opc != 0 and opc != 1 and opc != 2 and opc != 3 and opc != 4 and opc != 5:
            print('''Opção invalida, digite um numero de 0 a 5 correspondente
a materia.''')
    lista.append([opc,dic[opc]])
    return lista

# Printa as três notas da materia selecionada aluno por aluno
def print_notas_por_materia(lista):
    cadeira = receber_cadeira()
    print('Cadeira: ', cadeira[0][1])
    for i in range(len(lista)):
        if lista[i][6] > 0:
            indice_da_cadeira = cadeira[0][0]
            nota1 = 'SN'
            nota2 = 'SN'
            nota3 = 'SN'
            if lista[i][6] > 0:
                for k in range(1,len(lista[i][7][indice_da_cadeira])):
                    nota = lista[i][7][indice_da_cadeira][k]
                    if k == 1:
                        nota1 = nota
                    elif k == 2:
                        nota2 = nota
                    elif k == 3:
                        nota3 = nota
            print('Nome: ', lista[i][0],'Nota1: ', nota1,'Nota2: ',nota2,'Nota3:',nota3)

# Printa as três notas materia por materia do aluno            
def print_nota_por_aluno(lista):
    indice = validar_aluno(lista)
    indice_do_aluno = indice[0][1]
    if indice[0][1] > -1:
        print('Aluno: ', indice[0][0])
        print('Turma: ', lista[indice_do_aluno][8])
        print('Nome completo: ', lista[indice_do_aluno][0])
        for i in range(len(lista[indice_do_aluno][7])):
            nota1 = 'SN'
            nota2 = 'SN'
            nota3 = 'SN'
            print('Materia: ', lista[indice_do_aluno][7][i][0])
            if len(lista[indice_do_aluno][7][i]) == 2:
                nota1 = lista[indice_do_aluno][7][i][1]
            elif len(lista[indice_do_aluno][7][i]) == 3:
                nota1 = lista[indice_do_aluno][7][i][1]
                nota2 = lista[indice_do_aluno][7][i][2]
            elif len(lista[indice_do_aluno][7][i]) == 4:
                nota1 = lista[indice_do_aluno][7][i][1]
                nota2 = lista[indice_do_aluno][7][i][2]
                nota3 = lista[indice_do_aluno][7][i][3]
            print('Primeira nota: ', nota1)
            print('Segunda nota: ', nota2)
            print('Terceira nota: ', nota3)

# Recebe a turma desejada e só permite continuar apos digitado uma opção valida.
def buscar_por_turma_receber():
    mensagem = 'Digite a turma; '
    opc = ''
    while opc != 'a' and opc != 'b' and opc != 'c':
        opc = bib.correstr(mensagem)
    return opc

# print os aluno da turma selecionada.
def buscar_por_turma(lista):
    turma = buscar_por_turma_receber()
    for i in range(len(lista)):
        if len(lista[i]) == 9:
            if turma in lista[i][8]:
                print(lista[i][2])
# Printa e recebe a materia selecionada pelo usuario, e retorna a opção escolhida.
def select_materia():
    dic = {0:"Introdução A Programação",1:"Matemática Elementar",2:"Introdução Ao Computador",3:"Administração",4:"Sociologia",5:"Metodologia Do Trabalho Cientifico"}
    mensagem = 'Digite o numero correspondente a materia que deseja selecionar: '
    opc = ''
    while opc!= 0 and opc!= 1 and opc!= 2 and opc!= 2 and opc!= 4 and opc!= 5:
        for i in range(len(dic)):
            print('[',i,'] ', dic[i])
        opc = bib.correint(mensagem)
    return opc
# Recebe qual a nota o usuario deseja alterar e caso ela ja exista na materia
# troca a nota antiga pela nova.
def escolher_nota(lista,indice_do_usuario):
    if lista[indice_do_usuario][6] == 0:
        materia = select_materia()
        indice = validar_aluno(lista)
        indice_do_aluno = indice[0][1]
        if indice_do_aluno > -1:
            quant_notas = len(lista[indice_do_aluno][7][materia])
            mensagem = 'Digite qual nota deseja alterar, exemplo(1): '
            qual_nota = bib.correint(mensagem)
            if qual_nota +1 <= quant_notas and qual_nota > 0:
                mensagem = 'Digite o valor da nova nota: '
                valor_nota = bib.correfloat10(mensagem)
                lista[indice_do_aluno][7][materia][qual_nota] = valor_nota
                salvararquivo(lista)
            else:
                print('A nota ainda não foi cadastrada.')
        else:
            print('Não existe aluno com este nome cadastrado.')
    else:
        print('''Somente professores podem editar a nota dos alunos.
Seu nivel de acesso não lhe permite efetuar esta operação.''')

# Recebe a lista e caso aja o aluno e o usuario confirme a operação
# remove o indice do aluno da lista.
def remover_aluno(lista,indice_do_usuario):
    if lista[indice_do_usuario][6] == 0:
        indice = validar_aluno(lista)
        indice_do_aluno = indice[0][1]
        if indice_do_aluno > -1:
            print('Deseja realmente excluir os dados deste aluno? [s/n] ')
            mensagem = '> '
            opc = bib.correstr(mensagem)
            if opc == 's':
                lista.pop(indice_do_aluno)
                salvararquivo(lista)
            elif opc == 'n':
                print('Processo de remoção cancelado.')
            else:
                print('Opção in valida.')
        else:
            print('Não existe aluno com este nome.')
    else:
        print('Alunos não podem fazer este tipo de procedimento.')

def gerar_media(lista):
    cont = 0
    media = [['sem aluno',0],['sem aluno',0],['sem aluno',0]]
    for i in range(len(lista)):
        if lista[i][6] == 1:
            nota = 0
            cont_aluno = 0
            nome = lista[i][0]
            for k in range(len(lista[i][7])):
                for j in range(1,len(lista[i][7][k])):
                    nota = nota + lista[i][7][k][j]
                    cont_aluno = cont_aluno + 1
            media_aluno = nota/cont_aluno
            print(media_aluno)
            if media[0][1] < media_aluno:
                media.insert(0,[nome,media_aluno])
    print(media[0][0],' ', media[0][1])
    print(media[1][0],' ', media[1][1])
    print(media[2][0],' ', media[2][1])

