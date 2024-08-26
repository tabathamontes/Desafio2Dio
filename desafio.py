def rank (vitorias):
   
    if vitorias < 10 :
        nivel = "Ferro"
    elif vitorias >= 11 and vitorias <= 20:
        nivel = "Bronze"
    elif vitorias >= 21 and vitorias <= 50:
        nivel = "Prata"
    elif vitorias  >= 51 and vitorias <= 80: 
        nivel = "Ouro"
    elif vitorias  >= 81 and vitorias <= 90: 
        nivel =" Diamante"
    elif vitorias  >= 91 and vitorias <= 100: 
        nivel = "Lendário"
    else:
        nivel = "Imortal"
   
    return nivel


while True:
    venceu = int(input(f"Quantas vezes o herói venceu? "))
    perdeu = int(input(f"Quantas vezes o herói perdeu? "))
    saldo = venceu - perdeu

    nivelHeroi = rank(saldo) 
    
    print(f"O saldo de vitorias do herói é: {saldo}.\nE ele está no nível {nivelHeroi}.\n") 

    continuar = " "
    while continuar not in "SN":
         continuar = str(input(f"Você deseja fazer outra consulta? ")) .strip() .upper() [0]
    if continuar == "N":
        break

print("Até breve!!!!")
