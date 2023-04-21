import random    
N = int(input())
x = int(input())
lst = [random.randint(1, 100) for i in range(N)]
print(lst)
print(lst.count(x))
