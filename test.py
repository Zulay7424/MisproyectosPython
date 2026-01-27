def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32
c = float(input("Introduce la temperatura en grados Celsius: "))
f = celsius_a_fahrenheit(c)
print(f"{c} grados Celsius equivalen a {f} grados Fahrenheit.")