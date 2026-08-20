DESCONTOS_POR_FORMA_PAGAMENTO = {
    "p": 10,  # Pix
    "d": 5,   # Débito
    "c": 0,   # Crédito
}


def calcular_preco_final(preco_original, forma_pagamento):
    """Calcula o preço final aplicando o desconto da forma de pagamento (p/d/c)."""
    if preco_original < 0:
        raise ValueError("Preço original não pode ser negativo.")
    if forma_pagamento not in DESCONTOS_POR_FORMA_PAGAMENTO:
        raise ValueError("Forma de pagamento inválida.")

    desconto_percentual = DESCONTOS_POR_FORMA_PAGAMENTO[forma_pagamento]
    preco_final = preco_original * (1 - desconto_percentual / 100)
    return preco_final, desconto_percentual


MAX_TENTATIVAS = 3


def main():
    for tentativa in range(1, MAX_TENTATIVAS + 1):
        preco_original = float(input("Qual o preço do produto? "))
        forma_pagamento = input(
            "Qual a forma de pagamento? Pix(p), Débito(d), Crédito(c) "
        ).strip().lower()

        try:
            preco_final, desconto_percentual = calcular_preco_final(
                preco_original, forma_pagamento
            )
        except ValueError:
            print("Forma de pagamento inválida.\n")
            continue

        print(f"Preço original: R$ {preco_original:.2f}")
        print(f"Desconto aplicado: {desconto_percentual}%")
        print(f"Preço final: R$ {preco_final:.2f}")
        return

    print("Número máximo de tentativas excedido. Procure a central de atendimento no 0800 000 123.")


if __name__ == "__main__":
    main()
