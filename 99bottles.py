# loop and range to mimic 99 bottles of beer on the wall song



for bottles in range (1,100):
	print "{0} bottles of beer on the wall, {0}  bottles of beer... \n If one of those bottles should happen to fall, {1} bottles of beer on the wall".format(100 - bottles, 99 - bottles)

	