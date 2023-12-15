# -- Descrição do Projeto

# Tema: Música
# O programa criado se conecta à API do Spotify.
# Feito isso, ele busca a Playlist "Top 50 - Global".
# Salva os dados da consulta em um arquivo JSON.
# Faz todas as manipulações listadas abaixo.

# -- Itens do projeto

# - Ler uma lista de um JSON:  Feito!
# - O JSON deve vir de um API: Feito!
# - Programa bem Modularizado: Feito!
# - Listar itens do JSON:      Feito! (Arquivo "list_items_json.py")
# - Listar item individual:    Feito! (Arquivo "list_individual_item.py")
# - Adicionar item ao JSON:    Feito! (Arquivo "add_item_json.py")
# - Remover item do JSON:      Feito! (Arquivo "remove_item_json.py")
# - Atualizar item do JSON:    Feito! (Arquivo "update_item_json.py")
# - Realizar um filter():      Feito! (Arquivo "list_more_popular.py")
# - Realizar um reduce():      Feito! (Arquivo "calc_stats.py")
# - Realizar um map():         Feito! (Arquivo "calc_stats.py")
# - Utiliza lambda:            Feito! (Arquivo "calc_stats.py")
# - Todas operações com validações (try-except, raise): Feito!
# - Função - Lista de Tuplas (Máx e Min): Feito! (Arquivo "tuple_list.py")
# - Função - Lista de Tuplas (Parâmetro Opcional): Feito!
# - Obter dados estatísticos:         Feito! (Arquivo "calc_stats.py")
# - Salvar dados estatísticos em CSV: Feito! (Arquivo "calc_stats.py")

from IPython.display import clear_output
from input_validator import input_int
from start_program import start
from list_items_json import list_ranking
from list_more_popular import more_popular
from list_individual_item import individual_item
from tuple_list import tuple_list
from add_item_json import add_track_json
from update_item_json import update_item
from remove_item_json import remove_item
from calc_stats import calculate_stats

# Inicia a conexão com o API e atualiza o JSON
# Está aqui para executar logo no início do programa
start()

# Menu Principal de Interface do Usuário com Estrutura de Repetição
continuar_menu = True

# Loop de exibição do Menu.
while continuar_menu:
    print("1. Atualizar Playlist")
    print("2. Listar 'Top 50 - Global'")
    print("3. Listar Músicas 'Mais Populares'")
    print("4. Listar Item Individual")
    print("5. Música com Maior/Menor Duração")
    print("6. Adicionar Música ao JSON")
    print("7. Atualizar Música do JSON")
    print("8. Remover Música do JSON")
    print("9. Calcular Estatísticas e Salvar")
    print("0. Encerrar Programa")
    print()

    # Input para seleção do Menu.
    escolha = input_int("\tEscolha uma opção acima " +
                        "e digite o número: \n\t")

    # Validação para Inserção de Número Válido.
    if escolha not in range(0, 10):
        clear_output()
        print("Opção Inválida! Tente novamente.\n\n")
        continue  # Volta ao início do loop para exibir o menu principal.

    # Relação de Funções a serem acionadas.
    if escolha == 1:
      # Chama a função para atualizar a playlist
      start()
      
    elif escolha == 2:
      # Chama a função para listar 'Top 50 - Global'
      list_ranking()
      
    elif escolha == 3:
      # Chama a função para listar "Músicas mais populares"
      more_popular()
      
    elif escolha == 4:
      # Chama a função para listar item individual
      individual_item()
      
    elif escolha == 5:
      # Chama a função para listar música com maior/menor duração
      tuple_list()
      
    elif escolha == 6:
      # Chama a função para adicionar música ao JSON
      add_track_json()
      
    elif escolha == 7:
      # Chama a função para atualizar música no JSON
      update_item()
      
    elif escolha == 8:
      # Chama a função para remover música do JSON
      remove_item()
      
    elif escolha == 9:
      # Chama a função para calcular estatísticas e salvar
      calculate_stats()
      
    elif escolha == 0:
      continuar_menu = False
      
    else:
      clear_output()
      print("Opção Inválida! Tente novamente.\n\n")
      continue  # Volta ao início do loop para exibir o menu principal.
