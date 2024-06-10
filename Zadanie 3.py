import itertools
""" Funkcja podzbiory, która dla zadanego zbioru x zwróci listę wszystkich podzbiorów
 
 :author Maciej Szychowski
 :param listaDoPrzechowywania - pusta lista do przechowywania podzbiorów
 :return listaDoPrzechowywania  - zwraca listę z podzbiorami
 """


def podzbiory(x):  # funkcja podzbiory, ktora zawiera zbior wejsciowy podany przez nas

    listaDoPrzechowywania = []          # tworzymy pusta liste do przechowywania podzbiorow

    for i in range(len(x) + 1):         # iteracja po dlugosci zbioru wejsciowego, https://stackoverflow.com/questions/19184335/is-there-a-need-for-rangelena

        listaDoPrzechowywania.extend(itertools.combinations(x, i))  # https://docs.python.org/pl/3.6/tutorial/datastructures.html
                                                                    # https://docs.python.org/3/library/itertools.html
    return listaDoPrzechowywania

x = {'a', 'b', 'c', 'd'}

podzbiory = podzbiory(x)

for podzbior in podzbiory:
    print(podzbior)