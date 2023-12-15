from api_connect import (
    get_access_token,
    get_playlist_data,
    save_to_json
)

##################################################################
#   Inicia a conexão com o API e atualiza o JSON                 #
##################################################################
def start():
  # ID da playlist "Top 50 - Global"
  playlist_id = '37i9dQZEVXbMDoHDwVN2tF'
  
  # Obter novo Token de acesso
  access_token = get_access_token()
  
  # Obter dados da playlist
  playlist_data = get_playlist_data(playlist_id, access_token)
  
  # Salvar dados em um arquivo JSON
  save_to_json(playlist_data, 'playlist_data.json')