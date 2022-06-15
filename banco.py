
from msilib.schema import Font
from tkinter import *


#front-end
root = Tk()

fr1 = Frame(root)
fr2 = Frame(root)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)


#criar os widgets frame1
lb0_fr1 = Label(fr1, text='ACESSE SUA CONTA', font= 'Arial 25', fg='black', bg='purple')
lb1_fr1 = Label (fr1, text='ADM', font= 'Arial 16', fg='black')
entr1_fr1 = Entry(fr1, font='Arial 16')
lb2_fr1 = Label(fr1, text='SENHA', font='Arial 16', fg='black')
entr2_fr1 = Entry(fr1, font='Arial 16')
lb3_fr1 = Label(fr1, text='FUNCIONÁRIOS', font='Arial 25', fg='black')
but1_fr1 = Button(fr1, text='ENTRAR', font='Arial 16', fg='black', bg='purple', command=lambda:[fr1.pack_forget(), fr2.pack()])

#criar os widgets frame 2
lb0_fr2 = Label(fr2, text='CADASTRO DE USUÁRIO', font='Arial 25', fg='black')
lb1_fr2 = Label(fr2, text='NOME', font='arial 16', fg='black' )
entr1_fr2 = Entry(fr2, font='arial 16')
lb2_fr2 = Label(fr2, text='CPF', font='arial 16', fg='black')
entr2_fr2 = Entry(fr2, font='arial 16')
lb3_fr2 = Label(fr2, text='N° DA CONTA', font='arial 16', fg='black')
entr3_fr2 = Entry(fr2, font='arial 16')
lb4_fr2 = Label(fr2, text='SENHA', font='arial 16', fg='black')
entr4_fr2 = Entry(fr2, font='arial 16')
bt1_fr2 = Button(fr2, text='VOLTAR', font='arial 16',bg='purple', fg='black', command= lambda: [fr2.pack_forget(), fr1.pack() ] )







fr1.pack()


#frame1
lb0_fr1.grid(row=2, column=1, sticky=NSEW)
lb1_fr1.grid(row=3, column=0, sticky=NSEW)
lb2_fr1.grid(row=4, column=0, sticky=NSEW)
but1_fr1.grid(row=5, column=1, sticky=NSEW)
entr1_fr1.grid(row=3, column=1, sticky=NSEW)
entr2_fr1.grid(row=4, column=1, sticky=NSEW)
lb3_fr1.grid(row=0, column=1, sticky=NSEW)

#frame2
lb0_fr2.grid(row=0, column=1, columnspan=4, sticky=NSEW)
bt1_fr2.grid(row=6, column=1, columnspan=4, sticky=NSEW)
lb1_fr2.grid(row=2, column=0, sticky=NSEW)
lb2_fr2.grid(row=3, column=0, sticky=NSEW)
lb3_fr2.grid(row=4, column=0, sticky=NSEW)
lb4_fr2.grid(row=5, column=0, sticky=NSEW)
entr1_fr2.grid(row=2, column=1, sticky=NSEW)
entr2_fr2.grid(row=3, column=1, sticky=NSEW)
entr3_fr2.grid(row=4, column=1, sticky=NSEW)
entr4_fr2.grid(row=5, column=1, sticky=NSEW)




root.mainloop()
