import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


def abrir_tela_aluno(nome_usuario):
    tela = tk.Tk()
    tela.title(f"Área do Aluno - {nome_usuario}")
    tela.geometry("500x450")

    # Função para mostrar atividades do aluno
    def ver_atividades():
        conn = sqlite3.connect("sistema_academico.db")
        cursor = conn.cursor()
        cursor.execute("SELECT atividade FROM atividades WHERE aluno = ?", (nome_usuario,))
        registros = cursor.fetchall()
        conn.close()

        lista = "\n".join([f"- {r[0]}" for r in registros])
        messagebox.showinfo("Minhas Atividades", lista if lista else "Nenhuma atividade registrada.")

    # Função para mostrar presenças do aluno
    def ver_presenca():
        conn = sqlite3.connect("sistema_academico.db")
        cursor = conn.cursor()
        cursor.execute("SELECT status FROM chamadas WHERE aluno = ?", (nome_usuario,))
        registros = cursor.fetchall()
        conn.close()

        presencas = "\n".join([f"- {r[0]}" for r in registros])
        messagebox.showinfo("Minhas Presenças", presencas if presencas else "Nenhum registro de presença encontrado.")

    # Função para visualizar informações completas (atividades, presenças juntas)
    def ver_resumo():
        conn = sqlite3.connect("sistema_academico.db")
        cursor = conn.cursor()

        cursor.execute("SELECT atividade FROM atividades WHERE aluno = ?", (nome_usuario,))
        atividades = cursor.fetchall()

        cursor.execute("SELECT status FROM chamadas WHERE aluno = ?", (nome_usuario,))
        chamadas = cursor.fetchall()

        conn.close()

        resumo = "📘 ATIVIDADES:\n"
