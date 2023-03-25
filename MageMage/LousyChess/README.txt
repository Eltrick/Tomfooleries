################################
#######Lousy Chess solver#######
################################
by MageMage81

Lousy Chess solver for the ktane Module:
https://github.com/johnvt/KtaneLousyChess
https://steamcommunity.com/sharedfiles/filedetails/?id=1866367885

Program to run is found in ..\Program\Project1.exe
Most of the important code here also provided in ..\Program\Unit1.pas (be warned it is quite unoptimized and chaotic)

White & Black Rules:
- select corresponding ruleset the pieces follow

White/Black Numbers & Fields at the bottom:
- for various input methods of the RNG
	- Seed + Base Number:
		- Enter the seed followed by the Serial Number of the bomb i.e. 8LC1EW2
		- will not throw an error if an invalid serial number is given, as such will also work with longer or shorter custom strings using 0-9, a-z, A-Z
		- will generate the input for Seed + Direct Key that results in the same actions
	- Seed + Direct Key:
		- Enter the seed number followed by the numbers directly pulled from the RNG
		- if less than 40 RNG numbers have been given the provided ones will just be repeated i.e. 325 turns into 325252525...
	- Complete Random:
		- Considers the given set of numbers and adds as many as needed with a different RNG
		- Can also generate a random seed if no digits are provided

Press "Calculate" once all inputs have been made to create the solution.


The Textbox will provide all the moves from start till end, till any game ending condition is reached.
This will also display who won or if a tie occured.

With the previous and next step buttons one can cycle through the steps on the displayed chessboard.

"Change Size" switches between the normal Lousy Chess board and a standard 8x8 chess board.

