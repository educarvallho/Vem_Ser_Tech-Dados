# Função - Exibir Restaurantes Cadastrados

def exibir_restaurantes(restaurantes):
    # Índice dos Restaurantes nas Listas.
    NUMERO_RESTAURANTE = 0

    if not restaurantes:
        print("Nenhum restaurante cadastrado.\n")
    else:
        print("Restaurantes cadastrados:")
        for restaurante in restaurantes:
            print(f"Número do Restaurante: {restaurante[NUMERO_RESTAURANTE]}\n")