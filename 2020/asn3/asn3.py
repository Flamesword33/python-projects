## asn3.py
##
## by Nathan Pelletier
## started April 16
## finished April 19

## Requires command line inputs
## python asn3.py input.txt output.txt
##
## Asks user if it is training or testing
##
## if training Code sets up neural network of
##  16x16 grid
##  10 hidden nodes
##  1 bias node
##  3 output nodes
## with random weights
##
## 1 0 0 --> 1
## 0 1 0 --> 8
## 0 0 1 --> 9
##
## Procedure then follows:
##  file inputs 16x16 nodes
##  code calculates a1, a2, a3, ... a10 by:
##    preforming E input(x) * weight(x)
##  code then calculates y1, y2, y3, ... y10 by:
##    preforming 1/(1 + e^-a)
##  Code takes highest number output to be most probable
##    ex 0.0001 0.1000 0.9020 --> 9 as it is most probable
##  If tie exists then the tie breaker is which number
##  (1,8,9) has previously appeared the most in the training data
##
##  If the code guesses the wrong answer then:
##    code calculates output deltas:
##      y * (1 - y) * (target - y)
##    code calculates second layer deltas:
##      y * (1 - y) * weight * previous delta
##    It then corrects all weights with formula:
##      weight[i][j] = learning_rate * delta[j] * i + w[i][j]
##      learning_rate = 0.1
##  Code ends when 90% correct
##
## If testing code then:
##  code proceeds as normal but instead of checking answers
##  and adjusting weights it will assume its output is correct

## use random.uniform(-1,1)


import os
import sys
import math
import random


###########
##globals##
weights1 = list()
weights2 = list()
guesses = list()
answers = list()
y = list()
y2 = list()
count_cycles = 0


## start()
##
## Resets guesses, asks user what the program should do
## and either tests the data set, trains the data set or ends the program
def start():
  global guesses
  global y
  global y2

  guesses.clear()
  y.clear()
  y2.clear()
  
  is_test = ask_user()

  if(is_test == "exit"):
    print("Program terminating...")
    return True

  path = os.getcwd()
  input_file = get_file(path, sys.argv[1])
  output_file = get_file(path, sys.argv[2])
  
  
  if(is_test):
    test_network(input_file, output_file)
    return True
  else:
    train_network(input_file, output_file)
    return True
#start


## asks user if program should preform training,
## testing or just end
def ask_user():
  """ask_user() --> boolean, String"""

  output = input("Should the program train a new data set? [y/n]: ")

  if(output == 'y'):
    return False
  else:
    print("Should the program attempt to read ", end = '')
    print("your handwriting? [y/n]: ", end = '')
    output = input()

    if(output == 'y'):
      return True
    else:
      return "exit"
  #else
#ask_user_test


## get_file(String, String) --> String
##
## takes a path and a name and combines them, then fixes them 
## for open() functions use
def get_file(path, file_name):
  """get_file(String, String) --> String"""
  
  new_path = path + '/' + file_name
  return correct_backslashes(new_path)
#get_file


## removes backslashes from string, 
## replacing them with forward slashes
def correct_backslashes(path):
  """correct_backslash(String) --> String"""
  
  new_path = ""

  for letter in path:
    if letter == "\\":
      new_path = new_path + '/'
    else:
      new_path = new_path + letter
  #for

  return new_path

#correct_backslashes


def train_network(input_file, output_file):
  global answers
  global guesses
  global y
  global y2
  global count_cycles
  
  accuracy = 0.0
  num_correct = 0
  total_num = 0
  first_pass = True

  initialize_weights()

  while(accuracy < 0.9):
    count_cycles = count_cycles + 1
    if(first_pass):
      answers.clear()
    guesses.clear()
    
    fi = open(input_file, 'r')
    total_num = 0
    num_correct = 0
    
    for line in fi:
      y.clear()
      y2.clear()
      
      total_num = total_num + 1
      x = line.split(' ')
      x.pop(-1)
      x = change_str_to_float(x)
      
      answer = find_answer(x,first_pass)
      guess = calculate_a(x)
      
      if(answer == guess):
        num_correct = 1 + num_correct
      else:
        correct_network(x)
    #for
      
    accuracy = num_correct / total_num
    print(num_correct, '/', total_num, "accuracy = ", accuracy)
    fi.close()
    first_pass = False
  #while
    
  write_train_output(output_file)
#train_network
  

def initialize_weights():
  """Sets global weights1 and weights2 to
     257x10 and 11x3 random floats between -1 and 1"""
  
  global weights1
  global weights2

  for i in range(257):
    weights1.append([])
    for j in range(10):
      weights1[i].append(random.uniform(-5,5))
    #for
  #for

  for k in range(11):
    weights2.append([])
    for l in range(3):
      weights2[k].append(5 - k + l)
    #for
  #for
#initialize_weights


def change_str_to_float(list_of_strings):
  for i in range(len(list_of_strings)):
    list_of_strings[i] = float(list_of_strings[i])
  return list_of_strings
#change_str_to_float


def find_answer(ans_file, first_pass):
  if(ans_file[-1] == 1.0):
    if(first_pass):
      answers.append(9)
    return 9
  elif(ans_file[-2] == 1.0):
    if(first_pass):
      answers.append(8)
    return 8
  elif(ans_file[-3] == 1.0):
    if(first_pass):
      answers.append(1)
    return 1
#find_answers


def calculate_a(inputs):
  global weights1

  #biases#
  a1 = weights1[-1][0]
  a2 = weights1[-1][1]
  a3 = weights1[-1][2]
  a4 = weights1[-1][3]
  a5 = weights1[-1][4]
  a6 = weights1[-1][5]
  a7 = weights1[-1][6]
  a8 = weights1[-1][7]
  a9 = weights1[-1][8]
  a10 = weights1[-1][9]
  
  for i in range(256):
    a1 = a1 + (weights1[i][0] * inputs[i])
    a2 = a2 + (weights1[i][1] * inputs[i])
    a3 = a3 + (weights1[i][2] * inputs[i])
    a4 = a4 + (weights1[i][3] * inputs[i])
    a5 = a5 + (weights1[i][4] * inputs[i])
    a6 = a6 + (weights1[i][5] * inputs[i])
    a7 = a7 + (weights1[i][6] * inputs[i])
    a8 = a8 + (weights1[i][7] * inputs[i])
    a9 = a9 + (weights1[i][8] * inputs[i])
    a10 = a10 + (weights1[i][9] * inputs[i])
  #for

  return calculate_y([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10])
#calculate_a


def calculate_y(a):
  global y

  for i in a:
    temp = 1/(1 + math.exp(-i))
    y.append(temp)
  #for

  return calculate_a2(y)
#calculate_y


def calculate_a2(inputs):
  global weights2
  
  #biases#
  a1 = weights2[-1][0]
  a2 = weights2[-1][1]
  a3 = weights2[-1][2]
  
  for i in range(10):
    a1 = a1 + (weights2[i][0] * inputs[i])
    a2 = a2 + (weights2[i][1] * inputs[i])
    a3 = a3 + (weights2[i][2] * inputs[i])
  #for

  return calculate_y2([a1,a2,a3])
#calculate_a2


def calculate_y2(a):
  global y2
  
  for i in a:
    temp = 1/(1 + math.exp(-i))
    y2.append(temp)
  #for

  return take_a_guess(y2)
#calculate_y2


def take_a_guess(guesses):
  which_were_largest = list()
  largest = max(guesses)

  for x in range(len(guesses)):
    if(guesses[x] == largest):
      which_were_largest.append(x)
    #if
  #for

  return interpret_guess(which_were_largest)
#take_a_guess


def interpret_guess(largest):
  global guesses
  if(len(largest) == 1):
    if(largest[0] == 0):
      guesses.append(1)
      return 1
    elif(largest[0] == 1):
      guesses.append(8)
      return 8
    else:
      guesses.append(9)
      return 9
  else:
    return interpret_guess2(largest)
#interpet_guess


def interpret_guess2(largest):
  global answers
  count = [0,0,0]
  max_count = 0
  min_count = 0
  a = 0

  for x in answers:
    if(x == 1):
      count[0] = count[0] + 1
    if(x == 8):
      count[1] = count[1] + 1
    if(x == 9):
      count[2] = count[2] + 1
  #for

  max_count = max(count)
  min_count = min(count)

  while(a < len(largest)): #has to be a while loop as
                          #python for does not allow you
                          #to affect the itterator
    temp = largest[a]
    if(max_count == count[temp]):
      return interpret_guess([temp])
    if(min_count == count[temp] and len(largest) > 1):
      largest.pop(a)
      a = a - 1
    a = a + 1
      
  #for
  return interpret_guess([largest[0]])
#interpret_guess2


def correct_network(inputs):
  global weights1
  global weights2
  global y
  global y2
  learning_rate = 1
  temp = 0
  delta = list()
  delta2 = list()

  for j in range(len(y2)):
    temp = y2[j]
    delta.append(temp * (1 - temp) * (inputs[j+256] - temp))
    for i in range(10):
      weights2[i][j] = (learning_rate * delta[j] * y[i]) + weights2[i][j]
    #for
  #for
  
  for j in range(len(y)):
    temp = y[j]
    delta2.append(temp * (1 - temp) * (weights2[j][0] * delta[0] + weights2[j][1] * delta[1] + weights2[j][2] * delta[2]))
    for i in range(256):
      weights1[i][j] = (learning_rate * delta2[j] * inputs[i]) + weights1[i][j]
    #for
  #for
#correct_network

      
def write_train_output(output_file):
  global guesses
  global answers
  global count_cycles
  counter = 0
  accuracy = 0.0
  gue = 0
  ans = 0
  output = open(output_file, 'a')

  output.write("my_predicted_digit   target(correct_digit)\n")

  for i in range(len(guesses)):
    gue = guesses[i]
    ans = answers[i]

    output.write(str(gue))
    output.write("                        ")
    output.write(str(ans))
    output.write('\n')

    if(gue == ans):
      counter = counter + 1
    #if
  #for
  accuracy = counter / len(answers)
  output.write("Accuracy: ")
  output.write(str(counter))
  output.write('/')
  output.write(str(len(answers)))
  output.write(" = ")
  output.write(str(accuracy))
  output.write("%\n Final cycles used: ")
  output.write(str(count_cycles))
  output.close()

  save_weights()
#write_train_output
  

def test_network(input_file, output_file):
  global y
  global y2

  load_weights()
  
  fi = open(input_file, 'r')
  write_test_output(output_file)
  for line in fi:
    y.clear()
    y2.clear()

    x = line.split(' ')
    x.pop(-1)
    x = change_str_to_float(x)
      
    guess = calculate_a(x)

    write_test_output1(guess, output_file)
      
  #for
    
  fi.close()
#test_network

def write_test_output(output_file):
  f = open(output_file, 'a')
  f.write("Guesses made: \n")
  f.close()
#write_test_output

  
def write_test_output1(guess, output_file):
  f = open(output_file, 'a')
  f.write(str(guess))
  f.write("\n")
  f.close()
#write_test_output1


def save_weights():
  global weights1
  global weights2
  path = os.getcwd()
  path = get_file(path, "weights.txt")
  w = open(path, 'a')
  for a in range(len(weights1)):
    w.write('\n')
    for b in weights1[a]:
      w.write(str(b))
      w.write(' ')
  w.write("\n")
  for c in range(len(weights2)):
    w.write('\n')
    for d in weights2[c]:
      w.write(str(d))
      w.write(' ')
  w.close()


def load_weights():
  global weights1
  global weights2

  initialize_weights()
  path = os.getcwd()
  path = get_file(path, "weights.txt")
  w = open(path, 'r')
  
  w.readline()
  for a in range(len(weights1)):
    line = w.readline()
    x = line.split(' ')
    x.pop(-1)
    x = change_str_to_float(x)
    for b in range(len(weights1[a])):
      weights1[a][b] = x[b]
    #for
  #for
  w.readline()
  for c in range(len(weights2)):
    line = w.readline()
    x = line.split(' ')
    x.pop(-1)
    x = change_str_to_float(x)
    for d in range(len(weights2[c])):
      weights2[c][d] = x[d]
    #for
  #for
#load_weights


start()
