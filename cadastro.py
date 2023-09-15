from tkinter import messagebox
import customtkinter as ctt
import database
import random

class CadastroBanco:
        #  Functions ---------------------------------------------------------------------------------------------
        def Register(email:str, nome:str, senha:str):

            if not nome or not senha or not email:
                messagebox.showerror(title='DR - System', message='Campos obrigatórios')
            else:
                # Verifica se o email já está registrado
                database.mycursor.execute("""SELECT email FROM usuario WHERE email = %s""", (email,))
                result = database.mycursor.fetchone()
                
                if not result:
                    # Email não está registrado, então podemos inserir o novo usuário
                    database.mycursor.execute(
                        """INSERT INTO usuario VALUES(DEFAULT, %s, %s, %s)""", (nome, senha, email)
                    )
                    messagebox.showinfo(title='DR - System', message='Cadastrado com sucesso')
                else:
                    # Email já está registrado
                    messagebox.showerror(title='DR - System', message='Email já registrado')

        #Label - Recuperar senha
        def trocasenha(self):

            NumCod = (random.getrandbits(20))

            nova_janela = ctt.CTkToplevel(self.FrameDados)
            
            nova_janela.title("DR - System")
            nova_janela.geometry("300x400")
            nova_janela.resizable(width=False, height=False)

            codigoLabel =  ctt.CTkLabel(
                nova_janela,
                text='Codigo:', 
                text_color="white",
                font=ctt.CTkFont(family='Arial', size=20)
            )
            codigoLabel.place(x=15, y=10)

            
            def Verificador():
                cod = codigoEntry.get()
                if( int(cod) == NumCod):
                    VerificadorLabel = ctt.CTkLabel(
                        nova_janela,
                        text='Verificação com sucesso',
                        text_color='green'
                    )
                    VerificadorLabel.place(x=75, y=80)
                    NVemailLabel =  ctt.CTkLabel(
                        nova_janela,
                        text='Email:', 
                        text_color="white",
                        font=ctt.CTkFont(family='Arial', size=20)
                    )
                    NVemailLabel.place(x=15, y=145)
                    NVemailEntry = ctt.CTkEntry(
                        nova_janela,
                        width=200, 
                        height=40, 
                        fg_color='white', 
                        text_color='black',
                        font=ctt.CTkFont(family='arial', size=13)
                    )
                    NVemailEntry.place(x=75, y=140)

                    NVsenhaLabel = ctt.CTkLabel(
                        nova_janela,
                        text='Nova Senha:', 
                        text_color="white",
                        font=ctt.CTkFont(family='Arial', size=20)
                    )
                    NVsenhaLabel.place(x=15, y=200)
                    NVsenhaEntry = ctt.CTkEntry(
                        nova_janela,
                        width=130, 
                        height=40, 
                        fg_color='white', 
                        text_color='black',
                        font=ctt.CTkFont(family='arial', size=13)
                    )
                    NVsenhaEntry.place(x=145, y=195)

                    def redsenha():
                            email = NVemailEntry.get()
                            senha = NVsenhaEntry.get()

                            database.mycursor.execute("SELECT * FROM usuario WHERE email = %s", (email,))
                            Verificador = database.mycursor.fetchone()

                            if Verificador:
                                database.mycursor.execute("UPDATE usuario SET senha = %s WHERE email = %s", (senha, email))
                                database.bdc.commit()  # Certifique-se de commitar a transação no banco de dados
                                messagebox.showinfo(title='DR - System', message='Senha trocada com sucesso')
                                nova_janela.iconify()
                            else:
                                messagebox.showerror(title='DR - System', message='Erro ao trocar a senha')

                    buttonVeri = ctt.CTkButton(
                        nova_janela,
                        width=60,
                        height=40,
                        text='Trocar',
                        bg_color= '#3A3939',
                        text_color='white',
                        command=redsenha        
                    )
                    buttonVeri.place(x= 120, y=300)

            codigoEntry = ctt.CTkEntry(
                    nova_janela,
                    width=100,
                    height=40,
                    fg_color='white',
                    text_color='black',
                )
            codigoEntry.place(x= 100, y=5)
            ButtonCod = ctt.CTkButton(
                nova_janela,
                width=60,
                height=30,
                text='Verificar',
                fg_color='green',
                text_color='white',
                command=Verificador
            )
            ButtonCod.place(x=220, y=10)
            print(NumCod)

        def EntrarUser(nome:str, senha:str):

            database.mycursor.execute(
                """SELECT nome, senha FROM usuario WHERE nome = %s AND senha = %s;""",(nome, senha)
            )
            vereficador = database.mycursor.fetchone()

            if vereficador:
                messagebox.showinfo(title='DR - system', message='BEM-VINDO')
                print('entrou')
            else:
                messagebox.showerror(title='DR - system', message='senha ou usuário incorreto')    
