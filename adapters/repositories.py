from core.domain import Livro
from core.interfaces import ILivroRepository

class TXTLivroRepository(ILivroRepository):
    def __init__(self, arquivo):
        self.arquivo = arquivo

    def buscar_todos(self):
        livros = []
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                for linha in f:
                    id, titulo, autor, preco = linha.strip().split(';')
                    livros.append(Livro(id, titulo, autor, float(preco)))
        except FileNotFoundError:
            pass # Retorna lista vazia se o arquivo não existir
        return livros