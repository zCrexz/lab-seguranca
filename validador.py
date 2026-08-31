def validar_senha(senha):
    if len(senha) < 8:
        return "Alerta de Seguranca: Senha muito curta (minimo 8 caracteres)."
    return "Senha atende aos requisitos minimos."

print(validar_senha("12345678"))