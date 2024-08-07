""" switch printer.py
    by Nathan Pelletier
    Started August 6 2024

    Program takes a language and a number and outputs a switch skeleton
      start with javascript
      python
      c
      scheme
"""


def js_switch(num):
    print("switch(ID) {")
    for i in range(num + 1):
        print("  case " + str(i) + ":")
        print("    //your code here")
        print("    break;")
    print("  default:")
    print("    //your code here")
    print("}")

def python_switch(num):
    print("match ID:")
    for i in range(num + 1):
          print("    case "  + str(i) + ":")
          print("        #your code here")
          print("        pass")
    print("    case _:")
    print("        #your code here")
    print("        pass")

