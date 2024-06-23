class Wielomian:
    def __init__(self, wspolczynniki):      # init" to skrót od "initialization", czyli "inicjalizator. https://kt.academy/pl/article/py-klasy#definition-1
        """
        :init:  Inicjalizator klasy Wielomian
        :param wspolczynniki:Lista współczynników wielomianu
        :ValueError: błędy
        """
        if len(wspolczynniki) ==0:          # sprawdzamy czy lista wspolczynikow nie jest pusta
            raise ValueError("Lista wspołczynników nie może być pusta")
        if wspolczynniki[0] == 0:           # sprawdzamy czy pierwszy wspolczynnik jest 0
            raise ValueError("an nie moze byc rowne 0")

        self.wspolczynniki = wspolczynniki

    def stopien(self):                  # stopien wielomianu dlugosc listy ze wspolczynnikami minus 1
        """
        :return: metoda zwraca stopien wielomianu
        """
        return len(self.wspolczynniki)-1

    def __str__(self):
        """
        :return: metoda zwracajaca postac textowa wielomianu
        """

        text = "W(x)="
        for i in range(len(self.wspolczynniki)):            # pętlą przechodzimy przez wszystkie wspolczynniki
            text+= f"+{self.wspolczynniki[i]}x^{self.stopien()-i}"  # wspolczynnik w formie +a_n*x^n, += zwieksza poprzednią wartosc o wartosc po prawej stronie, https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
        return text

    def __call__(self,x):                   # https://www.geeksforgeeks.org/__call__-in-python/
        """
        :param x: wartosc dla ktorej chcemy obliczyc wielomian
        :return: zwraca wartosc wielomianu dla podanej x
        """
        wartosc = 0
        for i in range(len(self.wspolczynniki)):  # pętlą przechodzimy przez wszystkie wspolczynniki
             wartosc += self.wspolczynniki[i]*x**(self.stopien()- i)    # wspolczynnik w formie +a_n*x^n, ** znak potegowania
        return wartosc

    def __add__(self, drugi_wielomian):               # https://medium.com/nishkoder/understanding-pythons-add-and-iadd-magic-methods-b8eb8821dea1
        """
        :param drugi_wielomian: drugi wielomian ktory ma byc dodany do pierwszego wielomianu
        :return: zwraca nowy obiekt klasy wielomian, ktory jest suma dwoch wielomianow
        """
        krotszy= []
        wspolczynniki = []                          # tworzymy pusta liste na wspolczynniki
        if self.stopien()>drugi_wielomian.stopien():
            krotszy=drugi_wielomian.wspolczynniki
            wspolczynniki=self.wspolczynniki
        else:
            krotszy =self.wspolczynniki
            wspolczynniki = drugi_wielomian.wspolczynniki
        krotszy=krotszy[::-1]                  # odwrocenie listy, zeby zaczac od ostatniego wspolczynnika
        wspolczynniki=wspolczynniki[::-1]
        for i in range(len(krotszy)):
            wspolczynniki[i]=wspolczynniki[i]+krotszy[i]
        wspolczynniki=wspolczynniki[::-1]
        return Wielomian(wspolczynniki)

    def __sub__(self,drugi_wielomian):
        krotszy = []
        wspolczynniki = []  # tworzymy pusta liste na wspolczynniki
        if self.stopien() > drugi_wielomian.stopien():
            krotszy = drugi_wielomian.wspolczynniki
            wspolczynniki = self.wspolczynniki
        else:
            krotszy = self.wspolczynniki
            wspolczynniki = drugi_wielomian.wspolczynniki
        krotszy=krotszy[::-1]  # odwrocenie listy, zeby zaczac od ostatniego wspolczynnika
        wspolczynniki=wspolczynniki[::-1]
        for i in range(len(krotszy)):
            wspolczynniki[i] = wspolczynniki[i] - krotszy[i]
        wspolczynniki=wspolczynniki[::-1]
        return Wielomian(wspolczynniki)

    def __iadd__(self, drugi_wielomian):                #iadd - inplace add = +=
        """
        :param drugi_wielomian: drugi wielomian ktory ma byc odjety od pierwszego
        :return: zwraca nowy obiekt klasy wielomian ktory jest roznica dwoch wielomianow
        """
        krotszy = []
        wspolczynniki = []  # tworzymy pusta liste na wspolczynniki
        if self.stopien() > drugi_wielomian.stopien():
            krotszy = drugi_wielomian.wspolczynniki
            wspolczynniki = self.wspolczynniki
        else:
            krotszy = self.wspolczynniki
            wspolczynniki = drugi_wielomian.wspolczynniki
        krotszy.reverse()  # odwrocenie listy, zeby zaczac od ostatniego wspolczynnika
        wspolczynniki=wspolczynniki[::-1]
        for i in range(len(krotszy)):
            wspolczynniki[i] = wspolczynniki[i] + krotszy[i]
        wspolczynniki=wspolczynniki[::-1]
        self.wspolczynniki=wspolczynniki
        return self

    def __isub__(self, drugi_wielomian):
        """
        :param drugi_wielomian: drugi wielomian, ktory ma byc odjety od biezacego
        :return: zwraca biezacy obiekt klasy wielomian po odjeciu drugiego wielomianu
        """
        krotszy = []
        wspolczynniki = []  # tworzymy pusta liste na wspolczynniki
        if self.stopien() > drugi_wielomian.stopien():
            krotszy = drugi_wielomian.wspolczynniki
            wspolczynniki = self.wspolczynniki
        else:
            krotszy = self.wspolczynniki
            wspolczynniki = drugi_wielomian.wspolczynniki
        krotszy.reverse()  # odwrocenie listy, zeby zaczac od ostatniego wspolczynnika
        wspolczynniki=wspolczynniki[::-1]
        for i in range(len(krotszy)):
            wspolczynniki[i] = wspolczynniki[i] - krotszy[i]
        wspolczynniki=wspolczynniki[::-1]
        self.wspolczynniki = wspolczynniki
        return self

    def __mul__(self, drugi_wielomian):                                                     # mul - multiplikation (mnozenie) https://www.geeksforgeeks.org/multiply-two-polynomials-2/
        wynik = [0]*(len(self.wspolczynniki)+len(drugi_wielomian.wspolczynniki)-1)          # tworzymy pusta lista o dlugosci ktora bedzie miala lista wspolczynnikow wynikowego wielomianu
        for i in range(len(self.wspolczynniki)):
            for j in range(len(drugi_wielomian.wspolczynniki)):
                wynik[i+j]+=self.wspolczynniki[i]+drugi_wielomian.wspolczynniki[j]
        return Wielomian(wynik)

    def __imul__(self, drugi_wielomian):                                                    #inplace multiplikation (*=)
        """
        :param drugi_wielomian: drugi wielomian ktory ma byc pomnozony przez pierwszy wielomian
        :return: zwraca iloczyn dwoch wielomianow
        """
        wynik = [0] * (len(self.wspolczynniki) + len(
            drugi_wielomian.wspolczynniki) - 1)  # tworzymy pusta lista o dlugosci ktora bedzie miala lista wspolczynnikow wynikowego wielomianu
        for i in range(len(self.wspolczynniki)):
            for j in range(len(drugi_wielomian.wspolczynniki)):
                wynik[i + j] += self.wspolczynniki[i] + drugi_wielomian.wspolczynniki[j]
        self.wspolczynniki=wynik
        return self


wspolczynniki = [1, 2, 3]  # lista współczynników
wielomian = Wielomian(wspolczynniki)
print(wielomian)
print(wielomian.stopien())
print(wielomian(1))
wspolczynniki2 = [1,2,3,4]
wielomian2 = Wielomian(wspolczynniki2)
print(wielomian2)
print(wielomian+wielomian2)
print(wielomian2-wielomian)
print(wielomian*wielomian2)
wielomian+=wielomian2
print(wielomian)
wielomian-=wielomian2
print(wielomian)
wielomian*=wielomian2
print(wielomian)
