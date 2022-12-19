import numpy as np
from numpy import sign
from math import sqrt, asin, degrees, pi
from time import sleep


ip_adress = '192.168.0.1'
port = '1883'
topic = 'abot/command'
file_name = 'path.txt'
V_motion = 1
V_rotation = 10

current_angle = 0


def get_distance(start, end):
    summa = 0
    for i in range(len(start)):
        summa += (start[i] - end[i]) ** 2
    dist = sqrt(summa)
    return dist


def get_time_motion(distance):
    return distance/V_motion


def get_rotation(start, end):
    if end[0] - start[0] > 0:
        angle = asin((end[1] - start[1]) / get_distance(start, end))
    else:
        angle = pi - abs(asin((end[1] - start[1]) / get_distance(start, end))) * (end[1] - start[1])/abs(end[1] - start[1])
    if abs(angle) >= 180:
        angle = (abs(angle) - 2 * pi) * sign(angle)
    return degrees(angle)


def get_time_rotate(angle):
    return abs(angle) / V_rotation


if __name__ == '__main__':

    file_data = np.loadtxt(file_name, dtype=float)

    for index in range(len(file_data) - 1):
        current_coord = file_data[index]

        dist = get_distance(current_coord, file_data[index + 1])
        time_mot = get_time_motion(dist)

        angle = get_rotation(current_coord, file_data[index + 1]) - current_angle
        current_angle += angle
        time_rotate = get_time_rotate(angle)

        print('{' + '"turn": {}, "go": {}'.format(angle, dist) + '}')
        sleep(time_rotate + time_mot + 2)
