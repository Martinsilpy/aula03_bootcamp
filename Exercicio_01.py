def verifica_dados_vendas(quantidade, preco):
    if quantidade > 0 and preco > 0:
        return "Dados válidos"
    else:
        return "Dados inválidos"
    
def main():
    try:
        quantidade = float(input("Digite a quantidade: "))

        preco = float(input("Digite o preço: "))

        resultado = verifica_dados_vendas(quantidade, preco)

        print(resultado)

    except ValueError:
        print("Entrada inválida! Certifique-se de que você digitou números válidos para a quantidade e preço.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__=="__main__":
    main()
