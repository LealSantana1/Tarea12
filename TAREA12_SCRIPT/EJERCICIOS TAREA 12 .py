#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ejercicio 1
import numpy as np
import matplotlib.pyplot as plt
muestra = np.random.normal(60, 15, 1000)
plt.hist(muestra, bins=30, alpha=0.7, color='green')
plt.title("Histograma de la distribución normal")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.show()
media = np.mean(muestra)
desviacion_estandar = np.std(muestra)
# resultados
print("Media:", media)
print("Desviación Estándar:", desviacion_estandar)



# In[24]:


#EJERCICIO 3
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
media = 75
desviacion_estandar = 8
n = 500

muestra = np.random.normal(loc=media, scale=desviacion_estandar, size=n)

media_muestra = np.mean(muestra)
desviacion_muestra = np.std(muestra, ddof=1)  

error_estandar = desviacion_muestra / np.sqrt(n)
intervalo_confianza = stats.t.interval(0.95, df=n-1, loc=media_muestra, scale=error_estandar)
plt.figure(figsize=(8, 6))
plt.hist(muestra, bins=30, alpha=0.7, color='black', edgecolor='black')
plt.axvline(x=media_muestra, color='red', linestyle='dashed', linewidth=2, label=f'Media de la muestra = {media_muestra:.2f}')
plt.axvline(x=intervalo_confianza[0], color='green', linestyle='dashed', linewidth=2, label=f'Limite inferior IC = {intervalo_confianza[0]:.2f}')
plt.axvline(x=intervalo_confianza[1], color='green', linestyle='dashed', linewidth=2, label=f'Limite superior IC = {intervalo_confianza[1]:.2f}')

plt.title('Distribución de la muestra y el intervalo de confianza al 95%')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()
print(f"El intervalo de confianza al 95% para la media de la muestra es: ({intervalo_confianza[0]:.2f}, {intervalo_confianza[1]:.2f})")


# In[20]:


#EJERCICIO 5
import numpy as np
import matplotlib.pyplot as plt
muestra = np.random.normal(loc=100, scale=20, size=100)
percentil_90 = np.percentile(muestra, 90)
print(f"El percentil 90 de la muestra es: {percentil_90:.2f}")
print("\nInterpretación:")
print(f"El percentil 90 significa que el {percentil_90:.2f}% de los valores de la muestra son menores o iguales a {percentil_90:.2f}.")
plt.hist(muestra, bins=15, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(percentil_90, color='red', linestyle='dashed', linewidth=2, label=f'Percentil 90: {percentil_90:.2f}')

plt.title("Histograma de la muestra generada")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")

plt.legend()
plt.show()


# In[22]:


#EJERCICIO 7 
import numpy as np
import matplotlib.pyplot as plt

muestra = np.random.normal(loc=0, scale=1, size=1000)
valores_entre_menos1_y_1 = np.sum((muestra >= -1) & (muestra <= 1))
porcentaje = (valores_entre_menos1_y_1 / len(muestra)) * 100
print(f"Porcentaje de valores entre -1 y 1: {porcentaje:.2f}%")

if 65 <= porcentaje <= 71:
    print("El porcentaje está aproximadamente cerca del 68%, como se espera para la distribución normal estándar.")
else:
    print("El porcentaje no es cercano al 68%, algo podría estar mal.")
plt.figure(figsize=(10, 6))
plt.hist(muestra, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

plt.axvline(x=-1, color='red', linestyle='dashed', linewidth=2, label='x = -1')
plt.axvline(x=1, color='red', linestyle='dashed', linewidth=2, label='x = 1')
x_values = np.linspace(-1, 1, 100)
y_values = (1/np.sqrt(2 * np.pi)) * np.exp(-0.5 * x_values**2)  # Función de densidad normal
plt.fill_between(x_values, y_values, color='red', alpha=0.3, label="Área entre -1 y 1")
plt.title("Histograma de la Distribución Normal Estándar")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.legend()

plt.show()


# In[23]:


#EJERCICIO 9 
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
muestra = np.random.normal(loc=60, scale=10, size=150)

muestra_transformada = (muestra - np.mean(muestra)) / np.std(muestra)

media_transformada = np.mean(muestra_transformada)
desviacion_transformada = np.std(muestra_transformada)

print(f"Media de la muestra transformada: {media_transformada:.4f}")
print(f"Desviación estándar de la muestra transformada: {desviacion_transformada:.4f}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.hist(muestra, bins=20, color='skyblue', edgecolor='black')
plt.title('Histograma de la Muestra Original')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

plt.subplot(1, 2, 2)
plt.hist(muestra_transformada, bins=20, color='salmon', edgecolor='black')
plt.title('Histograma de la Muestra Transformada')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

plt.tight_layout()
plt.show()



# In[ ]:




