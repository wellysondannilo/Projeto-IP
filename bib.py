def correint(mensagem):
    resp = False
    while resp == False:
        try:
            variavel = int(input(mensagem))
            resp = True
        except:
            print("Entrada invalida.")
    return variavel

def correfloat(mensagem):
    resp = False
    while resp == False:
        try:
            variavel = float(input(mensagem))
            resp = True
        except:
            print("Entrada invalida.")
    return variavel

def correstr(mensagem):
    resp = False
    while resp == False:
        try:
            variavel = str.lower(input(mensagem))
            resp = True
        except:
            print("Entrada invalida.")
    return variavel

def correint10(mensagem):
    resp = False
    while resp == False:
        try:
            variavel = int(input(mensagem))
            resp = True
        except:
            print("Entrada invalida.")
    while variavel > 10 or variavel < 0:
        try:
            variavel = int(input(mensagem))
        except:
            print("Entrada invalida.")
    return variavel

def correfloat10(mensagem):
    resp = False
    while resp == False:
        try:
            variavel = float(input(mensagem))
            resp = True
        except:
            print("Entrada invalida.")
    while variavel > 10 or variavel < 0:
        try:
            variavel = float(input(mensagem))
        except:
            print("Entrada invalida.")
    return variavel
def correfloatmult(mensagem,intervalo1,intervalo2):
    resp = False
    while resp == False:
        try:
            variavel = float(input(mensagem))
            resp = True
        except:
            print("Entrada invalida.")
    while variavel >intervalo1  or variavel < intervalo2:
        try:
            variavel = float(input(mensagem))
        except:
            print("Entrada invalida.")
    return variavel

def correintmult(mensagem,intervalo1,intervalo2):
    resp = False
    while resp == False:
        try:
            variavel = int(input(mensagem))
            resp = True
        except:
            print("Entrada invalida.")
    while variavel >intervalo2  or variavel < intervalo1:
        try:
            variavel = float(input(mensagem))
        except:
            print("Entrada invalida.")
    return variavel
    
