"""
Frank Lubek
flube2@uic.edu
CS 418 Sp18
HW 1 Part 1 - Reformatting Data: Super Bowl Champions
transform.py
"""

from bs4 import BeautifulSoup
import urllib

# Obtain web site info using beautiful soup
# source 2
webAddress = "http://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
header = {'User-Agent': 'Mozilla/54.0'}
request = urllib.request.Request(webAddress, headers=header)
webPage = urllib.request.urlopen(request)
results = BeautifulSoup(webPage, "html.parser")

# Get all tables and navigate to the second one
tables = results.findAll("table", { "class" : ["sortable", "plainrowheaders"] })
specificTable = tables[1] # Get the second table on the webpage
row1 = specificTable.find('tr')
# source 3
row = row1.find_next_sibling() # Skip headers, added manually

# Set up CSV file for writing
csvfile = open('transformed.csv', 'w')
firstLine = 'Game,Year,Winning team, Score, Losing team, Venue\n'
csvfile.write(firstLine)


# Parse table into variables, manipulate, and write to file
# source 2
while row:
    cells = row.findAll('td')
    
    try:
        game = cells[0].find(text=True)
        gameFinal = '{:.2}'.format(game)
    except IndexError:
        break;

    date = cells[1].find(text=True)
    dateFinal = date[8] + date[9] + date[10] + date[11]

    winTeam = cells[2].find(text=True)
    # source 4 - [:-2]
    winTeam = winTeam[:-2]

    score = cells[3].findAll(text=True)
    scoreFinal = score[1].replace('(', '').replace(')', '')

    loseTeam = cells[4].find(text=True)
    loseTeam = loseTeam[:-2]

    venue = cells[5].find(text=True)
    venue = venue[:-2]

    city = cells[6].find(text=True)

    attendance =  cells[7].find(text=True)
    attendance = attendance[:-2]
    try:
        attend = int(attendance)
    except ValueError:
        break; 

   
    if attend > 1000: # Don't write data for games that haven't happened yet
        line = gameFinal+','+dateFinal+','+winTeam+','+scoreFinal+','+loseTeam+','+venue
        csvfile.write(line + '\n')
        #print(line) Uncomment to see CSV data in terminal without manually opening file
    # source 3    
    row = row.find_next_sibling()



csvfile.close()
print('transformed.csv created and written to successfully!')




