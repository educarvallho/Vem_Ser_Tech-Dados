# Função - Cadastrar um Restaurante e Menu

from input_handlers import (
    input_float,
    input_inteiro,
)

def cadastrar_restaurante(numero_restaurante, restaurantes):
    # Índice dos Restaurantes nas Listas.
    NUMERO_RESTAURANTE = 0
    
    restaurante_existente = False

    # Verificar se já existe um restaurante com o mesmo número.
    index = 0
    while index < len(restaurantes) and not restaurante_existente:
        restaurante = restaurantes[index]
        restaurante_existente = restaurante[NUMERO_RESTAURANTE] == numero_restaurante
        index += 1

    if restaurante_existente:
        print(f"Restaurante com número {numero_restaurante} já cadastrado!\n")
    else:

        # Se o restaurante não existe, criar um novo cadastro.
        menu = []
        cadastro_ativo = True
        while cadastro_ativo:
            nome = input("Nome do Prato [Vazio Termina Cadastro]: ")
            if nome == "":
                cadastro_ativo = False
            else:
                valor = input_float()
                tempo = input_inteiro()
                menu.append((nome, valor, tempo))

        # Insere os dados cadastrados na Lista Principal.
        restaurante = [numero_restaurante, menu]
        restaurantes.append(restaurante)
        print(f"Restaurante {numero_restaurante} cadastrado com sucesso!\n")