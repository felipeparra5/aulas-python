conta = []

nome = input('Digite seu nome: ')
conta.append(nome)
idade = input('Digite sua idade: ')
conta.append(idade)
altura =float (input('Digite sua altura: '))

conta.append(altura)

peso = float(input('Digite seu peso: '))
conta.append(peso)

imc = peso / (altura**2)

print(f'\nSeu nome é: {conta[0]}\nSua idade é: {conta[1]}\nSua altura é: {conta[2]}\nSeu peso é: {conta[3]}\nSeu imc é: {imc:.1f}\n')  

if imc <= 18.5:
  print('Você está abaixo do peso')
elif imc >= 18.5 and imc <= 24.9:
  print('Seu peso está normal')
elif imc >= 25 and imc <= 29.9:
  print('Você tem sobrepeso')
elif imc >= 30 and imc <= 39.9:
  print('Você temm obesidade')
elif imc >= 40:
  print('Você tem obesidade grave')