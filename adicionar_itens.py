# Função - Adicionar Itens a um Restaurante Existente

from input_handlers import (
    input_float,
    input_inteiro,
)

def adicionar_itens(numero_restaurante, restaurantes):
    # Índice dos Restaurantes nas Listas.
    NUMERO_RESTAURANTE = 0
    
    restaurante_encontrado = None
    continuar_cadastro = True
    
    # Loop para selecionar Restaurante com o número informado.
    index = 0
    while index < len(restaurantes) and not restaurante_encontrado:
        restaurante = restaurantes[index]
        restaurante_existe = restaurante[NUMERO_RESTAURANTE] == numero_restaurante

        if restaurante_existe:
            restaurante_encontrado = restaurante
        index += 1

    # Seleção do Restaurante desejado para acrescentar itens ao Menu.
    if restaurante_encontrado:
        numero_restaurante, menu = restaurante_encontrado

        # Loop para inserir os itens ao cadastro.
        while continuar_cadastro:
            nome = input("Cadastre o item (Nome) [Vazio Termina Cadastro]: ")
            if not nome:
                continuar_cadastro = False
            else:
                valor = input_float()
                tempo = input_inteiro()
                menu.append((nome, valor, tempo))

        print(f"Itens adicionados ao restaurante {numero_restaurante}.\n")
    else:
        print("Restaurante não encontrado.\n")