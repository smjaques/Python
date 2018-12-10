
Executable file: markPoker.py
Helper file with functions: pokerFuncs.py

How to run:
	To use your script:
		./run_tests ./markPoker.py


	**NOTE**
	./run_tests3 had error in the check_output function and didn't run
	Tried to fix it but stackoverflow wasn't much help!

	I included many of my own tests.
	How to run tests:
		./markPoker.py < testname	

If I had more time, I would have created a similar script file to yours to run 
with all of my test files to show they passed, however it is finals week!!



About my Code:

Due to the possible necessity for more information/cards in one hand,
I wanted to store everything needed in a dictionary for each person.
dictionary = {
		'id' = int (id of player used for stdout of winner(s))
		'highest' = int (the highest num in hand)
		'hand' = int array (holds all num values used for tie comparisons)
		'high_pair' = int (value of pair)
		'high_triple' = int (value of three of kind)
		'best' = int (best hand saved as int):
			5 - straight flush
			4 - 3 of a kind
			3 - straight
			2 - flush
			1 - pair
			0 - high card
		

I stored the best hand of each player as an int in the dictionary to make
comparing two hands very easy. 

I realized that the suit of the cards aren't needed after a check for a flush,
So I did that check first, then continued with checks only using the number values.

After the flush check, I made all card values into numbers (T-> 10, J-> 11, ...)

Then I checked the rest of possible hands. I checked for a straight twice, 
once when A= 14 and once when A=1.

The only part of my code that I am really unhappy with is my tieComparisons 
function.
I dislike all of the if statements in one function as it seems messy. 
However, like I mentioned before - finals are here...
