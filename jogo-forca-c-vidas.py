palavra = 'banana'
vidas = 0

#letras_usadas = ['m','a','u','t','e']
letras_usadas = []
adivinhou = False
while not adivinhou:
    adivinhou = True
    mostra = ""
    for letra in palavra:
      if letra in letras_usadas:
        mostra += letra
      else:
        adivinhou = False
        mostra += "_ "
    print(mostra)

    palpite = input('Adivinhe uma letra: ')
    print(f'adivinou {adivinhou}')

    letras_usadas.append(palpite)
  
    if not palpite in palavra:
        print(f'A palavra não tem = {palpite}')
        vidas += 1
        print(f'você errou {vidas} vezes, o limite é 7')
        if vidas == 7:
          print(f'acabou o jogo, a palavra era : {palavra}')
          break

    if  palpite in palavra:
        print(f'A palavra tem {palpite}')