## Convert float file to int
##
## by Nathan Pelletier

## her images are 16 by 16
## 0 0 1 means the image is 9 (could have just put a 9 up front) :\
## 0 1 0 means 8
## 1 0 0 means 1

## I'm not impressed by the lack of communication and the unnessisary complexity
## this project did not need such a system to id 1, 8 and 9
## This project did not need to be in binary and especially not in floats

import os

def start():
  path = os.getcwd() + "/train.txt"
  path = correct_backslash(path)

  file = open(path, "r")

  change_file(file)
  file.close()
#end start


## correct_backslash(string) --> string
def correct_backslash(path):
  """replaces \ with /"""
  new_path = ""

  for letter in path:
    if letter == "\\":
      new_path = new_path + '/'
    else:
      new_path = new_path + letter
  #end for

  return new_path

#end correct_backslash


def change_file(file):
  for line in file:
    words = line.split(' ')
    for number in words:
      print(number[0], end = ' ')
