"""
Frank Lubek
flube2@uic.edu
CS 418 Sp18
HW 1 Part 2 - Entity Resolution: UIC Courses: Data Cleaning
clean.py
"""

import sys

class Professor:
    
    def __init__(self) :
        self.lastName = ""
        self.courses = list([])
        self.normalizeTmpFix = ""
    def AddName(self, name):
        self.lastName = name.title().strip()
    def GetName(self):
        return self.lastName
    def AddCourse(self, course):
        self.courses.append(course.title())
    def GetCourses(self):
        return self.courses


def InList(masterList, profName):
    length = len(masterList)
    i = 0
    while i < length:
        if masterList[i].GetName() == profName:
            return i
        i += 1
    return -1

def filterAndMerge(masterList, curProf):
    profName = curProf.GetName()
    courses = curProf.GetCourses()
    profName.strip()
    inList = InList(masterList, profName)
    if inList == -1: # professor not in list yet so add them
        masterList.append(curProf)
    else:            # professor is in list so append courses
        for course in courses:
            masterList[inList].AddCourse(course)

def main():

    # Set Up Storage
    masterList = list([])

    # File I/O
    # source 4
    fileName = sys.argv[1]

    # source 3
    with open(fileName) as dirtyDataSet:
        mylist = [curLine.rstrip('\n') for curLine in dirtyDataSet]
        dirtyDataSet.close()


        for line in mylist:
            pair = line.split('-') # separate professors from courses
            pair[0].strip(' ')
            profFullName = pair[0]
            profCourses = pair[1]
        
            try:
                profCourses = pair[1] + '-' + pair[2] # in case of accidental split due to a '-' in course title
            except IndexError:
                profCourses = pair[1]
            curProf =  Professor() # This is the object that will be added to the master list
            #print(profFullName)
            #print(profCourses)
            ln = profFullName.split() # Used to detect last names on their own

           
            # Need to deal with professors and their courses separately so do professors first

            if len(ln) == 1 and '.' not in ln[0]:              # Doe
                profLastName = ln[0]       
                profLastName.strip()
                curProf.AddName(profLastName)
                #print(profLastName)

            elif (',' in profFullName):            # Doe, John
    
                temp = profFullName.split(',')
                profLastName = temp[0] 
                profLastName.strip()
                curProf.AddName(profLastName)
                #print(profLastName)
        
            elif ('.' in profFullName): 
        
                if ' ' not in profFullName:        # Doe.John
                    tmp = profFullName.split('.')
                    profLastName = tmp[0]
                    profLastName.strip()
                    #profLastName.rstrip(' ')
                    curProf.AddName(profLastName)
                    #print(profLastName) 

                else:                              # John.Doe
                    tmp = profFullName.split('.') 
                    profLastName = tmp[1].strip()
                    if len(profLastName.split(' ')) == 2:
                       tmp = profLastName.split(' ')
                       profLastName = tmp[1]
                    curProf.AddName(profLastName)
                    #print(profLastName)               

            else:                                  

                temp = profFullName.split(' ')
                if len(temp[1]) == 1:              # John A. Doe
                    profLastName = temp[2]
                else:
                    profLastName = temp[1]         # John Doe
                curProf.AddName(profLastName.strip())
                #print(profLastName)




            # now here deal with courses
            courseList = profCourses.split("|")                        
            courseList.sort()
            for course in courseList:
                c1 = course
                curProf.AddCourse(c1)

    
            #print("curProf is:  " + curProf.lastName)
            filterAndMerge(masterList, curProf)        
    
    # finally sort before printing
    # source 2
    masterList.sort(key = lambda obj:obj.lastName)
    

    FiLe = open("cleaned.txt", 'w')
    for prof in masterList:
        courses = prof.GetCourses()
        courses.sort() 
        acc = "|".join(courses)        
        name = prof.GetName()
        FiLe.write( name + ' - ' + acc + '\n')
    FiLe.close()
    print("cleaned.txt created and written to successfully!")


if __name__=='__main__' :
     main()


