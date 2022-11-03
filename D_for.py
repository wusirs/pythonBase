count = 0
for i in "hello":
    if i == 'l':
        count += 1
print(f"'hello'中共有{count}个'l'")

for i in range(10):
    print(i, end=" ")
print()

for i in range(2, 6):
    print(i, end=" ")
print()

count_even = 0
for i in range(2, 100, 2):
    count_even += 1
print(f"1~100有{count_even}个偶数")

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i} = {j * i}\t", end=" ")
    print()

