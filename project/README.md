# x-y plotting of a simple polynomial function
#### Video Demo:  <https://youtu.be/P75WBD9eR24>
#### Description:
My final project is a python program that takes input of a simple polynomial function as input and generates a plot for that polynomial function.

FILES : finalproj.py

INPUT: A polynomial function as a string
OUTPUT: Plot for the provided function

PROGRAM DESCRIPTION:
This program does the following:
1- Takes a polynomial function as a string.
2- Validates the string against a set of user defined limitations. This validation is done in a user defined function called 'validate'.
3- Evaluates the function for values of x in the range of -100 to 100. This evaluation is done in a user defined function called 'evaluate'.
4- Supplies the computed x-y values to matplotlib for generataing the plot.

LIMITATIONS:
1-Function cannot contain fractional or decimal values
2-The first term cannot contain a negative integer
3-Cannot contain division operator
4-Has to be a valid polynomial function (eg. cannot have variable ‘x’ as a power)
5-Uses '*' for multiplication operation and '**' for exponential operation
6-In multiplication, the numeric value must come before variable 'x'
7-Completely numeric terms(not containing variable 'x')should be in their simplest form(not exponential or multiplicative)

EXAMPLES:
1-Valid Inputs:
    2*x
    x**3
    2*x**5
    2*x + x**3 - 3*x**4 + 5
2-Invalid Inputs:
    dskfhsdukhffshgs
    x*2
    2**x
    2/3*x

HOW TO RUN:
1- Following commands to be run in terminal window
    'cd project'    -- (to go into the project directory)
    'python project.py'    --(to run the program)

REQUIRED PYTHON LIBRARIES:
matplotlib
numpy

There are two functions i have made in this program.
VALIDATE and EVALUATE

The VALIDATE function has one purpose, to check the validity of the inputed equation.
This function ensures that the user does not enter any random characters in the input prompt, and also checks to make sure that the inputed string follows the specified rules.
The function first checks all the individual characters of the inputed expression. If any character is found other than numeric values, +, -, *, empty space or 'x', the program recognizes the expression as invalid and exits.
After this, the function deletes all the empty spaces from the inputed expression that the user might have entered.
It also temporarily replaces all '-' with '+' for later term splitting.
Then the expression is split into all the individual terms where terms are seperated by an addition sign.
It then makes sure that the expression does not start with a negative integer.
THEN, the validity of each individual term is checked.


The EVALUATE function evaluates the function for values of x between the range of -100 to 100.
It does so by splitting the expression into the individual terms and saving the (+ or -) signs in a list.
Then, it individually calculates the value of each term by converting each character to an integer.
For the calculation of the value of each term, it appends the multiplicative an exponential solved answers of the term to a single answer.
It then adds or subtracts all the values of the solves terms together by using the list of signs.