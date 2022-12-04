letter = ''' Dear name,
\tGreetings from Google. I am happy to inform you about your selection for the role of a software developer.
\tBest of luck for your future!
\tHave a great day ahead!

Basanti
Date: date'''
n=input("Enter the name :")
d=input("Enter the date :")
letter=letter.replace("name", n)
letter=letter.replace("date", d)
print(letter)