# Author: Matveev Vadim Igorevich

from math import sqrt
import re


# 1. Функция, которая рисует равнобедренный треугольник при помощи звездочек (*)
def triangle(a):
    for i in range(a + 1):
        print(' ' * (a - i) + '*' * (1 + i * 2) + ' ' * (a - i))


# 2. Функция для вычисления декартова расстояния между гистограммами
def histDistanve(hist1, hist2):
    summa = 0
    for i in range(len(hist1)):
        summa += (hist1[i] - hist2[i]) ** 2
    dist = sqrt(summa)
    return dist


# 3. Функция для записи гистограмм в файл
def write_hist(*hist):
    f = open('histograms.txt', 'a')
    for i in hist:
        f.write(str(i) + '\n')
    f.close()


# 4. Функция для чтения гистограмм из файла
def read_hist(file):
    f = open(file, 'r')
    lst_hists = []
    line = f.readline()
    while line:
        tuple_ = tuple(map(int, re.findall(r'\d+', line)))
        lst_hists.append(tuple_)
        line = f.readline()
    return lst_hists


if __name__ == '__main__':
    triangle(5)
    print(histDistanve((0, 0, 0), (3, 4, 9)))
    write_hist((0, 0, 3), (1, 1, 0))
    print(read_hist('histograms.txt'))
