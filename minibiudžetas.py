import datetime

pajamos = []
islaidos = []
data1 = []
data2 = []

while True:
    print('1. Ivesti pajamas\n'
          '2. Ivesti islaidas\n'
          '3. Atspausdinti pajamu eilutes\n'
          '4. Atspausdinti islaidu eilutes\n'
          '5. Atspausdinti statistika\n'
          'q - Iseiti\n')

    pasirinkimas = input('Iveskite pasirinkima: ')

    if pasirinkimas == "q":
          break

    if pasirinkimas == "1":
        data1 = input('Iveskite data formatu(YYYY-MM-DD): ')
        dt = datetime.datetime.strptime(data1, '%Y-%m-%d')
        avansas = float(input('Avansas: '))
        atlyginimas = float(input('Atlyginimas: '))
        stipendija = float(input('Stipendija: '))
        investicijos = float(input('Investiciju uzdarbis: '))
        papildomos = float(input('Papildomos pajamos: '))
        naujos_pajamos = [avansas, atlyginimas, stipendija, investicijos, papildomos]
        pajamos.append(naujos_pajamos)
        suma = sum(naujos_pajamos)
        print(suma)

    if pasirinkimas == "2":
        data2 = input('Iveskite data formatu(YYYY-MM-DD): ')
        dt = datetime.datetime.strptime(data2, '%Y-%m-%d')
        maistas = float(input('Maistas: '))
        bustas = float(input('Bustas: '))
        masina = float(input('Masina: '))
        papildomos2 = float(input('Papildomos islaidos(rubai, augintinio ar vaiku islaidos, kiti ivairus pirkiniai): '))
        naujos_islaidos = [maistas, bustas, masina, papildomos2]
        islaidos.append(naujos_islaidos)
        suma2 = sum(naujos_islaidos)
        print(suma2)

    if pasirinkimas == "3":
        if not pajamos:
            print('Neivestos pajamos!!!')
        else:
            for elem in pajamos:
                print(f'Data: {data1}\n'
                      f'Avansas: {elem[0]}\n'
                      f'Atlyginimas: {elem[1]}\n'
                      f'Stipendija: {elem[2]}\n'
                      f'Investiciju uzdarbis: {elem[3]}\n'
                      f'Papildomos pajamos: {elem[4]}')

    if pasirinkimas == "4":
        if not islaidos:
            print('Neivestos islaidos!!!')
        else:
            for elem in islaidos:
                print(f'Data: {data2}\n'
                      f'Maistas: {elem[0]}\n'
                      f'Bustas: {elem[1]}\n'
                      f'Masina: {elem[2]}\n'
                      f'Papildomos islaidos(rubai, augintinio ar vaiku islaidos, kiti ivairus pirkiniai): {elem[3]}')




