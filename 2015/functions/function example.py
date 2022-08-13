#def factorial (banana):
 #   if banana<=0 :
  #      return 0
   # f=1
    #for i in range (2, banana + 1):
     #   f=f*i
    #return f

#example 2

#can use to make tools like range()
#def song (name):
#gives explination to user
    #'Prints out Happy Birthday song to <name>'
#peramiters
   # print('Happy Birthday to you')
    #print('Happy Birthday to you')
   # print('Happy Birthday dear '+ name)
    #print('Happy Birthday to you!')
    
#numOFbds = int(input('How many birthdays?'))

#allNAMES = []

#for i in range(numOFbds):
    #name= input('Who? ')
    #allNAMES= allNAMES + [name]

#for name in allNAMES:
    #song(name)
   # print()

#example 3

def locationINlist (anOBJECT, aLIST):
    'Finds the location of <anOBJECT> in <aLIST>; False if not found'
    location= 0#start at beginning
    for obj in aLIST:
        if anOBJECT==obj :
            return location
        location = location + 1
    return False
