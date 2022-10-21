soma = 0

lista_de_notas = [nota1, nota2, nota3, nota4]

print(f"A lista das notas é: {lista_de_notas}")
print(f"Vamos somar...\n")

for i in range(4):
    print(f"Por enquanto, a soma das notas é {soma}")

    print(f"Agora vamos somar {lista_de_notas[i]}\n")
    soma = soma + lista_de_notas[i]


print(f"Somamos todas as notas!\nA soma é {soma:.2f}\nE a média é {soma/4:.2f}")