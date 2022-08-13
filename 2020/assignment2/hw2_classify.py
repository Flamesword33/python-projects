## Spam filter.py
##
## by Nathan Pelletier
## started March 28 2020
## finished March 29 2020

## Using the command prompt
##  a user enters the txt file which may be spam.
## Program then checks probability for each word inculded.
## Program uses P(1) * P(2) * P(3) * ... P(n) to calculate chance
##  email is spam or ham.
## We will use a easier formula log(P(1)) + log(P(2)) + ... log(P(n))

## Program results with two negitive numbers. The greater one is
## our answer. Expect small numbers with lots of decimals.

## Work plan:
##  Is able to read ham_prob and spam_prob
##    first line is denominator
##    third line on is numerator
##    may construct dictionary from data
##  Is able to read input file from command line
##    I think I will ask for files to be placed in
##    .\Data\Data\Test\test_Lemmatized
##  Can determine both probabilities for specified email
##  Can determine if email is spam by probabiliy scores
##  saves result to file
##    save in form:
##      P(Spam, all words)
##      P(Spam) =
##      P('you'|Spam) =
##      ...
##      log P(Spam, all words) =
##      P(Ham, all words)
##      ...
##      log P(Ham, all words) =
##
##      Conclusion: This message is classified as Spam.


import math
import sys
import os


def start():
  
  path = get_path()
  
  sp_path = path + "/spam_prob.txt"
  spam_prob = open(sp_path, "r")

  hp_path = path + "/ham_prob.txt"
  ham_prob = open(hp_path, "r")

  total_words = calculate_total_words(spam_prob, ham_prob)

  spam_prob = open(sp_path, "r") #restarts reading head on files
  ham_prob = open(hp_path, "r")  

  email = get_user_email(sys.argv[1], path)
  final_spam = spam_calculations(email, spam_prob, total_words, path)

  email = get_user_email(sys.argv[1], path)
  final_ham = ham_calculations(email, ham_prob, total_words, path)

  is_spam(final_spam, final_ham, path)

#end start


def get_path():
  path = os.getcwd()
  new_path = ""

  for letter in path:
    if letter == "\\":
      new_path = new_path + '/'
    else:
      new_path = new_path + letter
  #end for

  return new_path

#end get_path


def calculate_total_words(spam, ham):
  total = int(spam.readline()) + int(ham.readline())
  spam.close()
  ham.close()
  return total


def get_user_email(email, path):
  new_path = path + "/Data/Data/Test/test_Lemmatized/" + email
  return open(new_path, "r")
#get_user_email


def spam_calculations(email, spam, total_words, path):
  output_path = path + "/" + sys.argv[2]
  output = open(output_path, "a")
   
  denominator = int(spam.readline())
  #reads past blank line
  spam.readline()

  words = interpret_email(email)
  spam_dic = create_dictionary(spam)

  spam_chance = math.log(denominator/total_words)
  output.write("P(Spam, all words)\n")
  output.write("P(Spam) = " + str(denominator/total_words) + "\n")
  
  for line in words:
    for word in line:
      if word.isalpha():
        spam_chance = spam_chance + math.log(spam_dic.setdefault(word, 1)/denominator)
        catologue_spam(word, (spam_dic.get(word)/denominator), output)  
      #end if
    #end for
  #end for

  output.write("log P(Spam, all words) = " + str(spam_chance) + "\n\n")
  output.close()

  return spam_chance
#end spam_calculations


def ham_calculations(email, ham, total_words, path):
  output_path = path + "/" + sys.argv[2]
  output = open(output_path, "a")
   
  denominator = int(ham.readline())
  #reads past blank line
  ham.readline()

  words = interpret_email(email)
  ham_dic = create_dictionary(ham)
  
  ham_chance = math.log(denominator/total_words)
  output.write("P(Ham, all words)\n")
  output.write("P(Ham) = " + str(denominator/total_words) + "\n")
  
  for line in words:
    for word in line:
      if word.isalpha():
        ham_chance = ham_chance + math.log(ham_dic.setdefault(word, 1)/denominator)
        catologue_ham(word, (ham_dic.get(word)/denominator), output)
      #end if
    #end for
  #end for

  output.write("log P(Ham, all words) = " + str(ham_chance) + "\n\n")
  output.close()

  return ham_chance
#end ham_calculations


## interpret_email(.txt file) --> string[][]
def interpret_email(email):
  """Take a text file and breaks it into a list of words"""
  
  words = []
  for line in email:
    words.append(line.split())
  return words

#end interpret_email


def create_dictionary(file):
  dictionary = {}
  words = []

  for line in file:
    words.append(line.split())
  #end for

  for pair in words:
    print(pair[1])
    dictionary[pair[0]] = int(pair[1])
  #end for

  return dictionary
#end create_dictionary


def catologue_spam(word, chance, output):
  output.write("P(" + word + "|Spam) = " + str(chance) + "\n")


def catologue_ham(word, chance, output):
  output.write("P(" + word + "|Ham) = " + str(chance) + "\n")  


def is_spam(spam, ham, path):
  output_path = path + "/" + sys.argv[2]
  output = open(output_path, "a")
  
  if spam == ham:
    output.write("\n  Conclusion: This message is indeterminate.\n")
  elif spam > ham:
    output.write("\n  Conclusion: This message is classified as Spam.\n")
  else: #ham > spam
    output.write("\n  Conclusion: This message is classified as Ham.\n")
    output.write("mmm ham...")
    
  output.close()


start()
