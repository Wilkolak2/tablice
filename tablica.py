class Tablica:
    def __init__(self):
        self.tablica = []

    def dodaj(self,element):
        self.tablica.append(element)

    def wyswietl(self):
        print(self.tablica)

    def wyszukaj(self, wartosc):
        for element in self.tablica:
            if element == wartosc:
                return element
        return None

    #metoda wyszukujaca indeks zadanego elementu
    def wyszukajIndeks(self, wartosc):
        for i in range(len(self.tablica)):
            if self.tablica[i] == wartosc:
                return i
        return None

    #metoda wyszukujaca ostatni znaleziony indeks zadanego elementu
    def wyszukajOstatniIndeks(self, wartosc):
        for i in range(len(self.tablica)-1,-1,-1):
            if self.tablica[i] == wartosc:
                return i
        return None