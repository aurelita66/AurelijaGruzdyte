import datetime

from funkcijos import sumuok, vidurkis, didziausias, maziausias, balansas

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
        data = input('Iveskite data (YYYY-MM-DD): ')
        dt = datetime.datetime.strptime(data, '%Y-%m-%d')
        pavadinimas = input('Iveskite pajamu pavadinima: ')
        suma = float(input('Iveskite suma: '))
        pajamos.append([dt, pavadinimas, suma])
        continue

    elif pasirinkimas == "2":
        data = input('Iveskite data (YYYY-MM-DD): ')
        dt = datetime.datetime.strptime(data, '%Y-%m-%d')
        pavadinimas = input('Iveskite islaidu pavadinima: ')
        suma = float(input('Iveskite suma: '))
        islaidos.append([dt, pavadinimas, suma])
        continue

    elif pasirinkimas == "3":
        if not pajamos:
            print('Pajamos neivestos!')
        else:
            for elem in pajamos:
                print(f'{elem[0]}, {elem[1]}: {elem[2]}')
        continue

    elif pasirinkimas == "4":
        if not islaidos:
            print('Islaidos neivestos!')
        else:
            for elem in islaidos:
                print(f'{elem[0]}, {elem[1]}: {elem[2]}')
        continue

    elif pasirinkimas == "5":
        pajamu_sumos = list(elem[2] for elem in pajamos)

        print(f'Visu pajamu suma: {sumuok(pajamu_sumos)}')
        print(f'Visu pajamu vidurkis: {vidurkis(pajamu_sumos)}')
        print(f'Didziausios pajamos suma: {didziausias(pajamu_sumos)}')
        print(f'Maziausios pajamos suma: {maziausias(pajamu_sumos)}')

        islaidu_sumos = list(elem[2] for elem in islaidos)

        print(f'Visu islaidu suma: {sumuok(islaidu_sumos)}')
        print(f'Visu islaidu vidurkis: {vidurkis(islaidu_sumos)}')
        print(f'Didziausios islaidos suma: {didziausias(islaidu_sumos)}')
        print(f'Maziausios islaidos suma: {maziausias(islaidu_sumos)}')

        sk1 = sumuok(pajamu_sumos)
        sk2 = sumuok(islaidu_sumos)

        print(f'Balansas (likusi pajamu suma): {balansas(sk1, sk2)}')
        continue

    else:
        print('Tokio pasirinkimo nera!')
        continue

print('Programa baigia darba')
