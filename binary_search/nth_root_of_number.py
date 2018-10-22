def findNthRoot(x, n):
    # Initialize boundary values
    x = float(x)
    n = int(n)

    if (x >= 0 and x <= 1):
        low = x
        high = 1
    else:
        low = 1
        high = x

    # used for taking approximations of the answer
    epsilon = 0.00000001

    # Do binary search
    guess = (low + high) / 2
    while abs(guess**n - x) >= epsilon:
        if guess ** n > x:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2
    print(guess)


# Python Program to find n-th real root of x
# Driver code
x = 5
n = 2
findNthRoot(x, n)
