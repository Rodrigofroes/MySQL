import customtkinter as ctt
from tkinter import *
from cadastro import CadastroBanco

class Application:
    def __init__(self, master):
        self.master = master
        self.setup_app()

    def setup_app(self):
        self.master.title("DR - System")
        self.master.resizable(width=False, height=False)
        self.img = PhotoImage(file="img/icon-semfundo.png")
        
        # Variables
        self.largura = 700
        self.altura = 500
        self.font_label = ('arial', 20)
        self.font_entry = ('arial', 15)

        self.screen_height = self.master.winfo_screenheight()
        self.screen_width = self.master.winfo_screenwidth()

        self.pos_x = self.screen_width / 2 - self.largura / 2 
        self.pos_y = self.screen_height / 2 - self.altura / 2 

        self.master.geometry("%dx%d+%d+%d" %(self.largura, self.altura, self.pos_x, self.pos_y))

        self.setup_frames()
        self.setup_login_tab()
        self.setup_register_tab()

    def setup_frames(self):
        self.frameIcon = ctt.CTkFrame(
            self.master, width=300, 
            height=500, 
            fg_color='#252222'
        )
        self.frameIcon.place(x=0 , y=0)

        self.FrameDados = ctt.CTkFrame(
            self.master, width=400, 
            height=500, 
            fg_color='#3A3939'
        )
        self.FrameDados.place(x=300, y=0)

        frame_width = 300
        frame_height = 500

        img_width = 250
        img_height = 250

        x = (frame_width - img_width) / 2
        y = (frame_height - img_height) / 2

        self.ImgLabel = Label(self.frameIcon, image=self.img, bg='#252222')
        self.ImgLabel.place(x=x, y=y)

        self.ButtonViews = ctt.CTkTabview(
            self.FrameDados,
            width=400,
            height=500,
            fg_color='#3A3939',
            text_color="black",
            segmented_button_fg_color="white", 
            segmented_button_unselected_color="white",
            segmented_button_unselected_hover_color="#2B92F0",
            segmented_button_selected_color="#2B92F0"
        )
        self.ButtonViews.place(x=0, y=0)

        self.ButtonViews.add('Login')
        self.ButtonViews.add('Cadastra-se')

    def setup_login_tab(self):
        self.BVLabel = ctt.CTkLabel(
            self.ButtonViews.tab('Login'),
            text='BEM-VINDO',
            text_color="white",
            font=ctt.CTkFont(family="UniSansHeavyItalicCAPS", size=35)
        )
        self.BVLabel.place(x=100, y=60)

        self.UserLabel = ctt.CTkLabel(
            self.ButtonViews.tab('Login'), 
            text='Usuário:', 
            text_color="white",
            font=ctt.CTkFont(family='Arial', size=20)
        )
        self.UserLabel.place(x=30, y=150)

        self.UserEntry = ctt.CTkEntry(
            self.ButtonViews.tab('Login'), 
            width=200, 
            height=40, 
            fg_color='white', 
            text_color='black',
            font=ctt.CTkFont(family='arial', size=13)
        )
        self.UserEntry.place(x=110, y=150)

        self.SenhaLabel = ctt.CTkLabel(
            self.ButtonViews.tab('Login'),
            text='Senha:', 
            text_color="white",
            font=ctt.CTkFont(family='Inter', size=20), 
        )
        self.SenhaLabel.place(x=30, y=230)

        self.SenhaEntry = ctt.CTkEntry(
            self.ButtonViews.tab('Login'),
            width=200, 
            height=40, 
            fg_color='white', 
            text_color='black',
            show='*',
            font=ctt.CTkFont(family='arial', size=13)
        )
        self.SenhaEntry.place(x=110, y=230)
        
        self.BtnEntrar = ctt.CTkButton(
            self.ButtonViews.tab('Login'),
            width=90, 
            height=35, 
            text='Entrar', 
            bg_color='#3A3939', 
            text_color='white',
            command=lambda: CadastroBanco.EntrarUser(self.UserEntry.get(), self.SenhaEntry.get())  # Corrección aquí
        )
        self.BtnEntrar.place(x=150, y=330)

        self.btnES = ctt.CTkButton(
            self.ButtonViews.tab('Login'),
            text='Esqueceu sua senha?', 
            text_color='#F8774E', 
            fg_color='#3A3939',
            hover_color='#3A3939'
        )
        self.btnES.place(x=130, y=400)

    def setup_register_tab(self):
        self.EmailLabel = ctt.CTkLabel(
            self.ButtonViews.tab('Cadastra-se'),
            text='Email:',
            text_color='White',
            font=ctt.CTkFont(family='Arial', size=20)
        )
        self.EmailLabel.place(x=30, y=90)

        self.EmailEntry = ctt.CTkEntry(
            self.ButtonViews.tab('Cadastra-se'),
            width=200, 
            height=40, 
            fg_color='white', 
            text_color='black',
            font=ctt.CTkFont(family='arial', size=13)
        )
        self.EmailEntry.place(x=110, y=90)

        self.UserCadLabel = ctt.CTkLabel(
            self.ButtonViews.tab('Cadastra-se'), 
            text='Usuário:', 
            text_color="white",
            font=ctt.CTkFont(self.font_label)
        )
        self.UserCadLabel.place(x=30, y=170)

        self.UserCadEntry = ctt.CTkEntry(
            self.ButtonViews.tab('Cadastra-se'), 
            width=200, 
            height=40, 
            fg_color='white', 
            text_color='black',
            font=ctt.CTkFont(self.font_entry)
        )
        self.UserCadEntry.place(x=110, y=170)

        self.SenhaCadLabel = ctt.CTkLabel(
            self.ButtonViews.tab('Cadastra-se'),
            text='Senha:', 
            text_color="white",
            font=ctt.CTkFont(self.font_label), 
        )
        self.SenhaCadLabel.place(x=30, y=250)

        self.SenhaCadEntry = ctt.CTkEntry(
            self.ButtonViews.tab('Cadastra-se'),
            width=200, 
            height=40, 
            fg_color='white', 
            text_color='black',
            show='*',
            font=ctt.CTkFont(self.font_entry)
        )
        self.SenhaCadEntry.place(x=110, y=250)
        
        self.BtnCad = ctt.CTkButton(
            self.ButtonViews.tab('Cadastra-se'),
            width=90, 
            height=35, 
            text='Cadastrar', 
            bg_color='#3A3939', 
            text_color='white', 
            fg_color='#2B92F0',
            command=lambda: CadastroBanco.Register(self.EmailEntry.get(), self.UserCadEntry.get(), self.SenhaCadEntry.get())
        )
        self.BtnCad.place(x=150, y=330)

if __name__ == "__main__":
    app = ctt.CTk()
    Application(app)
    app.mainloop()
