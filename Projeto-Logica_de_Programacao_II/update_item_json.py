import json
from input_validator import input_int

##################################################################
#  Atualizar item individual do arquivo JSON                     #
##################################################################
def update_item():
    try:
        with open('playlist_data.json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        # Obtém o tamanho da lista "items" do JSON
        tamanho_lista = len(json_data["tracks"]["items"])

        # Verifica se há itens para atualizar
        if tamanho_lista == 0:
            print("A lista de itens está vazia.\n")
            return

        while True:
            # Solicita ao usuário que insira o número do índice
            mensagem = (
                f"Digite o índice (de 1 a {tamanho_lista}) do "
                "item que deseja atualizar (ou 0 para abortar): \n"
            )
            index_input = input_int(mensagem)

            # Verifica se o usuário deseja abortar
            if index_input == 0:
                print("Operação de atualização abortada.\n")
                return

            # Verifica se está dentro do intervalo válido
            if 1 <= index_input <= tamanho_lista:
                # Converte para índice de lista
                index = index_input - 1

                # Obtém o item atual
                current_item = json_data["tracks"]["items"][index]

                # Exibe as informações atuais
                print("Informações atuais do item:")
                print(f"Índice: {index_input}")
                print(f"Nome: {current_item['track']['name']}")
                print(f"Artista: {current_item['track']['artists'][0]['name']}")
                print(f"Álbum: {current_item['track']['album']['name']}")
                print(f"Duração: {current_item['track']['duration_ms']} ms")
                print(f"Popularidade: {current_item['track']['popularity']}")

                # Solicita ao usuário as novas informações
                new_name = input("Novo nome da música: ")
                new_artist = input("Novo nome do artista: ")
                new_album = input("Novo nome do álbum: ")
                new_duration = input_int("Nova duração (em ms): ")
                new_popularity = input_int("Nova popularidade: ")

                # Atualiza as informações do item
                json_data["tracks"]["items"][index]['track']['name'] = new_name
                json_data["tracks"]["items"][index]['track']['artists'][0]['name'] = new_artist
                json_data["tracks"]["items"][index]['track']['album']['name'] = new_album
                json_data["tracks"]["items"][index]['track']['duration_ms'] = new_duration
                json_data["tracks"]["items"][index]['track']['popularity'] = new_popularity

                print("Item atualizado com sucesso.\n")

                # Salva as alterações de volta no arquivo JSON
                with open('playlist_data.json', 'w', encoding='utf-8') as file:
                    json.dump(json_data, file, indent=4)
                break
            else:
                print(
                    f"Índice inválido. Por favor, insira um número "
                    f"entre 1 e {tamanho_lista} ou 0 para abortar.\n"
                )
    except Exception as e:
        print(f"Erro ao atualizar item: {e}\n")
        raise e
