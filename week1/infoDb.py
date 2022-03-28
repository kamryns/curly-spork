
InfoDb = []
# List with dictionary records placed in a list
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars
InfoDb.append({
    "FirstName": "Kamryn",
    "LastName": "Sinsuan",
    "Grade": "11th",
    "Classes":["Photography 2","APEL","AP Calc","APCSP", "US History 2"]
})

InfoDb.append({
    "FirstName": "Khloe",
    "LastName": "Sinsuan",
    "Grade": "7th",
    "Classes":["PE","Language Arts","Math","Social Studies", "Science", "Art"]
})

# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Schedule: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Classes"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
## hack 2b: def while_loop(0)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
## hack 2c : def recursive_loop(0)
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def tester():
    print_data(0)
    print_data(1)
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

if __name__ == "__main__":
    tester()