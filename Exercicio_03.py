def filtra_mensagem_erro(log):
    """
    Esta função verifica se o nível de severidade é 'ERROR' e imprime a mensagem correspondente.
    """
    if log.get('level') == 'ERROR':
        print(log.get('message'))

# Exemplo de log
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# Chama a função para verificar e imprimir a mensagem se o nível for 'ERROR'
filtra_mensagem_erro(log)
