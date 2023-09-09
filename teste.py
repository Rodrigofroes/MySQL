import database
import customtkinter as ctt
from tkinter import * 
from tkinter import messagebox

app = ctt.CTk()

app.title("DR - System")
app.geometry("700x500")
app.resizable(width=False, height=False)
img = PhotoImage(file="img/icon-semfundo.png")

#  Variables ---------------------------------------------------------------------------------------------
font_label = ('arial', 20)
font_entry = ('arial', 15)

#  Functions ---------------------------------------------------------------------------------------------
def Register():
    email = EmailEntry.get()
    nome = UserCadEntry.get()
    senha = SenhaCadEntry.get()

    if(nome == '' or senha == '' or email == ''):
        messagebox.showerror(title='DR - System', message='Campos obrigatorios')
    else:
        database.mycursor.execute(
            """INSERT INTO usuario VALUES(DEFAULT, %s, %s, %s)""",(nome, senha, email)
        )
        messagebox.showinfo(title='DR - System', message='Cadastrado com sucesso')

#Label - Recuperar senha
def trocasenha():
    NovaTab = ctt.CTkTabview(FrameDados, width=500, height=250)
    NovaTab.pack()


def EntrarUser():
    nome = UserEntry.get()
    senha = SenhaEntry.get() 

    database.mycursor.execute(
        """SELECT nome, senha FROM usuario WHERE nome = %s AND senha = %s;""",(nome, senha)
    )
    vereficador = database.mycursor.fetchone()

    if vereficador:
        messagebox.showinfo(title='DR - system', message='BEM-VINDO')
        print('entrou')
        app.iconify()
    else:
        messagebox.showerror(title='DR - system', message='senha ou usuário incorreto')    


#  Page  ---------------------------------------------------------------------------------------------
#Posicionamento de frames
frameIcon = ctt.CTkFrame(
    app, width=300, 
    height=500, 
    fg_color='#252222'
)
frameIcon.place(x=0 , y=0)

FrameDados = ctt.CTkFrame(
    app, width=400, 
    height=500, 
    fg_color='#3A3939'
)
FrameDados.place(x=300, y=0)

#Posicionamento da img
ImgLabel = Label(frameIcon, image=img, bg='#252222')
ImgLabel.place(x=50, y=180)

#Tabs Login e cadastro
ButtonViews = ctt.CTkTabview(
    FrameDados,
    width=400,
    height=500,
    fg_color='#3A3939',
    text_color="black", 
    segmented_button_fg_color="white", 
    segmented_button_unselected_color="white"
)
ButtonViews.place(x=0, y=0)

ButtonViews.add('Login')
ButtonViews.add('Cadastra-se')

#Mensagem 'Bem-vindo'
BVLabel = ctt.CTkLabel(
    ButtonViews.tab('Login'),
    text='BEM-VINDO',
    text_color="white",
    font=ctt.CTkFont( family="UniSansHeavyItalicCAPS", size=35)
)
BVLabel.place(x=100, y=60)

#Label e Entry - Usuário e Senha
UserLabel = ctt.CTkLabel(
    ButtonViews.tab('Login'), 
    text='Usuário:', 
    text_color="white",
    font=ctt.CTkFont(family='Arial', size=20)
)
UserLabel.place(x=30, y=150)

UserEntry = ctt.CTkEntry(
    ButtonViews.tab('Login'), 
    width=200, 
    height=40, 
    fg_color='white', 
    text_color='black',
    font=ctt.CTkFont(family='arial', size=13)
)
UserEntry.place(x=110, y=150)

SenhaLabel = ctt.CTkLabel(
    ButtonViews.tab('Login'),
    text='Senha:', 
    text_color="white",
    font=ctt.CTkFont(family='Inter', size=20), 
)
SenhaLabel.place(x=30, y=230)

SenhaEntry = ctt.CTkEntry(
    ButtonViews.tab('Login'),
    width=200, 
    height=40, 
    fg_color='white', 
    text_color='black',
    show='*',
    font=ctt.CTkFont(family='arial', size=13)
)
SenhaEntry.place(x=110, y=230)

#cadastro
EmailLabel = ctt.CTkLabel(
    ButtonViews.tab('Cadastra-se'),
    text='Email:',
    text_color='White',
    font=ctt.CTkFont(family='Arial', size=20)
)
EmailLabel.place(x=30, y=90)

EmailEntry = ctt.CTkEntry(
    ButtonViews.tab('Cadastra-se'),
    width=200, 
    height=40, 
    fg_color='white', 
    text_color='black',
    font=ctt.CTkFont(family='arial', size=13)
)
EmailEntry.place(x=110, y=90)

UserCadLabel = ctt.CTkLabel(
    ButtonViews.tab('Cadastra-se'), 
    text='Usuário:', 
    text_color="white",
    font=ctt.CTkFont(font_label)
)
UserCadLabel.place(x=30, y=170)

UserCadEntry = ctt.CTkEntry(
    ButtonViews.tab('Cadastra-se'), 
    width=200, 
    height=40, 
    fg_color='white', 
    text_color='black',
    font=ctt.CTkFont(font_entry)
)
UserCadEntry.place(x=110, y=170)

SenhaCadLabel = ctt.CTkLabel(
    ButtonViews.tab('Cadastra-se'),
    text='Senha:', 
    text_color="white",
    font=ctt.CTkFont(font_label), 
)
SenhaCadLabel.place(x=30, y=250)

SenhaCadEntry = ctt.CTkEntry(
    ButtonViews.tab('Cadastra-se'),
    width=200, 
    height=40, 
    fg_color='white', 
    text_color='black',
    show='*',
    font=ctt.CTkFont(font_entry)
)
SenhaCadEntry.place(x=110, y=250)

BtnCad = ctt.CTkButton(
    ButtonViews.tab('Cadastra-se'),
    width=90, 
    height=35, 
    text='Cadastrar', 
    bg_color='#3A3939', 
    text_color='white', 
    fg_color='#2B92F0', command=Register
)
BtnCad.place(x=150, y=330)

#Button Entrar
BtnEntrar = ctt.CTkButton(
    ButtonViews.tab('Login'),
    width=90, 
    height=35, 
    text='Entrar', 
    bg_color='#3A3939', 
    text_color='white', 
    fg_color='#2B92F0', command=EntrarUser
)
BtnEntrar.place(x=150, y=330)

btnES = ctt.CTkButton(
    ButtonViews.tab('Login'),
    text='Esqueceu sua senha?', 
    text_color='#F8774E', 
    fg_color='#3A3939',
    hover_color='#3A3939', command=trocasenha
)
btnES.place(x=130, y=400)

app.mainloop()