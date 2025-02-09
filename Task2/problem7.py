def findCommon(set1, set2):
    return set1.intersection(set2) 

# Example usage
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

result = findCommon(set_a, set_b)
print("Common Elements:", result)
