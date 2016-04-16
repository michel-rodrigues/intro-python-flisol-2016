#!/usr/bin/env python3

"""
Você irá escrever um programa para criptografar e decriptografar uma mensagem seguindo a ideia
do Imperador César.

O programa terá 4 funções, a função principal será a qual chamaremos no final do código, 
ela utilizará as outras 3 funções para processar a mensagem do usuário.

As outras 3 funções serão:

'recebeModo' - pergunta se o usuário quer criptografar ou decriptografar e garante que uma entrada
válida foi recebida.

'recebeChave' - pede o valor da chave para o usuário e devolve esse valor caso ele seja adequado.

'geraMsgTraduzida' - traduz a mensagem do usuário trocando cada caractere por caractere correspondente
à chave passada pelo usuário.

"""


# Tamanho máximo da chave
TAM_MAX_CH = 26


# Defina uma função chamada recebeModo, ela não recebe nenhum parâmetro


    # Enquanto for verdade
    

        # Uma variável 'modo' recebe uma entrada do usuário convertida para letras minúsculas
        

        # Se modo estiver entre os modos disponíveis (criptografar, c, decriptografar, d)
        

            #Retorna a variável modo
            

        # Senão imprime uma mensagem para o usuário
        # Exemplo: "Digite 'criptografar' ou 'c' ou 'decriptografar' ou 'd'."
        


# Defina uma função chamada 'recebeChave', ela não recebe nenhum parâmetro


    # A instrução 'global' diz ao Python que TAM_MAX_CH se refere a variável declarada fora da função
    global TAM_MAX_CH

    # Enquanto for verdade
    

        # Uma variável chave recebe um valor do usuário, indicando que deve ser entre 1 e TAM_MAX_CH
        

        # Se chave é um valor entre 1 e TAM_MAX_CH
        

            # Retorna chave
            

# Defina uma função chamada 'geraMsgTraduzida' que recebe os seguintes parâmetros: modo, mensagem, chave


    # 'Se' o primeiro elemento da variável 'modo' for igual a string 'd'
    

        # Converte chave para um valor negativo
        

    # Inicializa a variável com um string vazia
    traduzido = ''

    # Para cada caractere na variável mensagem
    

        # Se caractere é uma string
        # Dica: utilize o método 'isalpha' - caractere.isalpha()
        

            # Atribui à variável 'num' um valor inteiro, que representa o código Unicode do caractere
            num = ord(simbolo)

            # Soma o valor de 'num' com o valor da 'chave' e faz uma nova atribuição em 'num'
            num += chave


            # Verifica se o caractere é maiusculo
            if caractere.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26

            # 'Senão se' caractere é uma letra minúcula
            
                # 'Se' a variável 'num' for maior que o valor do código Unicode de 'z'
                
                    # Subtrai 26 da variável 'num'

                # 'Senão se' a variável num for menor que o valor do código Unicode de 'a'
                

                    # Soma 'num' com 26
                    
            # A função chr() faz o oposto da função ord(), ou seja, a partir de um valor inteiro
            # retorna o caractere correspondente ao código Unicode desse valor
            traduzido += chr(num)

        else:
            traduzido += simbolo

    return traduzido


# Defina uma função principal chamada 'main', ela não recebe nenhum parâmetro


    """

    Para que o programa imprima a mensagem criptografada ou decriptografada para o usuário,
    a função 'geraMsgTraduzida' é chamada como um argumento para a função print().
    Entretanto, a função geraMsgTraduzida também recebe parâmetros (modo, mensagem, chave).
    Declare esses 3 parâmetros como variáveis, fazendo a devida atribuição a cada uma delas
    Dica: duas variáveis receberão um valor retornado por função; outra variável receberá 
    um valor inserido pelo usuário.

    """


    print("Seu texto traduzido é:")
    print(geraMsgTraduzida(modo, mensagem, chave))



# Chama a função main para ser executada
main()



