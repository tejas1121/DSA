i = 0
j = len(numbers) - 1

while i < j:
    value = numbers[i] + numbers[j]
    if target < value:
        j -= 1
    elif target > value:
        i += 1    
    else:
        return [i + 1, j + 1]