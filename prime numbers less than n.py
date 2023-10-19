n = int(input("Enter an integer n: "))
print(f"The prime numbers less than {n} are:")
for i in range(2, n):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
