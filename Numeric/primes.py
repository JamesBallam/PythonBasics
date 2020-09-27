"""Print prime numbers in the range 0 to 100."""


# Loop i from 2 to 100 (inclusive)
for i in range(2, 101):
    # Start by assuming the number is a prime
    prime = True

    # Loop j from 2 up to (but not including) i
    for j in range(2, i):
        # Test if j evenly divides i
        if i % j == 0:
            # j evenly divides i, therefore i cannot be a prime number.
            # Indicate this isn't a prime and break out of the j loop
            prime = False
            break

    # If j is a prime number (not evenly divisable by any integer in
    # the range 2 .. i-1) then print it
    if prime:
        print(i)
