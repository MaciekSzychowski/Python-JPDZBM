def fibonacci(n):
    if n <= 0:          # Sprawdzam, czy n jest nieujemne, jeżeli jest ujemne lum mniejsze od zera zwraca pustą listę, ciąg nie ma sensu
        return []

    lista2Pel = [0, 1]   # tworzę listę zawierającą dwa pierwsze elementy ciągu

    if n == 1:          # zabezpieczenie, jeżeli n = 1, zwracam pierszy element ciągu
        return [0]

    for i in range(2, n):       # iteracja od 2 no zadanego n
        nastepneLiczbyCiagu = lista2Pel[-1] + lista2Pel[-2]
        lista2Pel.append(nastepneLiczbyCiagu) # dodawanie do listy nowych elementow,  https://www.w3schools.com/python/ref_list_append.asp

    return lista2Pel[:n]  # zwracanie elementow z listy, https://stackoverflow.com/questions/509211/how-slicing-in-python-works


n = 20
print(fibonacci(n))