import tkinter as tk
from tkinter import messagebox
import sqlite3


def abrir_tela_coordenador():
    tela = tk.Tk()
    tela.title("Painel do Coordenador")
    tela.geometry("400x400")

    # Função para cadastrar usuário (Aluno ou Professor)
    def cadastrar_usuario():
        nome = entry_nome.get()
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        perfil = combo_perfil.get()

        if nome == "" or usuario == "" or senha == "" or perfil == "":
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        # Salvar no banco
        conn = sqlite3.connect("sistema_academico.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, usuario, senha, perfil) VALUES (?, ?, ?, ?)",
                       (nome, usuario, senha, perfil))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", f"{perfil} cadastrado com sucesso!")
        entry_nome.delete(0, tk.END)
        entry_usuario.delete(0, tk.END)
        entry_senha.delete(0, tk.END)

    # Função para listar usuários
    def listar_usuarios():
        conn = sqlite3.connect("sistema_academico.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nome, usuario, perfil FROM usuarios")
        registros = cursor.fetchall()
        conn.close()

        lista = "\n".join([f"{r[0]} - ({r[2]})" for r in registros])
        messagebox.showinfo("Usuários Cadastrados", lista if lista else "Nenhum usuário cadastrado.")

    # Interface
    tk.Label(tela, text="Cadastro de Usuários", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(tela, text="Nome completo:").pack()
    entry_nome = tk.Entry(tela, width=30)
    entry_nome.pack()

    tk.Label(tela, text="Usuário (login):").pack()
    entry_usuario = tk.Entry(tela, width=30)
    entry_usuario.pack()

    tk.Label(tela, text="Senha:").pack()
    entry_senha = tk.Entry(tela, show="*", width=30)
    entry_senha.pack()

    tk.Label(tela, text="Perfil:").pack()
    combo_perfil = tk.StringVar()
    tk.OptionMenu(tela, combo_perfil, "Aluno", "Professor").pack()

    tk.Button(tela, text="Cadastrar", command=cadastrar_usuario, width=20).pack(pady=10)
    tk.Button(tela, text="Ver Usuários", command=listar_usuarios, width=20).pack(pady=5)
    tk.Button(tela, text="Sair", command=tela.destroy, width=20, bg="red", fg="white").pack(pady=20)

    tela.mainloop()


if __name__ == "__main__":
    abrir_tela_coordenador()
