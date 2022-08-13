class Animal():
    legs = 4
    eyes = 2
    mainQuality = 'fuzzy'
    speak = 'mmrrff'

    ## Constructor that we are defining
    def __init__(self,legs,mainQuality,speak):
        self.legs = legs
        legs = 1000
        self.mainQuality = mainQuality
        self.speak = speak

#try removing and using a varible with (legs,mainQuality,speak) saved to it
    def __repr__(self):
        return 'Animal with ' + str(self.legs) + ' legs, ' + str(self.eyes) +\
               ' eyes, which is a ' + str(self.mainQuality)
    
    def talk(self):
        print(self.speak)
