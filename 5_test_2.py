from queue import PriorityQueue as PQueue

def chooseApple(numbers):
    pq = PQueue()
    for n in numbers:
        pq.put(n)

    while pq.qsize() > 1:
        n1 = pq.get()
        n2 = pq.get()

        pq.put(n1+n2)

    return pq.get()


n = int(input())
line = input().split(" ")

numbers = []
for i in range(n):
    numbers.append(int(line[i]))

print(chooseApple(numbers))
