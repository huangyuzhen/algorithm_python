from queue import PriorityQueue as PQueue

def chooseApple(numbers):
    ans = 0
    pq = PQueue()
    for n in numbers:
        pq.put(n)

    while pq.qsize() > 1:
        n1 = pq.get()
        n2 = pq.get()

        ans += n1+n2
        pq.put(n1+n2)

    return ans


n = int(input())
line = input().split(" ")

numbers = []
for i in range(n):
    numbers.append(int(line[i]))

print(chooseApple(numbers))
