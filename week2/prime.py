class primeNumbers:
    def __init__(self):
        pass
    def __call__(self, min, max):
      print("Results:")
      for Number in range(min, max + 1):
              count = 0
              for i in range(2, (Number // 2 + 1)):
                  if (Number % i == 0):
                      count = count + 1
                      break
              if (count == 0 and Number != 1):
                  print(" %d" % Number, end='  ')

def tester():
  primes_of = primeNumbers() # object instantiation and run __init__ method
  print(primes_of(min, max)) # object running __call__ method
  if __name__ == "__main__":
    tester()
  
