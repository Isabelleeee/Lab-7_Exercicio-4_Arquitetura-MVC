class Livro:
    def __init__(self, id, titulo, autor, preco):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

# Simulação de um banco de dados (Lista na memória)
db_livros = [
    Livro(1, "O Alquimista", "Paulo Coelho", 45.00),
    Livro(2, "1984", "George Orwell", 39.90),
    Livro(3, "Dom Casmurro", "Machado de Assis", 25.00)
]