## Lab 6.py
## by Nathan Pelletier
## AUCSC 460
## started March 15 2020
## finished March __ 2020

## Takes letters in the form of facts and rules
## uses forward chaining to find facts from the rules
## shows process of finding a queried fact

## Project goals:
## Needs to:
##  interpet user inputs as rules or fact
##  take rules from user
##  take facts from user
##  save rules to a matrix
##  save facts to a list of booleans
##  read through rules finding facts
##  print out facts
##  use user prompts

## Problems:
##  Several major glitches when objects used
##  class causes program to crash or hang for no reason
##  Program is only good for one instance
##    must restart shell and program to make second instance


##Globals##
Facts = [False for i in range(26)]
Rules = []
Count = []
Agenda = []


##Methods##
def start():
  set_up_facts_and_rules()
  preform_queries()
#end start


def set_up_facts_and_rules():
  """Sets up global data for preform_queries()"""
  
  done = False

  while(not done):
    user_input = get_rule_or_fact()
    done = interpret_user_input(user_input)
  #end while
#end set_up_facts_and_rules


def get_rule_or_fact():
  """Asks the user for rules and facts, exits on exit or e"""
  
  print("Please input knowledge base:", end = ' ')
  print("(type 'exit' if you want to stop)")
  user_input = input(": ")
  return user_input
#end get_rule_or_fact


## facts are one letter words
## rules have letters and symbols
## exit is exit or e
## capitols don't matter except for E vs e
def interpret_user_input(user_string):
  """parses data into rules, exits and facts. Returns boolean"""
  
  if user_string.lower() == "exit" or user_string == "e":
    print("stopped", end = "\n\n")
    return True
  #end if
  
  user_string = user_string.upper()
  
  if len(user_string) == 1 and user_string.isalpha():
    print("Agenda[", len(Agenda), "]:", user_string, sep = '') 
    input_fact(user_string)
    return False
  #end if

  else:
    modified_string = remove_symbols(user_string)
    print_rule(modified_string)
    input_rule(modified_string)
    return False
  #end else
#end interpret_user_input


## ascii representation of letters allows number opperations
## to apply to letters.
## A is 65 in ascii
## Z is 90 in ascii
def remove_symbols(user_string):
  """Takes away symbols from a string using ascii. Returns string"""
  
  new_string = ""

  for x in user_string:
    if(ord(x) >= ord('A') and ord(x) <= ord('Z')):
      new_string = new_string + x
    #end if
  #end for
      
  return new_string
#end remove_symbols


## unfortunatly not in object form due to python being python
## very sorry but unable to impliment objects for complex
## classes
def print_rule(user_string):
  """prints out rules as if object implimented"""
  
  for x in range(len(user_string) - 1):
    print("KB[",len(Rules),"].premise[", x,"]:", user_string[x], sep ='', end = ", ")
  #end for

  print("KB[",len(Rules),"].conclusion:",user_string[-1], sep = '', end = ", ")
  print("count:", len(user_string)-1, sep = '')
#end print_rule
  

## takes a string with only letters
## adds said string to rules list
def input_rule(user_string):
  ##adds new rule to rule list
  Rules.append(user_string)
  ##adds number of propositions to count
  Count.append(len(user_string)-1)
#end input_rule


## note: ord() takes character and returns decimal number
## based on ascii
## A is the smallest letter of 65 so that is my 0
def input_fact(fact):
  index_num = ord(fact) - ord('A')
  ##adds fact to agenda
  Agenda.append(fact)
  ##adds fact to fact list
  Facts[index_num] = True
#end input_fact


def preform_queries():
  """ Takes a user query and sends info to follow_current_agenda(char)"""

  query = get_query()
  query = query.upper()

  if Facts[ord(query) - ord('A')]:
    print("=============")
    print("Forward chaining not required")
    print("Query is already a fact")
    print("=============")
    print_results(query, True)
  #end if
    
  else:
    print("=============")
    print("Forward chaining algorithm starts")
    
    follow_current_agenda(query)
  #end else
#end preform_queries


def get_query():
  """gets and returns input from user"""

  query = input("What is your query?\n")
  return query
#end get_query


def follow_current_agenda(query):
  """Looks at each rule and applies forward chaining to
current element of agenda
returns boolean"""
  
  query_found = False
  counter = -1

  while(len(Agenda) > 0 and not query_found):
    counter = -1
    current_agenda = Agenda.pop(0)
    print_current_agenda(current_agenda)

    if(current_agenda == query):
      print_results(query, True)
      return True
    #end if

    for current_rule in Rules:
      counter = counter + 1
      print_current_rule_and_count(Count[counter],current_rule)

      for letter in current_rule[0:-1]:
        if(current_agenda == letter):
          Count[counter] = Count[counter] - 1
          print("Premise",current_agenda,"matched agenda")
          print("Count is reduced to", Count[counter])
          modify_agenda(counter, current_rule)
        #end if
      #end for letter
    #end for current_rule
  #end while

  print_results(query, query_found)
  return False
#end follow_current_agenda


def print_current_agenda(current_agenda):
  print("=============")
  print("***** Current agenda:", current_agenda," ******", sep ='')
#end print_current_agenda


def print_current_rule_and_count(current_count, current_rule):
  print(current_rule[0], end = '')
  for letter in current_rule[1:-1]:
    print('^', letter, sep = '', end = '')
  #end for
    
  print("=>", current_rule[-1], sep = '', end = ", ")
  print("count:", current_count)
#end print_current_rule_and_count


def modify_agenda(counter, current_rule):
  """Turns proven rules into facts"""
  if(Count[counter] == 0):
    print("==> Agenda", current_rule[-1], "is created")
    input_fact(current_rule[-1])
    Count.pop(counter)
    Rules.pop(counter)
  #end if
#end modify_agenda
  

def print_results(query, query_found):
  if(query_found):
    print("Goal Achieved")
    print("The query", query, "is true based on the knowledge.")
  #end if
    
  elif(len(Agenda) == 0):
    print("Failed to find goal")
    print("The query", query, "is false based on the knowledge.")
  print("---- The End -----")
  #end elif
#end print_results
          

start()
