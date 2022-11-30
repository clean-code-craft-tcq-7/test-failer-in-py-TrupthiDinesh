
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
def get_number(majorColor, minorColor):
    return major_colors.index(majorColor) * 5 + minor_colors.index(minorColor)
def print_color_map():
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)

result = print_color_map()
assert(result == 25)
assert(get_number("White", "Blue") == 1)
print("All is well (maybe!)\n")
