import matplotlib.pyplot as plt

productos = ['Laptop', 'Mouse', 'Monitor', 'Teclado'] 
ingresos = [12500, 2800, 6200, 3500]

print("--- GENERANDO REPORTE FINAL ---")

plt.figure(figsize=(8, 5)) 
plt.bar(productos, ingresos, color='teal')
plt.title('Ventas Totales - Ingeniera Zulay') 
plt.show()