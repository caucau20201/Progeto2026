# 1. criando uma lista vazia
liata_compras = []
print("=== bem_vindo ao gerenciador de compras! ===")

# 2. adicionado itens com um loop
while True:
    item = input("digite um item para a lista (ou 'sair' para finalizar): ")

    if item.lower () == 'sair':
        break

    # o metodo ppend( adiciona o item ao final da lista
    liata_compras.append(item)
    print(f"'{item}' foi adicionado com sucesso!")
    print(f"\nsua lista de compras finalizada:")

# 3. exibindo o tamanho da lista
total_item = len(liata_compras)
print(f"\nvoce adicionou um total de{total_item} intens.")

# 4.moatrando os itens usado um loop 'for'
print("\nsua lista de compras finalizada:")
for i, item in enumerate(liata_compras, start=1):
    print(f"{i}. {item}")

print("\n=== fim do programa ===")