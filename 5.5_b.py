'''
哈夫曼编码, 一种变长编码方式
优先队列, 自底向上构造
'''

from queue import PriorityQueue as PQueue

class CompareAble:
    def __init__(self, name, freq):
        self.name = name
        self.freq = freq

    # 这里是按python3语法，定义的 < 方法
    def __lt__(self, other):
        if self.freq <= other.freq:
            return True
        else:
            return False


def haffmanCoding(freq):
    pq = PQueue()
    total = 0
    sumFreq = 0

    for item in freq:
        total += item.freq
        pq.put(item)

    level = 0
    while pq.qsize() >= 2:
        item1 = pq.get()
        item2 = pq.get()
        level+= 1
        print(level, item1.name, item2.name)
        jointFreq = item1.freq + item2.freq
        jointName = item1.name + item2.name

        sumFreq += jointFreq

        pq.put(CompareAble(jointName, jointFreq))
    else:
        item = pq.get()
        print(item.name)

    return sumFreq/total

freq = [
    CompareAble('a', 45),
    CompareAble('b', 13),
    CompareAble('c', 12),
    CompareAble('d', 16),
    CompareAble('e', 9),
    CompareAble('f', 5),
]

r = haffmanCoding(freq)
print(r)
