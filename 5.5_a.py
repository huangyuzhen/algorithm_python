'''
哈夫曼编码
优先队列
自底向上构造
'''

from queue import PriorityQueue as PQueue


def haffmanCoding(freq):
    pq = PQueue()
    total = 0
    sumFreq = 0

    for number in freq:
        total += number
        pq.put(number)

    while pq.qsize() > 1:
        jointFreq = 0
        for _ in range(2):
            jointFreq += pq.get()

        sumFreq += jointFreq
        pq.put(jointFreq)

    return sumFreq/total

freq = [45, 13, 12, 16, 9, 5]
r = haffmanCoding(freq)
print(r)
