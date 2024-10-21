alpha = float(input('Informe o Alpha: '))
x = float(input('informe X: '))
if alpha > 0.1:
    print('Valor invalido para AlPha')
else:
    if x < 0:
        print(alpha * x)
    else:
        print(x)