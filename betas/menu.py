from tkinter import *
import time

class Jogo:
    def telamaster():
        master = Tk()
        master.title("WIZARD CODE - MENU DE LOGIN")
        master.geometry("490x560+610+153")
        master.resizable(width=1, height=1)

        def telalogin():

            esconda_senha = StringVar()

            img_fundo = PhotoImage(file="./imagens/fundo.png")
            img_botao = PhotoImage(file="./imagens/PLAY.png")
            img_cadastro = PhotoImage(file="./imagens/cadastro.png")
            img_telacadastro = PhotoImage(file="./imagens/telacadastro.png")


            lab_fundo = Label(master, image=img_fundo)
            lab_fundo.pack()

            en_user = Entry(master, bd=2, font=("Times", "24", "bold italic"), justify=CENTER)
            en_user.place(width=304, height=41, x=92.9, y=197.6)

            label1 = Label(master, text="TODOS OS CAMPOS SÃO OBRIGATÓRIOS", font=("Times", "8"))
            label1.place(x=94, y=240)

            en_senha = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Times", "24", "bold italic"), justify=CENTER)
            en_senha.place(width=304, height=41, x=92.9, y=324.7)

            def cadastro ():
                bt_cadastro = Button(master, bd=0, image=img_cadastro, command=tela_cadastro)
                bt_cadastro.place(width=90, height=41, x=330, y=410)
                def tela_cadastro():
                    master.destroy()
                    time.sleep(0.3)
                    tela_cadastro = Label(master, image=img_telacadastro)
                    tela_cadastro.pack()
                    


            bt_entrar = Button(master, bd=0, image=img_botao)
            bt_entrar.place(width=90, height=41, x=60, y=410)

            check = Checkbutton(master, text="Pronto para se tornar o mago mais sábio de todos?").place(x=100, y=460)

             
             
        master.mainloop()

