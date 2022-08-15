def nota(*num):

    resp = {}
    resp['total'] = len(num)
    resp['maior'] = max(num)
    resp['menor'] = min(num)
    resp['media'] = sum(num) / len(num)

    return resp


#Programa principal

r = nota(8, 9, 7)
print(r)



