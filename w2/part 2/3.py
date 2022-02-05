'''
items = input().split()
projection = map(int, items)
a = list(projection) 
'''
memory = []

def f(a, c):
    if memory[c] == -1:
        if(c >= len(a) - 1): memory[c] = 1
        else:
            found = False
            for i in range(1, a[c] + 1):
                if f(a, c + i) == 1:
                    memory[c] = 1
                    found = True
                    break

            if not found: memory[c] = 0
        
    return memory[c]


a = list(map(int, input().split()))

for i in range(len(a)):
    memory.append(-1)

print(f(a, 0))
    
    



       
        