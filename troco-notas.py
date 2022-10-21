preco = int (input('Digite o valor: '))
dinheiro = int(input('Digite o troco: '))

troco = dinheiro - preco

for notas in [100, 50, 20, 10, 5, 1]:
  if troco >= notas:
    qtd_notas = troco // notas
    novo_valor = preco - dinheiro * qtd_notas
    print('%s notas(s) de R$ %s' %(qtd_notas,notas))

  else:
    print ('O dinheiro entregue é menor que a compra')
