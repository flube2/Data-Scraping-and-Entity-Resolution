Frank Lubek
flube2@uic.edu
CS 418 Sp18
HW 1 - Reformatting Data: Super Bowl Champions and Entity Resolution: UIC Courses
readme.txt



Part 1 (trnasform.py):
Not knowing any python or how to do any web/networking stuff, I started by looking at BeautifulSoup's documentation
Still confused, I consulted a web page listed in my sources
I took that approach to read and parse the table into variables that I could then manipulate to my liking.

Issue: upon extracting the data I needed I noticed all lines ended in ' !'
Solution: I consulted a web page from my sources "pyformat" which told me how to strip those characters using "[:-2]"

I then made a print statement and formatted my output accordingly

Issue: I was only getting one superbowl and didn't know how to get next one
Solution: I wasn't looping correctly, I consulted a website from my sources for the correct function

Issue: I wasn't able to get OT
Solution: I was using score[1] instead of score[2]

Current known issues:
None



Part 2 (clean.py):
I wanted to be able to read in the data before getting command line arguments
I opened and read from the file
I split professors and courses

Issue: When I split it also split the courses with  '-' in their titles, resulting in me losing any appended data
Solution: After splitting I checked if there was a pair[2] and is so added it back to the first part of course list

I parsed the names to get all of the last names
Then I parsed courses, and stored data in a list of my custom Professor objects
I implemented command line arguments

Current known issues:
If a course list for a professor has 2 or more hyphens in the title, all data after the second '-' would be lost



Part 3 (query.py):
I used code from clean.py and made them functions
I edited them as I knew I would be dealing only with clean data
I navigated through the data from the file and added courses to a set (for distinct courses)
I then implemented command line arguments 
I wrote the Jaccard function in main()
Moved code to Jaccard()
Dealt with cases like Bailey that prevented program from giving accurate output

Current known issues:
None






