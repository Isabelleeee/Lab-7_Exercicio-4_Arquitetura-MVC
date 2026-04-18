# 📚 Livraria MVP - Clean Architecture & Persistência TXT

Esta é a versão definitiva do MVP da livraria, implementada com foco em boas práticas de engenharia de software. O projeto segue os princípios da **Clean Architecture** e garante o **DIP (Dependency Inversion Principle)** do SOLID. O sistema agora utiliza arquivos de texto (`.txt`) para persistência de dados, mantendo o núcleo da aplicação totalmente independente de ferramentas externas.

---

## 🏗️ Arquitetura Clean

O projeto foi organizado para isolar a lógica de negócio de detalhes técnicos e de infraestrutura:

1. **Core (Enterprise & Application Rules):** A parte mais importante do sistema, que não conhece nada sobre Flask ou arquivos TXT.
   - **Domain:** Contém as entidades de negócio puras (ex: `Livro`).
   - **Interfaces:** Define os contratos (Interfaces Abstratas) que garantem a inversão de dependência.
   - **Use Cases:** Contém a lógica de aplicação (ex: feature de busca).
2. **Adapters (Interface Adapters):**
   - **Repositories:** Implementa a persistência lendo o arquivo TXT e traduzindo os dados para os objetos de domínio.
3. **Infrastructure / Frameworks:**
   - **Flask App:** Atua apenas como o orquestrador (Composition Root), recebendo requisições HTTP e injetando as dependências corretas.

---

## 🛠️ Princípio de Inversão de Dependência (DIP)

A principal evolução técnica desta versão é a aplicação do **DIP**. 
- O caso de uso (`LivroUseCase`) não importa a classe que lê o arquivo TXT. 
- Ele depende exclusivamente de uma interface abstrata (`ILivroRepository`).
- Isso permite que a persistência em TXT seja substituída no futuro por um banco SQL, NoSQL ou API externa sem alterar uma única linha de código da lógica de negócio.

---

## ✨ Nova Feature: Busca Dinâmica

Foi adicionado um sistema de busca por título:
* O usuário pode filtrar o catálogo por meio de um parâmetro na URL/interface.
* A lógica de filtragem reside exclusivamente no **Use Case**, mantendo a responsabilidade de negócio isolada da view e do repositório.

---

## 💾 Persistência em TXT

Os dados são lidos e processados a partir do arquivo `db_livros.txt`. Cada linha do arquivo segue rigorosamente o formato:
`id;titulo;autor;preco`

---

## 📂 Estrutura de Pastas

```text
├── app.py                   # Orquestrador (Framework / UI)
├── core/
│   ├── domain.py            # Entidades de Negócio
│   ├── use_cases.py         # Lógica de Aplicação
│   └── interfaces.py        # Abstrações (DIP)
├── adapters/
│   └── repositories.py      # Implementação da Persistência
├── templates/               # View (HTML)
├── static/                  # CSS
└── db_livros.txt            # Base de dados em texto
```

---

## 🚀 Como Executar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio-clean.git](https://github.com/seu-usuario/seu-repositorio-clean.git)
   ```

2. **Instale as dependências:**
   ```bash
   pip install flask
   ```

3. **Configure a Base de Dados:**
   Certifique-se de que o arquivo `db_livros.txt` existe na raiz do projeto com pelo menos um registro. Exemplo:
   ```text
   1;O Alquimista;Paulo Coelho;45.00
   2;1984;George Orwell;39.90
   ```

4. **Inicie o servidor:**
   ```bash
   python app.py
   ```

5. **Acesse no navegador:**
   Abra `http://127.0.0.1:5000` e teste a aplicação e a nova funcionalidade de busca.
