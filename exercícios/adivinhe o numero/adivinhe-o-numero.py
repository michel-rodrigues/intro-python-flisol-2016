#!/usr/bin/env python3

"""
Você irá escrever um jogo que pede ao usuário que chute um número entre 1 e 50.
O programa irá verificar se esse valor é menor, maior ou igual ao valor gerado
aleatoriamente e retornará uma resposta adequada ao jogador. O jogador terá 10
chances para acertar o número.

"""

from random import randint    # Importa o método randint do módulo ramdom


num_secreto = randint(1, 50)    # randint gera uma número aleatório entre 1 e 50

chute = 0
tentativas = 0

# 'Enquanto' chute for 'diferente' de num_secreto


    # 'Se' tentativas for 'menor que' 10
    

        # chute 'recebe' um valor 'inteiro' do 'usuário' entre 1 e 50
        

        # 'Se' chute estiver 'entre' 0 e 50
        

            # 'Se' chute for menor que num_secreto
            

                # Soma 1 à variável tentativas
                

                # Se 10 menos tentativas for diferente de zero
                

                    #Imprime uma instrução para o usuário
                    '''
                    Dica: "\nRestam %d tentativas. Tente um número maior"
                    ''' 
                    

            # Senão se chute for maior que num_secreto
            

                # Soma 1 à variável tentativas
                

                # Se 10 menos tentativas for diferente de 0
                

                    # Imprime uma instrução para o usuário
                    '''
                    Dica: "\nRestam %d tentativas. Tente um número maior"
                    '''
                    

        # Senão imprime uma mensagem para o usuário e encerra a execução
        '''
        Dica: "\nOnde você aprendeu a contar? O_o")
        '''
        

    # Senão imprime uma mensagem para o usuário e encerra a execução
    '''
    Dica: "\nSuas tentativas acabaram, o número era %d"
    '''
    

# Senão imprime uma mensagem para o usuário
'''
Dica: "\nAcertou em %d tentativas."
'''



