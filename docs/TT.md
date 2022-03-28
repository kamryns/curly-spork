{% include navigation.html %}
### [Github](https://github.com/kamryns/curly-spork) 
### [Replit](https://replit.com/@kamryns1/curly-spork#.replit)

<iframe height="1000px" width="800px" src="https://replit.com/@kamryns1/curly-spork?lite=true#menu.py"></iframe>

## TT2 Factorial


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
    
## TT2 Factors
number = int(input("What number do you want to find the factors of? "))
def findFactors(number):
    print("Factors of a Given Number {0} are:".format(number))
    for value in range(1, number + 1):
        if number % value == 0:
            print("{0}".format(value), end=" ")
    print()
findFactors(number)

class Factors:
    def __init__(self):
        self.factors = []

    def __call__(self,number):
        for value in range(1, number + 1):
            if number % value == 0:
                self.factors.append(value)
        return self.factors

def tester():
    n = int(input("What number do you want to find the factors of? "))
    fac_of = Factors()
    print(fac_of(n))

if __name__ == "__main__":
    tester()

## TT1 InfoDb


`InfoDb = []`

`InfoDb.append({
"FirstName": "Kamryn",
"LastName": "Sinsuan",
"Grade": "11th",
"Classes":["Photography 2","APEL","AP Calc","APCSP", "US History 2"]
})`

`InfoDb.append({
"FirstName": "Khloe",
"LastName": "Sinsuan",
"Grade": "7th",
"Classes":["PE","Language Arts","Math","Social Studies", "Science", "Art"]
})`


`def print_data(n):`

`print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
print("\t", "Schedule: ", end="")  
print(", ".join(InfoDb[n]["Classes"])) 
print()`

`def for_loop():
for n in range(len(InfoDb)):
print_data(n)`

`def while_loop(n):
while n < len(InfoDb):
print_data(n)
n += 1
return`

`def recursive_loop(n):
if n < len(InfoDb):
print_data(n)
recursive_loop(n + 1)
return # exit condition`

`def tester():
print_data(0)
print_data(1)
print("For loop")
for_loop()
print("While loop")
while_loop(0)  # requires initial index to start while
print("Recursive loop")
recursive_loop(0)  # requires initial index to start recursion`

`if __name__ == "__main__":
tester()`

## TT1 Fibonacci

`def recur_fibonacci(n):`

`if n <= 1:
return n
else:
return(recur_fibonacci(n-1) + recur_fibonacci(n-2))`

`print("How many integers should this sequence be?")`

`nterms = input()
nterms = int(nterms)`


`try:`

`if nterms >= 0:
print("Fibonacci sequence:")
for i in range(nterms):
print(recur_fibonacci(i))
except:
print("Plese enter a positive integer")`

## TT0 Menu
`menu = [`

`["1. Swap", "swap.py"],
["2. Matrix", "matrix.py"],
["3. Exit"],
]`

`if __name__ == "__main__":`

`while True:
for i in range(len(menu)):
print(menu[i][0])
print("Select an Option:")
userInput = input("")`

        if userInput == "swap" or userInput == "1":
            print(" ")
            #swap.swap_test(a, b)
            a = input("First Number:")
            b = input("Second number:")
            if a > b:
                print(b, a)
            else:
                print(a, b)

        elif userInput == "matrix" or userInput == "2":
            print(" ")
            #matrix.matrix_test()
            matrix = [ [1,2,3],[4,5,6],[7,8,9] ]
            for row in matrix:
                for col in row:
                    print(col, end="")
                print()
        elif userInput == "exit" or userInput == "3":
            exit()
        else:
            print("Enter a valid input")
        print("   ")

## TT0 Animation
`from time import sleep`

`def printRocket():
print(
"""
_
/^\\
|-|
| |
|N|
|A|
|S|
|A|
/| |\\
/ | | \\
|  | |  |`
`-\\"\\"\\"-`
""")

`printRocket()`

`delay = 300
for i in range(60):
print()
sleep(delay/1000)
delay = delay * 0.9`

`printRocket()`




