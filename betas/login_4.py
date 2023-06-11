import tkinter as tk #tkinter: FERRAMENTA PARA INTERFACE GRÁFICA
import sqlite3

def criar_tabela():
        conn = sqlite3.connect('usuariosjogo.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS cadastro
                 (nome TEXT, email TEXT, telefone TEXT primary key)''')

        conn.commit()
        conn.close()

def cadastrar():
        #obter os dados digitados pelo usuário
        nome = tk.entry_nome.get()
        email = tk.entry_email.get()
        telefone = tk.entry_telefone.get()

        conn = sqlite3.connect('usuarios.db')
        c = conn.cursor()

        c.execute("INSERT INTO cadastro VALUES (?, ?, ?)", (nome, email, telefone))

        conn.commit()
        conn.close()


def abrir_janela(): #tudo que tem na tela de cadastro está aqui como uma função
        
    janela2 = tk.Toplevel()
    janela2.title('TELA DE CADASTRO')
    janela2.geometry("490x560+610+153")
    lab_fundo = tk.Label(janela2, image=img_telacadastro)
    lab_fundo.grid(row = 0, column = 0 )  
    entry_nome = tk.Entry(janela2, bd=2, font=("Times", "24", "bold italic"))
    entry_nome.place(width=310, height=45, x=49, y=146)
    entry_email = tk.Entry(janela2, bd=2, font=("Times", "24", "bold italic"))
    entry_email.place(width=310, height=45, x=49, y=251)
    entry_telefone = tk.Entry(janela2, bd=2, font=("Times", "24", "bold italic" ))
    entry_telefone.place(width=310, height=45, x=49, y=365)
    bt_cadastro = tk.Button(janela2, bd=3, text="PLAY", command=cadastrar, bg='CYAN').place(width= 290, height=43, x=100, y=460)

def historia_jogo1():
       
       janela3 = tk.Toplevel()
       janela3.title("HISTÓRIA DO MAGO MAIS SÁBIO DE TODOS")
       janela3.geometry("490x560+610+153")
       janela3.resizable(width=1, height=1)

       janela3 = tk.Label(janela3, image=img_pg1)
       janela3.grid(row = 0, column = 0)
       pg1 = tk.Button(janela3, text="PRÓXIMA PAGINA", bd=2, command=historia_jogo2, bg='indianred3').place(width=110, height=41, x=330, y=410)
       pg1_1 = tk.Button(janela3, text="PÁGINA ANTERIOR", bd=2, command=tela_login, bg='GREY').place(width=110, height=41, x=330, y=500)

def historia_jogo2():
       janela4 = tk.Toplevel()
       janela4.title("HISTÓRIA DO MAGO MAIS SÁBIO DE TODOS")
       janela4.geometry("490x560+610+153")
       janela4.resizable(width=1, height=1)

       janela4 = tk.Label(janela4, image=img_pg2 )
       janela4.grid(row = 0, column = 0)
       pg2 = tk.Button(janela4, text="PRÓXIMA PÁGINA", bd=2, command=historia_jogo3, bg='indianred3').place(width=110, height=41, x=330, y=410)
       pg2_1 = tk.Button(janela4, text="PÁGINA ANTERIOR", bd=2, command=historia_jogo1, bg='GREY').place(width=110, height=41, x=70, y=410)

def historia_jogo3():
       janela5 = tk.Toplevel()
       janela5.title("HISTÓRIA DO MAGO MAIS SÁBIO DE TODOS")
       janela5.geometry("490x560+610+153")
       janela5.resizable(width=1, height=1)

       janela5 = tk.Label(janela5, image=img_pg3)
       janela5.grid(row = 0, column = 0)
       pg3 = tk.Button(janela5, text="PÁGINA ANTERIOR", bd=2, command=fechar_e_redirecionar, bg='GREY').place(width=110, height=41, x=100, y=410)

def fechar_e_redirecionar():
    janela5 = tk.Tk()
    janela5.destroy()
    

def tela_login():
       janela6 = tk.Toplevel()
       janela6.title("LOGIN DO JOGADOR")
       janela6.geometry("490x560+610+153")
       janela6.resizable(width=1, height=1)
       janela6 = tk.Label(janela6, image=img_fundo)
       janela6.grid(row = 0, column = 0)

       en_user = tk.Entry(janela6, bd=2, font=("Times", "24", "bold italic"))
       en_user.place(width=304, height=41, x=33, y=197.6)
       label1 = tk.Label(janela6, text="TODOS OS CAMPOS SÃO OBRIGATÓRIOS", font=("Times", "8"))
       label1.place(x=33, y=240)
       en_senha = tk.Entry(janela6, show="*", bd=2, font=("Times", "24", "bold italic"))
       en_senha.place(width=304, height=41, x=33, y=325.499)
       botaojogar = tk.Button(janela6, text= "JOGAR", bg='darkolivegreen1')
       botaojogar.place(width=90, height=41, x=250, y=410)
       botaocadastrologin = tk.Button(janela6, text = "NÃO TEM CADASTRO?", command=abrir_janela, bg='CYAN').place(width=130, height=40, x=29, y=410)

def como_jogar():
       janela7 = tk.Toplevel()
       janela7.title("COMO JOGAR?")
       janela7.geometry("490x560+610+153")
       janela7.resizable(width=1, height=1)
       janela7 = tk.Label(janela7, image=img_comojogar)
       janela7.grid(row = 0, column = 0)
       bt_skins=tk.Button(janela7, text="ARQUIVO DE SKINS", command=(arquivo_skins), bg='antiqueWhite1').place(width=130, height=41, x=300, y=315)

def arquivo_skins():
       janela8 = tk.Toplevel()
       janela8.title("ARQUIVO DE SKINS")
       janela8.geometry("490x560+610+153")
       janela8 = tk.Label(janela8, image=img_skins)
       janela8.grid(row = 0, column = 0)

janela = tk.Tk() #principais caracteristicas da tela de login
janela.title("WIZARD CODE - TELA DE LOGIN")
janela.geometry("490x560+610+153")
janela.resizable(width=1, height=1)

#importei as imagens do meu pc
img_fundo = tk.PhotoImage(file="./imagens/fundo.png")
img_telacadastro = tk.PhotoImage(file="./imagens/telacadastro.png")
img_livro = tk.PhotoImage(file="./imagens/livro.png")
img_pg1 = tk.PhotoImage(file="./imagens/pag1.png")
img_pg2 = tk.PhotoImage(file="./imagens/pag2.png")
img_pg3 = tk.PhotoImage(file="./imagens/pag3.png")
img_hall = tk.PhotoImage(file="./imagens/hall.png")
img_comojogar = tk.PhotoImage(file="./imagens/comojogar.png")
img_skins = tk.PhotoImage(file="./imagens/skins.png")

#tudo oque há na tela de login, assim como os componentes na tela de cadastro que estão na função

lab_fundo = tk.Label(janela, image=img_hall)
lab_fundo.pack()

bt_historia = tk.Button(janela, bd=2, image=img_livro, command=historia_jogo1).place(width=100, height=41, x=200, y=250)

botaocadastro = tk.Button(janela, text="CADASTRAR", command= abrir_janela, bg='PINK')
botaocadastro.place(width=100, height=41, x=200, y=320)

botaojogar = tk.Button(janela, text= "REALIZAR LOGIN", command= tela_login, bg='PURPLE')
botaojogar.place(width=100, height=41, x=200, y=400)

botaocomojogar = tk.Button(janela, text="COMO JOGAR", bg='light green', command=como_jogar)
botaocomojogar.place(width=100, height=41, x=200, y=480)

janela.mainloop()