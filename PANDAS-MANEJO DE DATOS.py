#!/usr/bin/env python
# coding: utf-8

# # VIDEO 09 MANEJO DE DATOS AUSENTES
# 
# NaN y Nose son valores ausentes / pandas.isnull() determina si existen valores ausentes en los datos
# #### Maigualida Lizet Rangel Serrano 1951

# In[ ]:


import numpy as np
import pandas as pd

df = pd.DataFrame({
    'VarA':['aa', None, 'cc'],
    'VarB':[20, 30, None],
    'VarC':[1234, 3456, 6789]
    },
    index = ['Caso1','Caso2','Caso3']
)

df


# In[ ]:


pd.isnull(df)


# In[ ]:


#Decidir que hacer con los valores nulos
#Descartar filas con numeros ausentes
df.dropna(subset=["VarA",'VarB'])


# In[ ]:


#Sustituir valores nulos con un valor determinado
df.fillna("")


# In[ ]:


df.fillna(df.mean())


# In[ ]:


df.fillna(25)


# # VIDEO 10 MUESTRAS ALEATORIAS

# In[ ]:


import numpy as np
import pandas as pd

def CrearDataSet(Number=1):
    Output = []
    for i in range(Number):
        #Crear un rango de fechas semanal
        rng = pd.date_range(start='1/1/2016', end='12/31/2020', freq='W-MON')
        
        #crear valores aleatorios
        data = np.random.randint(low=25,high=1000,size=len(rng))
        
        #Estatus posible
        status = [1,2,3]
        
        #lista de estatus aleatorios
        random_status = [status[np.random.randint(low=0,high=len(status))] for i in range(len(rng))]
        
        #estatus posibles
        states = ['Libertador','El Hatillo','El hatillo','Chacao', 'Baruta','Sucre']
        
        #Crear una lista aleatoria de estatus
        random_states = [states[np.random.randint(low=0,high=len(states))] for i in range (len(rng))]
        
        Output.extend(zip(random_states, random_status, data, rng))
    return Output
        
        


# In[ ]:


dataset = CrearDataSet(4)

df = pd.DataFrame(data=dataset,columns=['Local', 'Estatus_local', 'Cantidad_Clientes', 'Fecha_Status'])
df


# In[ ]:


filas = np.random.choice(df.index, 10, replace = False)
filas


# In[ ]:


df.loc[filas]


# # VIDEO 11 LECTURA DE FICHEROS DE DATOS
# 
# Nos permite leer/escribir en varrios formatos .csv, .txt, .xlsx .json, .etc
# ###### read_csv() / read_excel()
# 

# In[ ]:


import numpy as np
import pandas as pd

datos = {
    'CHIN': {'COUNTRY': 'China', 'POP': 1_398.72, 'AREA': 9_596.96,
            'GDP': 12_234.78, 'CONT': 'Asia'},
    'IND': {'COUNTRY': 'India', 'POP': 1_351.16, 'AREA': 3_287.26,
            'GDP': 2_575.67, 'CONT': 'Asia', 'IND_DAY': '1947-08-15'},
    'USA': {'COUNTRY': 'ChUSina', 'POP': 329.74, 'AREA': 9_833.52,
            'GDP': 19_485.39, 'CONT': 'N.America', 'IND_DAY': '1776-07-04'},
    'IDN': {'COUNTRY': 'Indonesia', 'POP': 268.07, 'AREA': 1_910.83,
            'GDP': 1_015.24, 'CONT': 'Asia', 'IND_DAY': '1945-08-17'},
    'BRA': {'COUNTRY': 'Brasial', 'POP': 210.32, 'AREA': 8_515.77,
            'GDP': 2_055.21, 'CONT': 'S.America', 'IND_DAY': '1822-09-07'}
    
}
columnas = ('COUNTRY','POP','AREA','GDP','CONT','IND_DAY')


# In[ ]:


df = pd.DataFrame(data=datos, index=columnas)
#Convierte o transforma ah matriz transpuesta
df


# In[ ]:


df = pd.DataFrame(data=datos, index=columnas).T
#Convierte o transforma ah matriz transpuesta
df


# In[ ]:


#PERMITE CREAR EL FRAME EN UN CSV
df.to_csv('datos.csv')


# In[ ]:


#LEER EL CSV
df2 = pd.read_csv('datos.csv')
df2.head()


# In[ ]:


df2 = pd.read_csv('datos.csv', index_col=0)
df2.head()


# In[ ]:


df.to_csv('nuevos_datos.csv',header=True, na_rep='(missing)')


# In[ ]:


df2 = pd.read_csv('nuevos_datos.csv',
                  index_col=0,
                 na_values='(missing)')
df2


# In[ ]:


df2 = pd.read_csv('nuevos_datos.csv')
                  #index_col=0,
                 #na_values='(missing)')
df2


# In[ ]:


df2.dtypes


# In[ ]:


ti_da = {'POP': 'float32', 'AREA': 'float32', 'GDP': 'float32'}

df3 = pd.read_csv('datos.csv',
                 index_col=0,
                 parse_dates=['IND_DAY'],
                 dtype = ti_da)
df3.dtypes 


# In[ ]:


df3.IND_DAY


# In[ ]:


#como almacenara la columna de tiempo
#%B nombre mes completo/%d dia de mes / %Y año
df3.to_csv('datos-fechas-format.csv', date_format='%B %d, %Y')


# In[ ]:


df4 = pd.read_csv('datos-fechas-format.csv',
                 index_col=0
                 )
df4


# In[ ]:


df5 = pd.read_csv('datos.csv',
                  index_col=0,
                  usecols=[0,1,3,5]
                 )
df5


# In[ ]:


df5 = pd.read_csv('datos.csv',
                  usecols=[1,3,5],
                  index_col=0
                 )
df5


# In[ ]:


#comprimir archivos y exportarlos a un zip
df.to_csv('datos.csv.zip')


# In[ ]:


df = pd.read_csv('datos.csv.zip', index_col=0, parse_dates=['IND_DAY'])
df


# In[ ]:


#Exportar a hoja de excel
#sheet_name / nombre de hoja
df.to_excel('data.xlsx', sheet_name='paises')
print('listo')


# In[ ]:


df = pd.read_excel('data.xlsx', sheet_name='paises',
                  index_col=0,
                  parse_dates=['IND_DAY'])
df


# # VIDEO 12 COMBINACION DE CONJUNTOS DE DATOS
# 
# ![image.png](attachment:image.png)

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


clima_p=pd.read_csv(r'C:\Users\maigu\ACTIVIDAD 3 Y 4 PYTHON\ar\029 ny_precipitaciones.csv')
clima_p.shape
#dataframe de 2000 filas * 13 columnas


# In[ ]:


clima_p.head()


# In[ ]:


clima_t = pd.read_csv(r'C:\Users\maigu\ACTIVIDAD 3 Y 4 PYTHON\ar\029 ny_temperaturas.csv')
clima_t.shape


# In[ ]:


#subconjunto de ellos, serie de pandas con todos los nombres

clima_t.NAME


# In[ ]:


#serie de pandas con valores booleanos
clima_p["NAME"] == "ITHACA CORNELL UNIVERSITY, NY US"


# In[ ]:


clima_p[clima_p["NAME"] == "ITHACA CORNELL UNIVERSITY, NY US"]


# In[ ]:


precip_itaca = clima_p[clima_p["NAME"] == "ITHACA CORNELL UNIVERSITY, NY US"]
precip_itaca.shape

#filas / columnas


# In[ ]:


#inner join entre ambos dataframes
itaca_inner_merge = pd.merge(precip_itaca, clima_t)
itaca_inner_merge.shape


# In[ ]:


itaca_inner_merge.head()


# In[ ]:


#Outer join / podemos especificar la clase de join
itaca_outer_merge = pd.merge(precip_itaca, clima_t, how="outer", on=["STATION", "DATE"])
itaca_outer_merge.columns


# In[ ]:


itaca_outer_merge.shape


# In[ ]:


itaca_outer_merge.head(15)


# In[ ]:


#left join 
itaca_left_merge = pd.merge(precip_itaca, clima_t,
                        how="left", on=["STATION", "DATE"])
itaca_left_merge.shape


# In[ ]:


itaca_left_merge.head()


# In[ ]:


#Right join 
itaca_right_merge = pd.merge(clima_t, precip_itaca, 
                        how="right", on=["STATION", "DATE"])
itaca_right_merge.shape


# # VIDEO 13 COMBINACION DE CONJUNTOS DE DATOS II

# In[ ]:


#merge funcion del modulo pandas
#join union de dataframes a partir de indices


# In[ ]:


clima_join = clima_t.join(clima_p, lsuffix = '_left')
clima_join.head()


# In[ ]:


clima_join.columns


# In[ ]:


#permite mover una o mas columnas del dataframe a los indices
clima_p.set_index(["STATION", "DATE"])


# In[ ]:


clima_joined_total = clima_t.join(clima_p.set_index(["STATION", "DATE"]),
                                  lsuffix="_x",#subfijo
                                  rsuffix="_y",#subfijo
                                  on=["STATION", "DATE"], #que columnas van a servir para realizar el cruce
                                 )
clima_joined_total.head()


# In[ ]:


#CONCAT / juntar dataframes a traves de un eje, filas o columnas
#lista de nombre de variables a concatenar, axis o eje
clima_total_outer_concat = pd.concat([clima_t, clima_p], axis=1)
clima_total_outer_concat.head()


# In[ ]:


clima_total_outer_concat.tail()


# In[ ]:


clima_total_outer_concat = pd.concat([clima_t, clima_p], axis=0)
clima_total_outer_concat.shape


# In[ ]:


clima_total_outer_concat.head()


# In[ ]:


df_jerar = pd.concat([clima_t, clima_p], keys=["temp", "precip"])
df_jerar


# # VIDEO 14 FUNCION DE AGRUPACION

# In[18]:


import numpy as np
import pandas as pd

data = pd.read_csv(r'C:\Users\maigu\ACTIVIDAD 3 Y 4 PYTHON\ar\031 data_celular.csv',
                  header = 0,
                  index_col = 0,
                  names = ['indice', 'fecha', 'duracion', 'item', 'mes', 'red', 'tipo_red'],
                  parse_dates = ['fecha'])
data.head()


# In[19]:


print('cuantas filas tiene el DF:  ')
print(data['item'].count())


# In[20]:


print('el tiempo total (en segundos) registrado en llamadas es: ')
print(data['duracion'][data['item'] == 'call'].sum())


# In[21]:


print('con cuantas redes telefonicas se contacto en el periodo de 2014/11 al 2015/03:  ')
print(data['red'].nunique())


# In[22]:


#.GROUPBY() / AGRUPAR POR
data.groupby('mes')


# In[23]:


#.GROUPBY() / AGRUPAR POR
data.groupby('mes').groups.keys()


# In[24]:


data.groupby('mes').sum()


# In[25]:


print('en el siguiente cuadro vemos la cantidad de entradas por mes \n segregadas en llamadas, sms y datos: \n \n ', data.groupby(['mes','item'])["duracion"].count())


# In[26]:


print('la duracion total de llamadas realizadas a cada una de las operadoras es:  ')
data[data['item'] == 'call'].groupby('red')['duracion'].sum()


# In[27]:


print('¿cuantas llamadas, sms y datos son enviados a cada operadora por mes?:  ')
data.groupby(['mes','tipo_red'])['fecha'].count()


# # VIDEO 15 OPERACIONES SOBRE DATOS AGRUPADOS

# In[1]:


import numpy as np
import pandas as pd

ratings = pd.read_csv(r'C:\Users\maigu\ACTIVIDAD 3 Y 4 PYTHON\ar\032 ratings.csv')
peliculas = pd.read_csv(r'C:\Users\maigu\ACTIVIDAD 3 Y 4 PYTHON\ar\032 peliculas.csv')
usuarios = pd.read_csv(r'C:\Users\maigu\ACTIVIDAD 3 Y 4 PYTHON\ar\032 usuarios.csv')


# In[2]:


ratings.columns


# In[3]:


ratings.head()


# In[4]:


peliculas.columns


# In[5]:


peliculas.head()


# In[6]:


usuarios.columns


# In[7]:


usuarios.head()


# In[8]:


#
peli_ratings = pd.merge(peliculas, ratings)
clasif = pd.merge(peli_ratings, usuarios)


# In[9]:


mas_ratings = clasif.groupby('titulo').size().sort_values(ascending=False)[:25]
mas_ratings


# In[11]:


#agg / agregar o agregacion
peli_stats = clasif.groupby('titulo').agg({'rating': [np.size, np.mean]})
peli_stats.head()


# In[14]:


peli_stats.sort_values([('rating', 'mean')], ascending=False).head()


# In[15]:


minimo_100 = peli_stats['rating']['size'] >= 100


# In[17]:


minimo_100


# In[16]:


peli_stats[minimo_100].sort_values([('rating','mean')], ascending=False)[:15]


# In[ ]:




