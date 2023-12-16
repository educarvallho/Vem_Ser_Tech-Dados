import requests
import base64
import json

# Credenciais do Spotify
CLIENT_ID = 'xxxxx'
CLIENT_SECRET = 'xxxxx'

# ID da playlist "Top 50 - Global"
playlist_id = '37i9dQZEVXbMDoHDwVN2tF'

##################################################################
#   Requisição à API do Spotify para obter token de acesso       #
##################################################################
def get_access_token():
  try:
      token_url = 'https://accounts.spotify.com/api/token'
      token_params = {
          'grant_type': 'client_credentials',
      }
      token_headers = {
          'Authorization': 'Basic ' + base64.b64encode(
              f'{CLIENT_ID}:{CLIENT_SECRET}'.encode('utf-8')
          ).decode('utf-8'),
      }
      token_response = requests.post(token_url, data=token_params, 
                                  headers=token_headers)

      token_response.raise_for_status()

      token_data = token_response.json()
      access_token = token_data['access_token']

      print("Token de acesso obtido com sucesso.\n")
      return access_token
  except requests.exceptions.HTTPError as e:
      print(f"Erro HTTP ao obter o token de acesso: {e}\n")
      raise e
  except requests.exceptions.RequestException as e:
      print(f"Erro ao obter o token de acesso: {e}\n")
      raise e
  except KeyError as e:
      print(f"Erro ao extrair o token de acesso: {e}\n")
      raise e
    
##################################################################
#  Requisita à API do Spotify para obter a playlist              #
##################################################################
def get_playlist_data(playlist_id, access_token):
    playlist_url = (
    f'https://api.spotify.com/v1/playlists/{playlist_id}'
    )
    playlist_headers = {
      'Authorization': f'Bearer {access_token}'
    }
  
    try:
        # Requisição à API do Spotify
        playlist_response = requests.get(playlist_url, 
                                         headers=playlist_headers)
        playlist_data = playlist_response.json()

        print("Dados da playlist obtidos com sucesso.\n")
        return playlist_data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter dados da playlist: {e}\n")
        raise e
  
##################################################################
#  Salva a consulta da playlist em arquivo JSON                  #
##################################################################
def save_to_json(data, filename='playlist_data.json'):
  try:
      with open(filename, 'w', encoding='utf-8') as json_file:
          json.dump(data, json_file, ensure_ascii=False, indent=4)

      print(f"Dados salvos em {filename} com sucesso.\n")
  except IOError as e:
      print(f"Erro ao salvar os dados em {filename}: {e}\n")
      raise e
