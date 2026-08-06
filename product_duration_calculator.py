def calcular_duracao_dias(total_porcoes, porcoes_por_dia):
    """Calcula quantos dias um produto dura dado o consumo diário em porções."""
    if porcoes_por_dia <= 0:
        raise ValueError("Porções por dia deve ser maior que zero.")
    if total_porcoes < 0:
        raise ValueError("Total de porções não pode ser negativo.")
    return total_porcoes / porcoes_por_dia


def main():
    total_porcoes = float(input("Quantas porções o produto tem no total? "))
    porcoes_por_dia = float(input("Quantas porções serão usadas por dia? "))

    dias = calcular_duracao_dias(total_porcoes, porcoes_por_dia)
    dias_inteiros = int(dias)
    dias_fracao = dias - dias_inteiros

    print(f"\nO produto vai durar aproximadamente {dias:.1f} dias.")
    if dias_fracao > 0:
        print(f"({dias_inteiros} dias completos + uma última porção parcial)")


if __name__ == "__main__":
    main()
