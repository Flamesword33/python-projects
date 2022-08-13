## calculate probability.py
##
## by Nathan Pelletier
## started: March 25 2020
## finished: March 28 2020

## Outputs to two txt files
##  ham_prob.txt
##  spam_prob.txt
##    Each file has a total word count at the top of the page
##    Each line after the first contains a word and a number
##      the number is the number of times said word was found.

## work plan:
##   read all words from email into list of words for either spam or ham
##   sort list alphabetically (or could just pop reocurrences in list)
##   count total words used pending on spam or ham
##   write total word count to txt file
##   append word from list
##     count total number of occurances
##     append total number of occurances


import os

#########
#GLOBALS#
Word_count_sp = 0
Word_count_hp = 0
List_of_words_sp = []
List_of_words_hp = []

###########
#FUNCTIONS#
def start():
  """Finds the training directory and begins determining what is spam"""
  global List_of_words_sp
  global List_of_words_hp

  path = os.getcwd() + "/Data/Data/Train/train_Lemmatized"
  path = correct_backslash(path)
  files = os.listdir(path)
  
  for email in files:
    p_email = path + '/' + email
    
    f = open(p_email, "r")
    is_spam(f, email)
    f.close()
    
  #end for

  create_ham_file(sorted(List_of_words_hp))
  create_spam_file(sorted(List_of_words_sp))
  
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
      

## is_spam(.txt file, string)
def is_spam(email,email_name):
  """checks if email title starts with sp"""
  if(email_name[0:2] == "sp"):
    spam(email)
  else:
    ham(email)
#end is_spam


## ham(.txt file)
def ham(email):
  """takes all words in email and converts them into a ham list"""
  for line in email:
    words = line.split(' ')
    for word in words:
      if word.isalpha():
        ham_word(word)
    #end for words
  #end for lines
#end ham
    
    
## spam(.txt file)
def spam(email):
  """takes all words in email and converts them into a spam list"""
  for line in email:
    words = line.split(' ')
    for word in words:
      if word.isalpha():
        spam_word(word)
    #end for words
  #end for lines
#end spam


## ham_word(string)
def ham_word(word):
  """adds current word to a list of ham words"""
  global List_of_words_hp
  global Word_count_hp

  List_of_words_hp.append(word)
  Word_count_hp = Word_count_hp + 1
#end ham_word


## spam_word(string) 
def spam_word(word):
  """adds current word to a list of spam words"""
  global List_of_words_sp
  global Word_count_sp

  List_of_words_sp.append(word)
  Word_count_sp = Word_count_sp + 1
#end spam_word


## create_ham_file(string[])
def create_ham_file(ham_list):
  """Counts all words given after sorting them alphabetically"""
  """Also counts how many words were entered in total"""
  global Word_count_hp
  last_word = ""
  counter = 1

  file = open("ham_prob.txt","a")
  file.write(str(Word_count_hp))
  file.write("\n")

  for word in ham_list:
    if(last_word == word):
      counter = counter + 1
    else:
      file.write(last_word)
      file.write(' ')
      file.write(str(counter))
      file.write("\n")

      counter = 1
      last_word = word
    #else
  #for
#create_ham_file
  

## create_spam_file(string[])
def create_spam_file(spam_list):
  global Word_count_sp
  last_word = ""
  counter = 1
  
  file = open("spam_prob.txt","a")
  file.write(str(Word_count_sp))
  file.write("\n")

  for word in spam_list:
    if(last_word == word):
      counter = counter + 1
    else:
      file.write(last_word)
      file.write(' ')
      file.write(str(counter))
      file.write("\n")

      counter = 1
      last_word = word
    #else
  #for
#create_spam_file

start()
