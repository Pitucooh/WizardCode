import sqlite3
from tkinter import *
import os

# variavéis globais
conn = None
janela = None

def fechar_janela_anterior():
    global janela
    if janela is not None:
        janela.destroy()

def criar_tabela():
    global conn
    conn = sqlite3.connect('cadastro.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS cadastro
                 (nome TEXT, email TEXT, senha TEXT)''')

    conn.commit()

def abrir_tela_cadastro():
    fechar_janela_anterior()

    global janela
    janela = Tk()
    janela.title("Cadastro")
    janela.geometry("490x560+610+153")

    janela.configure(bg="purple4")
    label_wizard_code = Label(janela, text="WIZARD CODE", font=("times", 24), fg="olivedrab1", bg="slateblue4")
    label_wizard_code.pack(pady=20)

    #campos de entrada da tela de cadastro
    label_nome = Label(janela, bd=2, text="Nome:", font=("times", "11"), bg="slateblue4", fg='peachpuff2').place(x=92.9, y=121.6)
    entry_nome = Entry(janela, bd=2, font=("Times", "24", "italic"))
    entry_nome.place(width=304.3, height=41, x=92.9, y=143.8)


    label_email = Label(janela, text="Email institucional:", font=("times", "11"), bg="slateblue4", fg='peachpuff2').place(x=92.9, y=228.6)
    entry_email = Entry(janela, bd=2, font=("Times", "24", "italic"))
    entry_email.place(width=304.3, height=41, x=92.9, y=251.8)

    label_senha = Label(janela, text="Senha mágica:", font=("times", "11"), bg="slateblue4", fg='peachpuff2').place(x=93, y=355)
    entry_senha = Entry(janela, bd=2, font=("Times", "24", "italic" ))
    entry_senha.place(width=304.3, height=41, x=92.9, y=375.7)

    def cadastrar():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()

        conn = sqlite3.connect('cadastro.db')
        c = conn.cursor()

        c.execute("SELECT * FROM cadastro WHERE email=?", (email,))
        if c.fetchone():
            label_status.configure(text="Usuário já existe!", fg="red")
        else:
            #insere dados na tabela
            c.execute("INSERT INTO cadastro VALUES (?, ?, ?)", (nome, email, senha))
            label_status.configure(text="Cadastro realizado com sucesso!", fg="green")
            fechar_janela_anterior()
            os.system('WizardCode\WizardCodeJogo.py')
            

        conn.commit()
        conn.close()

    botao_cadastrar = Button(janela, text="Cadastrar", font=("times", 16), width=20, command=cadastrar, bg='darkseagreen').place(width=202, height=47.3, x=150, y=470)

    #status do cadastro
    label_status = Label(janela, text="", font=("times", 12))
    label_status.pack(pady=10)

def abrir_tela_login():
    #funçaõ que fecha a janela anterior
    fechar_janela_anterior()

    #cria a janela de login
    global janela
    janela = Tk()
    janela.title("Login")
    janela.geometry("490x560+610+153")

    janela.configure(bg="steelblue3")
    label_wizard_code = Label(janela, text="WIZARD CODE", font=("times", 24), fg="medium purple", bg='light cyan')
    label_wizard_code.pack(pady=20)

    #campos de entrada padrão
    label_email = Label(janela, text="Email institucional:", font=("times", "11"), bg="light cyan").place(x=93, y=181.5)
    entry_email = Entry(janela, bd=2, font=("Times", "24", "italic"))
    entry_email.place(width=310, height=45, x=92.9, y=201.7)

    label_senha = Label(janela, text="Senha mágica:", font=("times", "11"), bg="light cyan").place(x=93, y=305)
    entry_senha = Entry(janela, bd=2, font=("Times", "24", "italic" ))
    entry_senha.place(width=310, height=45, x=92.9, y=324.7)

    def login():
        #verificação de dados digitados pelo usuário
        email = entry_email.get()
        senha = entry_senha.get()

        #conexão
        conn = sqlite3.connect('cadastro.db')
        c = conn.cursor()

        c.execute("SELECT * FROM cadastro WHERE email=? AND senha=?", (email, senha))
        if c.fetchone():
            label_status.configure(text="Login bem-sucedido!", fg="green")
            fechar_janela_anterior()
            os.system('WizardCode\WizardCodeJogo.py')
        else:
            label_status.configure(text="Email ou senha inválidos!", fg="red")

        conn.commit()
        conn.close()

    botao_login = Button(janela, text="Login", font=("times", 16), width=20, command=login, bg='mediumpurple').place(width=202, height=47.3, x=150, y=413.6)

    label_status = Label(janela, text="", font=("times", 12))
    label_status.pack(pady=10)

criar_tabela()

def como_jogar():
    janela = Tk()
    janela.title("COMO JOGAR?")
    janela.geometry("490x560+610+153")
    janela.configure(bg='darkslategray')
    label_como_jogar = Label(janela, text="TUTORIAL DE COMO JOGAR", font=("times", 24), fg="white", bg="darkslategray")
    label_como_jogar.pack(pady=20)
    label_texto = Label(janela, text=f"EVITE ERRAR PERGUNTAS,\n VOCÊ PERDE 1 VIDA POR PERGUNTA RESPONDIDA ERRADA", font=("times", 12), bg='antiquewhite')
    label_texto.place(x=20, y=140)
    label_texto2 =  Label(janela, text=f"SE FOR ATINGIDO POR UMA BIGORNA, PERDERÁ 1 VIDA", font=("times", 12), bg='antiquewhite')
    label_texto2.place(x=30, y=240)
    label_texto3 = Label(janela, text=f"A CADA PERGUNTA RESPONDIDA CERTA VOCÊ GANHA PONTOS \nE MUDA DE SKIN, \nATÉ RECEBER A SKIN DE MAGO", font=("times", 12), bg='antiquewhite')
    label_texto3.place(x=1.7, y=340)

#padrão da janela principal
janela = Tk()
janela.title("Menu")
janela.geometry("490x560+610+153")

janela.configure(bg="light green")
label_wizard_code = Label(janela, text="WIZARD CODE", bd=3, font=("TIMES", 30), fg="white", bg="lightslateblue")
label_wizard_code.pack(pady=20)

botao_cadastro = Button(janela, text="Cadastro", font=("TIMES", 16), width=20, command=abrir_tela_cadastro, bg='steelblue1').place(width=327.2, height=65.2, x=81.4, y=227.6)

botao_login = Button(janela, text="Login", font=("TIMES", 16), width=20, command=abrir_tela_login, bg='dodgerblue').place(width=327.2, height=65.2, x=81.4, y=342.7)

botao_comojogar = Button(janela, text="Como jogar", font=("TIMES", 16), width=20, bg='antiqueWhite1', command=como_jogar).place(width=327.2, height=65.2, x=81.4, y=120)


#incia a janela principal (janela)
janela.mainloop()
