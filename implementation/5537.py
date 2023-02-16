lst = [False] * 30
for _ in range(28) :
    lst[int(input())-1] = True
for i in range(30) :
    if lst[i] == False :
        print(i+1)
