from tkinter import messagebox
import database
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
        def trocasenha(ctt, teste):
            NovaTab = ctt.CTkTabview(teste.FrameDados, width=500, height=250)
            NovaTab.pack()

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
