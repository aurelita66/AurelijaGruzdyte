import datetime

pajamos = []
islaidos = []

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


