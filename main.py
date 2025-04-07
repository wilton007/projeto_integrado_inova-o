from produto import Produto
from estoque import Estoque, SistemaEstoque


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
