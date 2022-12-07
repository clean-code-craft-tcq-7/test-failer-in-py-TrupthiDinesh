def size(cms):
    if cms <= 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

assert(size(37) == 'S')
assert(size(43) == 'L')
assert(size(42) == 'L')
assert(size(41) == 'M')
assert(size(38) == 'S')

print("All is well (maybe!)\n")
