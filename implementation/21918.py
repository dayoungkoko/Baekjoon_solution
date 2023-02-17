n, m = map(int, input().split())
s = list(map(int, input().split()))

def bulb(case, left, right) :
    global s
    if case == 1 :
        s[left-1] = right
    elif case == 2 :
        for i in range(left-1, right) :
            s[i] = int(not s[i])
    elif case == 3 :
        for i in range(left-1, right) :
            s[i] = 0
    else :
        for i in range(left-1, right) :
            s[i] = 1
    
for _ in range(m) :
    a, b, c = map(int, input().split())
    bulb(a, b, c)
    
print(*s)
