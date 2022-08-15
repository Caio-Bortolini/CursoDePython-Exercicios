def voto(ano):
    '''

    :param ano: ano de nascimento
    :return: Situação (OBRIGATÓRIO, OPCIONAL, NEGADO)
    '''

    from datetime import date
    today = date.today().year
    idade = today - ano

    if idade < 16:
        return f"Com {idade} o voto esta NEGADO!"
    elif idade <=16 and idade <18 or idade >65:
        return f"Com {idade} o voto é OPCIONAL!!"
    else:
        return f"Com {idade} o voto é OBRIGATÓRIO!!"



#PROGRAMA PRINCIPAL

nascimento = int(input("Ano de nascimento: "))

#voto(nascimento)


print(voto(nascimento))

print(voto(1975))


