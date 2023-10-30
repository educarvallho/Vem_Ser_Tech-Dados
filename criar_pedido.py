#  Função - Criar Pedido

def criar_pedido(numero_restaurante, restaurantes):
    restaurante_encontrado = None

    # Índice dos Restaurantes, Valor do Prato e Tempo de Preparo nas Listas.
    NUMERO_RESTAURANTE = 0
    VALOR_PRATO = 1
    TEMPO_PRATO = 2

    # Loop para selecionar Restaurante com o número informado.
    index = 0
    while index < len(restaurantes) and not restaurante_encontrado:
        restaurante = restaurantes[index]
        restaurante_existe = restaurante[NUMERO_RESTAURANTE] == numero_restaurante

        if restaurante_existe:
            restaurante_encontrado = restaurante
        index += 1

    # Seleção do Restaurante desejado para criação de Pedido.
    if restaurante_encontrado:
        numero_restaurante, menu = restaurante_encontrado
        pedido = []
        continuar_pedido = True

        # Loop para exibir itens do Menu do Restaurante selecionado.
        while continuar_pedido:
            for i, item in enumerate(menu, 1):
                nome, valor, tempo = item
                print(f"{i} - {nome} — R$ {valor:.2f}".replace(".", ",") +
                      f" - Tempo: {tempo} minutos.\n")

            # Validação dos Itens escolhidos de acordo disponibilidade.
            escolha = input("Incluir [Vazio Termina Pedido]: ")
            if not escolha:
                continuar_pedido = False
            else:
                escolha = int(escolha)
                escolha_valida = 1 <= escolha <= len(menu)
                if escolha_valida:
                    pedido.append(menu[escolha - 1])
                else:
                    print("Opção inválida.\n")

        # Soma do Valor Total e Tempo de Preparo do Pedido de acordo aos itens.
        total_valor = sum(item[VALOR_PRATO] for item in pedido)
        total_tempo = sum(item[TEMPO_PRATO] for item in pedido)
        print(f"Seu pedido ficou R$ {total_valor:.2f}".replace(".", ",") +
              f" e será entregue em {total_tempo} minutos!\n")
    else:
        print("Restaurante não encontrado.\n")