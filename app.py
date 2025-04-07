# sistema_estoque.py

from typing import List

class Produto:
    def __init__(self, nome: str, categoria: str, quantidade: int, preco: float, localizacao: str):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

    def __repr__(self):
        return f"{self.nome} | {self.categoria} | Qtd: {self.quantidade} | Preco: {self.preco} | Local: {self.localizacao}"

class SistemaEstoque:
    def __init__(self):
        self.produtos: List[Produto] = []

    def cadastrar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def atualizar_estoque(self, nome: str, quantidade: int):
        for produto in self.produtos:
            if produto.nome == nome:
                produto.quantidade += quantidade
                return f"Estoque atualizado: {produto.nome} agora tem {produto.quantidade} unidades."
        return "Produto não encontrado."

    def rastrear_localizacao(self, nome: str):
        for produto in self.produtos:
            if produto.nome == nome:
                return f"Produto '{nome}' está localizado em: {produto.localizacao}"
        return "Produto não encontrado."

    def gerar_relatorio(self):
        relatorio = {
            'estoque_baixo': [],
            'estoque_excesso': [],
            'todos_produtos': []
        }
        for produto in self.produtos:
            relatorio['todos_produtos'].append(produto)
            if produto.quantidade < 5:
                relatorio['estoque_baixo'].append(produto)
            if produto.quantidade > 100:
                relatorio['estoque_excesso'].append(produto)
        return relatorio

######################### Aqui eu Deixei um Exemplo de uso ################################
if __name__ == "__main__":
    sistema = SistemaEstoque()
    sistema.cadastrar_produto(Produto("Mouse", "Informática", 3, 49.90, "Corredor A1"))
    sistema.cadastrar_produto(Produto("Teclado", "Informática", 150, 99.90, "Corredor A2"))
    sistema.atualizar_estoque("Mouse", 10)
    print(sistema.rastrear_localizacao("Mouse"))

    relatorio = sistema.gerar_relatorio()
    print("\nProdutos com estoque baixo:")
    for p in relatorio['estoque_baixo']:
        print(p)
    print("\nProdutos com excesso de estoque:")
    for p in relatorio['estoque_excesso']:
        print(p)
