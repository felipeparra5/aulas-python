movendo = input('ta se movendo? ')

if movendo == 'não':
  deveria = input('deveria? ')
  if deveria == 'não':
    print ('Perfeito')
  elif deveria == 'sim':
    print ('Use wd')
  else:
   print('escreva se deveria  :')

if movendo == 'sim':
  deveria = input('deveria? ')
  if deveria == 'sim':
    print('Perfeito')
  if deveria == 'não':
    print('use fita')

