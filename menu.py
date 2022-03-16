menu = [
    ["1. Swap", "swap.py"],
    ["2. Matrix", "matrix.py"],
    ["3. Exit"],
]

if __name__ == "__main__":
    while True:
        for i in range(len(menu)):
            print(menu[i][0])
        print("Select an Option:")
        userInput = input("")

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