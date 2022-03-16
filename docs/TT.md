{% include navigation.html %}
#[Github](https://github.com/kamryns/curly-spork)
#[Replit](https://replit.com/@kamryns1/curly-spork#.replit)

# TT0 Menu
menu = [ </br>
["1. Swap", "swap.py"], </br>
["2. Matrix", "matrix.py"], </br>
["3. Exit"], </br>
] </br>

if __name__ == "__main__": </br>
while True: </br>
for i in range(len(menu)):</br>
print(menu[i][0])</br>
print("Select an Option:")</br>
userInput = input("")</br>

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
from time import sleep

def printRocket(): </br>
print( </br>
""" </br>
 _</br>
/^\\</br>
|-|</br>
| |</br>
|N|</br>
|A|</br>
|S|</br>
|A|</br>
/| |\\</br>
/ | | \\</br>
|  | |  |</br>
`-\\"\\"\\"-`</br>
""")</br>

printRocket()

delay = 300</br>
for i in range(60):</br>
print()</br>
sleep(delay/1000)</br>
delay = delay * 0.9</br>

printRocket()
