import sys

t = int(input())
for _ in range(t) :
    data = sys.stdin.readline().rstrip()
    a,b = map(int, data.split())
    print(a+b)
