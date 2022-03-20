# Hack 3: Fibonacci.  Write a recursive program to create a fibonacci sequence including error handling(with try/except) for invalid input
def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recur_fibonacci(n-1) + recur_fibonacci(n-2))

print("How many integers should this sequence be?")
nterms = input()
nterms = int(nterms)


try:
    if nterms >= 0:
        print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibonacci(i))
except:
    print("Plese enter a positive integer")