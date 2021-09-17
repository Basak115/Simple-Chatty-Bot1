a = int(input())
year = 0
while 50000 <= a <= 700000:
    b = a * 7.1 / 100
    a += b
    year += 1
print(year)
