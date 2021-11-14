def number(num, end):
    while num < end:
        yield num ** 2
        num += 1


g = number(2, 12)

for item in g:
    print(item)
    