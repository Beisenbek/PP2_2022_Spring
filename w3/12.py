def run(boost):
    return lambda step: print(1) if (step == 1) else print(boost * 3)
    
x = run(boost = 4)
x(step = 2)