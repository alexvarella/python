def proximo_numero(sequencia):
    """Retorna o próximo número de uma sequência tipo Fibonacci (soma dos dois últimos)."""
    if len(sequencia) < 2:
        raise ValueError("A sequência precisa ter pelo menos dois números.")
    return sequencia[-2] + sequencia[-1]


def _formatar(numero):
    return int(numero) if numero == int(numero) else numero


def main():
    entrada = input("Digite os números da sequência separados por vírgula: ")
    sequencia = [float(n) for n in entrada.split(",") if n.strip() != ""]

    resultado = proximo_numero(sequencia)
    print(f"\nO próximo número da sequência é: {_formatar(resultado)}")


if __name__ == "__main__":
    main()
