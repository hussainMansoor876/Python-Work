def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1
lazy_range(4)