import itertools
s = {1, 2, 3, 4}
x = 1
a=2
b=3
c=4

def findsubsets(s, x):
    return [set(i) for i in itertools.combinations(s, x)]
def findsubsets(s, a):
    return [set(i) for i in itertools.combinations(s, a)]
def findsubsets(s, b):
    return [set(i) for i in itertools.combinations(s, b)]
def findsubsets(s, c):
    return [set(i) for i in itertools.combinations(s,c)]


 
print(findsubsets(s,x))
print(findsubsets(s,a))
print(findsubsets(s,b))
print(findsubsets(s,c))