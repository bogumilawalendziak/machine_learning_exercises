import numpy as np

# 1. W zmiennej X zapisz tablicę dwuwymiarową z kolejnymi liczbami od 1 do 25. (Skorzystaj z arange() i reshape())

x = np.arange(1, 26)
x = x.reshape((5, 5))

# 2. W zmiennej Ones zapisz tablicę o takim samym kształcie jak X, ale całą wypełnioną tylko jedynkami. (Skorzystaj z ones())

ones = np.ones((5, 5))

# 3. Kiedy mnożąc przez siebie zwykłe liczby, chcesz żeby liczba pomnożona przez jakąś wartość dawała w wyniku tą samą liczbę, to tą jakąś wartością powinno być 1 (tzw. element neutralny). Czy tablica Ones jest taką "macierzową jedynką"? Sprawdź to  mnożąc przez siebie X i Ones. Czy wynik jest równy X? (Skorzytaj z dot() )
b = np.dot(x, ones)

# 4. W algebrze macierzy elementem neutralnym jest macierz zer, wypełniona jedynkami na przekątnej. Do zmiennej diag zapisz macierz o takich wymiarach jak X i wypełnioną samymi zerami (skorzystaj z zeros())
# Wypełnij diag jedynkami na przekątnej. (Skorzystaj z fill_diagonal()
# Pomnóż przez siebie X i diag i sprawdź czy wynik to X. (Skorzystaj z dot())

DIAG = np.zeros((5, 5))

# DIAG = np.fill_diagonal(ZEROS, 1) <-  zwraca null

np.fill_diagonal(DIAG, 1)
c = np.dot(x, DIAG)

# 5. Wyświetl tablicę o wymiarach takich jak X, gdzie (we wszystkich punktach korzystaj z where):

# występują tylko jedynki i zera. Jedynki mają się pojawić tam, gdzie w X występuje wartość większa od 10, a zero w pozostałych przypadkach

# występują tylko jedynki i zera. Jedynki mają się pojawiać tam, gdzie w X występuje wartość parzysta, a zero w pozostałych przypadkach

# występują tylko liczby parzyste. Jeśli w X wartość była parzysta, to należy ją przepisać. Jeśli była nieparzysta , to dodać 1

uno = np.where(x > 10, 1, 0)
dos = np.where(x % 2 == 0, 1, 0)
tres = np.where(x % 2 == 0, x, x + 1)

# 6. Utwórz tablicę X_bis wyznaczoną w następujący sposób. Dla wartości w X większych od 10 zwrócona jest wartość 2 razy większa, a dla pozostałych 0. Policz ile jest elementów niezerowych w X_bis (skorzystaj z count_nonzero())

X_bis = np.where(x > 10, 2 * x, 0)
u = np.count_nonzero(X_bis)

# 7. Oto dwie tablice:
# x = np.array([[10,20,30], [40,50,60]])
# y = np.array([[100], [200]])
# Dodaj (a właściwie doklej) do tablicy x tablicę y jako nową kolumnę. (Skorzystaj z append() z parametrem axis=1)

x = np.array(([[10, 20, 30], [40, 50, 60]]))
y = np.array([[100], [200]])

z = np.append(x, y, 1)

# 8. Oto dwie tablice: Dodaj (a właściwie doklej) do tablicy x tablicę y, jako nowy wiersz

x = np.array([[10, 20, 30], [40, 50, 60]])
y = np.array([[100, 200, 300]])

z = np.append(x, y, 0)

# 9. Do tablicy x z poprzedniego punktu, doklej tablicę x jako nowe wiersze (wiersze będą zduplikowane)

f = np.append(z, x, 0)

print("")
