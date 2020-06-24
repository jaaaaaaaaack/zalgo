# zalgo.py
# Jack Beal, June 2020
# A small module to give any text a flavor of ancient doom

from random import random

def validCharacter(char, stoplist):
    """ Helps to prevent unwanted manipulation of certain characters."""

    if char in stoplist:
        return False
    else:
        return True


def uniformMangle(s, additives, n=1, p=1, stoplist=[]):
    """ Convenience function for uniformly mangling longer strings."""

    mangled = ""
    for c in s:
        mangled += mangle(c, additives, n, p, stoplist)
    return mangled


def mangle(char, additives, n=1, p=1, stoplist=[]):
    """ Accumulate additive characters from the list of possible additives, up to a maximum n and with average density p, and join them to the input character."""

    mangled = ""

    if validCharacter(char, stoplist):
        joiners = ""
        for i in range(int(n)):
            if random() <= p:
                joiners += additives[int(random()*len(additives))]
        mangled += char+joiners
        return mangled

    else:
        return char


def main():

    testString = "ZALGO.py"
    additives = ["\u0300","\u0301","\u0302","\u0315","\u031b","\u0327","\u0316","\u0317","\u0318"]
    stoplist = ["."]

    greeting = uniformMangle(testString, additives, n=3, p=1, stoplist=stoplist)

    print(greeting, "- a salt shaker for your text, filled with anxiety and foreboding!")

if __name__ == "__main__":
    main()
