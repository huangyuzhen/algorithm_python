'''
活动安排问题
'''

def greedyEventSchedule(n, timeStart, timeFinish):
    # sort
    for i in range(n):
        for j in range(n-1):
            if timeFinish[j] > timeFinish[j+1]:
                timeFinish[j], timeFinish[j+1] = timeFinish[j+1], timeFinish[j]
                timeStart[j], timeStart[j+1] = timeStart[j+1], timeStart[j]

    # 记录已安排活动的最后结束时间
    lastFinishTime = 0

    s = []
    for i in range(n):
        if timeStart[i] >= lastFinishTime:
            s.append((timeStart[i], timeFinish[i]))
            lastFinishTime = timeFinish[i]

    return s

S = [1, 0, 3, 3, 5, 5, 6, 8, 8, 2, 12]
F = [4, 6, 5, 8, 7, 9, 10, 11, 12, 13, 14]

result = greedyEventSchedule(len(S), S, F)
print(len(result), result)

