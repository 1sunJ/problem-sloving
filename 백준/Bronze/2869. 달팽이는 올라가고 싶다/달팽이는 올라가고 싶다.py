import math

a, b, c = map(int, input().split())

df = a - b

print(math.ceil((c-a) / df) + 1)