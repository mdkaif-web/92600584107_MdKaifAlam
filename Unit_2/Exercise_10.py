def generate_numbers(n):
    for i in range(1,n+1):
        yield i

nums=generate_numbers(10)

for num in nums:
    print(num)