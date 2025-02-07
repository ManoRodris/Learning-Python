import tkinter as tk

root = tk.Tk()

# Configurar as colunas e linhas para expandirem corretamente
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Criar um widget no centro
btn = tk.Button(root, text="Clique Aqui")
btn.grid(row=0, column=0, padx=20, pady=20)

root.mainloop()
