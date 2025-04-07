from produto import Produto
from typing import List

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