def something(n):
    for i in range(n + 1):
        yield n ** i


print(list(something(15)))

for i in list(something(15)):
    print(i)
