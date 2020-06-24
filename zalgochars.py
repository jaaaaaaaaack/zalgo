# zalgochars.py
# Jack Beal, June 2020
# The classic zalgo unicode characters

TOP_SMALL = ["\u0300", "\u0301", "\u0302", "\u0303", "\u0304", "\u0306", "\u0307", "\u0308", "\u0309", "\u030a", "\u030b", "\u030c", "\u030d", "\u030e", "\u030f", "\u0310", "\u0311", "\u0312", "\u0313", "\u0314", "\u031a", "\u033d", "\u033e", "\u0342", "\u0343", "\u0344", "\u0346", "\u034a", "\u034b", "\u034c", "\u0350", "\u0351", "\u0352", "\u0357", "\u035b"]
TOP_LARGE = ["\u0305", "\u033f", "\u035d", "\u035e", "\u035f", "\u0360", "\u0361", "\u0362"]
TOP_LETTERS = ["\u0363", "\u0364", "\u0365", "\u0366", "\u0367", "\u0368", "\u0369", "\u036a", "\u036b", "\u036c", "\u036d", "\u036e", "\u036f"]

MIDDLE_SMALL = ["\u0315", "\u031b", "\u0327", "\u0328", "\u0334", "\u0335", "\u0337", "\u0340", "\u0341", "\u0358", "\u0489"]
MIDDLE_LARGE = ["\u0321", "\u0322", "\u0336", "\u0338"]

BOTTOM_SMALL = ["\u0316", "\u0317", "\u0318", "\u0319", "\u031c", "\u031d", "\u031e", "\u031f", "\u0320", "\u0323", "\u0324", "\u0325", "\u0326", "\u0329", "\u032a", "\u032b", "\u032c", "\u032d", "\u032e", "\u032f", "\u0330", "\u0331", "\u0339", "\u033a", "\u033b", "\u033c", "\u0345", "\u0347", "\u0348", "\u0349", "\u034d", "\u034e", "\u0353", "\u0354", "\u0355", "\u0356", "\u0359", "\u035a"]
BOTTOM_LARGE = ["\u0332", "\u0333", "\u035c"]


def getStandardAdditives(top=True, middle=True, bottom=True, dense=True, letters=True):
    """ Generates a set of additive characters."""

    additives = []

    if top:
        additives += TOP_SMALL
    elif top and dense:
        additives += TOP_LARGE

    if middle:
        additives += MIDDLE_SMALL
    elif middle and dense:
        additives += MIDDLE_LARGE

    if bottom:
        additives += BOTTOM_SMALL
    elif bottom and dense:
        additives += BOTTOM_LARGE

    if letters:
        additives += TOP_LETTERS

    return additives
