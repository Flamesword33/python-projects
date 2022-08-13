#Grading Assignment.py
#by Nathan Pelletier
#Completed October 24

#Prints First name, Last name, grade average and class average

#input:

#Bird, Big 78 42 76 75 80
#Bear, Jasper 81 80 81 81 83 82
#Bunny, Bugs 34 56 67 58 72
#Claus, Santa 43 70 56 84 62 73
#Duck, Donald 68 74 84 78 55 81
#Flintstone, Fred 50 49 52 53 50 54
#Frog, Kermit 90 87 92 93 88 82
#Goose, Canada 86 88 82 79 81 93
#Lot, Missa 73 57 62
#Mermaid, Ariel 62 67 79 72 80 68
#Monster, Cookie 70 70 80 60 80 60
#Mouse, Minnie 98 100 95 87 93 93
#Ranger, Lone 84 85 78 81 82 79
#Snowman, Frosty 90 57 84 85 65 72
#White, Snow 73 75 74 69 53 84
#Woodpecker, Woody 73 72 75 70 81 68

#output:

##      Marks Summary
##First   Last       Average
##
##Big     Bird        70.20
##Jasper  Bear        81.33
##Bugs    Bunny       57.40
##Santa   Claus       64.67
##Donald  Duck        73.33
##Fred    Flintstone  51.33
##Kermit  Frog        88.67
##Canada  Goose       84.83
##Missa   Lot         64.00
##Ariel   Mermaid     71.33
##Cookie  Monster     70.00
##Minnie  Mouse       94.33
##Lone    Ranger      81.50
##Frosty  Snowman     75.50
##Snow    White       71.33
##Woody   Woodpecker  73.17
##
##Class Average:      73.31
##Lowest Mark:        51.33 ( Fred Flintstone )
##Highest Mark:       94.33 ( Minnie Mouse )
#Known bugs:
# Needs tinkering to format other sets of data
# only reverses name order
# needs a tuple set of data with two names and a list of numbers following
#properly aranged in rows


#PROJECT GOALS STATUS: COMPLETE
## October 24, 2015
##Current update; got it to print lowest and highest mark finally
##To do list for next time: 
##      Needs to display names of lowest grade and highest grade
##      Need remove comma on names
##      Need to round to two decimals

## October 13, 2015
##Update; prints an average of marks
##      Needs to print names in order
##      Needs to print class average
##      Needs to be in neat collums
myFile=open('grades.txt','r')

def classAverage(gradesFILE):
    'Organizes the name of the student and averages their grades.'
    print('      Marks Summary')
    print('First   Last       Average')
    print()
    total=0   # to find the total grades
    final=0   # to find the class average
    count=0   # A number to divide by, which tracks the colum amounts
    biggest=0   #finds the largest average 
    smallest=100  #finds the lowest average
    biggest_name = ''
    smallest_name = ''
    
    for line in gradesFILE:
        count=count+1   ## counts total each line 
        listOFline=line.split()
        for number in range(2,len(listOFline)):
            total=(total+int(listOFline[number]))
        average=total/(len(listOFline)-2)
        if average > biggest:
            biggest=average
            biggest_name = listOFline[1] + ' ' + listOFline[0].replace(',','')
        if average< smallest:
            smallest=average
            smallest_name = listOFline[1] + ' ' + listOFline[0].replace(',','')
        final=average +final
        
        #print(average), ##my original step
        print('{:7}'.format(listOFline[1]),'{:11}'.format(listOFline[0].replace(',',''))\
            ,'{0:.2f}'.format(average))
            ##formats the list into first, name last, name and grade
            ## averages all in neat colums
            ##NOTE: only works for spcific data set, further toying required
        total=0
    final=final/count
    
    print()
    print('{:19}'.format('Class Average:'),'{0:.2f}'.format(final))
    print('{:19}'.format('Lowest Mark:'),'{0:.2f}'.format(smallest),'(',smallest_name,')')
    print('{:19}'.format('Highest Mark:'),'{0:.2f}'.format(biggest),'(',biggest_name,')')
#i found '{0:.2f}' online at
#http://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
    ## want to center on page but keep geting
    ##{0:11}
    ##IndexError: tuple index out of range
classAverage(myFile)
myFile.close()

