import hashlib
import re


def avaliar_seguranca_senha(senha):
    if len(senha) < 8:
        return "FRACA: Menos de 8 caracteres."
    if not re.search(r"[A-Z]", senha):
        return "FRACA: Falta letra maiúscula."
    if not re.search(r"[0-9]", senha):
        return "FRACA: Falta número."
    if not re.search(r"[!@#$%^&*]", senha):
        return "MÉDIA: Falta caractere especial."

    # Boa prática de segurança: gerar o hash em vez de tratar em texto puro
    hash_senha = hashlib.sha256(senha.encode()).hexdigest()
    return f"FORTE | Hash SHA-256: {hash_senha[:16]}..."




print(avaliar_seguranca_senha("Senha@1234"))

SENHAS_BANIDAS = ["12345678", "senha123", "admin123"]

def validar_blacklist(senha):
    if senha in SENHAS_BANIDAS:
        return "ALERTA CRÍTICO: Senha exposta em vazamentos conhecidos!"
    return "OK: Senha não consta na blacklist."

print(validar_blacklist("12345678"))