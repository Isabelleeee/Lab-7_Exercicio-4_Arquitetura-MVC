# 📚 Livraria MVP - Clean Architecture & Persistência TXT

Esta é a versão definitiva do MVP da livraria, implementada seguindo os princípios da **Clean Architecture** e garantindo o **DIP (Dependency Inversion Principle)** do SOLID. O sistema agora utiliza arquivos de texto (.txt) para persistência de dados, mantendo o núcleo da aplicação totalmente independente da tecnologia de armazenamento.

---

## 🏗️ Arquitetura Clean

O projeto foi organizado para isolar a lógica de negócio de detalhes técnicos e ferramentas externas:

1. **Core (Enterprise & Application Rules):**
   - **Domain:** Contém as entidades de negócio (`Livro`).
   - **Interfaces:** Define os contratos (Interfaces Abstratas) que garantem que o sistema não dependa de implementações específicas.
   - **Use Cases:** Contém a lógica de aplicação (como a nova feature de busca).
2. **Adapters (Interface Adapters):**
   - **Repositories:** Implementa a persistência em arquivos TXT, traduzindo os dados brutos para objetos de domínio.
3. **Infrastructure / Frameworks:**
   - **Flask App:** Atua como o ponto de entrada e orquestrador (Main/Composition Root), injetando as dependências necessárias.



---

## 🛠️ Princípio de Inversão de Dependência (DIP)

A principal evolução técnica desta versão é a aplicação do **DIP**. 
- O `LivroUseCase` não depende de uma classe que lê arquivos TXT. 
- Ele depende de uma interface abstrata `ILivroRepository`.
- Isso permite que o banco de dados seja trocado por SQL, NoSQL ou uma API externa sem que a lógica de busca ou o modelo de dados precisem ser alterados.

---

## ✨ Nova Feature: Busca Dinâmica

Foi implementado um sistema de busca por título:
* O usuário pode filtrar o catálogo através de um campo de busca na interface.
* A lógica de filtragem reside exclusivamente no **Use Case**, mantendo a responsabilidade de negócio isolada da interface e do repositório.

---

## 💾 Persistência em TXT

Os dados são lidos e processados a partir do arquivo `db_livros.txt`. Cada linha do arquivo segue o formato:
`id;titulo;autor;preco`

Isso demonstra como a arquitetura permite criar sistemas funcionais com recursos mínimos de infraestrutura.

---

## 📂 Estrutura de Pastas

```text
├── app.py                   # Orquestrador (Framework)
├── core/
│   ├── domain.py            # Entidades
│   ├── use_cases.py         # Lógica de Aplicação
│   └── interfaces.py        # Abstrações (DIP)
├── adapters/
│   └── repositories.py      # Implementação da Persistência (TXT)
├── templates/               # View (HTML)
├── static/                  # CSS
└── db_livros.txt            # Arquivo de dados
