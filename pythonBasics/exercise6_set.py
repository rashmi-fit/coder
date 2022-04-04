'''
Q1. Consider following set definitions.
language set - python, java, c, c++
data science language set - pytho, r

 Answer the following questions with help of appropriate code. 
 (a) What are all programming languages are available?
 (b) How many data science languages are available?
 (c) List languages which are not data science languages?
 (d) List languages which are both programming language and data science languages.
 (e) List languges which are only data science languages.
 '''
language_set ={'python', 'java', 'c', 'c++'}
datascience_language_set ={'pytho', 'r'}
total_language= language_set | datascience_language_set
print("What are all programming languages are available? ",total_language)
print("How many data science languages are available? ",len(datascience_language_set))
print("List languages which are not data science languages? ",language_set- datascience_language_set)
print("List languages which are both programming language and data science languages. ",language_set.intersection(datascience_language_set))
print("List languges which are only data science languages. ",datascience_language_set- language_set)
