from math import sqrt
import re


class NNClassifier():
    def __init__(self, hist, file='histograms3.txt'):
        """Инициализация"""
        self.file = file
        self.hist = hist

    def get_hists(self):
        """Получение списка гистограмм из файла"""
        f = open(self.file, 'r')
        lst_hists = []
        line = f.readline().strip()
        while line:
            hist = re.match(r'(\d+),\s\((.?\d+),\s(.?\d+)\)', line)
            lst_hists.append((hist.group(1), (int(hist.group(2)), int(hist.group(3)))))
            line = f.readline().strip()
        f.close()
        return lst_hists

    def determine_type(self):
        """Метод, определяющий к какому типу относится данный объект методом 3-х ближайших соседей"""

        distances = []      # Список кортежей вида (расстояние до другого объекта, тип объекта)

        for hist in self.get_hists():
            summa = 0
            for i in range(len(hist)):
                summa += (hist[1][i] - self.hist[i]) ** 2
            distances.append((sqrt(summa), hist[0]))

        distances.sort()

        # Определение типа объекта по трем ближайшим соседям
        type_hist = distances[0][1]
        if type_hist != distances[1][1]:
            if type_hist != distances[2][1]:
                if distances[1][1] == distances[2][1]:
                    type_hist = distances[1][1]
        return type_hist


if __name__ == '__main__':
    object1 = NNClassifier((-2, 1))
    print('Список гистограмм:', object1.get_hists())
    print('Тип нового объекта:', object1.determine_type())
