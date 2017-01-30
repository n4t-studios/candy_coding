# Candy Coding - (C) Ryan Kelley mr.kelley.teaches@gmail.com
# Version 0.2a - 01/29/2017

# The next line of code imports the function RANDINT from the RANDOM Python module. 
from random import randint # This allows us to generate random integers. 


# The next line of code DEFINES a FUNCTION.  This function is named roll_d6.  The emtpy () indicates this function takes no ARGUMENTS.
def roll_d6():
    die_roll = randint(1,6)
    print("You rolled a",die_roll,".\n")
    return die_roll # This function returns a random integer from 1 to 6. 
    
# The next line of code CALLS the function roll_d6.  This causes the code to execute. 
roll_d6()  

# The next lines define the VARIABLES used in this program.  The = tells Python to ASSIGN the VALUE on the right side to the variable on the left side of the = sign. 
choc_kiss = 1
gummy_bears = 1
star_b = 1
candy_type = 1
count = 1

while count < 20:
    candy = roll_d6()
    if candy == 1:
        
        count +=1 
    elif candy == 2:
        gummy_bears += 1
        count += 1
    elif candy == 3:
        m_mallow += 1
        count += 2
    elif candy == 4:
        star_b += 1
        count +=3
    elif candy == 5:
        swedish_fish += 1
        gummy_bears += 1
        m_mallow += 2
        star_b += 1
        count += 4
    else:
        swedish_fish -= 1
        gummy_bears -= 1
        m_mallow -= 1
        star_b -= 1
        count -= 1

print("You should have", swedish_fish, "Swedish Fish.")
print("You should have", gummy_bears, "Gummi Bears.")
print("You should have", star_b, "Star Bursts.")
print("You should have", m_mallow, "marshmallows.")

# Now for the fun stuff!

mnm = 0

if swedish_fish > 3:
    print("Woof. Woof.") # You must bark like a dog.
    mnm += 2
else:
    print("Cluck. Cluck.") # You must cluck like a chicken.
    mnm += 1

if gummy_bears != 4:
    print("Stand up on one leg and touch your nose for 10 seconds.") # Don't be shy.
    mnm += 2
else:
    print("You have four Gummy Bears! Eat one now.") # Tasty.
    mnm += 1
    
if star_b > 0:
    print("I have a nice collection of Star Bursts!") # Say this out loud.  SAY IT! 
    mnm += 1
else:
    print("Look on the bright side: you didn't get any yellow ones!") # 
    mnm += 5

if m_mallow % 2 == 0:
    print("Even Steven!") # Who's Steven?
    mnm += 2
else:
    print("Odd Todd!") # Wait, what happened to Steven?
    mnm += 3

print("You should have", mnm, "M&M's.") 


    


