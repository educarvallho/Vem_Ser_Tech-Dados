# Programa Principal

# Importando as funções de cada arquivo separado
from IPython.display import clear_output
from adicionar_itens import adicionar_itens
from cadastrar_restaurante import cadastrar_restaurante
from criar_pedido import criar_pedido
from exibir_restaurantes import exibir_restaurantes
from input_handlers import (
    validar_numero_restaurante,
)

# Cria uma Lista de Restaurantes vazia.
restaurantes = []

# Menu Principal de Interface do Usuário com Estrutura de Repetição
continuar_menu = True

# Loop de exibição do Menu.
while continuar_menu:
    print("1 - Cadastrar Restaurante")
    print("2 - Exibir Restaurantes Cadastrados")
    print("3 - Adicionar Novos Itens a um Restaurante")
    print("4 - Criar Pedido")
    print("5 - Sair")
    print()

    # Input para seleção do Menu.
    escolha = input("\tEscolha uma das opções acima " +
                    "e digite o número correspondente: \n\t")

    numero_restaurante = None

    # Validação para Inserção de Número Válido.
    if escolha in {'1', '3', '4'}:
        numero_restaurante = validar_numero_restaurante()
        if numero_restaurante is None:  # Verifica se o número é vazio (None).
            continue  # Volta ao início do loop para exibir o menu principal.

    # Relação de Função para serem acionadas.
    if escolha == '1':
        cadastrar_restaurante(numero_restaurante, restaurantes)
    elif escolha == '2':
        exibir_restaurantes(restaurantes)
    elif escolha == '3':
        adicionar_itens(numero_restaurante, restaurantes)
    elif escolha == '4':
        criar_pedido(numero_restaurante, restaurantes)
    elif escolha == '5':
        continuar_menu = False
    else:
        clear_output()
        print("Opção Inválida! Tente novamente.\n\n")