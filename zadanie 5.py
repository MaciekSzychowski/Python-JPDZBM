def collatz(c0):
    if c0 <= 0:     # warunek, ze c0 musi byc liczbą naturalną
        raise ValueError("c0 musi być liczbą naturalną większą od 0.")  # w przypadku gdy nie jest wyswietla sie komunikat, https://www.w3schools.com/python/ref_keyword_raise.asp

    listaWynikow = [c0]         # tworze listę do przechowywania wynikow

    while c0 != 1:              # pętla while pracuje aż c0 nie będize 1
        if c0 % 2 == 0:         # jęsli c0 jest liczbą parzystą, dzielimy przez dwa (%reszta z dzielenia)
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1     # w innym przypadku postępujemy zggodnie ze wzorem
        listaWynikow.append(c0) # dodawanie nowego wyniku do listy

    return listaWynikow


c0 = 7
print(collatz(c0))