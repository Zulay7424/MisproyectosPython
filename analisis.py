import random
import matplotlib.pyplot as plt
from statistics import mean, median

# 1. Generar los 10 números aleatorios que pide el curso
numeros = [random.randint(1, 100) for _ in range(10)]

# 2. Calcular los datos estadísticos
m_media = mean(numeros)
m_mediana = median(numeros)

# 3. Mostrar los resultados en la terminal
print(f"Lista de números: {numeros}")
print(f"La media es: {m_media}")
print(f"La mediana es: {m_mediana}")

# 4. Crear y mostrar el gráfico de barras
plt.bar(range(len(numeros)), numeros, color='skyblue')
plt.title('Análisis de Datos - Ejercicio C')
plt.xlabel('Posición del número')
plt.ylabel('Valor')
plt.show()