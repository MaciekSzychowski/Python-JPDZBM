""" Fuknkcja transkrybuj, która dla sekwencji nici matrycowej DNA znajduje i zwraca sekwencję RNA
:param DNA  - sekwencja nici DNA
:return   - zwraca sekwencję RNA
 """

def transkrybuj(DNA: str) -> str:
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
    return zamiana[::-1]

sekwencja_kodujaca = "CGTA"
sekwencja_RNA = transkrybuj(sekwencja_kodujaca)
print(f"Sekwencja nici kodującej:  {sekwencja_kodujaca}")
print(f"Sekwencja RNA: {sekwencja_RNA}")