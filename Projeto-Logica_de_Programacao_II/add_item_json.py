import json

# Segue a Árvore de Diretórios dos prinpais itens abaixo:

# "nome": raiz{tracks{items[{track{name}}]}}
# "album": raiz{tracks{items[{track{album{name}}}]}}
# "artist": raiz{tracks{items[{track{album{artists[{name}]}}}]}}
# "duration": raiz{tracks{items[{track{duration_ms}}]}}
# "popularity": raiz{tracks{items[{track{popularity}}]}}

##################################################################
#  Adicionar Faixa "Fake" no arquivo JSON                        #
##################################################################
def add_track_json():
    # Criar um novo item para adicionar no JSON
    new_track = {
        "added_at": "2023-11-25T12:00:00Z",
        "added_by": {
            "external_urls": {
                "spotify": "https://spotify.com"
            },
            "href": "https://spotify.com",
            "id": "000001",
            "type": "user",
            "uri": "Eduardo Carvalho"
        },
        "is_local": False,
        "primary_color": None,
        "track": {
            "album": {
                "album_type": "single",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://spotify.com"
                        },
                        "href": "https://spotify.com",
                        "id": "45dkTj5sMxR",
                        "name": "Zé Ramalho",
                        "type": "artist",
                        "uri": "spotify:artist:45dkTj5sMxR"
                    }
                ],
                "available_markets": [
                    "BR",
                    "US"
                ],
                "external_urls": {
                    "spotify": "https://spotify.com"
                },
                "href": "https://spotify.com",
                "id": "3UOV8XvCwM1KaATRNX",
                "images": [
                    {
                        "height": 640,
                        "url": "https://cdn.co/image/0",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://cdn.co/image/0",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://cdn.co/image/0",
                        "width": 64
                    }
                ],
                "name": "Ao Vivo 2005",
                "release_date": "2004-09-15",
                "release_date_precision": "day",
                "total_tracks": 1,
                "type": "album",
                "uri": "spotify:album:3UOV8XvCwM1KaATRNX"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://spotify.com"
                    },
                    "href": "https://api.spotify.com",
                    "id": "45dkTj5sMxRS",
                    "name": "Zé Ramalho",
                    "type": "artist",
                    "uri": "spotify:artist:45dkTj5sMxRS"
                }
            ],
            "available_markets": [
                "BR",
                "US"
            ],
            "disc_number": 1,
            "duration_ms": 135872,
            "episode": False,
            "explicit": True,
            "external_ids": {
                "isrc": "USRC123019322"
            },
            "external_urls": {
                "spotify": "https://spotify.com"
            },
            "href": "https://spotify.com",
            "id": "3rUxGC1vUpkDG9CZFHM",
            "is_local": False,
            "name": "Sinônimos",
            "popularity": 99,
            "preview_url": "https://cdn.co/mp3-preview",
            "track": True,
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:3rUxGC1vUpkDG9CZFHM"
        },
        "video_thumbnail": {
            "url": None
        }
    }
  
    # Ler o arquivo JSON
    try:
        with open('playlist_data.json', 'r', encoding='utf-8') as file:
            json_data = json.load(file)
  
        # Adicionar o novo item à lista do JSON
        json_data["tracks"]["items"].append(new_track)
  
        # Salvar as alterações de volta no arquivo JSON
        with open('playlist_data.json', 'w', encoding='utf-8') as file:
            json.dump(json_data, file, indent=4)
  
        print("Novo item adicionado ao JSON com sucesso.\n")
  
    except Exception as e:
        print(f"Erro ao adicionar novo item ao JSON: {e}\n")
        raise e
      