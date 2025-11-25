import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def abrir_tela_professor(nome_usuario):
    tela = tk.Tk()
    tela.title(f"Painel do Professor - {nome_usuario}")
    tela.geometry("500x450")

    # Função para registrar presença/falta
    def registrar_chamada():
        aluno = entry_aluno.get()
        status = combo_presenca.get()

        if aluno == "" or status == "":
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        conn = sqlite3.connect("sistema_academico.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS chamadas (aluno TEXT, status TEXT, professor TEXT)")
        cursor.execute("INSERT INTO chamadas (aluno, status, professor) VALUES (?, ?, ?)",
                       (aluno, status, nome_usuario))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Chamada registrada com sucesso!")
        entry_aluno.delete(0, tk.END)

    # Função para registrar atividade/nota
    def registrar_atividade():
        aluno = entry_aluno.get()
        atividade = entry_atividade.get()

        if aluno == "" or atividade == "":
            messagebox.showwarning("Aviso", "Digite o aluno e a descrição da atividade.")
            return

        conn = sqlite3.connect("sistema_academico.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS atividades (aluno TEXT, atividade TEXT, professor TEXT)")
        cursor.execute("INSERT INTO atividades (aluno, atividade, professor) VALUES (?, ?, ?)",
                       (aluno, atividade, nome_usuario))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Atividade registrada!")
        entry_atividade.delete(0, tk.END)

    # Interface
    tk.Label(tela, text=f"Painel do Professor", font=("Arial", 16, "bold")).pack(pady=10)

    # Campo aluno
    tk.Label(tela, text="Nome do Aluno:").pack()
    entry_aluno = tk.Entry(tela, width=40)
    entry_aluno.pack()

    # Registro de presença
    tk.Label(tela, text="Presença:").pack()
    combo_presenca = tk.StringVar()
    ttk.OptionMenu(tela, combo_presenca, "Presente", "Presente", "Falta").pack()

    tk.Button(tela, text="Registrar Chamada", command=registrar_chamada, width=25).pack(pady=10)
