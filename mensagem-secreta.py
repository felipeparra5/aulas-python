codigo = dict(zip("tenis" + "polar", "polar" "tenis"))

"m" in codigo

mensagem = "mensagem secreta"
resultado = ""

for letra in mensagem:

  if not letra in codigo:
    resultado += letra
  else:
    resultado += codigo[letra]

resultado