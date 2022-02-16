def caixa():
    print('=' * 30)
    print('{:^30}'.format("Banco da Anna"))
    print('=' * 30)
    value = int(input("Qual será o valor a ser sacado?"))
    total = value
    ced = 50
    totalced = 0
    while True:
        if total >= ced:
            total -= ced
            totalced += 1
        else:
            if totalced > 0:
                print("Total de {} cédulas de R${}".format(totalced, ced))
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totalced = 0
            if total == 0:
                break
    print('=' * 30)

caixa()







