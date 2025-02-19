def find_min(numbers):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num
    return min

def find_max(numbers):
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

def find_mean(numbers):
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)

def find_mode(numbers):
    freq = dict()
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    max_freq = find_max(list(freq.values()))
    mode = [key for key, value in freq.items() if value == max_freq]
    return mode

def find_median(numbers):
    sorted_nums = sorted(numbers)
    length = len(numbers)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]

def find_range(numbers):
    range = find_max(numbers) - find_min(numbers)
    return range

def find_variance(numbers): #population variance
    mean = find_mean(numbers)
    total = 0
    n = len(numbers)
    for num in numbers:
        total += (num - mean) ** 2
    return total / n

def find_STD(numbers):
    variance = find_variance(numbers)
    return variance ** 0.5

def find_Quartiles(numbers):
    sorted_nums = sorted(numbers)
    length = len(sorted_nums)
    mid = length // 2
    Q2 = find_median(sorted_nums)

    if length == 1:
        return sorted_nums[0], sorted_nums[0], sorted_nums[0]
    
    if length % 2 == 0:
        Q1 = find_median(sorted_nums[:mid])
        Q3 = find_median(sorted_nums[mid:])
    else:
        Q1 = find_median(sorted_nums[:mid])
        Q3 = find_median(sorted_nums[mid + 1:])

    return Q1, Q2, Q3

def find_IQR(numbers):
    quartiles = find_Quartiles(numbers)
    Q1, _, Q3 = quartiles
    
    if len(numbers) == 1:
        return 0
    
    return Q3 - Q1



while True:
    try:
        numbers = input("Enter numbers separated by spaces: ,Enter E to end")
        if(numbers=="E" or numbers=="e"):
            print("Programm Ended")
            break
        elif not numbers:
            print("List cannot be empty.")
            continue
        numbers = list(map(int, numbers.split()))
        print("Min:", find_min(numbers))
        print("Max:", find_max(numbers))
        print("Mean:", round(find_mean(numbers), 2))
        print("Mode:", find_mode(numbers))
        print("Median:", find_median(numbers))
        print("Range:", find_range(numbers))
        print("Variance:", round(find_variance(numbers), 2))
        print("Standard Deviation:", round(find_STD(numbers), 5))
        print("Quartiles:", find_Quartiles(numbers))
        print("Interquartile Range (IQR):", find_IQR(numbers))
    except ValueError:
        print("Invalid input.")