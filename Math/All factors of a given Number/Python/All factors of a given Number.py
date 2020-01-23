"""
Get all factors of a given number
"""

def factors(num):
    facts = []
    for i in range(2, num-1):
        #If the divided number has 0 as the division reminder, it'll be a factor
        if num%i == 0:
            facts += [i]
        i += 1
    return facts
