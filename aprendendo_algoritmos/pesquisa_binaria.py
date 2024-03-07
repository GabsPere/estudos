def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        media = (baixo+alto) / 2 # -> Igual a 4/2, pois pega a quantidade de itens.
        meio = int(media) # -> Precisei converter o float em int para conseguir fazer a iteração.
        chute = lista[meio] # -> lista[2] pegando o item 5, literalmente o meio. Mas retornar o índice.
        if chute == item:
            return meio # -> Retorna o índice 2.
        if chute > item:
            alto = meio -1 # Retorna o indíce 1 ou 0.
        else:
            baixo = meio + 1 # Retorna o índice 3 ou 4.
    return None
minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista,7)) # -> O resultado retorna o número do índice, exemplo 9 = 4

'''
Uma forma de deixar mais interessante é colocar a lista com números aleatórios e
o "item" com um input.

'''