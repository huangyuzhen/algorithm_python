'''
排列组合问题, 从n个元素取m个进行排列
'''
import itertools

def Perm_k(arrs, k):
    length = len(arrs)
    if length == 1:
        return [arrs]

    if k == 1:
        return list(map(lambda s:[s], arrs))  #  当 k 为 1 时，每(单)个元素都可以被选取

    result = []  # 最终的结果（即全排列的各种情况）
    for i in range(length):
        current = arrs[i]
        rest_arrs = arrs[:i] + arrs[i+1:]    # 取出arrs中的第 i个元素后剩余的元素
        rest_lists = Perm_k(rest_arrs, k-1)  # 剩余的元素选取 k-1元素

        lists = []
        for term in rest_lists:
            term.insert(0, current)
            lists.append(term)
        result += lists
    return result


L = [1, 2, 3, 4]

P = Perm_k(L, 3)
print(P)


P2 = list(itertools.permutations(L, 3))
print(P2)