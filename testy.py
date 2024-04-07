from index import calk_szesc

def test_calk_szesc():
    assert calk_szesc(40) == "28", "Konwersja liczby 40 nie powiodła się."
    assert calk_szesc(31) == "1F", "Konwersja liczby 31 nie powiodła się."
    assert calk_szesc(-1) == "Błąd: Podaj liczbę całkowitą dodatnią.", "Obsługa liczby ujemnej nie powiodła się."
    assert calk_szesc(0) == "Błąd: Podaj liczbę całkowitą dodatnią.", "Obsługa liczby 0 nie powiodła się."

    print("Wszystkie testy przeszły pomyślnie.")

if __name__ == "__main__":
    test_calk_szesc()
