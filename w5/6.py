def first_n(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(first_n(1000)))