'''
小数背包，贪心算法
优先装单位重量价值最高的物品
'''

Value = (25, 24, 15)
Weight = (18,15,10)


def greedyKnapsack(n, capacity):
    itemList = []
    for i in range(n):
        item = {
            "v": Value[i],
            "w": Weight[i]
        }
        itemList.append(item)

    itemList.sort(key = lambda x: x['v'] / x['w'], reverse = True)

    answer = 0
    for i in range(n):
        item = itemList[i]
        if capacity >= item['w']:
            answer   += item['v']
            capacity -= item['w']
        else:
            answer += capacity * (item['v'] / item['w'])
            break

    return answer

n = len(Value)
L = greedyKnapsack(n, 20)

print(L)
