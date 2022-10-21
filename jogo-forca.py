palavra = "banana"
vidas = 5

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

    palpite = input("Adivinhe uma letra: ")
    print(f"Adivinhou = {adivinhou}")

    letras_usadas.append(palpite)

    if not palpite in palavra:
      print(f'A palavra não tem = {palpite}')
      vidas -= 1
      print(f"voce perdeu 1 vida, você tem: {vidas} ")
      if vidas == 0:
        print (f"O jogo acabou, a palavra era {palavra} ")
        break

    if palpite in palavra:
      print(f'A palavra tem a letra: {palpite}')