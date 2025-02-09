if __name__ == '__main__':
    n=int(input())
    records=[]
    for _ in range(n):
        name = input()
        score = float(input())
        records.append([name , score])
    # find second lowest
    lowest = float('inf')
    secLowest = float('inf')
    for i in range(n):
        curr =  records[i][1]
        if( curr < lowest):
            secLowest = lowest
            lowest = curr
        elif(curr < secLowest and curr != lowest):
            secLowest = curr

    #select students
    selected = []
    for std in records:
        if(std[1] == secLowest):
            selected.append(std[0])

    selected.sort()
    for name in selected:
        print(name)