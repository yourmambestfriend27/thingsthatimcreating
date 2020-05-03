#first question
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
capital = initialCapital
year = 0
while year < maxTimeYears:
   capital+= round((capital*percent),2)
   year+=1
   print('In the end of',year,'you will have {:.2f}'.format(capital))
else:
   print('You will gain {:.2f}'.format(capital-initialCapital))
