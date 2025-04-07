class Produto:
    def __init__(self, nome: str, categoria: str, quantidade: int, preco: float, localizacao: str):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

    def __repr__(self):
        return f"{self.nome} | {self.categoria} | Qtd: {self.quantidade} | Preco: {self.preco} | Local: {self.localizacao}"