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

    selected = 0

    s = []
    s.append((timeStart[selected], timeFinish[selected]))

    for i in range(1, n):
        if timeStart[i] >= timeFinish[selected]:
            selected = i
            s.append((timeStart[selected], timeFinish[selected]))

    return s

S = [1, 0, 3, 3, 5, 5, 6, 8, 8, 2, 12]
F = [4, 6, 5, 8, 7, 9, 10, 11, 12, 13, 14]

result = greedyEventSchedule(len(S), S, F)
print(len(result), result)

