def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso >= 1:
        multa = valor_prestacao * (3/100)
        juros = valor_prestacao * dias_atraso * (0.1/100)
        multa_total = valor_prestacao + multa + juros
    else:
        multa_total = valor_prestacao
    return multa_total

valor_prestacao = float(input("Insira o valor da prestação: "))
dias_atraso = int(input("Insira os dias de atraso: "))

print(valorPagamento(valor_prestacao, dias_atraso))