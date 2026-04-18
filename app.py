from flask import Flask, render_template, request
from adapters.repositories import TXTLivroRepository
from core.use_cases import LivroUseCase

app = Flask(__name__)

# Configuração (Injeção de Dependência)
repo = TXTLivroRepository("db_livros.txt")
use_case = LivroUseCase(repo)

@app.route('/')
def index():
    busca = request.args.get('busca')
    # A feature de busca sendo chamada no Use Case
    livros = use_case.listar_livros(filtro_titulo=busca)
    return render_template('index.html', livros=livros, busca=busca)

if __name__ == '__main__':
    app.run(debug=True)