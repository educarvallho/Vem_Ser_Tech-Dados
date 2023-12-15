import csv
from statistics import mean, mode
from functools import reduce
from extract_data import read_json, extract_data

##################################################################
#  Calcula os dados estatísticos desejados                       #
##################################################################
def calculate_stats():
  try:
      # Ler dados da playlist do arquivo JSON
      read_data = read_json()

      # Extrair dados desejados
      extracted_data = extract_data(read_data)
    
      # Converter a duração para segundos
      duracao_segundos = list(map(
          lambda x: x["duration"] // 1000,
          extracted_data
      ))

      # Música com maior duração
      max_duration = max(duracao_segundos)

      # Música com menor duração
      min_duration = min(duracao_segundos)

      # Música com maior popularidade
      max_popularity = max(
          extracted_data,
          key=lambda x: x["popularity"]
      )["popularity"]
  
      # Música com menor popularidade
      min_popularity = min(
          extracted_data,
          key=lambda x: x["popularity"]
      )["popularity"]

      # Calcular a média da popularidade
      media_popularity = reduce(
          lambda x, y: x + y["popularity"],
          extracted_data,
          0
      ) / len(extracted_data)

      # Calcular a média da duração em segundos
      media_duration = mean(duracao_segundos)

      # Calcular a moda da duração
      duracoes = [item for item in duracao_segundos]
      moda_duration = mode(duracoes)

      # Calcular a mediana da duração
      duracao_ordenada = sorted(duracao_segundos)  
      tamanho_lista = len(duracao_ordenada)
      indice_mediana = tamanho_lista // 2

      # Verifica se possui um número par de elementos
      if tamanho_lista % 2 == 0:
           median_duration = (duracao_ordenada[indice_mediana - 1] 
              + duracao_ordenada[indice_mediana]) / 2
      else:
           median_duration = duracao_ordenada[indice_mediana]

      # Criar uma tupla com as estatísticas
      stats = (
          ("max_duration", max_duration),
          ("min_duration", min_duration),
          ("max_popularity", max_popularity),
          ("min_popularity", min_popularity),
          ("media_popularity", media_popularity),
          ("media_duration", media_duration),
          ("moda_duration", moda_duration),
          ("median_duration", median_duration)
      )
  
      # Chama a função para salvar as estatísticas em CSV
      save_stats_csv(stats)

  except Exception as e:
      print(f"Erro ao calcular estatísticas: {e}\n")
      raise e

##################################################################
#  Salva os dados estatísticos desejados em um arquivo CSV       #
##################################################################
def save_stats_csv(stats):
  try:
      with open('estatisticas.csv', 'w', newline='', 
                encoding='utf-8') as file:
          writer = csv.writer(file)

          # Escrever o cabeçalho
          writer.writerow(['Estatística', 'Valor'])

          # Escrever as estatísticas no arquivo CSV
          for stat, value in stats:
              writer.writerow([stat, value])

          print("Estatísticas salvas em 'estatisticas.csv'.\n")

  except Exception as e:
      print(f"Erro ao salvar estatísticas em CSV: {e}\n")
      raise e