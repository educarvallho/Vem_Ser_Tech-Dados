import json
from input_validator import input_int

##################################################################
#  Listar item individual do arquivo JSON                        #
##################################################################
def individual_item():
    try:
        # Ler o arquivo JSON
        with open('playlist_data.json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        while True:
            # Obtém o tamanho da lista "items" do JSON
            tamanho_lista = len(json_data["tracks"]["items"])

            # Verifica se há itens na lista
            if tamanho_lista == 0:
                print("A lista de itens está vazia.\n")
                return

            # Solicita ao usuário que insira o número do Ranking
            mensagem = (
                f"Digite o índice (de 1 a {tamanho_lista}) que "
                "deseja visualizar (ou digite 0 para abortar): \n"
            )
            index_input = input_int(mensagem)

            # Verifica se o usuário deseja abortar
            if index_input == 0:
                print("Operação abortada pelo usuário.\n")
                return

            # Verifica se o índice está dentro do intervalo válido
            if 1 <= index_input <= tamanho_lista:
                index = index_input - 1
                item = json_data["tracks"]["items"][index]
                position = index + 1
                name = item['track']['name']
                artist = item['track']['artists'][0]['name']
                print(f"{position} - {artist} - {name}\n")
                break  # Sai do loop se a operação for bem-sucedida
            else:
                print(
                    f"Índice inválido. Por favor, insira um número "
                    f"entre 1 e {tamanho_lista}.\n"
                )
    except Exception as e:
        print(f"Erro ao ler item individual: {e}\n")
        raise e
