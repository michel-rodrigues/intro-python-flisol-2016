#!/usr/bin/env python3

from random import randint    # Importa o método randint do módulo ramdom


num_secreto = randint(1, 50)    # randint gera uma número aleatório entre 1 e 50

chute = 0
tentativas = 0

# O laço inicia verificando se os valores de 'chute' e 'num_secreto' são diferentes,
# enquanto isso for verdadeiro ('chute' diferente de 'num_secreto'), o laço será executado.
# A execução do laço será interrompida em qualquer ponto do bloco quando essa condição não
# for mais verdadeira, ou seja, quando o valor do 'chute' for igual ao 'num_secreto'.
# Quando isso ocorre o programa salta para o último 'else' e a execução termina.

while chute != num_secreto:

    # Limita o número de tentivas
    if tentativas < 10:

        # Recebe o valor do chute
        chute = int(input("\nChute um número entre 1 e 50: "))

        # Se o chute estiver entre 0 e 50, verifica se 'chute' é maior ou menor que
        # o valor de 'num_secreto'.
        # Se o valor não estiver entre 0 e 50, a expressão 'break' encerra o programa.

        if 0 <= chute <= 50:

            if chute > num_secreto:
                tentativas += 1

                if 10 - tentativas != 0:
                    print("Restam %d tentativas. Tente um número menor" %(10 - tentativas))    
    
            elif chute < num_secreto:
                tentativas += 1

                if 10 - tentativas != 0:
                    print("\nRestam %d tentativas. Tente um número maior" %(10 - tentativas))

        else:
            print("\nOnde você aprendeu a contar? O_o")
            break

    else:
        print("\nSuas tentativas acabaram, o número era %d" % num_secreto)
        break

else:
    print("\nAcertou em %d tentativas." % tentativas)
