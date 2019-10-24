'''
活动安排问题
'''
from queue import PriorityQueue as PQueue

class TimeCompareAble:
    def __init__(self, start, finish):
        self.start  = start
        self.finish = finish

    # 这里是按python3语法，定义的 < 方法
    def __lt__(self, other):
        if self.finish <= other.finish:
            return True
        else:
            return False

def greedyEventSchedule(n, timeStart, timeFinish):
    pq = PQueue()
    for i in range(n):
        time = TimeCompareAble(timeStart[i], timeFinish[i])
        pq.put(time)

    # 记录已安排活动的最后结束时间
    lastFinishTime = 0
    s = []
    while pq.qsize() > 0:
        time = pq.get()
        if time.start >= lastFinishTime:
            s.append(time)
            lastFinishTime = time.finish
            print(time.start, time.finish)

    return s

#
S = [1, 0, 3, 3, 5, 5, 6, 8, 8, 2, 12]
F = [4, 6, 5, 8, 7, 9, 10, 11, 12, 13, 14]

result = greedyEventSchedule(len(S), S, F)
print(len(result))

