"""
Aluno: Daniel Macêdo
Escola de programação Fuctura tecnologia 
"""
import numpy as np

#Criando uma lista
lista=[0,1,2,3,4,5,6,7]
print(lista)

#Criando um array a partir da lista
array=np.array(lista)
print(array)

#Criando lista usando list
lista2=list(range(9))
print(lista2)

# Transformando essa lista em array numpy
array1=np.array(range(9))
print(array1)

#Criando array com arange, arange(n) é uma junção de array(range(n))
array2=np.arange(9)
print(array2)

#Arange start, stop, step
array3=np.arange(0,10,0.5)
print(array3)

array4=np.around(array3) # arredonda para cima os valores do array 3
print(array4)

array3=np.arange(0,10,0.5, dtype=int)
print(array3)

array4=np.arange(12) # Nesse caso teremos numeros inteiros.
print(array4)

array4=np.arange(12.) # Usando o ponto podemos predeterminar o tipo float no array.
print(array4)

print(type(array4)) # Verificando o tipo do objeto

print(array4.dtype)

# Podemos criar um array digitando os valores
vetor1=np.array([0,1,2,3,4])
print(vetor1)

# selecionando um elemento específico
vetor1[3]

#selecionando um intervalo específico
vetor1[0:2]
print(vetor1[0:2])

# Alterando um elemento do Array
vetor1[2]=10
print(vetor1)

# Vamos tentar incluir elementos
vetor1[0]='Novo elemento'
print(vetor1)

# agora testando com float
vetor1[0]=45.6
print(vetor1)
# Observe que o valor de 45.6 foi para 45 porque ele subentendeu que seria inteiro.

# criando a primeira matriz
matriz1=np.array([[1,2,3],[4,5,6]])
print(matriz1)

#Podemos criar uma matriz a partir de uma lista:
lista2=[[13,81,22],[0,34,59],[21,48,94]]
print(lista2)

#agora usaremos np.matriz
matriz2=np.matrix(lista2)
print(matriz2)

# np.zeros : pode formar vetores e matrizes
x = np.zeros(3)
print(x)

# matriz zeros
x = np.zeros((3,2))
print(x)

# vetores e matrizes com uns
x = np.ones((5,3))
print(x)
x = np.ones(5)
print(x)

#Desafio: Como obter uma matriz 4x4 apenas com numeros 8 ?
x =np.ones((4,4))*8
print(x)

# Matrizes diagonais
z=np.diag(np.array([1,2,3,4,5,6]))
print(z)

# Agora determinando o tipo int
y=np.eye(5, dtype=float)
print(y)

# verificando shape de duas maneiras:
print(np.shape(matriz2))
print("shape da matriz é:",matriz2.shape)

#verificando o tipo da matriz:
type(matriz2)

#Selecionando elementos da matriz:
print(matriz2[2,1])
#Selecionando a primeira linha da matriz:
print(matriz2[0,:])
#Selecionando a terceira coluna da matriz:
print(matriz2[:,2])
#Alterando um elemento da matriz:
matriz2[1,0]=100
print(matriz2)

# Obtendo a soma dos valores do array :
print(np.sum(array4))
# Obtendo o produto:
print(np.prod(array4))
# Obtendo a soma acumulada:
print(np.cumsum(array4))
print(array4)

#Obtendo o valor mínimo do array:
print(array4.min())
#Valor máximo:
print(array4.max())

#Obtendo a média:
print(np.mean(array4))
#Obtendo a mediana:
print(np.median(array4))
#Variância:
print(np.var(array4))
#desvio ppadrão
print(np.std(array4))

# Desafio da classe:
#criar um array unidimensional utilizando arange 20 elementos:
print(np.arange(20))
#varrer o array para obter os pares :
print(np.arange(0,20,2))
#varrer o array para obter os pares :
print(np.arange(0,20,2)+1)
# Obter média, soma, produto, variancia e desvio padr~~ao:
print(np.mean(np.arange(20)))
print(np.sum(np.arange(20)))
print(np.prod(np.arange(20)))
print(np.var(np.arange(20)))
print(np.std(np.arange(20)))
#saber quais valores são maiores que 5 :
print(np.arange(20)>5)
#Obter os valores maiores que 5 :