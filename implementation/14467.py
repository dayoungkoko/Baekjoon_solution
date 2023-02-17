n = int(input())
lst = [-1]*10
result = 0

def cow(n, loc) :
    global lst, result
    if lst[n-1] == -1 :
        lst[n-1] = loc
    elif lst[n-1] != loc :
        result += 1
        lst[n-1] = loc
    
for _ in range(n) :
    num, loc = map(int, input().split())
    cow(num, loc)
print(result)    
