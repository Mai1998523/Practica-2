#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
#La libreria es Numpy, pero le asignamos un nombre
#Maigualida Lizet Rangel Serrano 1951


# In[11]:


arreglo = np.array([0,1,2,3,4,5])


# In[12]:


arreglo, type(arreglo)


# In[13]:


notas = [16,17,14,17,19,15]
ar_notas = np.array(notas, dtype=float)


# In[14]:


ar_notas, type(ar_notas[0])


# In[15]:


ar_notas_todas = np.array(([0,1,2,3,4,5], notas))
ar_notas_todas


# In[18]:


#Numero de dimensiones de un array NDIM
print(ar_notas_todas.ndim)
print(ar_notas.ndim)


# In[19]:


#tamaño de cada dimension array SHAPE
print(ar_notas_todas.shape)
print(ar_notas.shape)


# In[21]:


#Arrays especiaes
#ZERO:Todos los elementos son igual a 0
#ones:Todos los elementos son igual a 1
#identity: Produce una matriz cuadrada identidad
#arange : nuevo array con rango especificado
arr = np.zeros((2,3), dtype=float)
print(arr)


# In[22]:


ar2 = np.ones((3,4), dtype=float)
print(ar2)


# In[23]:


ar4 = np.identity((4), dtype=float)
print(ar4)


# In[24]:


ar6 = np.eye((4), dtype=float)
print(ar6)


# In[25]:


ar5 = np.arange(1,9)
print(ar5)


# 02 OPERACIONES BASICAS: los array nos permite realizar 
# operaciones aritmeticas elemento a elemento directamente

# In[26]:


import numpy as np
arr = np.arange(1,9)

arr


# In[27]:


arr.shape=(2,4)
arr


# In[33]:


lista = [1,2,3,4,5,6,7]


# In[34]:


lista + lista


# In[28]:


arr + arr #suma


# In[29]:


arr - arr #sustraccion


# In[30]:


arr * arr #producto


# In[31]:


arr ** arr #Exponenciacion


# In[32]:


arr/arr #division


# 04 ALGEBRA LINEAL

# In[35]:


#Producto de arrays, producto escalar
import numpy as np

a = np.array([1,2,3], float)
b = np.array([0,1,1], float)

np.dot(b,a)


# In[36]:


a.dot(b)


# In[37]:


#Producto de matrices
a = np.array([[5,2],[4,8]], float)
b = np.array([[2,4],[5,3]], float)

print(a, "\n ----------------")
print(b, "\n ----------------")


# In[38]:


np.dot(a,b)


# In[39]:


a @ b


# In[42]:


a = np.array([[0,1,4],[5,2,3],[1,4,8]], float)
b = np.array([2,3,5], float)

print(b,"\n---------------------")
print(a,"\n---------------------")


# In[ ]:





# In[43]:


np.dot(a,b)


# In[44]:


b @ a


# In[45]:


print(np.matmul(a,b))


# In[46]:


#Determinante de una matriz

a=np.array([[8,5],[3,4]])
print(a, "\n-------------------")

np.linalg.det(a)


# In[47]:


#Autovalores y autovectores

vals, vecs = np.linalg.eig(a)
print(vals, "\n-----------")
print(vecs, "\n-----------")


# # VIDEO NUMERO 05
# FUNCIONES UNIVERSALES UNARIAS
# #Realizan operaciones elemento a
# elemento de un array
# #las funciones unarias comprende las 
# operaciones que recibe un solo array como argumento
# ![image-2.png](attachment:image-2.png)

# In[49]:


import numpy as np
a = np.array([2,4,9], float)


# In[50]:


a


# In[51]:


np.sqrt(a)


# In[52]:


np.exp(a)


# In[53]:


np.log(a)


# In[54]:


np.sin(a)


# In[55]:


np.cos(a)


# In[56]:


np.mean(a)


# In[57]:


np.std(a)


# In[58]:


np.var(a)


# # VIDEO NUMERO 6
# FUNCIONES UNIVERSALES BINARIAS. 
# Tomas dos arrays, y devuelven un arrays o mas
# ![image.png](attachment:image.png)

# In[ ]:


import numpy as np


# In[59]:


arr = np.array([5,36,17,18,9])
arr_2=np.array([8,24,17,19,9])


# In[60]:


np.add(arr, arr_2)


# In[61]:


np.subtract(arr, arr_2)


# In[62]:


np.multiply(arr, arr_2)


# In[63]:


np.divide(arr,arr_2)


# In[65]:


np.array_equal(arr,arr_2)


# In[66]:


np.fmin(arr, arr_2)


# In[68]:


np.fmax(arr, arr_2)


# # VIDEO 07
# AGREGAR O QUITAR VALORES A UN ARRAY
#  (X      Y)
# FILAS/COLUMNAS

# In[69]:


import numpy as np

arr = np.arange(0,20,2)
arr


# In[82]:


arr_flot = np.random.rand(4,3)
arr_flot


# In[80]:


arr_ent = np.random.randint(100, size=(2,3))
arr_ent
#NUMEROS ENTEROS/ 
#NUMEROS ALEATORIOS HASTA 10
#TAMAÑO DE LA MATRIZ


# In[81]:


arr_6 = np.full((3,3),6) 
#INDICAMOS TAMAÑO DE MATRIZ
#MATRIZ DEFINIDA POR EL NUMERO 6
arr_6


# In[76]:


np.append(arr, [12,13,14,51])
#SE AGREGAN LOS VALORES AL FINAL DEL ARREGLO


# In[77]:


np.insert(arr,2,[42,34])
#AGREGAR VALORES EN CUALQUIER POSICION
# ARRAY / POSICION A MODIFICAR / VALORES A AGREGAR


# In[79]:


np.insert(arr_6, 2,[1,2,4])


# In[84]:


np.delete(arr_ent,1,axis=0)
#columnas o final / define si horizontal o vertical


# # VIDEO 8 TRANSFORMACIONES
# 

# In[111]:


# AS TYPE / Permite modificar los valores de un array
import numpy as np

arr_ent = np.random.randint(100, size=(3,4))
arr_ent


# In[86]:


arr_ent.astype(float)


# In[112]:


#SORT / ordena los valores del arrays
arr_ent


# In[88]:


arr_ent.sort()
arr_ent


# In[89]:


arr_ent.sort(axis=0)
arr_ent 


# In[96]:


#RESHAPE / Permite modificar dimensiones
arr_ent


# In[102]:


arr_ent = arr_ent.reshape(6,2)
arr_ent


# In[92]:


#FLATTEN / Crea aray unidimencional del original / PLANAR
plano_arr = arr_ent.flatten()

print(arr_ent)
print(plano_arr)


# In[93]:


#TOLIST / Crea una lista apartir de un array
lista_arr = plano_arr.tolist()
lista_arr


# In[114]:


# SEPARAR Y JUNTAR ARRAYS
arrays=np.split(arr_ent,3)
arrays


# In[115]:


np.concatenate((arrays[1],arrays[0]), axis=0)
#0 verticalmente
#1 horizontalmente


# In[116]:


#Matriz transpuesta
t_arr = arr_ent.T
t_arr
# primera columna, se vuelve la primer fila


# # VIDEO 9 INDEXACION Y SLICING
# Slicing(filtrado) [i:j:k]
# i: indice inicial
# j: indice de parada
# k: incremento(step) no nulo

# In[117]:


import numpy as np
a = np.array(range(64)).reshape((8,8))
a


# In[119]:


a[1,1]
#fila/elemento con indice 1


# In[121]:


a[0:7:2,0:4]
#selecione desde fila 0 hasta fila con indice 7
#de dos en dos, elementos de filas


# In[125]:


a[1,3:5]


# In[127]:


a[[1,3,5],[3,6,7]]


# In[126]:


a[[1,3,5],::3]


# In[128]:


#INDECCION BOLEANA
data = np.arange(8)
data


# In[129]:


data < 4


# In[130]:


data[data<4]


# In[132]:


data[np.array([True,  True,  True,  True, False, False, False, False])]


# In[133]:


amigos = np.array(['giulia','victor','johel','andreina','valentina','albert','roque'])


# In[134]:


'giulia' in amigos


# In[137]:


amigos[amigos!='giulia']


# In[ ]:




