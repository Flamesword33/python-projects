"""letter grade converter.py
   by Nathan Pelletier
   started: October 21, 2024

   function takes a letter and returns a grade value
"""


def con(letter):
    match letter:
        case "A+":
            return 4
        case "A":
            return 4
        case "A-":
            return 3.7
        case "B+":
            return 3.3
        case "B":
            return 3
        case "B-":
            return 2.7
        case "C+":
            return 2.3
        case "C":
            return 2
        case "C-":
            return 1.7
        case "D+":
            return 1.3
        case "D":
            return 1
        case "F":
            return 0

