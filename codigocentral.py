opc = "3"
import bib
import bib3
import baidu
import pickle
import random
while opc != "x":
    data = bib3.carregararquivo()
    bib3.opc_inicial()
    mensagem = 'Digite a opção desejada: '
    opc = bib.correstr(mensagem)
    if opc == '1':
        indice = bib3.receber_e_validar_login(data)
        if indice > -1:
            opc2 = ''
            while opc2 != 'x':
                opc2 = bib3.opc_pos_login()
                if opc2 == '1':
                    bib3.receber_aluno_e_salvar(data,indice)
                elif opc2 == '2':
                    bib3.print_notas_por_materia(data)
                elif opc2 == '3':
                    bib3.print_nota_por_aluno(data)
                elif opc2 == '4':
                    bib3.buscar_por_turma(data)
                elif opc2 == '5':
                    bib3.escolher_nota(data,indice)
                elif opc2 == '6':
                    bib3.remover_aluno(data,indice)
    elif opc == '2':
        bib3.receber_dados(data)
    else:
        print('Opção invalida.')


