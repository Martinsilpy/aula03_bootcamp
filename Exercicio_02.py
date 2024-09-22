def classifica_temperatura(temperatura):
    """
    Esta função classifica a temperatura em 'Baixa', 'Normal' ou 'Alta'.
    """
    if temperatura < 15:
        return "Baixa"
    elif 15 <= temperatura <= 25:
        return "Normal"
    else:
        return "Alta"

def main():
    while True:
        try:
            # Solicita ao usuário que insira a leitura da temperatura
            entrada = input("Digite a temperatura medida (ou 'Q' para sair): ")

            if entrada.upper() == 'Q':
                print("Saindo do programa...")
                break

            # Converte a entrada para um número de ponto flutuante
            temperatura = float(entrada)

            # Classifica a temperatura usando a função classifica_temperatura
            classificacao = classifica_temperatura(temperatura)

            # Exibe o resultado da classificação
            print(f"A temperatura de {temperatura}°C é classificada como: {classificacao}")

        except ValueError:
            print("Entrada inválida! Certifique-se de que você digitou um número válido para a temperatura.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
