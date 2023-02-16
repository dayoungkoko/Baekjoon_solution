import math

n = int(input())
if n == 2 :
    num1, num2 = map(int, input().split())
    gcd = math.gcd(num1, num2)
else :
    num1, num2, num3 = map(int, input().split())
    gcd = math.gcd(num1, num2, num3)

for i in range(1, gcd+1) :
    if gcd%i == 0 :
        print(i)
