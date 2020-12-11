
a = int(input("a"))
b = int(input("B"))
result = 0

# not a good solution
# print(sum(range(a, b, 2)))

for x in range(a,b+1):
    if x % 2 != 0:
        result += x
print(result)

