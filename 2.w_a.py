def calcLuckyNumber(x):
    resultSet = set()
    for i in range(30):
        for j in range(30):
            for k in range(30):
                number = pow(3, i) * pow(5, j) * pow(7, k)
                if number > 1 and number <= x:
                    resultSet.add(number)

    return resultSet

x = input("input number: ")
if x != '':
    x = int(x)
    if x > 0:
        result = calcLuckyNumber(x)
        print(len(result))
        print(sorted(result))
