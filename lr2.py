import numpy as np
import pandas as pd
import matplotlib.pylab as pl
import csv
import ot
from ot import plot

n = 100  # строк

# 1. Осуществить чтение данных из двух csv файлов
data1 = pd.read_csv('new_york_hotels.csv', encoding='ANSI', header=None, nrows=n, skiprows=[0])
data2 = pd.read_csv('US_Accidents_Dec19.csv', encoding='utf-8', header=None, nrows=n, skiprows=[0])

# 2. Сформировать выборки
a1 = pd.DataFrame(data1, columns=[6, 7])
a2 = pd.DataFrame(data2, columns=[6, 7])

# преобразуем в numpy массив
xs = np.array(a1)
xt = np.array(a2)


a = np.ones((n,)) / n  # нормализация
b = np.ones((n,)) / n  # cjplftv массивы по 1 сотой lkz a-bb lfkmit

# 3. График местоположений пунктов назначения и расположений машин такси
pl.figure(1)
pl.plot(xs[:, 0], xs[:, 1], '+b', label='Source samples')
pl.plot(xt[:, 0], xt[:, 1], 'xr', label='Target samples')
pl.legend(loc=0)


# 4. Рассчитайте расстояние между точками из двух сформированных ранее датафреймов
M = ot.dist(xs, xt)  # находим евклидово расстояние
M /= M.max()  # нормализация

# Матрица расстояний
pl.figure(2)
pl.imshow(M, interpolation='nearest')  # Применяем проксимальную интерполяцию
pl.title('Cost matrix M')

# 5. Найдите матрицу оптимальных перемещений
G0 = ot.emd(a, b, M)

# Матрица оптимальных перемещений на основании расстояний
pl.figure(3)
pl.imshow(G0, interpolation='nearest')
pl.title('OT matrix G0')

# 6. Исходя из полученных данных местоположений отелей и машин отобразите оптимальные расстояния
pl.figure(4)
ot.plot.plot2D_samples_mat(xs, xt, G0, c=[.5, .5, 1])
pl.plot(xs[:, 0], xs[:, 1], '+b', label='Source samples')
pl.plot(xt[:, 0], xt[:, 1], 'xr', label='Target samples')
pl.legend(loc=0)
pl.title('OT matrix with samples')

# 7. Сформируйте датафрейм, содержащий данные по оптимальным местоположениям отелей и такси
table = []
table2 = []
i = 0
j = 0
while j < n:
    while i < n:
        if G0[i, j] > 0:  # значит что между точками проложенно перемещение, если не проложенно, то там 0
            table.append([i, j])
        i = i + 1
    table2.append(table)
    i = 0
    j = j + 1

pl.show()

with open('transition_matrix.csv', "w", newline="") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(table)
