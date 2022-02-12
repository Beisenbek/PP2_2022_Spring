def myfunc(n):
  return lambda a : list(map(print,a))

mydoubler = myfunc(2)
print(mydoubler([11, 12]))