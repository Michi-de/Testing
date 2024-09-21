sum = 0
for i in range(2,3002):
    print(str(i) + "+" + str(2))
    sum = sum + i + 2
print("Sum is: " + str(sum))


for i in range(3000):
    print(i)
    if i == 10:
        break

def sum_of_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum