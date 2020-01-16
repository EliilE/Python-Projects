#Declara a matriz:
a = False
matriz=[0]*10
for i in range (0,10):
    matriz[i]=[0]*10


#Alimenta a matriz:
from random import randint
for i in range (0,10):
    for j in range (0,10):
        matriz[i][j]=randint(0,9)

#Exibe a matriz:
for i in range (0,10):
    for j in range (0,10):
        print(' {} '.format(matriz[i][j]),end ='')
    print('')

#Recebe o numero do usuário:
n=int(input('Digite um número de três dígito -> '))

#Verifica se o número contém três digitos:
if(n<1 or n>999):
    print('Número digitado errado, digite um número om 3 digitos -> ')
else:

    #Converte o número digitado pelo usuário em unidade, dezena e centena:
    c=n//100
    d=n%100//10
    u=n%10

    #Verifica se a centena existe dentro da matriz:
    a=False
    for i in range(0, 10):
        for j in range(0, 10):
            if(c==matriz[i][j]):
                if(j < 8):
                    if(d==matriz[i][j+1] and u==matriz[i][j+2]):
                        print('{} está na posição {}/{}, {} está na posição {}/{} e {} está na posição {}/{}.'.format(c, i, j, d, i, j+1, u, i, j+2))
                        a=True
                        break
                if(j > 1):
                    if(d==matriz[i][j-1] and u==matriz[i][j-2]):
                        print('{} está na posição {}/{}, {} está na posição {}/{} e {} está na posição {}/{}.'.format(c, i, j, d, i, j-1, u, i, j-2))
                        a = True
                        break

                if(i < 8):
                    if(d==matriz[i+1][j] and u==matriz[i+2][j]):
                        print('{} está na posição {}/{}, {} está na posição {}/{} e {} está na posição {}/{}.'.format(c, i, j, d, i, i+1, u, i, i+2))
                        a = True
                        break

                if(i >1 ):
                    if(d == matriz[i-1][j] and u == matriz[i-2][j]):
                        print('{} está na posição {}/{}, {} está na posição {}/{} e {} está na posição {}/{}.'.format(c, i, j, d, i, j-1, u, i, j-2))
                        a = True
                        break
        if(a==True):
            break
if(a==False):
    print('Não há sequência dos números digitados.')