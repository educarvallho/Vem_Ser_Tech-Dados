import json
from input_validator import input_int

##################################################################
#  Adicionar Faixa "Fake" no arquivo JSON                        #
##################################################################
def remove_item():
    try:
        with open('playlist_data.json', 'r', encoding='utf-8') as file:
          json_data = json.load(file)

        # Obtém o tamanho da lista "items" do JSON
        tamanho_lista = len(json_data["tracks"]["items"])

        # Verifica se há itens para remover
        if tamanho_lista == 0:
            print("A lista de itens está vazia.\n")
            return

        while True:
            # Solicita ao usuário que insira o número do índice
            mensagem = (
                f"Digite o índice (de 1 a {tamanho_lista}) do "
                "item que deseja remover (ou 0 para abortar): \n"
            )
            index_input = input_int(mensagem)

            # Verifica se o usuário deseja abortar
            if index_input == 0:
                print("Operação de remoção abortada.\n")
                return

            # Verifica se está dentro do intervalo válido
            if 1 <= index_input <= tamanho_lista:
                # Converte para índice de lista
                index = index_input - 1

                # Remove o item da lista
                removed_item = json_data["tracks"]["items"].pop(index)

                print("Item removido com sucesso.\n")

                # Salva as alterações de volta no arquivo JSON
                with open('playlist_data.json', 'w', encoding='utf-8') as file:
                    json.dump(json_data, file, indent=4)
                break  # Sai do loop pois o índice foi válido
            else:
                print(
                    f"Índice inválido. Por favor, insira um número "
                    f"entre 1 e {tamanho_lista} ou 0 para abortar.\n"
                )
    except Exception as e:
        print(f"Erro ao remover item: {e}\n")
        raise e
