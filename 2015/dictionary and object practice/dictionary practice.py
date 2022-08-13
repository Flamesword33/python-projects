color = input('Please enter your faviourte color: ')   #inputed keys
color_tally = {}                                        #inputed dictionary
while color != '' :
    if color in color_tally:
        color_tally[color] = color_tally[color]+1      #adds one to count
    else:
        color_tally[color] = 1                        #starts count
    color = input('Please enter your faviourte color: ')    #continues loop

print(color_tally)
