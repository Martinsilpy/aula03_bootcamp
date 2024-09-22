def verifica_transacao_suspeita(transacao):
    """
    Esta função verifica se uma transação é suspeita com base no valor e no horário.
    Uma transação é suspeita se:
    - O valor for maior que 10.000.
    - O horário for antes das 9h ou depois das 18h.
    """
    valor = transacao.get('valor')
    hora = transacao.get('hora')

    # Verifica se o valor é superior a 10.000 ou se está fora do horário comercial
    if valor > 10000 or hora < 9 or hora > 18:
        return True
    else:
        return False

def main():
    # Exemplo de transação
    transacao = {'valor': 12000, 'hora': 20}

    # Verifica se a transação é suspeita
    if verifica_transacao_suspeita(transacao):
        print("Transação suspeita.")
    else:
        print("Transação normal.")

if __name__ == "__main__":
    main()
