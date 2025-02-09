if __name__ == '__main__':
    n=int(input())
    scores= list( map( int,input().split()) )
    # find second largest
    firstMax =float('-inf')
    secMax =float('-inf')
    for i in range(n):
        curr =  scores[i]
        if( curr > firstMax):
            secMax = firstMax
            firstMax = curr
        elif(curr > secMax and curr < firstMax):
            secMax = curr

    print(int(secMax))