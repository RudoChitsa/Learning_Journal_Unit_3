
#a recursive function that expects a negative function and counts up from that number.
def countup (n):
	if n >= 0:
		print ("BLASTOFF!")
	else:
		print (n)
		countup(n+1)
                

#Python program that gets a number using keyboard input
#if the number is positive, the program should call countdown
#if the number is negative, the program should call countup
#choose for yourself which function to call for input of zero


#countdown
def countdown (counting_down):
	if counting_down <= 0:
		print ("BLASTOFF!")
	else:
		print (counting_down)
		countdown(counting_down-1)


#countup
def countup (counting_up):
	if counting_up >= 0:
		print ("BLASTOFF!")
	else:
		print (counting_up)
		countup(counting_up+1)


#zero
def zero_it (zero):
	if zero == 0:
		print ("BLASTOFF")
	else:
		print(zero)
		zero_it(zero+2)


                
counting_down = input("Please enter a positive number\n")
print("you have entered" + " " + counting_down)
counting_down = int(counting_down)
if counting_down <= 1:
	print ("BLASTOFF!")
else:
	print (counting_down)
	countdown(counting_down-1)



counting_up = input("Please enter a negative number\n")
print("you have entered" + " " + counting_up)
counting_up = int(counting_up)
if counting_up >= 0:
	print ("BLASTOFF!")
else:
	print (counting_up)
	countup(counting_up+1)


#with input of 0
# I had to use zero+0 because either -1 and +1 does not end.
zero = input("lets try an input of zero\n")
zero = int(zero)
if zero != 0:
	print ("thats not a zero")
else:
    if zero == 0:
            print(zero)
            zero_it(zero+0)


#RUNTIME ERROR
print("example of a runtime error")
a = 2
b = 3
c = 4
d = a + b + c 

print (abcd)

















