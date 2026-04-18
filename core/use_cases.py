class LivroUseCase:
    def __init__(self, repository):
        self.repo = repository  # Ela recebe qualquer coisa que siga a ILivroRepository

    def listar_livros(self, filtro_titulo=None):
        livros = self.repo.buscar_todos()
        if filtro_titulo:
            # Lógica da nova feature de busca
            return [l for l in livros if filtro_titulo.lower() in l.titulo.lower()]
        return livros