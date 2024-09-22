def filtrar_usuarios_com_campo_faltando(usuarios, campo):
    """
    Esta função recebe uma lista de dicionários representando usuários e um campo específico.
    Retorna uma lista filtrada contendo apenas os usuários que possuem o campo.
    """
    return [usuario for usuario in usuarios if campo in usuario]

def main():
    # Exemplo de lista de dicionários representando usuários
    usuarios = [
        {'nome': 'João', 'idade': 28, 'email': 'joao@example.com'},
        {'nome': 'Maria', 'idade': 22},  # Faltando o campo 'email'
        {'nome': 'Pedro', 'idade': 35, 'email': 'pedro@example.com'},
        {'nome': 'Ana'},  # Faltando o campo 'idade' e 'email'
        {'nome': 'Lucas', 'idade': 30, 'email': 'lucas@example.com'}
    ]

    # Campo que queremos verificar se está faltando
    campo_faltando = 'email'

    # Filtra os usuários que têm o campo 'email' faltando
    usuarios_filtrados = filtrar_usuarios_com_campo_faltando(usuarios, campo_faltando)

    # Exibe os usuários que possuem o campo 'email'
    print(f"Usuários com o campo '{campo_faltando}' presente:")
    for usuario in usuarios_filtrados:
        print(usuario)

if __name__ == "__main__":
    main()
