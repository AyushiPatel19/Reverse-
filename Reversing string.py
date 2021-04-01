# Code by Ayushi Patel
# Text file Reference: Author - Agarwal Basant, 2018, Packet Publishing, book: Hands-on data structures and algorithms
# with Python

import time

start = time.time() # starts the time to measure how long it will take the algorithm to run

def reverse(j): # creating a function called reverse
    string = " "  # setting an empty string
    for i in j:
        string = i + string
    return string

string = open('10000 words.txt').read().lower().split()  #opening the text files as strings
new_string = " ".join(string) # combining the empty string with the reversed string

print("The original sentence is:", string) # displays the original input string
print("The reversed string is:", reverse(new_string)) # displays the reversed string
print("The time taken to run the algorithm is:{0:.6f}".format(time.time()-start, "seconds.")) # displays the time that
# is taken to run the whole algorithm


