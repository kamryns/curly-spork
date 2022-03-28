class Factorial:
    def __init__(self):
        self.facSeq = [0, 1]

    def __call__(self, n):
        if n < len(self.facSeq):
            return self.facSeq[n]
        else:
            # Compute the requested Factorial number
            fac_number = n * self(n-1) # two recursive calls to self (__call__(self, n))
            self.facSeq.append(fac_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.facSeq[n]

def tester():
    n = int(input("How many integers should this sequence be? "))
    fac_of = Factorial() # object instantiation and run __init__ method
    print(fac_of(n)) # object running __call__ method

if __name__ == "__main__":
    tester()