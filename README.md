# Learning_Journal_Unit_3
CS1101 Leaning Journal Unit 3
1. Copy the countdown function from Section 5.8 of your textbook.

def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)

Write a new recursive function countup that expects a negative argument and counts “up” from that number. Output from running the function should look something like this:

>>> countup(-3)
-3
-2
-1
Blastoff!

Write a Python program that gets a number using keyboard input. (Remember to use input for Python 3 but raw_input for Python 2.)

If the number is positive, the program should call countdown. If the number is negative, the program should call countup. Choose for yourself which function to call (countdown or countup) for input of zero.

Provide the following.

The code of your program.
Output for the following input: a positive number, a negative number, and zero.
An explanation of your choice for what to call for input of zero.
2. Write your own unique Python program that has a runtime error. Do not copy the program from your textbook or the Internet. Provide the following.

The code of your program.
Output demonstrating the runtime error, including the error message.
An explanation of the error message.
An explanation of how to fix the error.
