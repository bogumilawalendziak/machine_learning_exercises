import numpy as np

# Utwórz w zmiennej a jednowymiarową tablicę z elementami od 0 do 19. Hint: Służy do tego metoda np.arange(...)

a = np.arange(20)
a
# print(a)

# Wyświetl kształt tej tablicy. Hint: służy do tego właściwość shape
a.shape
a[0]
a[3]

#Zmień kształt tablicy na 2x10. Wynik przekształcenia zapisz w a. Potem ponownie sprawdź kształt i wyświetl zawartość tablicy. Hint: Skorzystaj z metody reshape(...)
reshaped = a.reshape((2,10))
print(reshaped)
reshaped[0]

reshaped = a.reshape((2,5,2))
print(reshaped)

#drugi element z czwartego wiersza w zerowym wierszu



b = np.arange(40)
# print(a)

# Wyświetl kształt tej tablicy. Hint: służy do tego właściwość shape
#b.reshape((4,5))

d = a_python_list =  [2**x for x in range(10)]

e = np.zeros(10)
f = np.ones(10)
g = np.empty(10)
h = np.full((5,5),13)
i = np.eye(5)
j = np.random.random(5)
print(e)
print(a)
