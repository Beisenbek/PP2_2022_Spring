def myfunc():
  global x
  x = 300

def f2():
    global x
    x = x * 2

myfunc()
print(x)

f2()
print(x)