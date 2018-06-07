# encoding=utf8
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import xlrd
import os
from datetime import datetime

data_e_hora_atuais = datetime.now()
data_em_texto = data_e_hora_atuais.strftime('%d%m%Y_%H%M%S')

root = Tk()
root.geometry("680x480")
root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("excel files", "*.xlsx"), ("all files", "*.*")))


try:
    book = xlrd.open_workbook(root.filename)
    Arq = 0
    sh = book.sheet_by_index(0)

    dir = os.path.dirname(os.path.realpath(root.filename))

    #print (os.path.dirname(os.path.realpath(root.filename)))

    try:
        otimo = open(dir+'\\OTIMO_'+data_em_texto+'.txt', 'r')
        conteudo1 = otimo.readlines()

        transf = open(dir+'\\TRANSFACIL_'+data_em_texto+'.txt', 'r')
        conteudo2 = transf.readlines()
    except Exception:
        otimo = open(dir+'\\OTIMO_'+data_em_texto+'.txt', 'w')
        otimo.close()
        otimo = open(dir+'\\OTIMO_'+data_em_texto+'.txt', 'r')
        conteudo1 = otimo.readlines()

        transf = open(dir+'\\TRANSFACIL_'+data_em_texto+'.txt', 'w')
        transf.close()
        transf = open(dir+'\\TRANSFACIL_'+data_em_texto+'.txt', 'r')
        conteudo2 = transf.readlines()

    for rx in range(sh.nrows):
        if rx ==0:
            pass
        else:
            try:
                if str(sh.row(rx)[17].value).strip() == 'OTIMO':
                    #OTIMO
                    MATRÍCULA = str(sh.row(rx)[0].value)
                    NOME = str(sh.row(rx)[2].value)
                    CARGA = str("%.2f" %sh.row(rx)[25].value).replace(".", ",")

                    conteudo = MATRÍCULA.strip()+";"+NOME.strip()+";"+CARGA.strip()+";"
                    texto = str(conteudo)
                    #print(texto)
                    conteudo1.append(texto)
                    otimo = open(dir+'\\OTIMO_'+data_em_texto+'.txt', 'w')
                    otimo.writelines(conteudo1)
                    conteudo1.append("\n")
                    otimo.close()
                else:
                    #TRANSFÁCIL
                    MATRÍCULA = str(sh.row(rx)[0].value)
                    CARGA = str("%.2f" %sh.row(rx)[25].value).replace(".", "")

                    conteudo = MATRÍCULA.zfill(15).strip()+CARGA.zfill(5).strip()
                    texto = str(conteudo)
                    #print(texto)
                    conteudo2.append(texto)
                    transf = open(dir+'\\TRANSFACIL_'+data_em_texto+'.txt', 'w')
                    transf.writelines(conteudo2)
                    conteudo2.append("\n")
                    transf.close()
            except Exception:
                messagebox.showinfo("Erro", "Erro ao gravar arquivo, tente novamente!")
    messagebox.showinfo("Arquivo Salvo", "Arquivo salvo em" + dir)

except Exception:
    messagebox.showinfo("Abortado", "Abortado pelo usuário!")





