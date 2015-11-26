#Memory Game

* A Memory Game
* Remember which word has been removed.
* Enter the word and which word was replaced.

#Parts of the Problem

* Load the words from a file.
	* ```open```, using ```with```
* Display a grid of nine words.
	* Using Sguigee - an array of nine labels.
	* Using console - use ```for``` and string formatting.
* Shuffle the words.
	* Using ```random.shuffle```
* Replace word.
	* Using ```random.randrange``` over the length of the list.
* Display the grid again.
* Ask for the users input.
	* Using sguigee, textboxes or ```ask_message```
	* Using console - ```input```
* Compare to the answers.
* Tell the user if they were successful.
	* Using sguigee - labels, textboxes, show_message
	* Using console - ```print```
