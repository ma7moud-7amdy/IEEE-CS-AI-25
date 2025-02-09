if __name__ == '__main__':
    commands=[]
    arr=[]
    n = int(input())
    for _ in range(n):
        commands.append( input().split() )

    for text in commands:
        match(text[0]):
            case "insert":
                arr.insert(int(text[1]) , int(text[2]))
            case "print":
                print(arr)
            case "remove":
                arr.remove(int(text[1]))
            case "append" :
                arr.append(int(text[1]))
            case "sort":
                arr.sort()
            case "pop":
                arr.pop()
            case "reverse":
                arr.reverse()