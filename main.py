import numpy as np
from perceptron import Perceptron

X = np.array([
    [2, 4, 20],  # 2*2 - 4*4 + 20 =   8 > 0
    [4, 3, -10],  # 2*4 - 4*3 - 10 = -14 < 0
    [5, 6, 13],  # 2*5 - 4*6 + 13 =  -1 < 0
    [5, 4, 8],  # 2*5 - 4*4 + 8 =    2 > 0
    [3, 4, 5],  # 2*3 - 4*4 + 5 =   -5 < 0
])

y = np.array([1, -1, -1, 1, -1])

perceptron = Perceptron(0.1, 100)
perceptron.fit(X, y)

print(perceptron.w)

print(perceptron.predict(np.array([[1, 2, 3, 1]])))  # 2*1 - 4*2 + 1 = -3 < 0
print(perceptron.predict(np.array([[2, 2, 8, 1]])))  # 2*2 - 4*2 + 8 =  4 > 0
print(perceptron.predict(np.array([[3, 3, 3, 1]])))  # 2*3 - 4*3 + 3 = -3 < 0

