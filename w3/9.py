def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
triple = myfunc(3)

print(mydoubler(11))
print(triple(11))