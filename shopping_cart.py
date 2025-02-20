import customtkinter as ctk 
from tkinter import messagebox 

# Configuração do tema
ctk.set_appearance_mode("Dark")  # Escolha entre "Light", "Dark" ou "System"
ctk.set_default_color_theme("dark-blue")  # Escolha entre "blue", "green", "dark-blue"

class CarrinhoCompras:
    def __init__(self, root):
        self.root = root
        self.root.title("Carrinho de Compras")
        self.root.geometry("600x600")  # Tamanho da janela
        self.produtos = []
        self.quantidades = []
        self.precos = []

        # Frame para adicionar produtos
        self.frame_produtos = ctk.CTkFrame(root)
        self.frame_produtos.pack(pady=10, padx=10, fill="x")

        self.label_nome = ctk.CTkLabel(self.frame_produtos, text="Nome do Produto:")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5)

        self.entry_nome = ctk.CTkEntry(self.frame_produtos)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_quantidade = ctk.CTkLabel(self.frame_produtos, text="Quantidade:")
        self.label_quantidade.grid(row=1, column=0, padx=5, pady=5)

        self.entry_quantidade = ctk.CTkEntry(self.frame_produtos)
        self.entry_quantidade.grid(row=1, column=1, padx=5, pady=5)

        self.label_preco = ctk.CTkLabel(self.frame_produtos, text="Preço Unitário:")
        self.label_preco.grid(row=2, column=0, padx=5, pady=5)

        self.entry_preco = ctk.CTkEntry(self.frame_produtos)
        self.entry_preco.grid(row=2, column=1, padx=5, pady=5)

        self.button_adicionar = ctk.CTkButton(self.frame_produtos, text="Adicionar", command=self.adicionar_produto)
        self.button_adicionar.grid(row=3, column=0, columnspan=2, pady=10)

        # Frame para listar produtos
        self.frame_lista = ctk.CTkFrame(root)
        self.frame_lista.pack(pady=10, padx=10, fill="both", expand=True)

        self.lista_produtos = ctk.CTkTextbox(self.frame_lista, width=400, height=150)
        self.lista_produtos.pack(pady=10, padx=10)

        # Frame para mostrar o total
        self.frame_total = ctk.CTkFrame(root)
        self.frame_total.pack(pady=10, padx=10, fill="x")

        self.label_total = ctk.CTkLabel(self.frame_total, text="Total: R$ 0.00", font=("Arial", 14, "bold"))
        self.label_total.pack(pady=10)

        self.button_calcular_total = ctk.CTkButton(root, text="Calcular Total", command=self.calcular_total)
        self.button_calcular_total.pack(pady=10)

    def adicionar_produto(self):
        nome = self.entry_nome.get()
        quantidade = self.entry_quantidade.get()
        preco = self.entry_preco.get()

        if nome and quantidade and preco:
            try:
                quantidade = int(quantidade)
                preco = float(preco)

                if quantidade <= 0 or preco <= 0:
                    messagebox.showerror("Erro", "Quantidade e Preço devem ser valores positivos.")
                    return

                self.produtos.append(nome)
                self.quantidades.append(quantidade)
                self.precos.append(preco)

                # Adiciona o produto à lista de exibição
                self.lista_produtos.insert("end", f"{nome} - {quantidade} x R$ {preco:.2f}\n")

                # Limpa os campos de entrada
                self.entry_nome.delete(0, "end")
                self.entry_quantidade.delete(0, "end")
                self.entry_preco.delete(0, "end")

            except ValueError:
                messagebox.showerror("Erro", "Quantidade deve ser um número inteiro e Preço deve ser um número válido.")
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    def calcular_total(self):
        total = sum(q * p for q, p in zip(self.quantidades, self.precos))
        self.label_total.configure(text=f"Total: R$ {total:.2f}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = CarrinhoCompras(root)
    root.mainloop()

