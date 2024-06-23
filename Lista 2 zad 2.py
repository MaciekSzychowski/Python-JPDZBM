class FastaSequence:  # klasa bazowa po któej bedziemy dziedziczyc
    def __init__(self, identifier, data):
        self.identifier=identifier  #pola klasy
        self.data=data
        self.lenght=len(data)       # długosc sekwencji
        self.VALID_CHARS= ""


    def __str__(self):      # metoda jak toString w kotlinie
        """"
        :return: zwraca reprezentacje obiektu w formacie FASTA
        """
        fasta=">"+ self.identifier+"\n"+self.data     # \n wstawienie znaku nowej linii
        return fasta

    def mutate(self, position, value):
        """
        :param position: pozycja na ktorej ma byc zamieniony znak
        :param value: nowy znak ktory ma byc umieszczony na danej pozycji
        """
        if value not in self.VALID_CHARS:                                         #https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method/3437070#3437070
            raise ValueError("Niedozwolony znak")
        if position > self.lenght-1:                                             # spradwdzenie cyz podana pozycja do podmiany nie jest weiksza niż dlugosc sekwencji
            raise ValueError("Pozycja wieksza niż dlugosc sekwencji ")
        if len(value)!=1:
            raise ValueError("Należy podać tylko jedną litere do podmiany")

        self.data[position]=value                                                     # podmiana w stringu literki na position na literke podana jako value

    def find_motif(self,motif):                                                 # https://stackoverflow.com/questions/1323364/in-python-how-to-check-if-a-string-only-contains-certain-characters
        """
        :param motif: dany motyw ktory ma zostac znaleziony w sekwencji
        :return: zwraca pozycje pierwszego wystamienia motywy w sekwencji
        """
        for letter in motif:                                        # sprawdzenie czy w naszym z zbiorze znajduja sie tylko dozwolone literki
            if letter not in self.VALID_CHARS:
                raise ValueError("Niedozwolony znak")
        position=self.data.find(motif)                              #https://www.freecodecamp.org/news/python-find-how-to-search-for-a-substring-in-a-string/
        if position !=-1:
            return position
        else:
            raise ValueError("Nieznaleziono zadanego motywu")


class DNASequence(FastaSequence):       #dziedziczenie po klasie Fasta
    def __init__(self,identifier, data):
        """
        :param identifier: unikalny identyfikator sekwencji
        :param data: sekwencja DNA
        """
        super().__init__(identifier,data)
        self.VALID_CHARS="ATGC"
        for letter in data:                                        # sprawdzenie czy w naszym z zbiorze znajduja sie tylko dozwolone literki
            if letter not in self.VALID_CHARS:
                raise ValueError("Niedozwolony znak")

    def transcribe(self):                          # https://www.biologia.net.pl/genetyka/transkrypcja.html
        """
        :return: zwraca obiekt klasy RNASequence, reprezentujący transkrypt sekwencji DNA
        """
        return RNASequence(self.identifier,self.data.replace("T","U"))  #zamiana T na U zgodnie z tym co w linku powyżęj




class ProteinSequence(FastaSequence):

    def __init__(self, identifier, data):
        """
        :param identifier: unikalny identyfikator sekwencji bialkowej
        :param data: sekwencja bialkowa
        """
        super().__init__(identifier, data)
        self.VALID_CHARS = "ARNDCQEGHILKMFPSTWYV"
        for letter in data:                                        # sprawdzenie czy w naszym z zbiorze znajduja sie tylko dozwolone literki
            if letter not in self.VALID_CHARS:
                raise ValueError("Niedozwolony znak")


class RNASequence(FastaSequence):
    def __init__(self,identifier, data):
        """
        :param identifier: idenntyfikator sekwencji RNA
        :param data: sekwencja danych RNA
        """
        super().__init__(identifier,data)
        self.VALID_CHARS="AUGC"
        for letter in data:                                        # sprawdzenie czy w naszym z zbiorze znajduja sie tylko dozwolone literki
            if letter not in self.VALID_CHARS:
                raise ValueError("Niedozwolony znak")

    def translate(self):
        """
        :return: zwraca obiekt klasy ProteinSequence reprezentujący przetłumaczoną sekwencję białkową
        """
        codon_map = {
            'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',                 # wygenerowane przez chat gpt
            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y',
            'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'UGU': 'C', 'UGC': 'C',
            'UGA': '*', 'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L',
            'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R',
            'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I',
            'AUA': 'I', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S',
            'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V',
            'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A',
            'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
        }
        protein_sequence=""
        codon=""
        for letter in self.data:
            if len(codon)!=3:       # jezeli nasz codon nie ma 3 liter to znaczy ze jeszcze nie jest pelnym codonem wiec dodoajemy kolejna litere
                codon+=letter
            else:
                aminoacid=codon_map.get(codon,"")
                if aminoacid=="":
                    raise ValueError("NIe można rozpoznać codonu")
                if aminoacid=="*":
                    break           # gdy trafimy na * przerywane jest czytanie sekwencji
                protein_sequence+=aminoacid
                codon=letter
        return ProteinSequence(self.identifier, protein_sequence)




almbumin_DNA=DNASequence("RatAlbumin","""ATGAAATGGGTGACCTTTCTGCTGCTGCTGTTTATTAGCGGCAGCGCGTTTAGCCGCGGC
GTGTTTCGCCGCGAAGCGCATAAAAGCGAAATTGCGCATCGCTTTAAAGATCTGGGCGAA
CAGCATTTTAAAGGCCTGGTGCTGATTGCGTTTAGCCAGTATCTGCAGAAATGCCCGTAT
GAAGAACATATTAAACTGGTGCAGGAAGTGACCGATTTTGCGAAAACCTGCGTGGCGGAT
GAAAACGCGGAAAACTGCGATAAAAGCATTCATACCCTGTTTGGCGATAAACTGTGCGCG
ATTCCGAAACTGCGCGATAACTATGGCGAACTGGCGGATTGCTGCGCGAAACAGGAACCG
GAACGCAACGAATGCTTTCTGCAGCATAAAGATGATAACCCGAACCTGCCGCCGTTTCAG
CGCCCGGAAGCGGAAGCGATGTGCACCAGCTTTCAGGAAAACCCGACCAGCTTTCTGGGC
CATTATCTGCATGAAGTGGCGCGCCGCCATCCGTATTTTTATGCGCCGGAACTGCTGTAT
TATGCGGAAAAATATAACGAAGTGCTGACCCAGTGCTGCACCGAAAGCGATAAAGCGGCG
TGCCTGACCCCGAAACTGGATGCGGTGAAAGAAAAAGCGCTGGTGGCGGCGGTGCGCCAG
CGCATGAAATGCAGCAGCATGCAGCGCTTTGGCGAACGCGCGTTTAAAGCGTGGGCGGTG
GCGCGCATGAGCCAGCGCTTTCCGAACGCGGAATTTGCGGAAATTACCAAACTGGCGACC
GATGTGACCAAAATTAACAAAGAATGCTGCCATGGCGATCTGCTGGAATGCGCGGATGAT
CGCGCGGAACTGGCGAAATATATGTGCGAAAACCAGGCGACCATTAGCAGCAAACTGCAG
GCGTGCTGCGATAAACCGGTGCTGCAGAAAAGCCAGTGCCTGGCGGAAATTGAACATGAT
AACATTCCGGCGGATCTGCCGAGCATTGCGGCGGATTTTGTGGAAGATAAAGAAGTGTGC
AAAAACTATGCGGAAGCGAAAGATGTGTTTCTGGGCACCTTTCTGTATGAATATAGCCGC
CGCCATCCGGATTATAGCGTGAGCCTGCTGCTGCGCCTGGCGAAAAAATATGAAGCGACC
CTGGAAAAATGCTGCGCGGAAGGCGATCCGCCGGCGTGCTATGGCACCGTGCTGGCGGAA
TTTCAGCCGCTGGTGGAAGAACCGAAAAACCTGGTGAAAACCAACTGCGAACTGTATGAA
AAACTGGGCGAATATGGCTTTCAGAACGCGGTGCTGGTGCGCTATACCCAGAAAGCGCCG
CAGGTGAGCACCCCGACCCTGGTGGAAGCGGCGCGCAACCTGGGCCGCGTGGGCACCAAA
TGCTGCACCCTGCCGGAAGCGCAGCGCCTGCCGTGCGTGGAAGATTATCTGAGCGCGATT
CTGAACCGCCTGTGCGTGCTGCATGAAAAAACCCCGGTGAGCGAAAAAGTGACCAAATGC
TGCAGCGGCAGCCTGGTGGAACGCCGCCCGTGCTTTAGCGCGCTGACCGTGGATGAAACC
TATGTGCCGAAAGAATTTAAAGCGGAAACCTTTACCTTTCATAGCGATATTTGCACCCTG
CCGGATAAAGAAAAACAGATTAAAAAACAGACCGCGCTGGCGGAACTGGTGAAACATAAA
CCGAAAGCGACCGAAGATCAGCTGAAAACCGTGATGGGCGATTTTGCGCAGTTTGTGGAT
AAATGCTGCAAAGCGGCGGATAAAGATAACTGCTTTGCGACCGAAGGCCCGAACCTGGTG
GCGCGCAGCAAAGAAGCGCTGGCG""".replace("\n","")) #usuwanie znakow konca linii z sekwencji
almbumin_RNA=almbumin_DNA.transcribe()
albumin_Sequence=almbumin_RNA.translate()
print(albumin_Sequence)
