# Candy Coding - (C) Ryan Kelley mr.kelley.teaches@gmail.com
# Version 0.0a - 09/14/2016

# This code imports data from the RANDOM Python module.

from random import randint

# What does the next line do?

def roll_d6():
    return randint(1,6)

s_fish = 1
g_bears = 1
m_mallow = 1
star_b = 1
candy = 1
count = 1

while count < 20:
    candy = roll_d6()
    if candy == 1:
        s_fish += 1
        count +=1 
    elif candy == 2:
        g_bears += 1
        count += 1
    elif candy == 3:
        m_mallow += 1
        count += 2
    elif candy == 4:
        star_b += 1
        count +=3
    elif candy == 5:
        s_fish += 1
        g_bears += 1
        m_mallow += 2
        star_b += 1
        count += 4
    else:
        s_fish -= 1
        g_bears -= 1
        m_mallow -= 1
        star_b -= 1
        count -= 1

print("You should have", s_fish, "Swedish Fish.")
print("You should have", g_bears, "Gummi Bears.")
print("You should have", star_b, "Star Bursts.")
print("You should have", m_mallow, "marshmallows.")

# Now for the fun stuff!

mnm = 0

if s_fish > 3:
    print("Woof. Woof.") # You must bark like a dog.
    mnm += 2
else:
    print("Cluck. Cluck.") # You must cluck like a chicken.
    mnm += 1

if g_bears != 4:
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


    


