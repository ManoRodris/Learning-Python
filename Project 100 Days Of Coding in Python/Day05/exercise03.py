number = int(input())
while number > 1000:
    print("Invalid input, please insert correctly")
    number = int(input())

total = 0

for i in range(1, number + 1):
    if i % 2 == 0:
        total += i

print(f"The sum of the even numbers between 1 and {number}: {total}")

