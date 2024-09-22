def contar_palavras(texto):
    """
    Esta função recebe um texto e retorna um dicionário contendo a contagem de cada palavra única no texto.
    """
    # Remove pontuação e converte para minúsculas
    texto = texto.lower()
    palavras = texto.split()  # Divide o texto em palavras

    contagem = {}  # Dicionário para armazenar a contagem de palavras

    for palavra in palavras:
        # Se a palavra já estiver no dicionário, incrementa o valor
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1  # Caso contrário, adiciona a palavra com contagem 1

    return contagem

def main():
    # Solicita ao usuário que insira o texto
    texto = input("Digite um texto: ")

    # Conta as ocorrências de cada palavra
    contagem_palavras = contar_palavras(texto)

    # Exibe as palavras e suas contagens
    print("\nContagem de palavras:")
    for palavra, contagem in contagem_palavras.items():
        print(f"'{palavra}': {contagem} vez(es)")

if __name__ == "__main__":
    main()
