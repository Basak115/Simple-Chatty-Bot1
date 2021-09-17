a = int(input())
b = int(input())
h = int(input())
if h >= a and h <= b:
    print("Normal")
else:
    if h < a:
        print("Deficiency")
    else:
        print("Excess")
