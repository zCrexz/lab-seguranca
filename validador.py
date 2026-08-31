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