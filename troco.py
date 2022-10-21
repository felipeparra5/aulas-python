def devolve_notas(valor, nota):
    
    qtd_notas = valor // nota
    if qtd_notas > 0:
        print(f"{qtd_notas} notas de R${nota}")

    novo_valor = valor - qtd_notas * nota
    print(f"Sobrou {novo_valor}")    
    return novo_valor

    valor = devolve_notas(50, 100)