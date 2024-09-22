def extrair_numeros_pares(numeros):
    """
    Esta função recebe uma lista de números e retorna uma lista contendo apenas os números pares.
    """
    return [num for num in numeros if num % 2 == 0]

def main():
    # Exemplo de lista de números
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Extrai os números pares da lista
    numeros_pares = extrair_numeros_pares(lista_numeros)

    # Exibe os números pares
    print("Números pares na lista:")
    print(numeros_pares)

if __name__ == "__main__":
    main()
