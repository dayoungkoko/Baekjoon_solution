from collections import deque
import sys

n = int(input())
queue = deque([])
for _ in range(n) :
    order = sys.stdin.readline().rstrip()
    if 'push' in order :
        queue.append(order[5:])
    elif order == 'pop' :
        if not queue :
            print(-1)
        else : 
            num = queue.popleft()
            print(num)
    elif order == 'size' :
        print(len(queue))
    elif order == 'empty' :
        if queue :
            print(0)
        else :
            print(1)
    elif order == 'front' :
        if not queue :
            print(-1)
        else :
            print(queue[0])
    else :
        if not queue :
            print(-1)
        else :
            print(queue[-1])
