'''
全排列问题
给定一组互不相同的字符，求这组字符的全排列
用递归实现
复杂度 n的阶乘
O(n!)
'''

result = []

# def permutations(aString, head = ''):
#     l = len(aString)
#     if l <= 1:
#         s = head + aString
#         result.append(s)
#         return

#     for i in range(l):
#         h = head + aString[i]
#         if i == 0:
#             a = aString[1:]
#         elif i == l -1:
#             a = aString[:-1]
#         else:
#             a = aString[:i] + aString[i+1:]
#         permutations(a, h)


def permutations(string, i, n):
    if i == n-1:
        s = ''.join(string)
        result.append(s)
        return

    for j in range(i,n):
        string[i], string[j] = string[j], string[i]
        permutations(string, i+1, n)
        string[i], string[j] = string[j], string[i]

s = 'ABC'
permutations(list(s), 0, 3)

print('length', len(result))
print(result)
