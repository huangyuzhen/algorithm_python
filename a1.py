'''

'''


repairTime = (8,12,14,18,20,24,30)

solution = ['0'] * 7
count = 0
minTime = 999999

def backtrack(t, n):
    global count
    global minTime
    if t >= n:
        count += 1
        usedTime = checkTime(solution)
        if usedTime <= minTime:
            print(usedTime, solution)
            minTime = usedTime
        return
    else:
        solution[t] = 'A'
        backtrack(t+1, n)

        solution[t] = 'B'
        backtrack(t+1, n)

        solution[t] = 'C'
        backtrack(t+1, n)

def checkTime(solution):
    A = []
    B = []
    C = []

    for i in range(len(solution)):
        person = solution[i]
        if person == 'A':
            A.append(i)
        elif person == 'B':
            B.append(i)
        else:
            C.append(i)

    usedTime = 0
    for i in range(len(A)):
        time = repairTime[A[i]]
        usedTime += time * (len(A) - i)

    for i in range(len(B)):
        time = repairTime[B[i]]
        usedTime += time * (len(B) - i)

    if (len(C)) > 0:
        for i in range(len(C)):
            time = repairTime[C[i]] / 2
            if i > 0:
                usedTime += (time+10) * (len(C)-i)
            else:
                usedTime += time * (len(C) - i)

    return usedTime


backtrack(0, len(repairTime))

print(count, minTime)
