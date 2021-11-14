def number(num, end):
    div = 1
    while div < end:
        yield div * num
        div = div * num


x = number(3, 14)
for item in x:
    print(item)
