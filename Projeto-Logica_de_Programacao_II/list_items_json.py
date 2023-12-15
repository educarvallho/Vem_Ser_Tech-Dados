import json

##################################################################
#  Listar o Ranking "Top 50 - Global" do JSON                    #
##################################################################
def list_ranking(filename='playlist_data.json'):
    try:
        # Ler dados da playlist do arquivo JSON
        with open(filename, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        # Listar as músicas do Ranking Top 50 Global
        print("Ranking das Músicas Top 50 Global:")
        for index, item in enumerate(json_data["tracks"]["items"]):
            position = index + 1
            artist_name = item['track']['artists'][0]['name']
            track_name = item['track']['name']
            print(f"{position} - {artist_name} - {track_name}")
        print()
      
    except FileNotFoundError:
        print(f"O arquivo {filename} não foi encontrado.\n")
        raise

    except json.JSONDecodeError:
        print(f"Erro ao decodificar o arquivo {filename}.\n")
        raise

    except KeyError as e:
        print(f"Chave ausente no arquivo JSON: {e}\n")
        raise e

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}\n")
        raise e
