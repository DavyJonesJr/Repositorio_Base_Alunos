a = 80000
b = 200000
anos = 0

while a < b:
    a += a * (3/100)
    b += b * (1.5/100)
    anos += 1

print(anos)