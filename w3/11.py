def move(step = 1):
    print(step)

def run(boost):
    if boost == 1:
        move(1)
    else: 
        move(boost * 3)
    

run(3)