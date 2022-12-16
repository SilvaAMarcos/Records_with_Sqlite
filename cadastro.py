import tkinter as tk
import sqlite3
#import pandas as pd
# criar o banco
# criar a tabela

connexao = sqlite3.connect('SisTicket.db')
c = connexao.cursor()


def create_table_usuario():
    c.execute( "CREATE TABLE  if not exists usuario (nome text, sobre_nome text,email text,telefone text)")


create_table_usuario()
connexao.commit()
connexao.close()


def cadastrar():
    conexao = sqlite3.connect('SisTicket.db')
    c = conexao.cursor()

    #Inserir dados na tabela:
    c.execute("INSERT INTO usuario VALUES (:nome,:sobrenome,:email,:telefone)",
              {
                  'nome': entry_nome.get(),
                  'sobrenome': entry_sobrenome.get(),
                  'email': entry_email.get(),
                  'telefone': entry_telefone.get()
              })


    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

def exporta():
    pass


janela_cadastro = tk.Tk()
janela_cadastro.title('Cadastro de Usuário')

# Labels:

label_nome = tk.Label(janela_cadastro, text='Nome')
label_nome.grid(row=0, column=0,padx=10,pady=10)

label_sobrenome = tk.Label(janela_cadastro, text='Sobrenome')
label_sobrenome.grid(row=1, column=0,padx=10,pady=10)

label_email = tk.Label(janela_cadastro, text='E-mail')
label_email.grid(row=2, column=0,padx=10,pady=10)

label_telefone = tk.Label(janela_cadastro, text='Telefone')
label_telefone.grid(row=3, column=0,padx=10,pady=10)

# Entrys:

entry_nome = tk.Entry(janela_cadastro, width=30)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela_cadastro, width=30)
entry_sobrenome.grid(row=1, column=1,padx=10,pady=10)

entry_email = tk.Entry(janela_cadastro, width=30)
entry_email.grid(row=2, column=1,padx=10,pady=10)

entry_telefone = tk.Entry(janela_cadastro, width=30)
entry_telefone.grid(row=3, column=1,padx=10,pady=10)

# Botões

botao_cadastrar = tk.Button(text='Cadastrar Cliente', command=cadastrar)
botao_cadastrar.grid(row=4, column=0,columnspan=2, padx=10, pady=10 , ipadx = 80)

botao_exportar = tk.Button(janela_cadastro, text='Exportar Base Usuario', command=exporta)
botao_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=69)
janela_cadastro.mainloop()