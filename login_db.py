import tkinter as tk
from tkinter import messagebox
import sqlite3

def realizar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Conectar ao banco
    con = sqlite3.connect('sistema_academico.db')
    cur = con.cursor()

    # Verificar se o usuário existe com a senha informada
    cur.execute("SELECT perfil FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
    resultado = cur.fetchone()

    con.close()

    if resultado:
        perfil = resultado[0]
        messagebox.showinfo("Login", f"Bem-vindo! Perfil: {perfil}")
        abrir_tela_perfil(perfil)
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

def abrir_tela_perfil(perfil):
    nova_janela = tk.Toplevel(root)
    nova_janela.title(f"Tela do {perfil}")
    nova_janela.geometry("300x200")
    label = tk.Label(nova_janela, text=f"Bem-vindo à área do {perfil}!", font=("Arial", 14))
    label.pack(pady=50)

# Janela principal
root = tk.Tk()
root.title("Sistema Acadêmico - Login")
root.geometry("300x200")

label_usuario = tk.Label(root, text="Usuário:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(root)
entry_usuario.pack(pady=5)

label_senha = tk.Label(root, text="Senha:")
label_senha.pack(pady=5)
entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=5)

botao_login = tk.Button(root, text="Login", command=realizar_login)
botao_login.pack(pady=10)

root.mainloop()
