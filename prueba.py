# Definir el nombre del curso
nombre_curso = "Curso de Cursor"

# Crear una lista de frutas
frutas = ["manzana", "banana", "cereza"]
print(frutas)

# Solicitar la edad al usuario y calcular la edad en 10 años
edad = int(input("¿Cuál es tu edad? "))
edad_en_diez = edad + 10
print(f"En diez años tendras: {edad_en_diez}")

# Pedir al usuario su ciudad preferida y mostrar un mensaje
ciudad = input("¿En qué ciudad te gustaría vivir? ")
frase = f"Que lindo debe ser vivir en {ciudad}"
print(frase)
# Fin de la practica de Zulay

# Calcular días vividos de forma precisa
from datetime import date

print("\n" + "="*50)
print("CALCULADORA DE DÍAS VIVIDOS")
print("="*50)

# Pedir fecha de nacimiento
anio_nacimiento = int(input("\n¿En qué año naciste? (ejemplo: 2000) "))
mes_nacimiento = int(input("¿En qué mes naciste? (1-12) "))
dia_nacimiento = int(input("¿Qué día naciste? (1-31) "))

fecha_nacimiento = date(anio_nacimiento, mes_nacimiento, dia_nacimiento)
fecha_actual = date.today()

# Calcular diferencia exacta
dias_vividos = (fecha_actual - fecha_nacimiento).days
anos_vividos = edad  # usando la edad que ya ingresaste

# Comparar métodos
dias_aproximados = anos_vividos * 365
diferencia = dias_vividos - dias_aproximados

print("\n" + "="*50)
print(f"Fecha de nacimiento: {fecha_nacimiento.strftime('%d/%m/%Y')}")
print(f"Fecha actual: {fecha_actual.strftime('%d/%m/%Y')}")
print("="*50)
print(f"\n✅ DÍAS VIVIDOS EXACTOS: {dias_vividos:,} días")
print(f"📊 Aproximación (edad × 365): {dias_aproximados:,} días")
print(f"⚠️  Diferencia: {diferencia} días")
print(f"\n💡 Como ves, multiplicar {anos_vividos} × 365 = {dias_aproximados:,}")
print(f"   pero en realidad has vivido {dias_vividos:,} días")
print(f"   (la diferencia incluye años bisiestos y días desde tu cumpleaños)")










