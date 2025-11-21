# Program Description:
# This program prints a pattern of numbers. 
# For a given number n, it prints each number from 1 to n,
# repeated as many times as its value.


#Follow the simple step-by-step 
# instructions to build the program


#1. Ask the user for a number
#Hint: We convert it to an integer because we will use it in math and loops.
num=int(input("enter any number: "))


#2. Start a counter at 1
#This counter will go from 1 up to the number the user typed.
i = 1

#3. Start the loop
#Hint: We want the loop to continue as long as i is less than or equal to n.

while  i <= num:

#4. Inside the loop, print the pattern
#Hint: str(i) * i means "repeat the digit i, i times."
    print(str(i)*i)

#5. Increase the counter
#Hint: Move to the next number so the loop continues correctly.
    i += 1 
