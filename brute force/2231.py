n = int(input())

def divide_sum(n) :
    for num in range(1, n) :
        result = 0
        for i in range(len(str(num))) :
            result+= int(str(num)[i])
        if result + num == n :
            return num
    return 0

answer = divide_sum(n)
print(answer)
