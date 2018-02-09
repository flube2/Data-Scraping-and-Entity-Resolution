# Data-Scraping-and-Entity-Resolution
HW1 for UIC CS 418 Spring 2018

This was a homework assignment for CSe 418 at UIC.
I would like to note that this was the very first time I had ever written anything in the very foreign language of Python.
NOTE: THIS IS WRITTEN IN PYTHON3 SO ADJUST PYTHON VERSION ACCORDINGLY BEFORE RUNNING!!

There are still some issues, like possible cmd line args formats that weren't released to us until after the due date (thanks for that)
and not all class names will match perfectly.

In query.py I implement a Jaccard function to see which two professors are the most similar.
Upon starting the Jaccard function and having no clue that Python has sets with built in union() and intersection() functions,
I implemented my own method. After I realized I could have just used intersection() and union() I felt like I had approached this problem the wrong way. But I have since changed my mind.
You see, although I have dirty data that gets cleaned and fed into this program, there could still be spelling errors within course/professor names.
If I had used sets and added classes to that, the same class spelled two different ways (Intro to calculus II and Intro to calculuz II) would have resulted as two classes in the set instead of one. 
While my word matching approach, which attempts to match two classes based on the percentage of similarity between their word contents by going through word for word, is far, far from optimal, it is better than using sets because it avoids the above problem.
On short class names such as Operating Systems and Operating Systemz, my Jaccard function wouldn't count as a match due to only 50% of the course title being matched. But if I had used sets it still would be no better off as it would also consider them 2 separate courses.
Therefore, although there are definitely more efficient ways to complete this assignment, I feel that I have implemented a better solution to this problem by using a quintuple nested for loop rather than using sets.

Please read the assignment pdf for more information on what command line arguments to pass and etc.
