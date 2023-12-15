import json

##################################################################
#  Listar Músicas mais populares do JSON (>90)                   #
##################################################################
def more_popular(filename='playlist_data.json'):
    try:
        # Ler dados da playlist do arquivo JSON
        with open(filename, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

        # Listar as músicas com popularidade maior que 90
        print("Músicas com Popularidade maior que 90:")
        more_popular = filter(
            lambda x: x["track"]["popularity"] > 90,
            json_data["tracks"]["items"]
        )
        for item in more_popular:
            artist_name = item['track']['artists'][0]['name']
            track_name = item['track']['name']
            print(f"{artist_name} - {track_name}")
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
