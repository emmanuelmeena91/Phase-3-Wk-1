def integers(a, b, c):
    count = 0

    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1

    return count == 2

print(integers(2 , 4 , -3))
print(integers(-4, 6, 0))