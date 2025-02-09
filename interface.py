import tkinter as tk
from tkinter import filedialog, messagebox
from funcoes import organizar_arquivos

def selecionar_e_organizar():
    """ Abre a janela de seleção de pasta e executa a organização. """
    pasta_origem = filedialog.askdirectory(title="Selecione a Pasta de Origem")
    if not pasta_origem:
        return
    
    logs = organizar_arquivos(pasta_origem)
    messagebox.showinfo("Sucesso", "Arquivos organizados com sucesso!\n\n" + "\n".join(logs))

def criar_interface():
    """ Cria a interface gráfica. """
    root = tk.Tk()
    root.title("Organizador de Arquivos")
    root.geometry("350x200")

    btn_organizar = tk.Button(root, text="Selecionar Pasta e Organizar", command=selecionar_e_organizar)
    btn_organizar.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()
