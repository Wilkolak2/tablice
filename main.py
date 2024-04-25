from tablica import Tablica

tablica = Tablica()
tablica.dodaj(10)
tablica.dodaj(4)
tablica.dodaj(2)
tablica.dodaj(6)
tablica.dodaj(10)
tablica.dodaj(11)

print(tablica.wyszukaj(10))
print(tablica.wyszukajIndeks(5))
print(tablica.wyszukajOstatniIndeks(10))