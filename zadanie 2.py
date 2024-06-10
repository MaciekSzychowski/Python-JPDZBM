from collections import Counter
"""
 Funkcja wspólne, która dla dwóch multizbiorów x i y zwróca ich część wspólną.
 
 :author Maciej Szychowski
 :param multizbiorX - pierwszy multizbior X
 :param multizbiorY - drugi multizbior Y
 :return  wspolny_multizbior - multizbior zawierajacy czesci wspolne
 """
# https://kajodata.com/python/jak-policzyc-elementy-listy-w-pythonie-python-dictionary-counte/
# https://www.geeksforgeeks.org/difference-between-and-and-in-python/
def wspolne(x,y):
    multizbiorX = Counter(x)  # zliczanie elementow w multizbiorze X
    multizbiorY = Counter(y)  # zliczanie elementow w multizbiorze y
    czescWspolna = multizbiorX & multizbiorY  # sprawdzamy elementy wystepujace w zbiorze x i y ( & sluzy do obliczania wspolnych elementow)
    wspolny_multizbior = list(czescWspolna.elements())  # lista zawierajaca wspolne elementy
    return wspolny_multizbior

x = [1,2,2,3,4,5,5]
y = [2,2,2,3,5]

print(wspolne(x,y))