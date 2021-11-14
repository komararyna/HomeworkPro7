def simple(end):
    num = 1
    k = 0
    while num < end:
        for item in range(2, 6):
            if num % item == 0:
                break
        else:
            yield num
        num += 1


g = simple(100)
for item in g:
    print(item)
