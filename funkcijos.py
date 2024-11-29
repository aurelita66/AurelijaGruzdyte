def sumuok(listas):
    res = sum(listas)
    return res


def vidurkis(listas):
    try:
        return sum(listas) / len(listas)
    except ZeroDivisionError:
        return 0


def didziausias(listas):
    res = max(listas)
    return res


def maziausias(listas):
    res = min(listas)
    return res


def balansas(sk1, sk2):
    res = sk1 - sk2
    return res
