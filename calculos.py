def calcular_cuadrados(lista):
    """Calcula el cuadrado de cada número en una lista.

    Args:
        lista (list): Lista de números. Puede contener enteros o números de punto flotante.

    Returns:
        list: Una nueva lista con el cuadrado de cada elemento de la lista original.

    Example:
        >>> calcular_cuadrados([2, 3, 4])
        [4, 9, 16]
    """
    return [n**2 for n in lista]


def process_text(text):
    """Recibe un texto, elimina los signos de puntuación, lo convierte a minúsculas
    y lo divide en una lista de palabras.
    
    Args:
        text (str): Texto a procesar.
    
    Returns:
        list: Lista de palabras en minúsculas sin signos de puntuación.
    
    Example:
        >>> process_text("¡Hola! ¿Cómo estás? Estoy bien, gracias.")
        ['hola', 'cómo', 'estás', 'estoy', 'bien', 'gracias']
    """
    import re
    
    # 1. Convertir a minúsculas
    text_lower = text.lower()
    
    # 2. Eliminar signos de puntuación
    #    Usamos una expresión regular que retira todo lo que no sea letra, número o espacio
    text_clean = re.sub(r'[^a-z0-9áéíóúüñ\s]', '', text_lower)
    
    # 3. Dividir el texto en palabras
    #    Separa por cualquier cantidad de espacios en blanco
    words = re.split(r'\s+', text_clean.strip())
    
    return words