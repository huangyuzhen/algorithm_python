'''
排列组合,全排列
递归实现与使用itertools实现
'''

import itertools

def Perms(arrs):
    length = len(arrs)
    if length == 1:
        return [arrs]

    result = []
    for i in range(length):
        current = arrs[i]
        rest_arrs = arrs[:i]+arrs[i+1:]  # 取出arrs中的第 i个元素后剩余的元素
        rest_lists = Perms(rest_arrs)     # 剩余的元素完成全排列,递归调用

        lists = []
        for term in rest_lists:
            term.insert(0, current)
            lists.append(term)
        
        result += lists
    return result

# 测试用例
L = [1, 2, 3]

P = Perms(L)
print(P)

P2 = list(itertools.permutations(L, len(L)))
print(P2)
