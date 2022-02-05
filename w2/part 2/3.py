'''
items = input().split()
projection = map(int, items)
a = list(projection) 
'''
def f(a, c):
    if(c >= len(a)):
         return "1"

    for i in range(1, a[c] + 1):
        if f(a, c + i) == "1":
            return "1"
    
    return "0"

a = list(map(int, input().split()))

print(f(a, 0))
    
    



       
        