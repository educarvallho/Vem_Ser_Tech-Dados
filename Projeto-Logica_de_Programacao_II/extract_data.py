import json

##################################################################
#  Faz leitura do arquivo JSON                                   #
##################################################################
def read_json(filename='playlist_data.json'):
  try:
      with open(filename, 'r', encoding='utf-8') as json_file:
          playlist_data = json.load(json_file)
          return playlist_data
  except FileNotFoundError:
      print(f"O arquivo {filename} não foi encontrado.\n")
      return None
  except Exception as e:
      print(f"Erro ao ler o arquivo {filename}: {e}\n")
      return None

##################################################################
#  Filtra as chaves desejadas do arquivo JSON                    #
##################################################################
def extract_data(json_data):
  resultados = []

  for index, item in enumerate(json_data["tracks"]["items"]):
      track_info = {
          "position": index + 1,
          "nome": item["track"]["name"],
          "album": item["track"]["album"]["name"],
          "artist": item["track"]["artists"][0]["name"],
          "duration": int(item["track"]["duration_ms"]),
          "popularity": item["track"]["popularity"]
      }

      resultados.append(track_info)

  return resultados
