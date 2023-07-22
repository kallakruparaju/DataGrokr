def divisible_by_5_and_7(n):
    for num in range(n+1):
        if num % 5 == 0 and num % 7 == 0:
            yield num

n = int(input("Enter a number: "))
result = ", ".join(str(num) for num in divisible_by_5_and_7(n))

print("Numbers divisible by 5 and 7 between 0 and", n, "are:", result)
