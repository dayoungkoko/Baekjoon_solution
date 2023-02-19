import sys
n = int(input())
stk = []

for _ in range(n) :
    order = sys.stdin.readline().rstrip()
    
    if 'push' in order :
        stk.append(int(order[5:]))
    elif order == 'pop' :
        if stk : 
            print(stk.pop())
        else :
            print(-1)
    elif order == 'size' :
        print(len(stk))
    elif order == 'empty' :
        if stk :
            print(0)
        else :
            print(1)
    else :
        if stk :
            print(stk[-1])
        else :
            print(-1)
