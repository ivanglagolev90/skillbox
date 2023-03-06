def calculating_math_func(data):
    for i in range(data, 0, -1):
        if i in factorials:
            result = factorials[i]
            break
    print(result)
    print(factorials)
    for index in range(i + 1, data + 1):
        result *= index
        factorials[index] = result
    result /= data ** 3
    result = result ** 10
    return result

factorials = {1: 1}

print(calculating_math_func(20))