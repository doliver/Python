#10.2 Write a program to read through the mbox-short.txt and
#figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time
#and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below. Note that the autograder
#does not have support for the sorted() function.


name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hour_counts = dict()                                                    #create empty dictionary
hlist = []                                                              #create empty list

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':                           #Select lines with 'From'
        hour = words[5].split(':')                                      #Select hour (5 in index) and split string with colon
        hour_counts[hour[0]] = hour_counts.get(hour[0],0) + 1           #increase count for each hour
    else:
        continue
        
for k,v in hour_counts.items():                                         #k = hour, v = count
    hlist.append((k,v))                                                 #append tuples to list
    
hlist.sort()                                                            #sort list by hour
for k,v in hlist:                                                       #loop through list of tuples
    print(k,v)                                                          #print counts sorted by hour
