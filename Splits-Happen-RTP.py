#################################
#    Bowling Score Tabulator    #
# Initial Draft - 21Jan2019 RTP #
#     Written for Python 2.7    #
#################################

import os
import sys


def get_val(my_tuple):
    # my_tuple is { int n,  str frame )
    # Where n is the position in the string frame
    
    # Break it apart for legibility, since I'm rusty
    n = my_tuple[0]
    frame = my_tuple[1]
        
    # Return the value of the n'th character in a string
    # Used to give value to X, -, and / characters
   
    # First, if we're returning value for a 13th + ball, return 0
    # E.g., spare in the 12th or a strike in the 11/12th
    if (n) > len(frame):
        return 0
    
    #Otherwise, return the value of this frame
    if  frame[n] == 'X' :
        return 10 
    elif frame[n] == 'x' :
        return 10
    elif frame[n] == '-' :
        return 0
    elif frame[n] == '/' :
        return (10 - int(frame[n-1]))
    else :
        #Normally, sanity check here.  Instructed not to, so we'll save time.
        return int(frame[n])
   
   
while ( True ):
    # Clear data; get new line of Bowling Data 
    sum = 0
    line = raw_input("Enter a line of Bowling data\n")

    frame_count = 1

    # Tally it up
    for i in range(len(line)) :
        print sum
        if frame_count < 11 :
            if line[i] == 'X' :
                #Special rules for a strike
                frame_count += 1
                sum += get_val((i,line)) + get_val((i+1,line)) + get_val((i+2,line))
            elif line[i] == '/' :
                #Special rules for a spare
                frame_count += 0.5
                sum += get_val((i,line)) + get_val((i+1,line))
            else :
                #No other special rules, proceed
                frame_count += 0.5
                sum += get_val((i,line))

        else :
            #We're in a special case of being in the 11th or 12th frame
            #These only give bonus score to previous balls,
            #But nothing else
            pass
    print "The bowler here has a total score of " + str(sum) + " . \n"
    keep_going = raw_input("\nDo you have another line of data to score up? (Yes/no)\n")
    if keep_going.lower() == 'yes' :
        continue
    else :
        print "Good bye!"
        break
