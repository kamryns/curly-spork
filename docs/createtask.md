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
* Describes the overall purpose of the program <br/>
The overall purpose of the program is to provide entertainment for people. It is a recreation of the trending game Wordle, where people have 6 attempts to guess a 5-letter word. People can use this program when they are bored and looking for a quick, but still engaging and fun challenge. <br/>
* Describes what functionality of the program is demonstrated in the video <br/>
The program contains a variety of different 5-letter words chosen at random, which the user will try to guess. It tells them which of their guessed letters are actually there/in the right spot and which ones are not by checking each tile against the real word. If the user gets the correct word in 6 or less tries, they have won. <br/>
* Describes the input and output of the program demonstrated in the video <br/>
The user inputs 5-letter words by typing in their keyboard. If they win the game, there will be an output message letting them know they’ve won, if they lose, there will be a message acknowledging they’ve lost and telling them the secret word.


3 b. Capture and paste two program code segments you developed during the administration of this task that contain a list (or other collection type) being used to manage complexity in your program. Approx. 200 words (for all subparts of 3b combined, exclusive of program code) <br/>
* The first program code segment must show how data have been stored in the list. <br/>
wordbank = ["cigar", "rebut", "sissy", "humph", "awake", "blush", "focal", "evade", "naval", "serve", "heath", "dwarf", "model", "karma", "stink", "grade", "quiet", "bench", "abate", "feign", "major", "death", "fresh", "crust", "stool", "colon", "abase", "marry", "react"...]<br/>
* The second program code segment must show the data in the same list being used, such as creating new data from the existing data or accessing multiple elements in the list, as part of fulfilling the program’s purpose. Then, provide a written response that does all three of the following: <br/>
word = random.choice(wordbank) <br/>
* Identifies the name of the list being used in this response <br/>
The name of the list is “wordbank.” <br/>
* Describes what the data contained in the list represent in your program <br/>
The data contained in the lists represents some of the possible solutions to the game to be chosen at random. <br/>
* Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list  <br/>
The selected list manages complexity because it allows a user to play the game with a new word each time. If we did not use the list, we would have to hard-code a single word each time someone wanted to play. <br/>


3 c. Capture and paste two program code segments you developed during the administration of this task that contain a student-developed procedure that implements an algorithm used in your program and a call to that procedure. Approx. 200 words (for all subparts of 3c combined, exclusive of program code) <br/>
* The first program code segment must be a student-developed procedure that: <br/> 
□ Defines the procedure’s name and return type (if necessary)<br/>
□ Contains and uses one or more parameters that have an effect on the functionality of the procedure <br/>
□ Implements an algorithm that includes sequencing, selection, and iteration <br/>
def checkwordlength(fword): <br/> 
  if len(fword) == 5: <br/> 
    return fword <br/> 
  else: <br/> 
    print (colored("not a 5 letter word", 'red')) <br/> 
    guessagain1 = input("guess another word:    ") <br/> 
    #pdb.set_trace() <br/> 
    guessagain1 = checkwordlength(guessagain1) <br/> 
    return guessagain1 <br/> 
* The second program code segment must show where your student-developed procedure is being called in your program. Then, provide a written response that does both of the following: <br/>
def checkall(fword): <br/>
  fword = checkwordlength(fword) <br/>
  fword = checkwordvalid(fword) <br/>
  fword = checkword(fword) <br/>
  return fword <br/>
* Describes in general what the identified procedure does and how it contributes to the overall functionality of the program <br/>
It checks if the length of the user's attempted word is exactly 5 letters. The word must be 5 letters in order to match the 5-letter secret word. Otherwise, they cannot move on with the game and could never win.<br/>
* Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it. <br/>
First, it checks if the guessed word is 5 letters. If it is, it returns that word and carries onto the next function. If it is more or less, it prints that it is not a 5 letter word, and gives and input for a user to guess again. This new input is then checked by the checkword length function again, but with "guessagain" passed through it instead of the original "fword".<br/>


3 d. Provide a written response that does all three of the following: Approx. 200 words (for all subparts of 3d combined) <br/>
* Describes two calls to the procedure identified in written response 3c. Each call must pass a different argument(s) that causes a different segment of code in the algorithm to execute. <br/>
First call: fword = checkwordlength(fword) <br/>
Second call: guessagain1 = checkwordlength(guessagain1) <br/>
* Describes what condition(s) is being tested by each call to the procedure <br/>
First call: Checks if the guessed word is the appropriate length. <br/>
Second call: Checks if the word that is re-guessed is the appropriate length. <br/>
* Identifies the result of each call <br/>
Result of the first call: If word length is 5, it moves onto checking if it is a valid word. <br/>
Result of the second call: If the length of the word that is re-guessed is 5, it checks if that re-guessed word is valid.<br/>

# Runtime Video
[Create Task Runtime](https://www.loom.com/share/4e2beeba2ce04d32ad07f629e0d4fe1c?sharedAppSource=personal_library)
