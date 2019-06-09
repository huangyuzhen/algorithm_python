'''
石头移动问题，优化

'''

stones = (0, 4, 5, 8, 10)

def Validate(d):
    global stones
    k = 2
    start = 0
    n = len(stones)

    end = 1
    while end < n:
        distCur = stones[end] - stones[start]
        # print(distCur)
        while distCur < d:
            # 需要移除第en个石头
            k -= 1 #个数
            if k < 0:
                return False

            end += 1
            if end >= n:
                if start == 0:
                    return False
                else:
                    return True

            distCur = stones[end] - stones[start]

        start = end
        end += 1

    return True


lb = 0
ub = 60
while ub > lb:
    mid = int((lb+ub)//2)
    # 因为除法运算向下取整，当lb与ub差1，会造成mid = lb,出现死循环
    if mid == lb:
        mid += 1

    if Validate(mid):
        lb = mid
    else:
        ub = mid - 1
else:
    print("lb=", lb)
    print("ub=", ub)


'''
Validate O(n)
复杂度 O(n*log(n))
'''
