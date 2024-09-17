import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from plyer import notification

class ListaAfazeres:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Afazeres")
        self.root.geometry("500x450")
        self.root.config(bg='#f0f0f0')  # Cor de fundo da janela
        
        self.tarefas = []

        # Frame para o título
        self.title_frame = tk.Frame(root, bg='gray', bd=5, relief=tk.RIDGE)
        self.title_frame.pack(pady=10, fill=tk.X)

        self.title_label = tk.Label(self.title_frame, text="Lista de Afazeres", font=("Arial", 20, "bold"),bg= "gray", fg='#ffffff')
        self.title_label.pack()

        # Frame principal
        self.frame = tk.Frame(root, bg='#f0f0f0')
        self.frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Entrada de nova tarefa
        self.entry_frame = tk.Frame(self.frame,bg='#f0f0f0')
        self.entry_frame.pack(pady=10)

        self.entrada_label = tk.Label(self.entry_frame, text="Nova Tarefa:", font=("Arial", 12))
        self.entrada_label.pack(side=tk.LEFT, padx=5)

        self.entrada = tk.Entry(self.entry_frame, width=30, font=("Arial", 12), bd=2, relief=tk.SUNKEN)
        self.entrada.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.entry_frame, text="Adicionar", command=self.add_tarefa, bg='#32CD32', font=("Arial", 12), bd=2, relief=tk.RAISED)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Lista de tarefas
        self.list_frame = tk.Frame(self.frame, bg='#f0f0f0')
        self.list_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.list_label = tk.Label(self.list_frame, text="Tarefas:", font=("Arial", 12), bg='#f0f0f0')
        self.list_label.pack(anchor=tk.W, padx=5)

        self.list = tk.Listbox(self.list_frame, width=50, font=("Arial", 12), bd=2, relief=tk.SUNKEN, bg='#ffffff', fg='#000000', selectbackground='#ADD8E6')
        self.list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

        self.scrollbar = tk.Scrollbar(self.list_frame, orient=tk.VERTICAL, command=self.list.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.list.config(yscrollcommand=self.scrollbar.set)

        # Botão de deletar tarefa
        self.delete_button = tk.Button(self.frame, text="Deletar Tarefa", command=self.delete_tarefa, font=("Arial", 12), relief=tk.RAISED)
        self.delete_button.pack(pady=5)

    def add_tarefa(self):
        task = self.entrada.get().strip()
        if task:
            self.tarefas.append(task)
            self.list.insert(tk.END, task)
            self.entrada.delete(0, tk.END)
            notification.notify(
                title="Tarefa adicionada",
                message=f"Tarefa '{task}' listada",
                timeout=5
            )
        else:
            messagebox.showwarning("Aviso", "Digite uma tarefa antes de adicionar")

    def delete_tarefa(self):
        try:
            index = self.list.curselection()[0]
            task = self.tarefas[index]
            self.list.delete(index)
            self.tarefas.remove(task)
            notification.notify(
                title="Tarefa Excluída",
                message=f"Tarefa '{task}' excluída",
                timeout=5
            )
        except IndexError:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para excluir")

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use('clam')
    app = ListaAfazeres(root)
    root.mainloop()
