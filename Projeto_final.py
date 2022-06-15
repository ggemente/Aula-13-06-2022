from classe_cliente import Cliente
from classe_conta import Conta

cliente1 = Cliente('Mateus Costa','12345678-0','14/07/1997')
print(cliente1)
cliente1.imprime_dados()
conta1 = Conta(cliente1, '123-4')
conta1.deposito(float(input('Digite um valor: ')))
conta1.extrato()
cliente2 = Cliente (input('Insira seu nome: '),input('Insira seu cpf: '),input('Insira sua data de nascimento:'))
print(cliente2)
conta2= Conta(cliente2, input('Insira o numero da sua conta: '))
conta2.deposito(float(input('Digite um valor:  ')))
conta2.extrato()



from tkinter import *
#from classe_cliente import *
#from classe_conta import *
#from projeto_final import *



root = Tk()

frame1= Frame(root)
frame2= Frame(root)
frame3= Frame(root)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


#frame1
lb1 = Label(frame1, text='Bem vindo ao Manus Bank', font='Arial 20')
bt1 = Button(frame1, text="cliente", font= 'arial 20', bg= '#0a0a0a', fg='#35a852', command=lambda: [frame1.pack_forget(), frame2.pack()])

#frame2
lb5 = Label(frame2, text='Cadastre sua conta', font= 'arial 25', bg= '#32a852', fg='#050505')
lb6 = Label(frame2, text='nome:', font='arial 25', bg= '#35a852', fg= '#050505')
en1 = Entry(frame2, font= 'arial 18',  bg = '#f7f7f7', fg = '#050505' )
lb7 = Label(frame2, text= 'cpf:', font='arial 25', bg='#35a852', fg='#050505', )
en2 = Entry(frame2,font= 'arial 25',  bg = '#f7f7f7', fg = '#050505' )
lb9 = Label(frame2, text= 'data nasc:', font='arial 25', bg='#35a852', fg='#050505')
en3 = Entry(frame2,font= 'arial 25',  bg = '#f7f7f7', fg = '#050505' )
bt2 = Button(frame2, text="Fazer Cadastro!", font= 'arial 20', bg= '#0a0a0a', fg='#35a852', command=lambda: [frame2.pack_forget(), frame3.pack()])
bt3= Button(frame2, text='Voltar', font= 'arial 20', bg= '#0a0a0a', fg='#35a852', command= lambda: [frame3.pack_forget(), frame2.pack()])

#frame3
bt8= Button(frame3, text= 'Voltar', font= 'arial 20', command= lambda: [frame3.pack_forget(), frame2.pack()])
lb8 = Label(frame3,text='Bem vindo, Mateus!', font='arial 20',bg='#35a852', fg='#050505')
frame1.pack()


#frame4
lb5 = Label(frame2, text='Cadastre sua conta', font= 'arial 25', bg= '#32a852', fg='#050505')
lb6 = Label(frame2, text='nome:', font='arial 25', bg= '#35a852', fg= '#050505')
en1 = Entry(frame2, font= 'arial 18',  bg = '#f7f7f7', fg = '#050505' )
lb7 = Label(frame2, text= 'cpf:', font='arial 25',  bg='#35a852', fg='#050505' )
en2 = Entry(frame2,font= 'arial 25',  bg = '#f7f7f7', fg = '#050505' )
lb9 = Label(frame2, text= 'data nasc:', font='arial 25', bg='#35a852', fg='#050505')
en3 = Entry(frame2,font= 'arial 25',  bg = '#f7f7f7', fg = '#050505' )
bt2 = Button(frame2, text="Fazer Cadastro!", font= 'arial 20', bg= '#0a0a0a', fg='#35a852', command=lambda: [frame2.pack_forget(), frame3.pack()])
bt3= Button(frame2, text='Voltar', font= 'arial 20', bg= '#0a0a0a', fg='#35a852', command= lambda: [frame3.pack_forget(), frame2.pack()])

#frame1
lb1.grid(row= 0, column=0, columnspan=4, sticky=NSEW)
bt1.grid(row=3, column= 1, sticky=NSEW)

#frame2
lb5.grid(row= 0, column=0, columnspan=4, sticky=NSEW)
lb6.grid(row=1, column=0,sticky=NSEW)
lb7.grid(row=2, column=0,sticky=NSEW)
en1.grid(row=1, column=1, sticky=NSEW)
en2.grid(row=2 ,column=1,sticky=NSEW)
lb9.grid(row=3, column=0,sticky=NSEW)
en3.grid(row=3, column=1, sticky=NSEW)
bt3.grid(row=4, column=0,sticky=NSEW)
bt2.grid(row=4, column= 1, sticky=NSEW)

#frame3
bt8.grid(row=1, column=0, sticky=NSEW)
lb8.grid(row= 0, column=0, columnspan=4, sticky=NSEW)


root.mainloop()
