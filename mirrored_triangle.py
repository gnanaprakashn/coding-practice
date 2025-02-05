def mirrored_reflections_triangle(size):
    # Upper part of the pattern
    for i in range(1, size + 1):
        print(" " * (size - i) + "* " * i)
    
    # Lower part of the pattern
    for i in range(size, 0, -1):
        print(" " * (size - i) + "* " * i)


size = 7
mirrored_reflections_triangle(7)
