"""
Frank Lubek
flube2@uic.edu
CS 418 Sp18
HW 1 Part 3 - Entity Resolution: UIC Courses: Data Analysis
query.py
"""

import sys


class Professor:
    
    def __init__(self) :
        self.lastName = ""
        self.courses = list([])
        self.normalizeTmpFix = ""
        self.jaccardIndex = 0.0
        self.jaccardPartner = ""


    def setJaccard(self, jaccardIndex):
        self.jaccardIndex = jaccardIndex
    def setJaccardPartner(self, partner):
        self.jaccardPartner = partner
    def getJaccard(self):
        return self.jaccardIndex
    def getJaccardPartner(self):
        return self.jaccardPartner
    def AddName(self, name):
        self.lastName = name.title().strip()
    def GetName(self):
        return self.lastName
    def AddCourse(self, course):
        self.courses.append(course.title().strip())
    def GetCourses(self):
        return self.courses



def Jaccard(jpl):

    for prof1 in jpl:
        courses1 = prof1.GetCourses()
        for prof2 in jpl:
            courses2 = prof2.GetCourses()
            coursesChecked = len(courses1) + len(courses2)
            coursesMatched = 0.0
            for course1 in courses1:
                wordsMatched = 0.0
                wordsChecked = 0.0
                #coursesChecked = coursesChecked + 1.0
                wordList = course1.split(' ')
                for course2 in courses2:
                    #coursesChecked = coursesChecked + 1.0
                    #print(course1 + ", " + course2)
                    for word in wordList:
                        wordsChecked = wordsChecked + 1.0
                        if word in courses2:
                            #print("matched word")
                            wordsMatched = wordsMatched + 1.0
                    if (wordsMatched / wordsChecked) > .75 or course1 == course2:
                        coursesMatched = coursesMatched + 1.0
                    #print(str(wordsMatched) + " of " + str(wordsChecked) + " matched")
            percent = float(coursesMatched / float(coursesChecked - coursesMatched))
            #print("prof1 is " + prof1.GetName() + " and prof2 is " + prof2.GetName())
            #print(courses1)
            #print(courses2)
            #print(str(coursesMatched) + " of " + str(coursesChecked) + " matched\n\n")
            #print(percent) 
            if percent > prof1.getJaccard() and prof1.GetName() != prof2.GetName() and prof1.getJaccardPartner() != prof1.GetName():
                prof1.setJaccard(percent)
                prof1.setJaccardPartner(prof2.GetName())
                prof2.setJaccard(percent)
                prof2.setJaccardPartner(prof1.GetName())
                #print(prof1.GetName() + ": " + str(prof1.getJaccard()))
                #print("Jaccard pair created")


    # Find the highest Jaccard Score
    maxJ = jpl[0]
    for p in jpl:
        if p.getJaccard() > maxJ.getJaccard():
            maxJ = p
    #for p in jpl:
        #print(p.getJaccard()) # To see that jaccard function worked

    return maxJ



def InList(masterList, profName):
    length = len(masterList)
    i = 0
    while i < length:
        #print(i)
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



def makeList(fileName):
    masterList = list([])
    with open(fileName) as dirtyDataSet:
        mylist = [curLine.rstrip('\n') for curLine in dirtyDataSet]
        dirtyDataSet.close()


        for line in mylist:
            pair = line.split('-') # separate professors from courses
            pair[0].strip(' ')
            profFullName = pair[0]
            profCourses = pair[1]

            try:
                profCourses = pair[1] + '-' + pair[2] # in case of split with a '-' in course title
            except IndexError:
                profCourses = pair[1]

            #print(profFullName)
            #print(profCourses)
            curProf =  Professor()

           
            # Need to deal with professors and their courses separately so do professors first
            curProf.AddName(profFullName)

            # now here deal with courses
            courseList = profCourses.split("|")                        
            courseList.sort()
            for course in courseList:
                course.strip()
                curProf.AddCourse(course)

    
            #print("curProf is:  " + curProf.lastName)
            filterAndMerge(masterList, curProf)        
    
    # finally sort before returning
    # source 2
    masterList.sort(key = lambda obj:obj.lastName)
    return masterList


def main():


    profInput = 1 # print conditional for later
    # source 4
    fileName = sys.argv[1]

    try:
        try:
            # source 4
            profNameToFind = sys.argv[3] # python3 query.py cleaned.txt Patrick Troy
        except IndexError:
            # source 4
            profNameToFind = sys.argv[2] # python3 query.py cleaned.txt Troy
    except IndexError:
        profNameToFind = "" # python3 query.py cleaned.txt
        profInput = 0 



    courseSet = set({}) # Distinct courses can be stored in a set
    profPrintStr = ""
       
    # source 3
    with open(fileName) as cleanedDataSet:
        mylist = [curLine.rstrip('\n') for curLine in cleanedDataSet]
        cleanedDataSet.close()

        for line in mylist:
            pair = line.split('-') # separate professors from courses
            pair[0].strip(' ')
            profLastName = pair[0]
            profCourses = pair[1]
            split = profCourses.split('|')

            # Q1 - How many distinct courses are in this dataset?                   COMPLETE ***********************************************
            for course in split:
                courseSet.add(course.strip().title())

            # Q2 - How many classes has Professor X taught?                         COMPLETE ***********************************************
            classesTaught = len(split)
            if profLastName.strip() == profNameToFind.strip():
                profPrintStr = "Classes " + profLastName.strip() + " has taught: " + str(classesTaught)

    # Q3 - 2 most similar teachers based on courses taught and Jaccard distance     COMPLETE ***********************************************  
    masterList = makeList(fileName)
    jaccardProfList = list([])

    for prof in masterList:
        courses = prof.GetCourses()
        #if prof.GetName() == profNameToFind:
            #print(len(courses))
        if len(courses) > 4:
            jaccardProfList.append(prof)       
        acc = "|".join(courses)        
        name = prof.GetName()
        #print( name + ' - ' + acc)
        

    maxJaccardProf = Jaccard(jaccardProfList)
    #maxJaccardProf = Jaccard(masterList) 




    # Output Answers
    helper = len(courseSet)
    print("Distinct Courses in this Data Set: " + str(helper))
    if profInput == 1:
        print(profPrintStr)
    print("Professors with most aligned teaching interests are: " + maxJaccardProf.GetName() + " and " + maxJaccardProf.getJaccardPartner())

    


if __name__ == "__main__":
    main()




