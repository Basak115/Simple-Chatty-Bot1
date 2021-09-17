def closest_higher_mod_5(x):
    while True:
        remainder = x % 5
        if remainder == 0:
            return x
        x += 1
