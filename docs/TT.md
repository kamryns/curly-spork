{% include navigation.html %}
### [Github](https://github.com/kamryns/curly-spork) 
### [Replit](https://replit.com/@kamryns1/curly-spork#.replit)
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@kamryns/curly-spork?lite=true"></iframe>
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




