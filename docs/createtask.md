{% include navigation.html %}

# My Plan
My create task idea is a recreation of the trending game "Wordle," where users have 6 attempts to guess one random five-letter word everyday. But I want to incorporate different themes or categories of words, and make it so users can play as many times as they want throughout the day. My code will meet Collegeboard's criteria by including the following:

# Requirements
1.  Instructions for input from the user, a device, an online data stream, OR a file
* Takes input from a user by asking them to try out different letters in order to figure out what the random word is
2.  At least one list to represent a collection of stored data
* List to generate random words that will be guessed by a user
* List to store the all of the letters attempted by a user
3.  At least one procedure that contributes to the program's intended purpose that defines procedure name, return type, AND one or more parameters
* Procedure to check if the word guessed by user has any correct letters/letter in the correct spot when compared to the actual word
* Procedure to  select a random word from the list for a user to guess
4.  An algorithm that includes, sequencing, selection, AND iteration
* Sequencing - The program needs to first generate the random word. Then it must take the input of a user. After it gets the inputs, it can use if statements to check the logic, and for loops to make it more efficient. If the user gets it in 6 or less tries, they win. If not, they lose.
* Selection - If Statements to check if the letters in the guessed word exist or match the letters in the real world
* Iteration -  For Loops to compare each individual letter entered by user (which will be stored in a list) against the letters of the correct word
5.  Calls to your student-developed procedure
* The program could use an "on-click" call in the HTML portion in order trigger the procedure
* When the user inputs their word by clicking an "ENTER" button, it will call the procedure which compares each of the user's letters to the word's letter
6.  Instructions for output based on input and program functionality
* If the user wins, the program will display an output of a banner that says "Congratulations, you won!" with an upbeat sound effect.
* If the user loses, the program will display an output of a banner that says "Sorry, you lost." with a somber sound effect.


# Written Response

3 a. Provide a written response that does all three of the following: Approx. 150 words (for all subparts of 3a combined): <br/>
i. Describes the overall purpose of the program <br/>
The overall purpose of the program is to provide entertainment for people. It is a recreation of the trending game Wordle, where people have 6 attempts to guess a 5-letter word. People can use this program when they are bored and looking for a quick, but still engaging and fun challenge. <br/>
ii. Describes what functionality of the program is demonstrated in the video <br/>
The program contains a variety of different 5-letter words chosen at random, which the user will try to guess. It tells them which of their guessed letters are actually there/in the right spot and which ones are not by checking each tile against the real word. If the user gets the correct word in 6 or less tries, they have won. <br/>
iii. Describes the input and output of the program demonstrated in the video <br/>
The user inputs 5-letter words by clicking the keyboard tiles. If they win the game, there will be an output message letting them know they’ve won, if they lose, there will be a message acknowledging they’ve lost.


3 b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program. Approx. 200 words (for all subparts of 3b combined, exclusive of program code) <br/>
i. The first program code segment must show how data have been stored in the list. <br/>
const keys = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', <br/>
'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'ENTER', <br/>
'Z', 'X', 'C', 'V', 'B', 'N', 'M', '«', <br/>
]<br/>
ii. The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. Then, provide a written response that does all three of the following: <br/>
keys.forEach(key => { <br/>
const buttonElement = document.createElement('button') <br/>
buttonElement.textContent = key <br/>
buttonElement.setAttribute('id', key) <br/>
buttonElement.addEventListener('click', () => handleClick(key)) <br/>
keyboard.append(buttonElement) <br/>
}) <br/>
iii. Identifies the name of the list being used in this response <br/>
The name of the list is “keys.” <br/>
iv. Describes what the data contained in the list represent in your program <br/>
The data contained in the lists represents each of the individual keys on the keyboard that users interact with to form words and give their inputs. <br/>
v. Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list  <br/>
The list enables me to create attributes for each individual key easily. Without the list, each key would have to be set as a variable one at a time. If that was the case, I couldn’t use a for loop to easily give each key the button and event attributes, or rather it would take significantly longer to do. <br/>


3 c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure. Approx. 200 words (for all subparts of 3c combined, exclusive of program code) <br/>
i. The first program code segment must be a student-developed procedure that: □ Defines the procedure’s name and return type (if necessary) □ Contains and uses one or more parameters that have an effect on the functionality of the procedure □ Implements an algorithm that includes sequencing, selection, and iteration <br/>
guessRows.forEach((guessRow, guessRowIndex) => { <br/>
const rowElement = document.createElement('div') <br/>
rowElement.setAttribute('id', 'guessRow-' + guessRowIndex) <br/>
guessRow.forEach((guess, guessIndex) => { <br/>
const tileElement = document.createElement('div') <br/>
tileElement.setAttribute('id', 'guessRow-' + guessRowIndex + '-tile-' + guessIndex) <br/>
tileElement.classList.add('tile') <br/>
rowElement.append(tileElement) <br/>
ii. The second program code segment must show where your student-developed procedure is being called in your program. Then, provide a written response that does both of the following: <br/>
tileDisplay.append(rowElement)<br/>
iii. Describes in general what the identified procedure does and how it contributes to the overall functionality of the program <br/>
It gives each row a unique ID and each tile within those rows unique IDs, which can be used later to compare each letter to the letters of the word that is being guessed. <br/>
iv. Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it. <br/>
There is an array titled “guessRows” with 6 rows of 5 empty spaces for each letter. For each row, I am creating a “div” element to actually separate each row. Then, within each separate row, I am creating a “div” element to actually separate each tile. <br/>


3 d. Provide a written response that does all three of the following: Approx. 200 words (for all subparts of 3d combined) <br/>
i. Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. <br/>
This procedure only has one function call.
First call: tileDisplay.append(rowElement) <br/>
Second call: <br/>
ii. Describes what condition(s) is being tested by each call to the procedure <br/>
Condition(s) tested by the first call: The rows' ids. <br/>
Condition(s) tested by the second call: <br/>
iii. Identifies the result of each call <br/>
Result of the first call: Adds a new row ID to the display of the tiles<br/>
Result of the second call: <br/>

# Runtime Video
[Create Task Runtime](https://www.loom.com/share/4e2beeba2ce04d32ad07f629e0d4fe1c?sharedAppSource=personal_library)