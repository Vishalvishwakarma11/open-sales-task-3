def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n - 10 + 1):  # Include n-10 in the loop
            out *= i
    else:
        lim = n - 20
        out = lim * lim
        out = out - lim
        if lim != 0:  # Avoid dividing by zero
            out = out / 2
    return out

n = int(input("Enter an integer: "))
result = compute(n)

print("Result:", result)
