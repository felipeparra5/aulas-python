import random

baralho = [1,2,3,4,5,6,7,8,9,10,10,10]

def dar_cartas():
    listaElementos = [[baralhos]]
    print(random.choice([listaElementos]))
    print(listaElementos)

print("\nBEM-VINDO(A) AO 21")

p1 = str(input("""\nDIGITE
                \n[1] PARA JOGAR
       \n[2] PARA SAIR
       \n"""))
p2 = 0
if p1 == "1":
    print("INICIANDO\n")
elif p1 == "2":
    print("SAINDO\n")
while p1 != "2":
        print("Sua carta é", random.choice(baralho))
        while p2 != "não":
            p2 = str(input("Você quer mais cartas?\n"))
            print("Sua carta é", random.choice(baralho))
        else:
            break           
else:
    pass