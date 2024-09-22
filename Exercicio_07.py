def normalizar_lista(numeros):
    """
    Esta função recebe uma lista de números e retorna uma nova lista com os números normalizados entre 0 e 1.
    """
    minimo = min(numeros)  # Encontra o menor valor da lista
    maximo = max(numeros)  # Encontra o maior valor da lista

    # Verifica se o máximo e o mínimo são iguais (evita divisão por zero)
    if maximo == minimo:
        return [0.0] * len(numeros)  # Se todos os números forem iguais, todos os normalizados serão 0

    # Aplica a fórmula de normalização em cada número
    numeros_normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]
    
    return numeros_normalizados

def main():
    # Exemplo de lista de números
    numeros = [5, 10, 15, 20, 25]

    # Normaliza a lista
    numeros_normalizados = normalizar_lista(numeros)

    # Exibe os números normalizados
    print("Lista de números normalizados:")
    print(numeros_normalizados)

if __name__ == "__main__":
    main()
