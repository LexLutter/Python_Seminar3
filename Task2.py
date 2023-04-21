import random    
N = int(input())
x = int(input())
lst = [random.randint(1, 100) for i in range(N)]
print(lst)
print(min(lst, key = lambda i: abs(i-x)))