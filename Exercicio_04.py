import re

def valida_idade(idade):
    """
    Verifica se a idade está entre 18 e 65 anos.
    """
    if 18 <= idade <= 65:
        return True
    else:
        return False

def valida_email(email):
    """
    Verifica se o email fornecido é válido usando uma expressão regular.
    Um email válido deve seguir o formato básico: 'algumacoisa@dominio.com'.
    """
    # Expressão regular básica para validar email
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(padrao_email, email):
        return True
    else:
        return False

def main():
    try:
        # Solicita ao usuário que insira a idade
        idade = int(input("Digite sua idade: "))
        
        # Solicita ao usuário que insira o email
        email = input("Digite seu email: ")

        # Valida idade e email
        if not valida_idade(idade):
            print("Erro: Idade deve estar entre 18 e 65 anos.")
        elif not valida_email(email):
            print("Erro: Email inválido.")
        else:
            print("Dados de usuário válidos.")
    
    except ValueError:
        print("Erro: A idade deve ser um número inteiro.")

if __name__ == "__main__":
    main()
