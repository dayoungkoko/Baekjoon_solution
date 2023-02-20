n, m = map(int, input().split())
lst = list(map(int, input().split()))

def blackjack(num, limit) :
    result = []
    for i in range(num-2) :
        for j in range(i+1, num-1) :
            for k in range(j+1, num) :
                if lst[i]+lst[j]+lst[k] <= limit :
                    result.append( lst[i] + lst[j] + lst[k] )
    return max(result)
        
answer = blackjack(n, m)
print(answer)
