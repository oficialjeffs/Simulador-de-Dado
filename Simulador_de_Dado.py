import random
x=1
e=input('Deseja jogar o dado?\n-----------------------------\nDigite [s] para sim ou [n] para não.\n-----------------------------\n:')

while x==1:
    
    if e=='s':  
        n=random.randint(1,6)
        print('O valor é:',n)
        e=input('\n-----------------------------\nDeseja jogar novamente?\n-----------------------------\nDigite [s] para sim ou [n] para não.\n-----------------------------\n:') 
    elif e=='n':   
        print('Finalizando Programa')
        x=0
    else:
        print('Digite Apenas valores Válidos')
        e=input('-----------------------------\nDeseja jogar o dado?\n-----------------------------\nDigite [s] para sim ou [n] para não.\n-----------------------------\n:')
