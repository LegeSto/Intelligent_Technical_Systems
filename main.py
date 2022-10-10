# Author: Matveev Vadim Igorevich

from random import randint
import time


# 1. Function to fill an array of 1 000 000 elements
def generate_list():
    nums_list = [randint(0, 999) for i in range(1000000)]
    return nums_list


# 2. Function of counting the frequency of occurrence of elements in the intervals
def calcHist(tdata):
    hist = [0] * 10
    for num in tdata:
        if num < 100:
            hist[0] += 1
        elif num < 200:
            hist[1] += 1
        elif num < 300:
            hist[2] += 1
        elif num < 400:
            hist[3] += 1
        elif num < 500:
            hist[4] += 1
        elif num < 600:
            hist[5] += 1
        elif num < 700:
            hist[6] += 1
        elif num < 800:
            hist[7] += 1
        elif num < 900:
            hist[8] += 1
        elif num < 1000:
            hist[9] += 1
    return hist


# 3. Function of the calculating the run time of the function calcHist()
def counting_run_time():
    tdata = generate_list()
    start = time.time()
    calcHist(tdata)
    end = time.time()
    run_time = end - start
    return run_time


if __name__ == '__main__':
    test_data = [0] * 1000000
    data = generate_list()
    test_a = calcHist(test_data)
    a = calcHist(data)
    print(test_a)
    print(a)

    list_run_times = []
    for i in range(100):
        list_run_times.append(counting_run_time())

    print('Max run time is', max(list_run_times),
          '\nMin run time is', min(list_run_times),
          '\nMean run time is', sum(list_run_times) / len(list_run_times))
