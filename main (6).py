print("Hi Dad! Welcome to the Fathers Day games. There are #3 games that go from easily programmed to hard programmed. Enjoy!")
print ("Hi Dad")

dad_m = int(input("We will start with the month of the date. Hint is think of this month :)"))

if dad_m > 6 or dad_m < 6:
   print("not quite there keep going.")
elif dad_m == 6:
  print("it is 6! now lets move on to the day")

dad_d = int(input("We will start with the day of the date. Hint is think of today :)"))

if dad_d > 19 or dad_d < 19:
  print("not quite there keep going.")
elif dad_d ==19:
  print("it is 19! now lets move on to the year")

dad_y = int(input("we will start with the year of the date. Hint is  think of two years before the Titanic sinking year"))
if dad_y > 1910 or dad_y < 1910:
  print("not quite there keep going.")
elif dad_y == 1910:

  print("it is 1910! could u guess what this date means (6/19/1910?")

guess = int(input("1 = 1st fathers day, two = first summer break, 3 = george washinton great grandson fathers day ( get it ) 4 = name fathers day got made"))

if guess == 1:
  print("yes lets move on to the next python game. as the games continue the coding and difficulty gets harder")
else:
  print("guess again")





