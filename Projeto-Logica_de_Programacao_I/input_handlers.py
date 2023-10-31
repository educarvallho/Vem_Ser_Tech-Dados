# Função - Verificar se número inserido é tipo [float]

def input_float():
    numero_valido = False
    while not numero_valido:
        numero = input('Digite o valor do Prato: ').replace(",", ".", 1)
        teste = numero.replace(".", "", 1).isdigit()
        if teste:
            n = float(numero)
            numero_valido = True
        else:
            print('Digite o valor do Prato válido.')
    return n


# Verificar se número inserido é tipo [int]

def input_inteiro():
    numero_valido = False
    while not numero_valido:
        numero = input('Digite o Tempo de Preparo: ')
        if numero.isdigit():
            n = int(numero)
            numero_valido = True
        else:
            print('Digite o Tempo de Preparo válido.')
    return n
    
    
# Função - Verificar se número do Restaurante é válido

def validar_numero_restaurante():
    numero_cadastro = None
    validar_numero = True

    while validar_numero:
        numero_cadastro = input("Número do Restaurante: ")

        verifica_numero = numero_cadastro == ""
        if verifica_numero:
            print("Voltando para o Menu Principal...")
            return None  # Retorna None se a entrada estiver vazia
                         # e volta ao menu principal.
        else:
            verifica_letras = not numero_cadastro.isdigit()
            if verifica_letras:
                print("Por favor, insira um número válido para o Restaurante.")
            else:
                numero_cadastro = int(numero_cadastro)
                validar_numero = False  # Interrompe loop se número for válido.
    return numero_cadastro