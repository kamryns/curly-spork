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

3 a. 
The overall purpose of the program is to provide entertainment for people. It is a recreation of the trending game Wordle, where people have 6 attempts to guess a 5-letter word. This program can be used for a quick, yet engaging and fun challenge. The program contains a variety of different 5-letter words chosen at random, which the user will try to guess. It tells them which of their guessed letters are actually there/in the right spot and which ones are not by checking each letter against those of the real word. If the user gets the correct word in 6 or less tries, they have won. The user inputs 5-letter words by typing on their keyboard. If they win the game, there will be an output message letting them know they’ve won, if they lose, there will be a message showing they’ve lost and displaying the secret word.

3 b. 
The list is called “wordbank.” The data contained in the lists being shown represents some of the possible five letter word choices for solutions to the game to be chosen at random. The selected list manages complexity because it allows a user to play the game with a new word each time they rerun. We also combined this list “wordbank” with another list “guessbank,” containing the list of every single five letter word that was not going to be a solution. That way, we could check to see if the user’s guessed words were real. We then used the “random.choice” function to select a new word every time. If we did not use the list with the randomizer, we would have to hard-code a single word each time someone wanted to play. Also, if we hadn’t combined the two lists, we wouldn't be able to tell if a user’s guess is a real word.

*both “wordbank” and “guessbank” were borrowed from the wordle.com source code*

3c.
Procedure “checkword” is being called in “checkall”


The procedure checkword checks each letter from the user’s guesses and determines if it is in the correct position, if it is in the word, or if it is even used at all. Then, it changes the colors accordingly in order to give the user hints to solve for the secret word. 

After a user’s guessed word is already checked for length and validity, their word is taken as the parameter and converted into a list of characters to be compared to the secret word’s character list. First, it checks if the list of the user’s word matches that of the solution word, which means the user wins. Then, using embedded FOR loops, it checks if the index position of each character in the guessed words’ lists equals that of the secret word’s list, and that character is printed in green. If the character is in the word’s letter list but not in the corresponding position, it is printed in yellow. In order to prevent duplicate yellow letters, we had to take into account future instances of “yellow” and “green” characters in the solution’s letters. Otherwise, if the character is not in the word’s letter list at all, it remains white.



3d. “Checkword” first called under a “checkall” function passing the user’s attempted word as the argument, where it calls the “checkwordlength” and “checkwordvalid” functions as well. “Checkword” is then called again under the “guess1” input field, passing the user’s first guess as the argument, so it checks the word after the first guess.

The conditions being tested by both calls are if the user’s guessed word matches the game’s solution word. If it does, then the user wins. However, the second instance of the function call is only testing the first guess, whereas the first one can take any of the user’s words.

The results are the same but call different functions depending on which guess the user is on. On the first guess, it takes the input of “guess1” to determine whether the letters are in the right place. On the rest of the user’s guesses, it passes “fword” into the checkword function.


# Runtime Video
[Create Task Runtime](https://loom.com/share/00cc8ed35ca24ad88e7eea2264037998)
