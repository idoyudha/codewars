def common_factors(int1, int2):
    first = []
    second = []
    for n in range(1, int1+1):
        if int1 % n == 0:
            first.append(n)
    
    for n in range(1, int2+1):
        if int2 % n == 0:
            second.append(n)

    # print(first, second)
    counter = 0
    for n in first:
        if n in second:
            counter += 1

    return counter

print(common_factors(10, 15))

inputnumber = '10 15'

print('s'+ str(2))