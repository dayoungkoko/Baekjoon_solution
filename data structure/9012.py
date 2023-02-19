t = int(input())

def vps(lst) :
    stk = []
    for i in range(len(lst)) :
        if not stk :
            stk.append(lst[i])
        elif stk[-1] == '(' and lst[i] == ')' : 
            stk.pop()
        else :
            stk.append(lst[i])
    return 'NO' if stk else 'YES'
    
for _ in range(t) :
    data = list(input())
    result = vps(data)
    print(result)
