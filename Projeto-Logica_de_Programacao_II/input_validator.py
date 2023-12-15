##################################################################
#  Validador de Input                                            #
##################################################################
def input_int(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print('Digite um número inteiro válido.\n')
