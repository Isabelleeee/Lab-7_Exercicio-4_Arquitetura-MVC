# core/domain.py
class Livro:
    def __init__(self, id, titulo, autor, preco):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

# core/interfaces.py (A Interface que garante o DIP)
from abc import ABC, abstractmethod

class ILivroRepository(ABC):
    @abstractmethod
    def buscar_todos(self):
        pass