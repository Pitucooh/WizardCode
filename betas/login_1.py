from tkinter import *
import time

master = Tk()
master.title("Menu de login do jogador")
master.geometry("490x560+610+153")
master.resizable(width=1, height=1)



def nova_janela():
    master.destroy()
    time.sleep(0.3)

    master1 = Tk()
    master1.title("WIZARD CODE")
    master1.geometry("490x560+400+153")



esconda_senha = StringVar()


img_fundo = PhotoImage(file="./imagens/fundo.png")
img_botao = PhotoImage(file="./imagens/PLAY.png")


lab_fundo = Label(master, image=img_fundo)
lab_fundo.pack()

en_user = Entry(master, bd=2, font=("Times", "24", "bold italic"), justify=CENTER)
en_user.place(width=304, height=41, x=92.9, y=197.6)

en_senha = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Times", "24", "bold italic"), justify=CENTER)
en_senha.place(width=304, height=41, x=92.9, y=324.7)


bt_entrar = Button(master, bd=0, image=img_botao, command=nova_janela)
bt_entrar.place(width=100, height=48, x=195.9, y=437.2)

master.mainloop()