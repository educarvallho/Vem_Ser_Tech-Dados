from input_validator import input_int
from extract_data import read_json, extract_data

##################################################################
#  Cria uma lista de Tuplas com Posição do Raking e Duração      #
##################################################################
def tuple_list():
  try:
      while True:
          mensagem = (
              "Por favor, escolha uma opção:\n"
              "0 - Abortar operação\n"
              "1 - Encontrar música com maior duração\n"
              "2 - Encontrar música com menor duração\n"
          )

          opcao = input_int(mensagem)

          if opcao == 0:
              print("Operação abortada pelo usuário.\n")
              return None, 0
          elif opcao in [1, 2]:
              # Ler dados da playlist do arquivo JSON
              read_data = read_json()

              # Extrair dados desejados
              extracted_data = extract_data(read_data)

              # Converter a duração para segundos
              lista_tuplas = list(map(
                  lambda x: (x["position"], x["duration"] // 1000),
                  extracted_data
              ))
              
            # Chamada da função analisar_duracao()
              analisar_duracao(lista_tuplas, opcao)
            
              return lista_tuplas, opcao
          else:
              print("Opção inválida! Por favor, escolha novamente.\n")

  except Exception as e:
      print(f"Erro ao processar opção: {e}\n")
      raise e

##################################################################
#  Retorna Música de Máxima/Mínima duração conforme escolha      #
##################################################################
def analisar_duracao(lista_tuplas, opcao):
  try:
      if not lista_tuplas:
          print("A lista está vazia.\n")
          return

      if opcao == 0:
          print("Operação abortada pelo usuário.\n")
          return

      if opcao == 1:
          # Encontrar o item com a maior duração
          max_item = max(lista_tuplas, key=lambda x: x[1])
          print(f"A música com maior duração está na Posição "
                f"{max_item[0]} "
                f"e tem duração de {max_item[1]} segundos.\n")

      elif opcao == 2:
          # Encontrar o item com a menor duração
          min_item = min(lista_tuplas, key=lambda x: x[1])
          print(f"A música com menor duração está na Posição "
                f"{min_item[0]} "
                f"e tem duração de {min_item[1]} segundos.\n")

      else:
          print("Opção inválida! Por favor, escolha:\n"
            "0 - Abortar operação\n"
            "1 - Encontrar música com maior duração\n"
            "2 - Encontrar música com menor duração\n")

  except Exception as e:
      print(f"Erro ao analisar a duração: {e}\n")
      raise e
