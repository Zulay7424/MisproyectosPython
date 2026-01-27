"""Módulo para contar palabras en un texto."""
import re
from typing import Dict


class ContadorDePalabras:
    """Clase para contar y analizar la frecuencia de palabras en un texto."""

    def __init__(self, texto: str) -> None:
        """
        Inicializa el contador con un texto.

        Args:
            texto: El texto a analizar.
        """
        self.texto = texto
        self._frecuencia_palabras: Dict[str, int] = {}

    def _limpiar_texto(self) -> str:
        """
        Limpia el texto eliminando puntuación y convirtiendo a minúsculas.

        Returns:
            El texto limpio.
        """
        return re.sub(r'[^\w\s]', '', self.texto).lower()

    def _contar_palabras(self) -> None:
        """Cuenta la frecuencia de cada palabra en el texto."""
        texto_limpio = self._limpiar_texto()
        palabras = texto_limpio.split()

        for palabra in palabras:
            self._frecuencia_palabras[palabra] = (
                self._frecuencia_palabras.get(palabra, 0) + 1
            )

    def obtener_top_palabras(self, cantidad: int = 10) -> Dict[str, int]:
        """
        Obtiene las palabras más frecuentes ordenadas por frecuencia.

        Args:
            cantidad: Número de palabras top a retornar. Por defecto 10.

        Returns:
            Diccionario con las palabras más frecuentes y sus conteos.
        """
        if not self._frecuencia_palabras:
            self._contar_palabras()

        palabras_ordenadas = sorted(
            self._frecuencia_palabras.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return dict(palabras_ordenadas[:cantidad])

    def obtener_frecuencia_completa(self) -> Dict[str, int]:
        """
        Obtiene la frecuencia completa de todas las palabras.

        Returns:
            Diccionario con todas las palabras y sus conteos.
        """
        if not self._frecuencia_palabras:
            self._contar_palabras()

        return self._frecuencia_palabras.copy()


if __name__ == "__main__":
    texto_ejemplo = input("Introduce el texto que quieres analizar: ")
    contador = ContadorDePalabras(texto_ejemplo)
    print(contador.obtener_top_palabras())
 