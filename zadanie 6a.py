""" Funkcja komplement,która dla sekwencji nici kodującej DNA znajduje i zwraca sekwencję nici matrycowej,
:author Maciej Szychowski
:param DNA  - sekwencja nici kodującej DNA
:return   - zwraca sekwencję nici matrycowej
 """
def komplement(DNA: str) -> str:
    zamiana = ""
    for char in DNA:
        if char == 'C':
            zamiana += "G"
        elif char == 'G':
            zamiana += "C"
        elif char == 'T':
            zamiana += "A"
        elif char == 'A':
            zamiana += "U"
    return zamiana

sekwencja_kodujaca = "CGTA"
sekwencja_matrycowej = komplement(sekwencja_kodujaca)
print(f"Sekwencja nici kodującej:  {sekwencja_kodujaca}")
print(f"Sekwencja nici matrycowej: {sekwencja_matrycowej}")



