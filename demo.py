# demo.py
# Jack Beal, June 2020
# Quick-and-dirty demonstration of zalgo.py

import zalgo # Import the thing we're demonstrating
import zalgochars as zc # Some characters to mix in with our source text
import string # We'll use a couple of constants from this for our stoplist

def main():

    # Some text to mess with
    testString = "So long, and thanks for all the fish!"

    # Generate an additive list and a blocklist
    additives = zc.getStandardAdditives()
    stoplist = string.punctuation + string.whitespace

    # Uniform distribution of added characters
    uniform = zalgo.uniformMangle(testString, additives, n=1, p=1, stoplist=stoplist)

    # Distribute added character density along a curve
    nonuniform = ""
    temp = 1
    for char in testString:
        nonuniform += zalgo.mangle(char, additives, n=8, p=temp, stoplist=stoplist)
        temp = temp * 0.9

    # Many blank lines because this is going to get messy
    print("\nUniform:\t", uniform, "\n\n")
    print("Nonuniform:\t", nonuniform, "\n")


if __name__ == "__main__":
    main()
