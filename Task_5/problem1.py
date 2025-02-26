def process_data(count):

    total_count = sum(count) 
    for i in range(0,256):
        if(count[i] > 0):
            min_val = i
            break
    for i in range(255, -1, -1):
        if(count[i] > 0):
            max_val = i
            break

    # mean
    total_sum = 0
    for i in range(0,256):
        total_sum += i * count[i]
    mean = total_sum / total_count

    # median
    mid1 = (total_count - 1) // 2
    mid2 = total_count // 2
    median = None
    freq_sum = 0
    for i in range(256):
        freq_sum += count[i]
        if freq_sum > mid1 and median is None:
            median = i  # First middle element
        if freq_sum > mid2:
            median = (median + i) / 2
            break

    # mode
    maxfreq = -1
    for i in range(0,256):
        if(count[i] > maxfreq):
            maxfreq = count[i]
            mode = i

    return [float(min_val), float(max_val), float(mean), float(median), float(mode)]


count = list(map(int, input().split()))

# Ensure valid input length
if len(count) != 256:
    print("Error: You must enter exactly 256 numbers.")
else:
    # Compute and display results
    result = process_data(count)
    print(result)
