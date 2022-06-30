print('='*30)
print("BANCO CEV")
print('='*30)

saque = int(input("Que valor voce deseja sacar? R$"))
total = saque
ced = 50
totCed = 0

while True:
    if total >=ced:
        total -= ced
        totCed+=1
    else:
        if totCed > 0:
            print(f"Total de {totCed} cédulas de {ced}")

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break



