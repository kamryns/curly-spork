### Review Ticket
[Week 0](https://github.com/kamryns/curly-spork/issues/2)
### Replit
[Kamryn's Replit](https://replit.com/@kamryns1/curly-spork#.replit)

### TPT 0.2
***

* The Digital Divide: the gap between people who have easy access to technology and those who don't
* Some contributing factors to the digital divide are socioeconomic, geographic, and demographic
* Individuals may have less access to latest updates
* In our environment, Del Norte CS preference is that you have your own computer, which can cause inequity issues

<table id="readmeinformation">

<tr>
<th>Question</th>
<th>Answer</th>
</tr>

<tr>
<td>How does someone empower themself in a digital world?</td>
<td>
Digital empowerment allows people to reach their full potential in a networked society. People can empower themselves in the digital world by investing time into expanding their knowledge of technology. From then on, students can use their existing knowledge to participate in the digital world, and even continue building on it.
</td>
</tr>

<tr>
<td>How does someone that is empowered help someone that is not empowered? Describe something you could do at Del Norte HS.</td>
<td>
Someone who is empowered in the digital world could help someone who is not by passing on their own knowledge to them. This could simply be done by answering any questions they might have, which is already tremendous guidance. However, something that could be done at greater level would be to start a club, at Del Norte for example, that is specifically dedicated to empowering people in the digital world.
</td>
</tr>

<tr>
<td>Is paper or red tape blocking digital empowerment? Are there such barriers at Del Norte? Elsewhere?</td>
<td>
The "paper/red tape" that is blocking digital empowerment is the digital divide, where not everyone has equal access to technology. These barriers can most often be seen in poorer places, and can be seen within Del Norte. Our high school encourages students to bring their own laptops/devices to school, but this may not be possible for some students. 
</td>
</tr>
  
</table>


### TPT 0.1
***
* UAVs/Drones are used in search & rescue, aerial photography, and for hobbies, but it also has unintended uses
* Dopamine plays a role in how we feel pleasure, can have posititve and negative effects
* Some people's computer time may be greater than their sleep time
* Innovations in phone trees, voice recognition, or keypads often enables efficient service

<table id="readmeinformation">

<tr>
<th>Question</th>
<th>Answer</th>
</tr>

<tr>
<td>Come up with three of your own Beneficial and corresponding Harmful Effects of Computing.</td>
<td> Computing is beneficial because it is more efficient, it is more accurate, and opens up a world of opportunities for people. However, it is harmful because it can become invasive, addicting, and distracting if used in the wrong ways.
</td>
</tr>

<tr>
<td>Talk about dopamine issues above. Real? Parent conspiracy? Anything that is impacting your personal study and success in High School?</td>
<td>
Dopamine is what allows people to feel pleasure. While it can be a positive experience for people, it can also have a negative impact on their mental and physical healths, as dopamine is addictive. For me, getting good grades is my source of dopamine that keeps me constantly feeling the need to do well in school. At times it can really affect my mental health, but when I get good grades, it is so worth it.
</td>
</tr>

</table>

### TT 0.0
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
   
from time import sleep

def printRocket():
    print(
        """ </br>
                   _
                  /^\\ </br>
                  |-| </br>
                  | | </br>
                  |N| </br>
                  |A| </br>
                  |S| </br>
                  |A| </br>
                 /| |\\ </br>
                / | | \\ </br>
               |  | |  | </br>
               `-\\"\\"\\"-` </br>
        """)

printRocket()

delay = 300
for i in range(60):
    print()
    sleep(delay/1000)
    delay = delay * 0.9

printRocket()


### Create Task
[Plan](https://github.com/sarayu-pr11/team-narks/wiki/Kamryn's-Create-Task) </br>
[Runtime Video](https://www.loom.com/share/4e2beeba2ce04d32ad07f629e0d4fe1c) </br>
[Code](https://github.com/sarayu-pr11/team-narks/blob/main/templates/wordle.html)

