import itertools
s = {'A', 'B', 'C', 'D'}
n = 1
a=2
b=3
c=4

def findsubsets(s, n):
    return [set(i) for i in itertools.combinations(s, n)]
def findsubsets(s, a):
    return [set(i) for i in itertools.combinations(s, a)]
def findsubsets(s, b):
    return [set(i) for i in itertools.combinations(s, b)]
def findsubsets(s, c):
    return [set(i) for i in itertools.combinations(s,c)]


 
print(findsubsets(s,n))
print(findsubsets(s,a))
print(findsubsets(s,b))
print(findsubsets(s,c))